# test_chat.ps1
# Script para testar o endpoint /chat

$TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc2NTc1MzA3MywidHlwZSI6ImFjY2VzcyJ9.8gLgVQV0vCHOZczwjkc0H4MBCN7-Fx8X828b3uHmZC4"
$API_URL = "http://localhost:8000/chat"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  TESTE DO ENDPOINT /chat" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ============================================
# 1. TESTE SIMPLES DO CHAT
# ============================================
Write-Host "1. Teste simples do chat..." -ForegroundColor Yellow

$headers = @{
    "Authorization" = "Bearer $TOKEN"
    "Content-Type" = "application/json"
}

$chatBody = @{
    message = "Olá! Como você está?"
    stream = $false  # Resposta completa, não streaming
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $API_URL -Method POST -Body $chatBody -Headers $headers
    Write-Host "   ✅ Chat funcionando!" -ForegroundColor Green
    Write-Host "   Conversation ID: $($response.conversation_id)" -ForegroundColor Gray
    Write-Host "   Resposta: $($response.reply.Substring(0, [Math]::Min(100, $response.reply.Length)))..." -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "   ❌ Erro no chat: $_" -ForegroundColor Red
    Write-Host ""
}

# ============================================
# 2. TESTE DE RATE LIMITING
# ============================================
Write-Host "2. Testando Rate Limiting (31 requisições)..." -ForegroundColor Yellow
Write-Host ""

$successCount = 0
$rateLimitCount = 0
$errorCount = 0

$simpleChatBody = @{
    message = "test"
    stream = $false
} | ConvertTo-Json

for ($i = 1; $i -le 31; $i++) {
    Write-Host -NoNewline "   Requisição $($i.ToString().PadLeft(2)): "
    
    try {
        $response = Invoke-WebRequest -Uri $API_URL -Method POST -Body $simpleChatBody -Headers $headers -ErrorAction Stop
        $statusCode = $response.StatusCode
        
        if ($statusCode -eq 200) {
            Write-Host "✅ OK (200)" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "⚠️  Status: $statusCode" -ForegroundColor Yellow
            $errorCount++
        }
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.value__
        if ($statusCode -eq 429) {
            Write-Host "🚫 RATE LIMITED (429)" -ForegroundColor Red
            $rateLimitCount++
        } else {
            Write-Host "❌ Erro: $statusCode" -ForegroundColor Red
            $errorCount++
        }
    }
    
    # Pequeno delay
    Start-Sleep -Milliseconds 100
}

# ============================================
# 3. RESULTADOS
# ============================================
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  RESULTADOS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ Sucessos (200): $successCount" -ForegroundColor Green
Write-Host "🚫 Rate Limited (429): $rateLimitCount" -ForegroundColor Red
Write-Host "⚠️  Outros erros: $errorCount" -ForegroundColor Yellow
Write-Host ""

if ($rateLimitCount -gt 0) {
    Write-Host "✅ Rate limiting está funcionando corretamente!" -ForegroundColor Green
} else {
    Write-Host "⚠️  Rate limiting não foi acionado" -ForegroundColor Yellow
    Write-Host "   (Pode estar desabilitado ou limite não atingido)" -ForegroundColor Gray
}

Write-Host ""