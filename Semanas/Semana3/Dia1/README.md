# 📅 Dia 1 - Terça (9 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **décimo quinto dia** do plano de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto
- **Objetivo do Dia:** Subir o esqueleto FastAPI com endpoints básicos (`/health` e `/chat` modo eco/LLM placeholder), preparando segurança mínima e ambiente para a semana de backend + IA.
- **Duração estimada:** 2h30-2h40 (160min exatos).
- **Foco:** Setup FastAPI + Pydantic v2, rotas iniciais, CORS básico, logs e placeholders para integração com LLM.

### 🗺️ Estrutura do Plano
- **Semana 3:** Backend FastAPI + IA (9-15 Dez)
- **Dia 0 (concluído):** Handoff do Dia 7 da Semana 2 ✅
- **Dia 1 (hoje):** Setup FastAPI + endpoints básicos 🟡
- **Dia 2 (próximo):** Autenticação JWT + hardening inicial

### 📁 Arquivos neste diretório
- `README.md` — Este arquivo (contexto do dia)
- `CONTEXTO_AGENTE.md` — Estado, stack e próximos passos
- `checklist.md` — Checklist 160min
- `journal.md` — Registro do dia (preencher)
- `requirements.txt` — Dependências Python do dia
- `CONTEXTO_PROXIMO_DIA.md` — Handoff para o Dia 2
- `exemplo_completo.py` — FastAPI nível 1 com `/health` e `/chat`
- `GUIA_PASSO_A_PASSO.md` — Setup guiado passo a passo (Nível 1)
- `exercicios.md` — Desafios incrementais de setup/segurança

### 🎯 O que você vai aprender/praticar
1. Inicializar um serviço HTTP com FastAPI + Pydantic v2.
2. Implementar validação de entrada e respostas padronizadas.
3. Preparar terreno para streaming/LLM e autenticação futura.

### 💡 Notas Importantes
- **Baseado em:** Semana 2 (agents + RAG) → agora expomos via HTTP.
- **Nível de Scaffolding:** **Nível 1 (Iniciante)** — conceito novo (FastAPI). Justificativa: setup + padrões iniciais exigem exemplo completo e guia detalhado (`../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`).
- **Pré-requisitos:** Python 3.12, venv ativo, `.env` com chaves de LLM se for testar integração.
- **Stack:** FastAPI, Pydantic v2, Uvicorn; LLM placeholder para eco ou integração posterior.

### 🔗 Referências
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- FastAPI Docs: https://fastapi.tiangolo.com/
- LangChain/LangGraph overview: https://docs.langchain.com/oss/python/langchain/overview

---

**Status:** 🟡 Em progresso  
**Última atualização:** 9 Dez 2025

