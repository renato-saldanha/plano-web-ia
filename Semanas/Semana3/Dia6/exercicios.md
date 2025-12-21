# 🧪 Exercícios - Testes Automatizados

Este arquivo contém exercícios práticos para validar seu entendimento de testes com pytest.

---

## Exercício 1: Criar Fixture de Cliente

**Objetivo:** Criar fixture básica de TestClient.

**Tarefa:**
1. Crie `tests/conftest.py`
2. Implemente fixture `client` que retorna `TestClient(app)`
3. Teste a fixture criando um teste simples que usa `client.get("/health")`

**Solução esperada:**
```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from template import app

@pytest.fixture
def client():
    return TestClient(app)
```

---

## Exercício 2: Teste de Login

**Objetivo:** Criar testes básicos de autenticação.

**Tarefa:**
1. Crie `tests/test_auth.py`
2. Implemente teste `test_login_success` que verifica login com credenciais válidas
3. Implemente teste `test_login_invalid_username` que verifica erro com usuário inválido
4. Implemente teste `test_login_invalid_password` que verifica erro com senha inválida

**Dicas:**
- Use `client.post("/login", json={...})`
- Verifique `response.status_code`
- Verifique campos na resposta JSON

---

## Exercício 3: Fixture de Autenticação

**Objetivo:** Criar fixture que retorna headers de autenticação.

**Tarefa:**
1. Adicione fixture `auth_headers` em `tests/conftest.py`
2. A fixture deve fazer login e retornar `{"Authorization": f"Bearer {token}"}`
3. Use a fixture em um teste para acessar rota protegida

**Solução esperada:**
```python
@pytest.fixture
def auth_headers(client: TestClient):
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
```

---

## Exercício 4: Teste de Chat

**Objetivo:** Criar testes para endpoint de chat.

**Tarefa:**
1. Crie `tests/test_chat.py`
2. Implemente teste que cria nova conversa
3. Implemente teste que envia mensagem em conversa existente
4. Verifique que `conversation_id` é retornado e pode ser reutilizado

**Dicas:**
- Use `auth_headers` fixture
- Teste fluxo completo: criar → enviar mensagem → verificar histórico

---

## Exercício 5: Teste de Rate Limiting

**Objetivo:** Validar que rate limiting funciona corretamente.

**Tarefa:**
1. Crie `tests/test_rate_limiting.py`
2. Implemente teste que faz 5 requisições de login (limite)
3. Verifique que 6ª requisição retorna 429
4. Implemente teste similar para chat (30/min)

**Dicas:**
- Use loop para fazer múltiplas requisições
- Verifique status code 429 na requisição que excede limite
- Para acelerar testes, você pode usar `time.sleep()` ou mock

---

## Exercício 6: Teste de Exception Handlers

**Objetivo:** Validar que exception handlers retornam JSON padronizado.

**Tarefa:**
1. Crie `tests/test_exceptions.py`
2. Implemente teste que verifica HTTPException retorna JSON com campos:
   - `error: true`
   - `message`
   - `status_code`
   - `path`
3. Implemente teste que verifica ValidationError retorna JSON com campo `errors`

**Dicas:**
- Teste endpoint que gera erro intencionalmente (ex: conversa inexistente)
- Teste requisição com dados inválidos (ex: login sem password)

---

## Exercício 7: Cobertura de Código

**Objetivo:** Verificar cobertura de testes.

**Tarefa:**
1. Execute testes com cobertura: `pytest --cov=template --cov-report=term-missing`
2. Identifique linhas não cobertas
3. Adicione testes para aumentar cobertura acima de 60%

**Dicas:**
- Foque em funcionalidades críticas primeiro
- Não é necessário testar código de configuração ou logging simples
- Use `--cov-fail-under=60` para falhar se cobertura < 60%

---

## Exercício 8: Teste de Integração Completo

**Objetivo:** Criar teste que valida fluxo completo da aplicação.

**Tarefa:**
1. Crie teste `test_complete_flow` que:
   - Faz login
   - Cria conversa
   - Envia múltiplas mensagens
   - Lista conversas
   - Obtém mensagens da conversa
   - Verifica que tudo está correto

**Dicas:**
- Use fixtures `client` e `auth_headers`
- Teste fluxo real de uso da API
- Verifique que dados são persistidos corretamente

---

## Exercício 9: Teste de Refresh Token

**Objetivo:** Validar funcionalidade de refresh token.

**Tarefa:**
1. Adicione testes em `tests/test_auth.py`:
   - `test_refresh_token_success`: refresh com token válido
   - `test_refresh_token_invalid`: refresh com token inválido
   - `test_refresh_token_expired`: refresh com token expirado (se possível)

**Dicas:**
- Obtenha refresh token do login
- Use refresh token para obter novo access token
- Verifique que novo token funciona

---

## Exercício 10: Organização e Refatoração

**Objetivo:** Melhorar organização dos testes.

**Tarefa:**
1. Revise todos os testes criados
2. Verifique que nomes são descritivos
3. Verifique que testes são independentes
4. Adicione docstrings aos testes
5. Agrupe testes relacionados (opcional: usar classes)

**Dicas:**
- Nomes devem descrever o que está sendo testado
- Cada teste deve poder rodar isoladamente
- Docstrings ajudam a entender propósito do teste

---

## Desafio Opcional: Testes de Streaming

**Objetivo:** Testar endpoint de streaming (mais complexo).

**Tarefa:**
1. Crie teste para endpoint `/chat` com `stream: true`
2. Valide que resposta é SSE (Server-Sent Events)
3. Valide que chunks são recebidos corretamente

**Dicas:**
- Streaming retorna `text/event-stream`
- Use `response.iter_lines()` para ler chunks
- Valide formato `data: {chunk}\n\n`

---

## Checklist de Validação

Antes de considerar os exercícios completos, verifique:

- [ ] Todos os testes passam: `pytest tests/ -v`
- [ ] Cobertura ≥ 60%: `pytest --cov=template --cov-report=term-missing`
- [ ] Testes estão organizados por funcionalidade
- [ ] Fixtures estão em `conftest.py`
- [ ] Testes têm nomes descritivos
- [ ] Testes são independentes
- [ ] Exception handlers são testados
- [ ] Rate limiting é testado
- [ ] Autenticação é testada completamente

---

**Última atualização:** 14 Dez 2025
