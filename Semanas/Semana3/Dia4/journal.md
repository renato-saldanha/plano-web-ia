# 📝 Journal - Dia 4 (Quinta, 12 Dez 2025)

## 🎯 Objetivo do Dia
Implementar sistema de histórico de conversas para manter contexto entre mensagens no `/api/chat`.

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [x] Implementar modelos Pydantic (Message, ConversationSummary, ChatRequest)
- [x] Criar estrutura de armazenamento em memória (conversations dict)
- [x] Implementar funções auxiliares de histórico:
  - `get_or_create_conversation()` - ⚠️ com bugs
  - `add_message()` - ✅ completo
  - `get_messages()` - ✅ completo
  - `list_conversations()` - ⚠️ com bug
- [x] Modificar endpoint `/chat` para usar histórico
- [x] Criar endpoint `GET /conversations`
- [x] Criar endpoint `GET /conversations/{id}/messages`

### Detalhes das Tarefas
- Implementação do sistema de histórico de conversas
- Integração com LangChain para manter contexto entre mensagens
- Endpoints RESTful para gerenciar conversas
- Identificados 5 bugs que precisam correção antes dos testes

---
-
## 🎓 O que aprendi hoje?

### Conceitos Novos
- Sistema de histórico de conversas em memória usando dicts aninhados
- Estrutura: `{user_id: {conversation_id: [messages]}}`
- Como integrar histórico com LangChain (HumanMessage/AIMessage)
- Streaming com histórico (acumular resposta completa antes de salvar)
- Dependency Injection do FastAPI para autenticação

### Ferramentas Utilizadas
- FastAPI (endpoints, dependencies, streaming)
- LangChain (ChatOpenAI, HumanMessage, AIMessage)
- Pydantic (validação de modelos)
- uuid (geração de IDs únicos)
- datetime (timestamps ISO format)

### Desafios Enfrentados
- Erros de conversão de tipo de dados (dict vs objeto)
- Bugs na verificação de existência de conversas
- Lógica de ordenação com valores None
- Escape incorreto em strings de streaming
- Retorno de objeto em vez de string no JSON

---

### O que funcionou bem?
- Estrutura geral do código está bem organizada
- Modelos Pydantic facilitam validação
- Funções `add_message()` e `get_messages()` funcionam corretamente
- Lógica de streaming está correta
- Segurança (verificação de usuário) implementada

### O que poderia ser melhorado?
- Verificação de bugs antes de considerar completo
- Testes incrementais após cada função
- Remover comentários TODO após implementação
- Melhor tratamento de casos edge (conversas vazias)

### Próximos Passos
- Corrigir 5 bugs identificados (3 críticos, 2 médios)
- Testar servidor e executar exercícios
- Completar documentação (CONTEXTO_PROXIMO_DIA.md)
- Fazer commit do código

---

## 📊 Métricas do Dia

- **Tempo total:** ~120 minutos (estimado)
- **Commits:** 0 (pendente)
- **Linhas de código:** ~675
- **Endpoints criados:** 5 (login, refresh, chat, conversations, conversations/{id}/messages)
- **Testes manuais rodados:** 0 (bloqueado por bugs)
- **Bugs encontrados:** 5 (3 críticos, 2 médios)
- **Funções implementadas:** 4/4 (2 com bugs)

---

## 🔗 Links e Referências Úteis

- 

---

## 📝 Notas Adicionais

_(Espaço livre para anotações)_

---

**Data:** 12 Dez 2025  
**Status:** 🟡 85% Completo - Bugs impedem testes finais

**Bugs a corrigir:**
1. Linha 244: `conversations["user_id"]` → `conversations[user_id]`
2. Linha 247: `conversations` → `conversations[user_id]`
3. Linha 322: Lógica de `created_at` com None
4. Linha 361: Escape `\\n\\n` → `\n\n`
5. Linha 559: `model` (objeto) → `model_name` (string)