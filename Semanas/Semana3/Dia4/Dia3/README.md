# 📅 Dia 3 - Quarta (11 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **terceiro dia** da Semana 3 do plano de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto
- **Objetivo do Dia:** Implementar streaming de respostas com FastAPI + SSE, integrando LLM via LangChain/LangGraph e protegendo os endpoints com o JWT criado no Dia 2.
- **Duração estimada:** 160min totais (leitura + código + testes + documentação) — **sem autocomplete/IA escrevendo código**.
- **Foco:** StreamingResponse + SSE + callbacks de streaming do LLM.

### 🗺️ Estrutura do Plano
- **Semana 3:** Backend FastAPI + IA (9-15 Dez)
- **Dia 2 (concluído):** Autenticação JWT e proteção de rotas ✅
- **Dia 3 (hoje):** Streaming + integração LLM real
- **Dia 4 (próximo):** Testes automatizados / hardening (rate limit + observabilidade)

### 📁 Arquivos neste diretório
- `README.md` — Contexto do dia (este arquivo)
- `CONTEXTO_AGENTE.md` — Estado, dependências e próximos passos
- `checklist.md` — Checklist dividido em 6 blocos (total 160min)
- `journal.md` — Journal para preenchimento ao final
- `requirements.txt` — Dependências Python (obrigatório)
- `CONTEXTO_PROXIMO_DIA.md` — Briefing para construir o Dia 4
- **Scaffolding Nível 2:** `template.py`, `GUIA_APRENDIZADO.md`, `exemplo_referencia.py`, `exercicios.md`

### 🎯 O que você vai aprender
1. `StreamingResponse` com async generators
2. Formato Server-Sent Events (SSE) para streaming de tokens
3. Streaming de LLM com LangChain/LangGraph (`langchain_openai.ChatOpenAI` + `astream`)

### 💡 Notas Importantes
- **Baseado em:** Dia 2 (JWT + rotas protegidas). Reaproveite `get_current_user`/verificação de token.
- **Foco:** UX moderna estilo ChatGPT (tokens em tempo real) e uso seguro com auth.
- **Nível de Scaffolding:** 2 (conceito parcialmente conhecido; aplicação em novo contexto).

### 🔗 Referências
- Plano macro: `../../1-Plano_Desenvolvimento.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Decisão de scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- FastAPI StreamingResponse: https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse
- SSE: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
- LangGraph (API moderna): https://python.langchain.com/docs/langgraph
- LangChain streaming: https://python.langchain.com/docs/how_to/streaming

---

**Status:** 🟡 Em progresso  
**Última atualização:** 11 Dez 2025

