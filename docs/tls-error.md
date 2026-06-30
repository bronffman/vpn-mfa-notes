# SSL/TLS secure channel error

Ошибка вида:

```text
The request was aborted: Could not create SSL/TLS secure channel
```

Обычно связана с отключённым или некорректно настроенным TLS 1.2 на сервере/компоненте.

## Что проверить

- TLS 1.2 включён для клиента и сервера.
- Для .NET включены системные версии TLS.
- Используется сильная криптография.
- Балансировщик принимает только актуальные протоколы и шифры.

## Пример обезличенных параметров

```reg
[HKLM\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
"SystemDefaultTlsVersions"=dword:00000001
"SchUseStrongCrypto"=dword:00000001

[HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
"Enabled"=dword:ffffffff
"DisabledByDefault"=dword:00000000
```

## Важно

Не применять изменения в реестре без согласования. В репозитории оставлен только общий пример, без привязки к конкретным серверам и внутренним адресам.
