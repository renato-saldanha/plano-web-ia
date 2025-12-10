# 🎯 Contexto para Construir o Dia 3

## 📚 O que aprendemos hoje (Dia 2)

### Conceitos Principais
- JWT (JSON Web Tokens): estrutura header.payload.signature
- Diferença entre access token (curta duração) e refresh token (longa duração)
- Password hashing com bcrypt via passlib
- FastAPI `Depends()` para criar guards de autenticação
- OAuth2PasswordBearer para extrair tokens do header Authorization

### Habilidades Desenvolvidas
- Criar e verificar tokens JWT com python-jose
- Implementar fluxo completo de login/refresh
- Proteger rotas com dependencies
- Hashear senhas de forma segura
- Testar endpoints autenticados com curl/httpie

### Código Criado
- `template.py` (ou versão completa) com:
  - `POST /login` - Autenticação e geração de tokens
  - `POST /refresh` - Renovação de tokens
  - `GET /chat` - Rota protegida
  - Funções `create_access_token`, `create_refresh_token`, `verify_token`
  - Dependency `get_current_user`

---

## 🔗 Por que o Dia 3 é importante

- Temos API segura, mas `/chat` ainda retorna resposta fixa (placeholder)
- Precisamos integrar LLM real (Claude/GPT) para respostas inteligentes
- Streaming é essencial para UX moderna (estilo ChatGPT)
- Combinar auth + streaming + LLM = API pronta para produção

---

## 🎯 O que será feito no Dia 3

### Objetivo Principal
Implementar streaming de respostas com `StreamingResponse` e integrar LLM real (LangChain) no endpoint `/chat` protegido.

### Conceitos que serão aprendidos
- `StreamingResponse` do FastAPI
- Async generators em Python
- Server-Sent Events (SSE) para streaming
- LangChain com streaming callbacks
- Integração LLM (Claude/GPT) via API

### Como se relaciona com Dia 2
- Reutiliza toda a estrutura de autenticação JWT
- `/chat` continua protegido, mas agora retorna resposta do LLM
- Adiciona `/api/generate` como novo endpoint de streaming
- Mantém `/login` e `/refresh` sem alterações

---

## 📋 Como Construir o Dia 3

### 1. Criar Estrutura Básica
```
Dia3/
├── README.md
├── CONTEXTO_AGENTE.md
├── checklist.md
├── journal.md
├── requirements.txt (adicionar langchain, httpx-sse)
├── CONTEXTO_PROXIMO_DIA.md
│
├── template.py (TODOs para streaming)
├── GUIA_APRENDIZADO.md (conceitos de streaming + LLM)
├── exemplo_referencia.py (implementação completa)
└── exercicios.md (otimizações e variações)
```

### 2. Definir Nível de Scaffolding
- Streaming é conceito parcialmente conhecido (visto no Dia 1 com `StreamingResponse`)
- LangChain já foi usado na Semana 2
- Recomendação: **Nível 2** (aplicação em novo contexto)

### 3. Arquivos necessários
- `template.py`: Estrutura com TODOs para:
  - Async generator que gera chunks
  - Endpoint `/api/generate` com StreamingResponse
  - Integração LangChain com streaming callback
  - Modificar `/chat` para usar LLM real
- `GUIA_APRENDIZADO.md`: 
  - Seção 1: StreamingResponse e async generators
  - Seção 2: Server-Sent Events (SSE)
  - Seção 3: LangChain streaming com callbacks
  - Seção 4: Implementação passo a passo
- `exemplo_referencia.py`: Código completo funcionando
- `exercicios.md`: 
  - Exercício 1: Adicionar typing indicator
  - Exercício 2: Implementar cancelamento de stream
  - Exercício 3: Rate limiting por usuário
  - Exercício 4: Cache de respostas

### 4. Endpoints a implementar no Dia 3
```
POST /api/generate
- Body: {"prompt": "...", "model": "gpt-3.5-turbo"}
- Header: Authorization: Bearer <token>
- Response: text/event-stream (SSE)

POST /chat (modificado)
- Body: {"message": "...", "stream": true/false}
- Header: Authorization: Bearer <token>
- Response: Streaming ou JSON
```

### 5. Checklist sugerido
- Preparação (5min): Revisar README, instalar deps (langchain, httpx-sse)
- Leitura (20min): GUIA_APRENDIZADO seções 1-3
- Construção (90min):
  - Implementar async generator básico (20min)
  - Criar endpoint `/api/generate` com SSE (30min)
  - Integrar LangChain com streaming callback (25min)
  - Modificar `/chat` para usar LLM (15min)
- Consolidação (25min): Testar streaming no navegador e curl
- Registro (20min): Journal e CONTEXTO_PROXIMO_DIA

---

## 📚 Recursos de Preparação

### O que revisar antes de começar:
- [ ] FastAPI StreamingResponse: https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse
- [ ] Async generators em Python: https://peps.python.org/pep-0525/
- [ ] LangChain Streaming: https://python.langchain.com/docs/how_to/streaming/
- [ ] Server-Sent Events: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events

### Conceitos pré-requisitos:
- Async/await em Python (usado no Dia 1-2)
- StreamingResponse básico (visto no Dia 1)
- LangChain básico (Semana 2)
- JWT Authentication (Dia 2)

### Dependências adicionais:
```
langchain>=0.1.0
langchain-openai>=0.0.5  # ou langchain-anthropic
httpx>=0.25.0
sse-starlette>=1.8.0
```

---

## 💡 Dicas Importantes

1. **Copiar base do Dia 2**: Use o `exemplo_referencia.py` do Dia 2 como ponto de partida
2. **Testar streaming no navegador**: Use `/docs` do FastAPI ou página HTML simples
3. **Variáveis de ambiente**: Adicionar `OPENAI_API_KEY` ou `ANTHROPIC_API_KEY`
4. **Se tempo exceder 160min**: Mover exercícios extras para Dia 4

---

## 🔍 Exemplo de código para Dia 3

### Async Generator básico
```python
async def generate_response(prompt: str):
    """Async generator que simula streaming."""
    words = prompt.split()
    for word in words:
        yield f"data: {word}\n\n"
        await asyncio.sleep(0.1)
    yield "data: [DONE]\n\n"
```

### StreamingResponse com SSE
```python
from fastapi.responses import StreamingResponse

@app.post("/api/generate")
async def generate(
    request: GenerateRequest,
    current_user: dict = Depends(get_current_user)
):
    return StreamingResponse(
        generate_response(request.prompt),
        media_type="text/event-stream"
    )
```

### LangChain com streaming callback
```python
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)
```

---

**Última atualização:** 10 Dez 2025  
**Status:** 🟡 Pronto como briefing para o Dia 3


