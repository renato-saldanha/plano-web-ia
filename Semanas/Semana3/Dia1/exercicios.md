# 🏋️ Exercícios - Dia 1 (Nível 1)

Objetivo: consolidar o setup FastAPI e preparar terreno para JWT/LLM.

---

## Exercício 1 — CORS seguro (15min)
- Ajuste `ALLOWED_ORIGINS` para incluir apenas as origens que você usará hoje.
- Teste com `curl` adicionando um header `Origin:` e verifique se a resposta inclui `access-control-allow-origin`.

## Exercício 2 — Validação estrita (15min)
- Adicione um campo opcional `temperature: float | None` em `ChatRequest` com limites (0-1).
- Teste enviando valores inválidos e observe o erro 422.

## Exercício 3 — Logs estruturados (15min)
- Inclua no `metadata` da resposta um `request_id` simples (ex.: `uuid4`).
- Registre nos logs o `request_id` junto com o payload.

## Exercício 4 — Esboço de streaming (20min)
- Esboce uma função `async def stream_reply(...)` retornando `StreamingResponse` com 3 chunks de texto simulando tokens.
- Não precisa integrar ao `/chat`; apenas deixe a função pronta para Dia 2/3.

## Exercício 5 — Testes rápidos (20min)
- Usando `httpx.AsyncClient`, escreva um teste simples para `/health` e `/chat` (eco) em um arquivo temporário `test_api.py`.
- Rode os testes e registre saídas no journal.

---

### Dicas
- Consulte FastAPI Docs (Response Model, Middleware, StreamingResponse).
- Mantenha o tempo total do dia dentro de 160min; se estourar, leve para o próximo dia.

