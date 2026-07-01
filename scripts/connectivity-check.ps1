Write-Host "VPN Connectivity Check"
Write-Host ""

$server = Read-Host "Enter VPN server"

Write-Host "`n=== DNS ==="
nslookup $server

Write-Host "`n=== Ping ==="
ping $server -n 4

Write-Host "`n=== HTTPS Port ==="
Test-NetConnection $server -Port 443

Write-Host "`n=== Route ==="
tracert $server
