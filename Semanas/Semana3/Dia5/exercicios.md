# 🧪 Exercícios - Dia 5

## Exercícios para Validar Implementação

Estes exercícios ajudam a validar que rate limiting, exception handling e logging estão funcionando corretamente.

---

## Exercício 1: Testar Rate Limiting por Usuário

### Objetivo
Verificar que rate limiting funciona por usuário, não apenas por IP.

### Passos
1. Fazer login e obter token:
```bash
TOKEN=$(curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}' \
  | jq -r '.access_token')
```

2. Fazer 31 requisições rápidas ao endpoint `/chat`:
```bash
for i in {1..31}; do
  echo "Requisição $i"
  curl -X POST http://localhost:8000/chat \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"message": "test"}' \
    -w "\nStatus: %{http_code}\n\n"
done
```

3. Verificar que a 31ª requisição retorna status 429 (Too Many Requests).

### Resultado Esperado
- As primeiras 30 requisições devem retornar status 200 ou 200 (streaming)
- A 31ª requisição deve retornar status 429 com mensagem de rate limit excedido

---

## Exercício 2: Testar Exception Handlers

### Objetivo
Verificar que todos os tipos de erro são tratados corretamente.

### 2.1 Testar HTTPException (404)
```bash
curl -X GET http://localhost:8000/endpoint-inexistente \
  -H "Authorization: Bearer $TOKEN" \
  -w "\nStatus: %{http_code}\n"
```

**Resultado esperado:** Status 404 com JSON:
```json
{
  "error": true,
  "message": "Not Found",
  "status_code": 404,
  "path": "/endpoint-inexistente"
}
```

### 2.2 Testar ValidationError (422)
```bash
curl -X POST http://localhost:8000/chat \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"invalid_field": "test"}' \
  -w "\nStatus: %{http_code}\n"
```

**Resultado esperado:** Status 422 com JSON contendo lista de erros de validação.

### 2.3 Testar Exception Genérica (500)
Para testar, você pode temporariamente adicionar um erro no código:
```python
@app.get("/test-error")
async def test_error():
    raise Exception("Erro de teste")
```

```bash
curl -X GET http://localhost:8000/test-error \
  -H "Authorization: Bearer $TOKEN" \
  -w "\nStatus: %{http_code}\n"
```

**Resultado esperado:** Status 500 com mensagem genérica (não deve expor stack trace).

---

## Exercício 3: Verificar Logging Estruturado

### Objetivo
Verificar que logs estão sendo gerados em formato JSON.

### Passos
1. Fazer algumas requisições (login, chat, etc.)
2. Verificar logs no console onde o servidor está rodando
3. Verificar que cada log é um objeto JSON válido

### Resultado Esperado
Logs devem estar no formato:
```json
{"timestamp": "2025-12-13T10:30:00", "level": "INFO", "message": "Login bem-sucedido", "user_id": "admin"}
{"timestamp": "2025-12-13T10:30:05", "level": "INFO", "message": "Início de chat", "user_id": "admin", "conversation_id": "..."}
```

---

## Exercício 4: Verificar Middleware de Request Logging

### Objetivo
Verificar que todas as requisições são logadas pelo middleware.

### Passos
1. Fazer requisições a diferentes endpoints:
   - `GET /health`
   - `POST /login`
   - `POST /chat`
   - `GET /conversations`

2. Verificar logs no console

### Resultado Esperado
Cada requisição deve gerar um log com:
- `method`: Método HTTP (GET, POST, etc.)
- `path`: Caminho da requisição
- `status_code`: Status HTTP da resposta
- `duration_ms`: Tempo de processamento em milissegundos

Exemplo:
```json
{"timestamp": "...", "level": "INFO", "message": "Request processada", "method": "POST", "path": "/chat", "status_code": 200, "duration_ms": 1234.56}
```

---

## Exercício 5: Testar Rate Limiting com Múltiplos Usuários

### Objetivo
Verificar que rate limiting é isolado por usuário.

### Passos
1. Criar dois tokens diferentes (se possível, criar dois usuários)
2. Fazer 31 requisições com o primeiro token
3. Verificar que o primeiro token atinge o limite (429)
4. Fazer requisições com o segundo token
5. Verificar que o segundo token ainda pode fazer requisições (não afetado pelo limite do primeiro)

### Resultado Esperado
- Rate limiting deve ser isolado por usuário
- Limitar um usuário não deve afetar outros usuários

---

## Exercício 6: Validar Logs de Erro

### Objetivo
Verificar que erros são logados corretamente.

### Passos
1. Forçar um erro (usar endpoint `/test-error` do Exercício 2.3)
2. Verificar logs no console
3. Verificar que o log de erro contém:
   - Nível ERROR
   - Mensagem de erro
   - Stack trace (no servidor, não na resposta ao cliente)

### Resultado Esperado
Log de erro deve conter informações completas para debug, mas a resposta ao cliente deve ser genérica.

---

## Checklist de Validação

Após completar os exercícios, verifique:

- [ ] Rate limiting por usuário funciona (retorna 429 após limite)
- [ ] HTTPException retorna JSON padronizado
- [ ] ValidationError retorna lista de erros formatada
- [ ] Exception genérica retorna mensagem genérica (não expõe detalhes)
- [ ] Logs estão em formato JSON
- [ ] Logs de login incluem user_id
- [ ] Logs de chat incluem user_id e conversation_id
- [ ] Middleware loga todas as requisições
- [ ] Logs de erro incluem stack trace (apenas no servidor)
- [ ] Rate limiting é isolado por usuário

---

## Dicas

1. **Para testar rate limiting rapidamente:** Use um script Python ou bash para fazer múltiplas requisições em loop.

2. **Para ver logs em tempo real:** Use `tail -f` ou redirecione logs para arquivo:
   ```bash
   uvicorn template:app --reload 2>&1 | tee logs.txt
   ```

3. **Para validar JSON dos logs:** Use `jq` ou validador JSON online:
   ```bash
   cat logs.txt | jq .
   ```

4. **Para testar exception handlers:** Use diferentes tipos de requisições inválidas e verifique que todas retornam JSON padronizado.

---

**Próximo passo:** Após validar todos os exercícios, preencher o journal e o CONTEXTO_PROXIMO_DIA.md.
