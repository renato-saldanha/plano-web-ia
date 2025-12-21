# 📝 Exercícios - Dia 7: Swagger e Deploy em Produção

Este arquivo contém exercícios práticos para consolidar o aprendizado sobre Swagger/OpenAPI e deploy em produção.

---

## Exercício 1: Personalizar Swagger UI

### Objetivo
Personalizar completamente os metadados da API no Swagger.

### Tarefas
1. Configure os seguintes metadados no `FastAPI()`:
   - **title**: "API FastAPI com IA Generativa"
   - **description**: Adicione uma descrição detalhada em Markdown explicando as funcionalidades
   - **version**: "1.0.0"
   - **contact**: Seu nome e email
   - **license_info**: {"name": "MIT"}

2. Verifique que os metadados aparecem corretamente em:
   - `/docs` (Swagger UI)
   - `/redoc` (ReDoc)

### Como validar
- Inicie o servidor: `uvicorn template:app --reload`
- Acesse `http://localhost:8000/docs`
- Verifique que todos os metadados estão visíveis no topo da página

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 1.3 e `exemplo_referencia.py` para ver exemplos.

---

## Exercício 2: Adicionar Tags e Descrições aos Endpoints

### Objetivo
Organizar endpoints com tags e adicionar descrições detalhadas.

### Tarefas
1. Adicione tags aos seguintes endpoints:
   - `@app.post("/login", tags=["Auth"])`
   - `@app.post("/refresh", tags=["Auth"])`
   - `@app.post("/chat", tags=["Chat"])`
   - `@app.get("/conversations", tags=["Chat"])`
   - `@app.get("/conversations/{conversation_id}/messages", tags=["Chat"])`
   - `@app.post("/api/generate", tags=["Chat"])`
   - `@app.get("/health", tags=["Health"])`

2. Adicione docstrings detalhadas em cada endpoint explicando:
   - O que o endpoint faz
   - Quais parâmetros recebe
   - O que retorna
   - Se requer autenticação
   - Rate limits (se aplicável)

### Como validar
- Acesse `http://localhost:8000/docs`
- Verifique que endpoints estão agrupados por tags
- Clique em cada endpoint e verifique que a descrição aparece

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 1.4 e 1.6.

---

## Exercício 3: Adicionar Exemplos nos Modelos Pydantic

### Objetivo
Melhorar documentação adicionando exemplos de request/response.

### Tarefas
1. Adicione `Field(example="...")` nos seguintes campos:

```python
class LoginRequest(BaseModel):
    username: str = Field(..., example="admin")
    password: str = Field(..., example="admin123")

class ChatRequest(BaseModel):
    message: str = Field(..., example="Explique o que é Python")
    conversation_id: Optional[str] = Field(None, example="uuid-here")
    model: Optional[str] = Field(None, example="gpt-4o-mini")
    stream: bool = Field(True, example=True)
```

2. Adicione descrições usando `Field(description="...")` em todos os campos dos modelos.

### Como validar
- Acesse `http://localhost:8000/docs`
- Clique em "Try it out" em qualquer endpoint
- Verifique que exemplos aparecem preenchidos automaticamente

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 1.5 e `exemplo_referencia.py`.

---

## Exercício 4: Criar Checklist de Deploy Completo

### Objetivo
Documentar todos os passos necessários para fazer deploy em produção.

### Tarefas
1. Crie um arquivo `CHECKLIST_DEPLOY.md` com:

#### Seção 1: Variáveis de Ambiente
Liste todas as variáveis necessárias com:
- Nome da variável
- Descrição do que faz
- Valor de exemplo (sem dados sensíveis)
- Se precisa ser gerada/alterada para produção

Exemplo:
```markdown
### JWT_SECRET_KEY
- **Descrição**: Chave secreta para assinar tokens JWT
- **Exemplo**: "sua_chave_super_secreta_aqui_minimo_32_caracteres"
- **Produção**: Gerar nova chave forte e única
```

#### Seção 2: Configurações de Segurança
- [ ] CORS configurado corretamente
- [ ] Headers de segurança implementados
- [ ] JWT_SECRET_KEY é forte e única
- [ ] HTTPS habilitado (automático em Railway/Render)

#### Seção 3: Funcionalidades Críticas
- [ ] Health check funcionando (`/health`)
- [ ] Logging estruturado funcionando
- [ ] Rate limiting funcionando
- [ ] Exception handling funcionando

### Como validar
- Revise o checklist antes de fazer deploy
- Use o checklist durante o deploy
- Marque cada item conforme completa

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 2.

---

## Exercício 5: Fazer Deploy no Railway

### Objetivo
Publicar a API em produção usando Railway.

### Tarefas
1. **Criar conta no Railway:**
   - Acesse https://railway.app
   - Faça login com GitHub

2. **Criar projeto:**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório

3. **Configurar variáveis de ambiente:**
   - Vá em "Variables" no projeto
   - Adicione cada variável necessária:
     - `JWT_SECRET_KEY` (gere nova para produção!)
     - `ALGORITHM`
     - `ACCESS_TOKEN_EXPIRE_MINUTES`
     - `REFRESH_TOKEN_EXPIRE_DAYS`
     - `OPENAI_API_KEY`

4. **Configurar start command:**
   - Vá em "Settings" → "Start Command"
   - Configure: `uvicorn template:app --host 0.0.0.0 --port $PORT`

5. **Fazer deploy:**
   - Railway faz deploy automático ao fazer push
   - Ou clique em "Deploy" no dashboard
   - Aguarde build completar

6. **Anotar URL:**
   - Vá em "Settings" → "Domains"
   - Anote a URL gerada: `https://...`

### Como validar
- Acesse a URL no navegador
- Deve retornar 404 (esperado para rota raiz)
- Acesse `{URL}/docs` - Swagger UI deve carregar

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 3.

---

## Exercício 6: Executar Smoke Tests em Produção

### Objetivo
Validar que a API funciona corretamente em produção.

### Tarefas
1. **Teste Health Check:**
```bash
curl https://sua-api.railway.app/health
```
**Esperado:** `{"status": "healthy", ...}`

2. **Teste Swagger UI:**
- Acesse `https://sua-api.railway.app/docs` no navegador
- Verifique que interface carrega

3. **Teste Login:**
```bash
curl -X POST https://sua-api.railway.app/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```
**Esperado:** Token retornado

4. **Teste Endpoint Protegido:**
```bash
# Use o token do passo anterior
curl https://sua-api.railway.app/conversations \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```
**Esperado:** Lista de conversas (pode estar vazia)

5. **Crie script Python de smoke tests:**
Crie arquivo `smoke_tests.py`:

```python
import requests

BASE_URL = "https://sua-api.railway.app"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    print("✅ Health check OK")

def test_login():
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": "admin", "password": "admin123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    print("✅ Login OK")
    return data["access_token"]

def test_protected_endpoint(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/conversations", headers=headers)
    assert response.status_code == 200
    print("✅ Protected endpoint OK")

if __name__ == "__main__":
    test_health()
    token = test_login()
    test_protected_endpoint(token)
    print("\n🎉 Todos os smoke tests passaram!")
```

Execute: `python smoke_tests.py`

### Como validar
- Todos os testes devem passar
- Nenhum erro 500 deve aparecer
- Logs devem aparecer no painel do Railway

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 5.

---

## Exercício 7: Documentar URL de Produção

### Objetivo
Criar documentação da API em produção.

### Tarefas
1. Crie arquivo `PRODUCAO.md` com:

```markdown
# API em Produção

## URLs
- **API Base**: https://sua-api.railway.app
- **Swagger UI**: https://sua-api.railway.app/docs
- **ReDoc**: https://sua-api.railway.app/redoc

## Endpoints Principais

### Autenticação
- `POST /login` - Login
- `POST /refresh` - Renovar tokens

### Chat
- `POST /chat` - Enviar mensagem
- `GET /conversations` - Listar conversas
- `GET /conversations/{id}/messages` - Ver mensagens

### Health
- `GET /health` - Health check

## Credenciais de Teste
- Username: admin
- Password: admin123

## Variáveis de Ambiente
- Configuradas no Railway Dashboard
- JWT_SECRET_KEY gerada exclusivamente para produção
```

2. Adicione link para este arquivo no README.md principal do projeto.

### Como validar
- Arquivo está completo e atualizado
- URLs estão corretas e funcionando

---

## Exercício 8: (Opcional) Deploy no Render

### Objetivo
Aprender alternativa ao Railway usando Render.

### Tarefas
1. Siga os passos equivalentes do Exercício 5, mas usando Render:
   - Acesse https://render.com
   - Crie Web Service
   - Configure build/start commands
   - Configure variáveis de ambiente
   - Faça deploy

2. Compare Railway vs Render:
   - Qual foi mais fácil de usar?
   - Qual tem melhor interface?
   - Qual tem melhor documentação?

### Como validar
- API funciona em ambos os serviços
- Você consegue escolher qual prefere

### Dica
Consulte `GUIA_APRENDIZADO.md` seção 4.

---

## 🎯 Critérios de Sucesso

Complete pelo menos os exercícios 1-7 antes de considerar o dia completo:

- [ ] Exercício 1: Metadados personalizados
- [ ] Exercício 2: Tags e descrições
- [ ] Exercício 3: Exemplos nos modelos
- [ ] Exercício 4: Checklist de deploy
- [ ] Exercício 5: Deploy no Railway
- [ ] Exercício 6: Smoke tests passando
- [ ] Exercício 7: Documentação de produção

---

**Última atualização:** 15 Dez 2025

