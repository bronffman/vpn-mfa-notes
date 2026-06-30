from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {'.md', '.txt', '.ps1', '.py', '.json', '.yml', '.yaml'}

PATTERNS = {
    'url': re.compile(r'https?://[^\s)]+', re.I),
    'email': re.compile(r'[\w.%-]+@[\w.-]+\.[a-zA-Z]{2,}'),
    'possible_internal_group': re.compile(r'\b[A-Z][A-Z0-9]+_[A-Z0-9_-]+\b'),
    'private_ip': re.compile(r'\b(10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(1[6-9]|2\d|3[0-1])\.\d+\.\d+)\b'),
}


def scan_file(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    result = []
    for num, line in enumerate(text.splitlines(), 1):
        for name, pattern in PATTERNS.items():
            if pattern.search(line):
                result.append((num, name, line.strip()))
    return result


def main():
    found = False
    for path in ROOT.rglob('*'):
        if path.is_file() and path.suffix.lower() in EXTENSIONS:
            matches = scan_file(path)
            if matches:
                found = True
                print(f'\n{path.relative_to(ROOT)}')
                for line_no, kind, line in matches:
                    print(f'  line {line_no}: {kind}: {line}')

    if not found:
        print('No obvious sensitive strings found.')


if __name__ == '__main__':
    main()
