# 📚 Guia de Aprendizado - Histórico de Chat

Este guia explica os conceitos e práticas necessárias para implementar um sistema de histórico de conversas em FastAPI.

---

## 1. Conceitos Fundamentais

### 1.1 Por que Histórico é Importante

**Contexto Continuado:**
- LLMs precisam de contexto completo da conversa para dar respostas coerentes
- Sem histórico, cada mensagem é tratada isoladamente (sem memória)
- Com histórico, o LLM pode referenciar mensagens anteriores

**Exemplo prático:**
```
Usuário: "Meu nome é João"
Assistant: "Olá João! Como posso ajudar?"

# Sem histórico, próxima mensagem:
Usuário: "Qual é meu nome?" 
Assistant: "Não sei seu nome. Como você gostaria de ser chamado?"

# Com histórico:
Usuário: "Qual é meu nome?"
Assistant: "Seu nome é João!"
```

### 1.2 Estrutura de Dados

**Conversa (Conversation/Thread):**
- Identificador único (conversation_id)
- Pertence a um usuário (user_id)
- Contém lista de mensagens ordenadas cronologicamente

**Mensagem (Message):**
- Role: "user" ou "assistant"
- Content: texto da mensagem
- Timestamp: quando foi criada (opcional mas útil)

**Hierarquia:**
```
usuário (user_id)
  └─ conversa 1 (conversation_id_1)
      ├─ mensagem 1 (role: user, content: "Olá")
      ├─ mensagem 2 (role: assistant, content: "Oi! Como posso ajudar?")
      └─ mensagem 3 (role: user, content: "Qual é meu nome?")
  └─ conversa 2 (conversation_id_2)
      └─ mensagem 1 (role: user, content: "Nova conversa")
```

---

## 2. Armazenamento em Memória

### 2.1 Estrutura Simples

Para este dia, usaremos armazenamento em memória (dict). Em produção, você usaria banco de dados.

**Formato:**
```python
conversations = {
    "user_id_1": {
        "conversation_id_1": [
            {"role": "user", "content": "Olá", "timestamp": "2025-12-12T10:00:00"},
            {"role": "assistant", "content": "Oi!", "timestamp": "2025-12-12T10:00:01"},
        ],
        "conversation_id_2": [...]
    },
    "user_id_2": {...}
}
```

### 2.2 Funções Auxiliares

**Criar ou obter conversa:**
```python
def get_or_create_conversation(user_id: str, conversation_id: Optional[str] = None) -> str:
    """
    Retorna conversation_id existente ou cria novo.
    Se conversation_id fornecido e existir, retorna ele.
    Se não existir ou None, cria novo com UUID.
    """
    if user_id not in conversations:
        conversations[user_id] = {}
    
    if conversation_id and conversation_id in conversations[user_id]:
        return conversation_id
    
    # Criar novo
    new_id = str(uuid.uuid4())
    conversations[user_id][new_id] = []
    return new_id
```

**Adicionar mensagem:**
```python
def add_message(user_id: str, conversation_id: str, role: str, content: str):
    """Adiciona mensagem à conversa."""
    if user_id not in conversations:
        conversations[user_id] = {}
    if conversation_id not in conversations[user_id]:
        conversations[user_id][conversation_id] = []
    
    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow().isoformat()
    }
    conversations[user_id][conversation_id].append(message)
```

---

## 3. Integração com LLM

### 3.1 Construindo Contexto

**LangChain usa listas de mensagens:**
```python
from langchain_core.messages import HumanMessage, AIMessage

# Histórico convertido para formato LangChain
history = []
for msg in stored_messages:
    if msg["role"] == "user":
        history.append(HumanMessage(content=msg["content"]))
    elif msg["role"] == "assistant":
        history.append(AIMessage(content=msg["content"]))

# Adicionar nova mensagem
history.append(HumanMessage(content=nova_mensagem))

# Enviar ao LLM
response = await llm.ainvoke(history)
```

### 3.2 Streaming com Histórico

**Para streaming, usar `astream` com histórico:**
```python
async def stream_with_history(messages: list, new_message: str):
    # Construir lista completa
    full_context = messages + [HumanMessage(content=new_message)]
    
    # Stream
    async for chunk in llm.astream(full_context):
        if chunk.content:
            yield chunk.content
```

### 3.3 Limites de Contexto

**Importante:** LLMs têm limite de tokens (context window).
- GPT-4: ~128k tokens
- GPT-3.5: ~16k tokens
- Claude 3.5: ~200k tokens

**Estratégias:**
1. Manter todas as mensagens (ok para conversas curtas)
2. Manter apenas últimas N mensagens (ex: últimas 10)
3. Summarizar mensagens antigas (avançado)

**Para hoje:** Manter todas as mensagens (simplicidade).

---

## 4. Endpoints REST

### 4.1 Modificar `/api/chat`

**Adicionar parâmetro `conversation_id`:**
```python
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None  # Novo!
    model: Optional[str] = None
    stream: bool = True
```

**Lógica do endpoint:**
1. Obter user_id do token JWT
2. Obter ou criar conversation_id
3. Buscar histórico da conversa
4. Construir lista de mensagens (histórico + nova)
5. Chamar LLM com contexto completo
6. Salvar ambas mensagens (user + assistant) no histórico
7. Retornar resposta

### 4.2 Novo Endpoint: Listar Conversas

```python
@app.get("/conversations", response_model=List[ConversationSummary])
async def list_conversations(current_user: dict = Depends(get_current_user)):
    """
    Lista todas as conversas do usuário autenticado.
    Retorna: [{id, created_at, last_message, message_count}]
    """
    user_id = current_user["username"]
    # Buscar conversas do user_id
    # Formatar resposta
```

### 4.3 Novo Endpoint: Obter Mensagens

```python
@app.get("/conversations/{conversation_id}/messages", response_model=List[Message])
async def get_messages(
    conversation_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Retorna todas as mensagens de uma conversa específica.
    """
    user_id = current_user["username"]
    # Buscar mensagens
    # Retornar lista formatada
```

---

## 5. Modelos Pydantic

### 5.1 Message

```python
from datetime import datetime
from typing import Literal

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: Optional[str] = None
```

### 5.2 ConversationSummary

```python
class ConversationSummary(BaseModel):
    id: str
    created_at: str
    last_message: Optional[str] = None
    message_count: int
```

### 5.3 ChatRequest (modificado)

```python
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = Field(None, description="ID da conversa (cria nova se não fornecido)")
    model: Optional[str] = None
    stream: bool = True
```

---

## 6. Fluxo Completo

### 6.1 Primeira Mensagem

1. Cliente: `POST /api/chat` com `{"message": "Olá"}` (sem conversation_id)
2. Backend: Cria nova conversa com UUID
3. Backend: Salva mensagem do usuário
4. Backend: Chama LLM com apenas uma mensagem
5. Backend: Salva resposta do LLM
6. Backend: Retorna resposta + conversation_id

### 6.2 Mensagens Subsequentes

1. Cliente: `POST /api/chat` com `{"message": "Qual é meu nome?", "conversation_id": "..."}`
2. Backend: Busca histórico da conversa
3. Backend: Constrói lista: [mensagem_anterior_user, mensagem_anterior_assistant, nova_mensagem_user]
4. Backend: Chama LLM com contexto completo
5. Backend: Salva ambas mensagens (nova user + nova assistant)
6. Backend: Retorna resposta

---

## 7. Considerações de Segurança

### 7.1 Isolamento por Usuário

**Importante:** Cada usuário só pode acessar suas próprias conversas!

```python
# ❌ ERRADO: Não validar user_id
messages = conversations[conversation_id]

# ✅ CORRETO: Validar user_id
if conversation_id not in conversations.get(user_id, {}):
    raise HTTPException(404, "Conversa não encontrada")
messages = conversations[user_id][conversation_id]
```

### 7.2 Validação de Dados

- Validar que `conversation_id` existe antes de usar
- Validar que `role` é "user" ou "assistant"
- Validar que `content` não está vazio

---

## 8. Exemplos Práticos

### 8.1 Criar Nova Conversa

```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Olá, meu nome é João",
    "stream": false
  }'
```

**Resposta:**
```json
{
  "reply": "Olá João! Como posso ajudar?",
  "conversation_id": "abc-123-def-456",
  "model": "gpt-4o-mini"
}
```

### 8.2 Continuar Conversa

```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Qual é meu nome?",
    "conversation_id": "abc-123-def-456",
    "stream": false
  }'
```

**Resposta:**
```json
{
  "reply": "Seu nome é João!",
  "conversation_id": "abc-123-def-456",
  "model": "gpt-4o-mini"
}
```

---

## 9. Referências

- FastAPI Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/
- LangChain Messages: https://python.langchain.com/docs/concepts/messages/
- LangChain Message History: https://python.langchain.com/docs/how_to/message_history

---

**Próximo passo:** Implementar no `template.py` seguindo os TODOs!