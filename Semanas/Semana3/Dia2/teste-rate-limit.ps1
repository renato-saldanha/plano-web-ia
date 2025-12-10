# Fazer mais de 5 requisições em 1 minuto
for ($i = 1; $i -le 10; $i++) {
    Write-Host "Requisição $i de 10..."
    
    $response = Invoke-RestMethod -Uri "http://localhost:8000/login" `
        -Method POST `
        -ContentType "application/json" `
        -Body '{"username": "admin", "password": "wrong"}'
    
    Write-Host "Status: $($response.StatusCode)"
    Write-Host ""
    
    Start-Sleep -Milliseconds 100  # Pequeno delay entre requisições
}