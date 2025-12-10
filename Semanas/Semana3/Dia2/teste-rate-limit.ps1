# Fazer mais de 5 requisições em 1 minuto
for ($i = 1; $i -le 10; $i++) {
    Write-Host "Requisição $i de 10..." -ForegroundColor Cyan
    
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8000/login" `
            -Method POST `
            -ContentType "application/json" `
            -Body '{"username": "admin", "password": "wrong"}' `
            -ErrorAction Stop
        
        Write-Host "Status: $($response.StatusCode)" -ForegroundColor Green
        Write-Host "Resposta: $($response.Content)" -ForegroundColor Gray
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.value__
        Write-Host "Status: $statusCode" -ForegroundColor $(if ($statusCode -eq 429) { "Yellow" } else { "Red" })
        
        if ($statusCode -eq 429) {
            Write-Host "✅ Rate limit funcionando! (429 Too Many Requests)" -ForegroundColor Green
        } else {
            $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
            $responseBody = $reader.ReadToEnd()
            Write-Host "Erro: $responseBody" -ForegroundColor Red
        }
    }
    
    Write-Host ""
    Start-Sleep -Milliseconds 100  # Pequeno delay entre requisições
}