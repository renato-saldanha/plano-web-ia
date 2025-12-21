# 📚 Guia de Aprendizado - Swagger/OpenAPI e Deploy em Produção

Este guia cobre os conceitos essenciais para configurar documentação interativa (Swagger/OpenAPI) no FastAPI e fazer deploy da API em produção (Railway ou Render).

---

## 1. Swagger/OpenAPI no FastAPI

### O que é Swagger/OpenAPI?

**OpenAPI** (antigamente Swagger) é uma especificação para documentar APIs REST. O FastAPI gera automaticamente documentação OpenAPI 3.0 que pode ser visualizada no **Swagger UI** (interface interativa) ou **ReDoc** (documentação alternativa).

### Por que documentar a API?

- **Facilita uso:** Desenvolvedores podem testar a API diretamente no navegador
- **Gera confiança:** API documentada parece mais profissional
- **Reduz suporte:** Menos perguntas sobre como usar a API
- **Padrão da indústria:** OpenAPI é o padrão para documentação de APIs REST

### Documentação Automática do FastAPI

O FastAPI gera automaticamente:
- **Swagger UI:** Disponível em `/docs` (padrão)
- **ReDoc:** Disponível em `/redoc` (padrão)
- **OpenAPI JSON:** Disponível em `/openapi.json` (padrão)

### Configurando Metadados OpenAPI

Para personalizar a documentação, você configura metadados ao criar a instância do FastAPI:

```python
from fastapi import FastAPI

app = FastAPI(
    title="Minha API",
    description="Descrição detalhada da API",
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seu.email@exemplo.com",
    },
    license_info={
        "name": "MIT",
    },
)
```

### Tags para Organizar Endpoints

Tags agrupam endpoints relacionados no Swagger UI:

```python
@app.post("/login", tags=["Auth"])
async def login():
    """Endpoint de login."""
    pass

@app.post("/chat", tags=["Chat"])
async def chat():
    """Endpoint de chat."""
    pass

@app.get("/health", tags=["Health"])
async def health():
    """Health check."""
    pass
```

### Descrições e Exemplos nos Modelos Pydantic

Você pode adicionar descrições e exemplos nos modelos:

```python
from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(
        ...,
        description="Nome de usuário",
        example="admin"
    )
    password: str = Field(
        ...,
        description="Senha do usuário",
        example="admin123"
    )
```

### Descrições nos Endpoints

Adicione docstrings e descrições nos endpoints:

```python
@app.post("/chat", tags=["Chat"])
async def chat(chat_request: ChatRequest):
    """
    Endpoint de chat com histórico.
    
    - **message**: Mensagem do usuário
    - **conversation_id**: ID da conversa (opcional, cria nova se não fornecido)
    - **model**: Modelo LLM a usar (opcional)
    - **stream**: Se true, responde via SSE (padrão: true)
    """
    pass
```

### Respostas Customizadas

Você pode especificar possíveis respostas:

```python
from fastapi.responses import JSONResponse

@app.post(
    "/login",
    response_model=Token,
    status_code=200,
    responses={
        200: {
            "description": "Login bem-sucedido",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJ...",
                        "refresh_token": "eyJ...",
                        "token_type": "bearer"
                    }
                }
            }
        },
        401: {
            "description": "Credenciais inválidas",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Usuário inválido"
                    }
                }
            }
        }
    }
)
async def login(login_data: LoginRequest):
    pass
```

---

## 2. Checklist de Deploy

### Variáveis de Ambiente Necessárias

Antes de fazer deploy, liste todas as variáveis de ambiente:

```env
# Segurança
JWT_SECRET_KEY=sua_chave_secreta_super_segura_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# OpenAI
OPENAI_API_KEY=sk-...

# Ambiente
ENVIRONMENT=production
```

### Configurações de Segurança

- ✅ **JWT_SECRET_KEY:** Use uma chave forte e única em produção
- ✅ **HTTPS:** Configure HTTPS (Railway/Render fazem isso automaticamente)
- ✅ **CORS:** Configure origins permitidas corretamente
- ✅ **Headers de segurança:** Já implementados no middleware

### Logging em Produção

O logging estruturado já está implementado. Em produção:
- Logs são enviados para stdout/stderr
- Railway/Render capturam esses logs automaticamente
- Você pode ver logs no painel da plataforma

### Health Checks

Endpoints de health check são importantes para:
- **Monitoramento:** Ferramentas podem verificar se API está online
- **Load balancers:** Saber quando redirecionar tráfego

Já temos `/health` implementado. Certifique-se de que retorna rapidamente.

---

## 3. Deploy no Railway

### Criando Conta no Railway

1. Acesse https://railway.app
2. Clique em "Login" e autentique com GitHub
3. Railway é gratuito para começar

### Criando Projeto

1. No dashboard do Railway, clique em "New Project"
2. Selecione "Deploy from GitHub repo"
3. Escolha o repositório do seu projeto
4. Railway detectará automaticamente que é Python

### Configurando Variáveis de Ambiente

1. No projeto, vá em "Variables"
2. Adicione cada variável de ambiente:
   - `JWT_SECRET_KEY` (gere uma nova para produção!)
   - `ALGORITHM`
   - `ACCESS_TOKEN_EXPIRE_MINUTES`
   - `REFRESH_TOKEN_EXPIRE_DAYS`
   - `OPENAI_API_KEY`

### Configurando Comando de Start

1. No projeto, vá em "Settings"
2. Em "Start Command", configure:
   ```
   uvicorn template:app --host 0.0.0.0 --port $PORT
   ```
   (Railway define `$PORT` automaticamente)

### Fazendo Deploy

1. Railway faz deploy automaticamente ao fazer push para o branch conectado
2. Ou clique em "Deploy" no dashboard
3. Aguarde o build e deploy completarem

### Verificando Logs

1. No projeto, vá em "Deployments"
2. Clique no deployment mais recente
3. Vá em "Logs" para ver logs em tempo real

### Obtendo URL de Produção

1. No projeto, vá em "Settings"
2. Em "Domains", você verá a URL gerada
3. Ou configure um domínio customizado

---

## 4. Deploy no Render (Alternativa)

### Criando Conta no Render

1. Acesse https://render.com
2. Clique em "Get Started" e autentique com GitHub
3. Render tem tier gratuito

### Criando Web Service

1. No dashboard, clique em "New +"
2. Selecione "Web Service"
3. Conecte seu repositório GitHub

### Configurações

1. **Name:** Nome do serviço
2. **Environment:** Python 3
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `uvicorn template:app --host 0.0.0.0 --port $PORT`

### Variáveis de Ambiente

1. No serviço, vá em "Environment"
2. Adicione cada variável de ambiente (mesmas do Railway)

### Fazendo Deploy

1. Render faz deploy automático ao fazer push
2. Ou clique em "Manual Deploy" no dashboard

### URL de Produção

1. Render gera URL automaticamente: `seu-servico.onrender.com`
2. Ou configure domínio customizado em "Settings" → "Custom Domain"

---

## 5. Smoke Tests em Produção

### O que são Smoke Tests?

**Smoke tests** são testes básicos que verificam se a API está funcionando em produção. São rápidos e focam em funcionalidades críticas.

### Testando Endpoints Principais

#### 1. Health Check

```bash
curl https://sua-api.railway.app/health
```

**Esperado:** `{"status": "healthy", ...}`

#### 2. Swagger UI

Acesse no navegador:
```
https://sua-api.railway.app/docs
```

**Esperado:** Interface Swagger UI carregando e mostrando todos os endpoints

#### 3. Autenticação

```bash
curl -X POST https://sua-api.railway.app/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Esperado:** Token de acesso retornado

#### 4. Endpoint Protegido

```bash
curl https://sua-api.railway.app/conversations \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

**Esperado:** Lista de conversas (pode estar vazia)

#### 5. Chat (se implementado)

```bash
curl -X POST https://sua-api.railway.app/chat \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{"message": "Olá!", "stream": false}'
```

**Esperado:** Resposta da IA

### Script de Smoke Tests

Você pode criar um script Python para automatizar:

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

---

## 6. Monitoramento Básico

### Logs em Produção

Railway e Render capturam logs automaticamente:
- Acesse logs no dashboard da plataforma
- Logs estruturados (JSON) facilitam análise
- Configure alertas para erros críticos

### Métricas

Railway e Render fornecem métricas básicas:
- Uso de CPU/RAM
- Requisições por minuto
- Tempo de resposta

### Alertas

Configure alertas para:
- Erros 5xx (erros do servidor)
- Tempo de resposta alto
- Alto uso de recursos

---

## 7. Melhorias Futuras

Após deploy básico, considere:

1. **CI/CD:** GitHub Actions para deploy automático
2. **Banco de dados:** Substituir armazenamento em memória por PostgreSQL
3. **Cache:** Redis para rate limiting distribuído
4. **Monitoramento:** Integração com Sentry, DataDog, etc.
5. **CDN:** Para assets estáticos (se houver)

---

## 📚 Referências

- FastAPI OpenAPI: https://fastapi.tiangolo.com/tutorial/metadata/
- Railway Docs: https://docs.railway.app/
- Render Docs: https://render.com/docs
- Swagger UI: https://swagger.io/tools/swagger-ui/
- OpenAPI Specification: https://swagger.io/specification/

---

**Última atualização:** 15 Dez 2025

