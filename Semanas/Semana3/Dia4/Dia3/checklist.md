# ✅ Checklist - Dia 3 (Quarta, 11 Dez 2025)

## 🎯 Objetivo do Dia
Implementar streaming de respostas (SSE) com FastAPI + LLM via LangChain/LangGraph, protegido por JWT.

> **Regra:** 160min totais (inclui leitura + código + testes + docs). Não use autocomplete/IA para escrever código.
> Marcadores: **[LEIA] [IMPLEMENTE] [EXECUTE] [TESTE] [DOCUMENTE]**

---

## 📋 FASE 1: Preparação (5 min)
- [ X] **[LEIA]** Revisar `README.md` e `CONTEXTO_AGENTE.md` (2 min)
- [ X] **[EXECUTE]** Ativar venv e instalar deps: `pip install -r requirements.txt` (3 min)
- [ ] **[EXECUTE]** Exportar/confirmar envs: `JWT_SECRET_KEY`, `JWT_ALGORITHM`, `OPENAI_API_KEY`

---

## 📋 FASE 2: Leitura Guiada (20 min)
- [ X] **[LEIA]** `GUIA_APRENDIZADO.md` seções 1-4 (StreamingResponse, SSE, async generators, LangChain streaming)
- [ X] **[LEIA]** Skim `exemplo_referencia.py` (não copiar; entender fluxo) (5 min)
- [ X] **[LEIA]** MDN SSE + FastAPI StreamingResponse links (5 min)

---

## 📋 FASE 3: Construção Guiada (90 min)
- [ X] **[IMPLEMENTE]** Completar TODOs em `template.py`:
  - Carregar envs e configurar CORS
  - Reutilizar `get_current_user`/verificação JWT (copiar do Dia 2)
  - Criar `stream_llm(prompt, model)` com `ChatOpenAI(..., streaming=True).astream(...)`
  - Formatar SSE: `yield f"data: {chunk}\\n\\n"` + `[DONE]`
  - Endpoint `POST /api/generate` → `StreamingResponse(..., media_type="text/event-stream")`
  - Endpoint `POST /chat` com opção `stream` (SSE) ou resposta única JSON
- [ X] **[IMPLEMENTE]** Ajustar modelos Pydantic (`GenerateRequest`, `ChatRequest`)
- [ X] **[TESTE]** Rodar `uvicorn template:app --reload --port 8000`

---

## 📋 FASE 4: Consolidação (25 min)
- [ X] **[TESTE]** `POST /login` (Dia 2) e usar token em `/docs`
- [ X] **[TESTE]** `POST /api/generate` com curl SSE:
  ```bash
  curl -N -X POST http://localhost:8000/api/generate \
    -H "Authorization: Bearer <ACCESS_TOKEN>" \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Explique SSE em 3 bullets", "model": "gpt-4o-mini"}'
  ```
- [ X] **[TESTE]** `/chat` com `stream=true` e `stream=false`
- [ X] **[TESTE]** Caso de erro: token inválido → 401

---

## 📋 FASE 5: Registro e Handoff (20 min)
- [ X] **[DOCUMENTE]** Marcar checklist
- [ X] **[DOCUMENTE]** Preencher `journal.md` (tempos, aprendizados, bloqueios)
- [ X] **[DOCUMENTE]** Atualizar `CONTEXTO_PROXIMO_DIA.md` (o que consolidou + foco do Dia 4)

---

## 📋 FASE 6: Buffer (10 min)
- [ ] **[TESTE]** Opcional: tentar exercício extra (typing indicator, cancelamento, cache)

---

## 🎉 Conclusão
**Total:** 160min (5 + 20 + 90 + 25 + 20 + 10)

### ✅ Critérios de Sucesso
- [ X] `/api/generate` retorna tokens via SSE (media_type `text/event-stream`)
- [ X] `/chat` protegido por JWT e responde com LLM real
- [ X] Streaming funcionando no curl e `/docs`
- [ X] Checklist + journal preenchidos
- [ X] `CONTEXTO_PROXIMO_DIA.md` pronto para o Dia 4

