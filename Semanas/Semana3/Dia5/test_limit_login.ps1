# test_login.ps1
# Script para testar o endpoint /login

$API_URL = "http://localhost:8000/login"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  TESTE DO ENDPOINT /login" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ============================================
# 1. TESTE DE RATE LIMITING
# ============================================
Write-Host "1. Testando Rate Limiting (6 requisições)..." -ForegroundColor Yellow
Write-Host ""

$successCount = 0
$rateLimitCount = 0
$errorCount = 0

# Headers necessários para JSON
$headers = @{
    "Content-Type" = "application/json"
}

# Body correto para login (apenas username e password)
$loginBody = @{
    username = "admin"
    password = "admin123"
} | ConvertTo-Json

for ($i = 1; $i -le 6; $i++) {
    Write-Host -NoNewline "   Requisição $($i.ToString().PadLeft(2)): "
    
    try {
        $response = Invoke-WebRequest -Uri $API_URL -Method POST -Body $loginBody -Headers $headers -ErrorAction Stop
        $statusCode = $response.StatusCode
        
        if ($statusCode -eq 200) {
            Write-Host "OK (200)" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "Status: $statusCode" -ForegroundColor Yellow
            $errorCount++
        }
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.value__
        if ($statusCode -eq 429) {
            Write-Host "RATE LIMITED (429)" -ForegroundColor Red
            $rateLimitCount++
        } else {
            Write-Host "Erro: $statusCode" -ForegroundColor Red
            $errorCount++
        }
    }
    
    # Pequeno delay
    Start-Sleep -Milliseconds 1
}

# ============================================
# 3. RESULTADOS
# ============================================
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  RESULTADOS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Sucessos (200): $successCount" -ForegroundColor Green
Write-Host "Rate Limited (429): $rateLimitCount" -ForegroundColor Red
Write-Host "Outros erros: $errorCount" -ForegroundColor Yellow
Write-Host ""

if ($rateLimitCount -gt 0) {
    Write-Host "Rate limiting está funcionando corretamente!" -ForegroundColor Green
} else {
    Write-Host "Rate limiting não foi acionado" -ForegroundColor Yellow
    Write-Host "   (Pode estar desabilitado ou limite não atingido)" -ForegroundColor Gray
}

Write-Host ""