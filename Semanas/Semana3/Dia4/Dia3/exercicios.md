# 🧪 Exercícios - Dia 3 (Streaming + LLM)

Nível: 2 (prática assistida). Se o tempo exceder 160min, mover para buffer ou Dia 4.

## Exercício 1 — Typing indicator (SSE)
- Adicione um evento inicial: `data: [TYPING]\n\n` antes dos tokens.
- Ao finalizar, envie `data: [DONE]\n\n`.
- Teste no curl e confirme que o cliente recebe o indicador antes do conteúdo.

## Exercício 2 — Cancelamento de stream
- Adicione suporte a cancelamento via flag global ou timeout curto.
- Dica: envolva `stream_llm` em `asyncio.timeout(20)` e trate `TimeoutError` enviando `data: [CANCELLED]\n\n`.

## Exercício 3 — Rate limit por usuário
- Reaplique slowapi ou middleware simples por `Authorization` header (ex.: 5 req/min).
- Retorne 429 em excesso e teste com duas requisições rápidas.

## Exercício 4 — Cache de resposta curta
- Para prompts curtos (<120 chars), guarde última resposta em dicionário e retorne sem chamar o LLM.
- Invalide cache a cada execução do servidor (memória).

## Exercício 5 — Teste rápido automatizado
- Usando httpx AsyncClient, escreva um teste que:
  - obtenha token em `/login`
  - chame `/api/generate` e verifique cabeçalho `content-type` e presença de `data:`

## Exercício 6 — Modo não-stream
- Ajuste `/chat` para aceitar `stream=false` e retornar JSON; já proposto no template.
- Verifique que a resposta consolida todos os tokens.

## Critérios de saída
- SSE funciona com typing indicator.
- 429 em excesso de chamadas (se rate limit implementado).
- Teste automatizado básico passando.

