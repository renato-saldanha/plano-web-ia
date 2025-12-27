# Módulos Compartilhados - Semana 3

Este diretório contém módulos compartilhados entre os dias da Semana 3, reduzindo duplicação de código e complexidade acumulada.

## Estrutura

### `logging.py`
- `JSONFormatter`: Formatter que serializa logs em formato JSON
- `log_structured()`: Função helper para logging estruturado
- `setup_logger()`: Configura logger com JSONFormatter

### `auth.py`
- `verify_token()`: Verifica e decodifica token JWT
- `get_current_user()`: Dependency do FastAPI para autenticação
- `create_access_token()`: Cria access token JWT
- `create_refresh_token()`: Cria refresh token JWT

### `models.py`
- Modelos Pydantic compartilhados:
  - `Message`: Mensagem de chat
  - `ConversationSummary`: Resumo de conversa
  - `ChatRequest`: Requisição de chat
  - `Token`: Tokens JWT
  - `LoginRequest`: Requisição de login
  - `RefreshRequest`: Requisição de refresh
  - `GenerateRequest`: Requisição de geração

### `conversations.py`
- `conversations`: Armazenamento em memória (dict global)
- `get_or_create_conversation()`: Obtém ou cria conversa
- `add_message()`: Adiciona mensagem à conversa
- `get_messages()`: Obtém mensagens de uma conversa
- `list_conversations()`: Lista conversas do usuário

## Uso

```python
# Importar módulos compartilhados
from common import (
    log_structured,
    get_current_user,
    create_access_token,
    ChatRequest,
    get_or_create_conversation,
)

# Usar em endpoints
@app.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    user_id = current_user["username"]
    conversation_id = get_or_create_conversation(user_id, request.conversation_id)
    
    log_structured("INFO", "Chat iniciado", user_id=user_id)
    # ...
```

## Benefícios

1. **Redução de duplicação**: Código compartilhado não precisa ser reescrito
2. **Manutenibilidade**: Mudanças em um lugar afetam todos os dias
3. **Consistência**: Garante que todos os dias usam a mesma implementação
4. **Complexidade reduzida**: Arquivos dos dias ficam menores e mais focados

## Notas

- Os módulos são importados a partir do Dia 5 em diante
- Dias anteriores (1-4) podem ser atualizados opcionalmente para usar estes módulos
- O armazenamento de conversas é em memória (dict global) - adequado para aprendizado, mas não para produção

