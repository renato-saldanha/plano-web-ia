# 📘 GUIA_APRENDIZADO - Dia 3 (Streaming + LLM)

Nível de scaffolding: **2** (conceito parcialmente conhecido; aplicação em novo contexto).

## 1) StreamingResponse
- `StreamingResponse(generator, media_type="text/event-stream")`
- Gera resposta incremental sem armazenar tudo em memória.
- Docs: FastAPI StreamingResponse.

## 2) Async Generators
- Assinatura: `async def gen() -> AsyncIterator[str]: ...`
- Use `async for` para produzir pedaços (tokens).
- Cada `yield` envia um chunk imediatamente ao cliente.

## 3) SSE (Server-Sent Events)
- Formato exige `data: <conteudo>\n\n`
- Cabeçalho: `Content-Type: text/event-stream`
- Última mensagem opcional: `data: [DONE]\n\n`
- Curl para testar: `curl -N http://localhost:8000/api/generate`

## 4) LangChain / LangGraph (API moderna)
- Evite AgentExecutor legado; use LLM com `astream` ou LangGraph.
- Exemplo simples:
  ```python
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import HumanMessage

  llm = ChatOpenAI(model="gpt-4o-mini", streaming=True)
  async for chunk in llm.astream([HumanMessage(content=prompt)]):
      if chunk.content:
          yield f"data: {chunk.content}\\n\\n"
  ```
- Se quiser LangGraph: `from langgraph.prebuilt import create_react_agent` e chame `agent.stream(...)` (opcional para experimentos extras).

## 5) Passo a passo sugerido (template.py)
1. Carregar envs (`load_dotenv`) e definir `DEFAULT_MODEL`.
2. Reutilizar `verify_token` / `get_current_user` do Dia 2.
3. Criar `stream_llm(prompt, model)` com `ChatOpenAI(..., streaming=True)`.
4. Formatar SSE: `yield f"data: {text}\\n\\n"` + `[DONE]`.
5. `/api/generate` → `StreamingResponse` (sempre stream).
6. `/chat` → se `stream=True` retorna SSE; caso contrário, uma resposta única (`ainvoke`).

## 6) Testes rápidos
- Iniciar servidor: `uvicorn template:app --reload --port 8000`
- Autenticar:
  ```bash
  curl -X POST http://localhost:8000/login \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"admin123"}'
  ```
- Gerar streaming:
  ```bash
  curl -N -X POST http://localhost:8000/api/generate \
    -H "Authorization: Bearer <TOKEN>" \
    -H "Content-Type: application/json" \
    -d '{"prompt":"Explique SSE em 3 bullets"}'
  ```

## 7) Troubleshooting
- 401: verifique header `Authorization: Bearer <token>`.
- Sem streaming: confirme `media_type="text/event-stream"` e `curl -N`.
- Resposta vazia: ignore chunks com `chunk.content == ""`.
- LLM não responde: verifique `OPENAI_API_KEY` (ou provider escolhido).

## 8) Boas práticas
- Não bloquear event loop: use `async` / `await`.
- Mantenha mensagens curtas para ver o streaming (prompt pequeno).
- Se exceder 160min, mova exercícios extras para buffer.

