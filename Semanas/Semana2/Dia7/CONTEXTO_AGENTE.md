# 🤖 Contexto para Agentes IA

Resumo do estado, stack e próximos passos para o Dia 7 (QA/polish).

---

## 📍 Localização Atual
- **Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
- **Semana:** 2 de 8  
- **Dia:** 7 de 7 (Domingo, 7 Dez 2025)  
- **Diretório:** `Semanas/Semana2/Dia7/`

---

## 🎯 Estado Atual do Projeto
### O que foi feito
- ✅ Dia 4: RAG avançado com FAISS (`../Dia4/faiss_index`).
- ✅ Dia 5: Tools/agents com LangChain (`GUIA_AGENTS.md`).
- ✅ Dia 6: Agent LangGraph com calculator + RAG (`template.py`, `exemplo_referencia.py`).

### O que está em progresso (hoje)
- 🟡 QA e polish do Knowledge Assistant: descrições das tools, mensagens de erro, testes adicionais e registro de evidências.

### O que falta fazer (hoje)
- [ ] Revisar docstrings e mensagens de erro das tools (quando usar / quando não usar).
- [ ] Rodar smoke tests adicionais (cálculo, RAG, pergunta mista, caso ambíguo) e registrar outputs.
- [ ] Documentar passos mínimos de uso e próximos passos no handoff.

---

## 📋 Estrutura de Arquivos (Dia 7)
- `README.md` — Contexto do dia
- `CONTEXTO_AGENTE.md` — Este arquivo
- `checklist.md` — Checklist 160min
- `journal.md` — Registro do dia
- `requirements.txt` — Dependências (reuso do Dia 6)
- `CONTEXTO_PROXIMO_DIA.md` — Handoff para o Dia 8
- Nível 3: `especificacoes.md`, `GUIA_CONCEITOS.md`, `exercicios.md`

---

## 🔑 Informações Importantes
-### Stack Tecnológica
- **Linguagem:** Python 3.12 (recomendada)
- **Orquestração:** LangChain Agents (`langchain.agents.create_agent`) + `@tool`
- **LLM sugerido:** Groq (Llama 3) via `langchain-groq`; fallback Gemini/Claude
- **Vector store:** FAISS em `../Dia4/faiss_index`
- **Observabilidade:** `verbose=True`, inspeção de `messages` e `recursion_limit` 6-10 para debugging

### Configuração Necessária
- `.env` com `GROQ_API_KEY` (ou `GOOGLE_API_KEY`/`ANTHROPIC_API_KEY`) carregado.
- Garantir acesso ao index FAISS (`../Dia4/faiss_index`); recriar com scripts do Dia 4 se ausente.
- Dependências: ver `requirements.txt` (igual ao Dia 6).

### Objetivo do Dia
Polir o Knowledge Assistant: reforçar descrições das tools, validar decisões de tool, melhorar mensagens de erro e registrar evidências para handoff.

---

## 🗺️ Próximos Passos
### Imediato (hoje)
1. Revisar descrições das tools no `template.py`/`exemplo_referencia.py` e alinhar prompt base.  
2. Rodar smoke tests extras: (a) só cálculo; (b) só RAG conceitual; (c) pergunta mista; (d) entrada ambígua/ruidosa.  
3. Registrar no journal outputs, raciocínio e ajustes feitos; atualizar `CONTEXTO_PROXIMO_DIA.md`.

### Próximo Dia (Dia 8 — início Semana 3: FastAPI + IA)
- Criar esqueleto FastAPI (Python 3.12 + Pydantic v2), endpoint simples e checklist de segurança.  
- Preparar `.env` para novas chaves/segredos e decidir modelo/LLM default para backend.  
- Ler `METODOLOGIA_ENSINO.md` e matriz de scaffolding para definir Nível (provável Nível 1, conceito novo de FastAPI).

---

## 📚 Referências Rápidas
- Dia 6: `README.md`, `GUIA_APRENDIZADO.md`, `template.py`, `exemplo_referencia.py`, `exercicios.md`
- Dia 4: `../Dia4/GUIA_RAG_AVANCADO.md`
- Dia 5: `../Dia5/GUIA_AGENTS.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- LangGraph Docs: https://python.langchain.com/docs/langgraph
- LangChain Overview: https://docs.langchain.com/oss/python/langchain/overview

---

**Última atualização:** 7 Dez 2025  
**Status:** 🟡 Em progresso

