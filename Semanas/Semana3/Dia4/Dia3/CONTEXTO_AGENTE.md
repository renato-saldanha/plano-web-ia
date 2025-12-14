# 🤖 Contexto para Agentes IA

## 📍 Localização
- **Projeto:** Plano 2 meses Web + IA
- **Semana:** 3 de 8 — Backend FastAPI + IA
- **Dia:** 3 de 7 (Quarta, 11 Dez 2025)
- **Diretório:** `Semanas/Semana3/Dia3/`

## 🎯 Estado Atual
- ✅ Dia 1: FastAPI básico (`/health`, `/chat`, CORS)
|- ✅ Dia 2: Autenticação JWT (login, refresh, `/chat` protegido)
- 🟡 Dia 3: Streaming + LLM real via LangChain/LangGraph

## 🧭 Objetivo do Dia
Implementar streaming de respostas (SSE) em FastAPI, integrando um LLM real e protegendo os endpoints com o JWT do Dia 2.

## 📌 Tarefas do Dia (resumo do checklist)
1) Preparação: abrir checklist, ativar venv, exportar chaves.  
2) Leitura: `GUIA_APRENDIZADO.md` (StreamingResponse, SSE, LangChain streaming).  
3) Construção: completar `template.py` com `/api/generate` (SSE) e `/chat` usando LLM real.  
4) Consolidação: testar `/login`, `/refresh`, `/api/generate` (SSE) e `/chat` com token.  
5) Registro: preencher checklist, `journal.md` e `CONTEXTO_PROXIMO_DIA.md`.

## 🔑 Dependências e Configuração
- **Ambiente:** Python 3.12 recomendado (evita warnings Pydantic).
- **Env vars:**  
  - `JWT_SECRET_KEY`, `JWT_ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`, `REFRESH_TOKEN_EXPIRE_DAYS` (herdados do Dia 2)  
  - `OPENAI_API_KEY` (ou `GROQ_API_KEY`/`ANTHROPIC_API_KEY` se trocar o provedor)
- **Stack:** FastAPI, LangChain + LangGraph (API moderna), SSE.
- **Padrão:** streaming com `StreamingResponse(media_type="text/event-stream")`.

## 🗺️ Próximos Passos (hoje)
1. Implementar async generator que formata SSE (`data: ...\\n\\n`).  
2. Integrar LLM com streaming (`ChatOpenAI(streaming=True).astream(...)`).  
3. Proteger `/api/generate` e `/chat` com `Depends(get_current_user)`.  
4. Testar via curl e `/docs` (auth Bearer).  
5. Atualizar `CONTEXTO_PROXIMO_DIA.md` com aprendizados e pendências.

## 📚 Referências Rápidas
- `../../METODOLOGIA_ENSINO.md`
- `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- FastAPI StreamingResponse
- MDN SSE
- LangGraph docs (API moderna)

**Status:** 🟡 Em progresso  
**Última atualização:** 11 Dez 2025

