# 💪 Exercícios - Dia 4

## Exercício 1: Testar Fluxo Básico

**Objetivo:** Validar criação de conversa e envio de mensagens.

**Passos:**
1. Fazer login e obter token
2. Enviar primeira mensagem ao `/chat` sem `conversation_id`
3. Anotar o `conversation_id` retornado
4. Enviar segunda mensagem usando o mesmo `conversation_id`
5. Verificar que o LLM lembra da primeira mensagem

**Validação:**
- Primeira resposta deve incluir `conversation_id`
- Segunda resposta deve referenciar conteúdo da primeira mensagem

---

## Exercício 2: Testar Listagem de Conversas

**Objetivo:** Validar endpoint de listagem.

**Passos:**
1. Criar 2-3 conversas diferentes (enviando mensagens sem `conversation_id`)
2. Chamar `GET /conversations`
3. Verificar que todas as conversas aparecem
4. Verificar ordenação (mais recente primeiro)

**Validação:**
- Todas as conversas criadas aparecem na lista
- Campos `id`, `created_at`, `last_message`, `message_count` estão preenchidos

---

## Exercício 3: Testar Recuperação de Histórico

**Objetivo:** Validar recuperação de mensagens de uma conversa.

**Passos:**
1. Criar conversa e enviar 3-4 mensagens
2. Anotar `conversation_id`
3. Chamar `GET /conversations/{id}/messages`
4. Verificar que todas as mensagens aparecem em ordem

**Validação:**
- Todas as mensagens (user + assistant) aparecem
- Ordem cronológica correta
- Campos `role`, `content`, `timestamp` preenchidos

---

## Exercício 4: Testar Streaming com Histórico

**Objetivo:** Validar que streaming funciona com histórico.

**Passos:**
1. Criar conversa e enviar 1 mensagem
2. Enviar segunda mensagem com `stream: true` e mesmo `conversation_id`
3. Verificar que tokens chegam via SSE
4. Após streaming, verificar que mensagens foram salvas

**Validação:**
- Streaming funciona corretamente
- Após streaming, chamar `GET /conversations/{id}/messages` e verificar que ambas mensagens (user + assistant) foram salvas

---

## Exercício 5: Testar Segurança (Isolamento por Usuário)

**Objetivo:** Validar que usuários não podem acessar conversas de outros.

**Passos:**
1. Criar conta 1 e conversa, anotar `conversation_id`
2. Fazer logout
3. Criar conta 2 (ou usar outro usuário)
4. Tentar acessar `GET /conversations/{id}/messages` com `conversation_id` da conta 1

**Validação:**
- Deve retornar 404 (não encontrado)
- Não deve expor mensagens de outros usuários

---

## Desafio Opcional: Adicionar Limite de Mensagens

**Objetivo:** Implementar limite de mensagens mantidas no histórico (ex: últimas 50).

**Passos:**
1. Modificar função `get_messages()` para retornar apenas últimas N mensagens
2. Testar com conversa que tem mais de N mensagens
3. Verificar que LLM ainda recebe contexto suficiente

**Dica:** Use `messages[-N:]` para pegar últimas N mensagens.

---

**Tempo estimado:** 30-40 minutos para exercícios 1-5  
**Tempo estimado (desafio):** 15 minutos adicional