Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "       CERTIFYHUB - INICIANDO SISTEMA   " -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# 1. Encerra qualquer instância anterior
Get-Process -Name dotnet -ErrorAction SilentlyContinue | Stop-Process -Force

# 2. Inicia a API em segundo plano
Write-Host "[1/2] Iniciando Backend API (.NET 10 Web API)..." -ForegroundColor Yellow
$apiProcess = Start-Process -FilePath "dotnet" -ArgumentList "run --project src/CertifyHub.Api --urls http://localhost:5005" -PassThru -NoNewWindow

Start-Sleep -Seconds 3

# 3. Inicia o Frontend Blazor
Write-Host "[2/2] Iniciando Frontend Blazor Web App..." -ForegroundColor Yellow
Write-Host ""
Write-Host ">> Acesse o simulado no navegador em: http://localhost:5044" -ForegroundColor Green
Write-Host ">> Pressione Ctrl+C para encerrar os servidores." -ForegroundColor Gray
Write-Host ""

try {
    dotnet run --project src/CertifyHub.Web --urls http://localhost:5044
}
finally {
    if ($apiProcess -and !$apiProcess.HasExited) {
        Stop-Process -Id $apiProcess.Id -Force
    }
}
