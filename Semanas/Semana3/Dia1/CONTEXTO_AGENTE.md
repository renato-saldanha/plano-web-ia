# 🤖 Contexto para Agentes IA

Resumo do estado, stack e próximos passos para o Dia 1 (setup FastAPI).

---

## 📍 Localização Atual
- **Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
- **Semana:** 3 de 8  
- **Dia:** 1 de 7 (Terça, 9 Dez 2025)  
- **Diretório:** `Semanas/Semana3/Dia1/`

---

## 🎯 Estado Atual do Projeto
### O que veio do dia anterior
- ✅ Knowledge Assistant em LangGraph (CLI/agent) com RAG FAISS e calculator.
- ✅ Handoff pronto (`Semanas/Semana2/Dia7/CONTEXTO_PROXIMO_DIA.md`).

### O que está em progresso (hoje)
- 🟡 Subir esqueleto FastAPI com `/health` e `/chat` (eco/placeholder LLM).
- 🟡 Configurar CORS básico, logs e estrutura de validação com Pydantic v2.

### O que falta fazer (hoje)
- [ ] Criar rotas `/health` e `/chat` no `exemplo_completo.py`.
- [ ] Garantir configuração mínima de CORS e logs.
- [ ] Documentar como rodar/testar (uvicorn + curl/httpie) e registrar no checklist/journal.

---

## 📋 Estrutura de Arquivos (Dia 1)
- `README.md` — Contexto do dia  
- `CONTEXTO_AGENTE.md` — Este arquivo  
- `checklist.md` — Checklist 160min  
- `journal.md` — Registro do dia  
- `requirements.txt` — Dependências (FastAPI, Uvicorn, Pydantic v2, python-dotenv)  
- `CONTEXTO_PROXIMO_DIA.md` — Handoff para o Dia 2 (JWT)  
- Nível 1: `exemplo_completo.py`, `GUIA_PASSO_A_PASSO.md`, `exercicios.md`

---

## 🔑 Informações Importantes
### Stack Tecnológica
- **Linguagem:** Python 3.12 (recomendada)
- **Framework:** FastAPI + Uvicorn
- **Validação:** Pydantic v2
- **LLM:** Placeholder/eco (integrar Groq/Gemini/Claude depois)
- **Observabilidade:** Logs estruturados simples; responses padronizadas

### Configuração Necessária
- `.env` opcional com chaves de LLM (`GROQ_API_KEY` ou `GOOGLE_API_KEY`/`ANTHROPIC_API_KEY`) — não obrigatório para eco.
- Ativar venv (`./venv/Scripts/Activate.ps1` ou equivalente) e instalar `requirements.txt`.
- Porta padrão sugerida: 8000 (`uvicorn exemplo_completo:app --reload`).

### Objetivo do Dia
Subir FastAPI básico com validação e segurança mínima (CORS controlado), preparando terreno para JWT e streaming nos próximos dias.

---

## 🗺️ Próximos Passos
### Imediato (hoje)
1. Instalar dependências e validar `/health`.
2. Implementar `/chat` com Pydantic Request/Response e eco (placeholder LLM).
3. Testar com `curl`/`httpie`, registrar no journal e checklist.

### Próximo Dia (Dia 2 — JWT + segurança)
- Implementar autenticação JWT (login/refresh) e middlewares básicos.
- Endpoints protegidos e ajustes de CORS/env.
- Preparar testes rápidos e hardening mínimo.

---

## 📚 Referências Rápidas
- FastAPI Docs: https://fastapi.tiangolo.com/
- Pydantic v2: https://docs.pydantic.dev/latest/
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- Handoff anterior: `../Semana2/Dia7/CONTEXTO_PROXIMO_DIA.md`

---

**Última atualização:** 9 Dez 2025  
**Status:** 🟡 Em progresso

