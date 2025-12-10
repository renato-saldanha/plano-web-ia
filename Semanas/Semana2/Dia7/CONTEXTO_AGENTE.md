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
- ✅ Dia 4: RAG avançado com Vector Databases (FAISS/Chroma).
- ✅ Dia 5: Tools/agents com LangChain (`GUIA_AGENTS.md`).
- ✅ Dia 6: Agent LangGraph com calculator + RAG (`template.py`, `exemplo_referencia.py`).
- ✅ Dia 7: Sistema completo com PGVector, indexação automática e comparação STUFF/MapReduce.

### O que foi implementado (Dia 7)
- ✅ Migração para PGVector com PostgreSQL
- ✅ Indexação automática de produtos da tabela SQL
- ✅ Comparação STUFF vs MapReduce implementada
- ✅ Tools com docstrings melhoradas (`search_knowledges`, `calculator`)
- ✅ Agent ReAct funcional com logging completo
- ✅ Sistema de alternância entre LLMs (Groq/OpenAI)

### O que está em progresso (hoje)
- 🟡 Documentação e handoff final

### O que falta fazer (hoje)
- [ ] Atualizar documentação com exemplos de uso
- [ ] Registrar evidências de testes no journal
- [ ] Preparar handoff para Dia 8

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

### Stack Tecnológica
- **Linguagem:** Python 3.12 (recomendada)
- **Orquestração:** LangChain Agents (`langchain.agents.create_agent`) + `@tool`
- **LLM:** Groq (Llama 3.1 8B) e OpenAI (GPT-4o-mini) via `langchain-groq` e `langchain-openai`
- **Vector store:** PGVector (PostgreSQL com extensão pgvector)
- **Banco de dados:** PostgreSQL com tabela `produtos`
- **Observabilidade:** Inspeção de `messages` e `recursion_limit` 10 para debugging

### Configuração Necessária
- **`.env` com:**
  - `GROQ_API_KEY` e/ou `OPENAI_API_KEY`
  - `DATABASE_NAME=postgresql://usuario:senha@localhost:5432/nome_banco`
- **PostgreSQL:**
  - Extensão `pgvector` instalada
  - Tabela `produtos` criada (veja estrutura no README.md)
- **Dependências:** ver `requirements.txt` (inclui `langchain-postgres`, `psycopg2`)

### Objetivo do Dia
Polir o Knowledge Assistant: reforçar descrições das tools, validar decisões de tool, melhorar mensagens de erro e registrar evidências para handoff.

---

## 🗺️ Próximos Passos
### Imediato (hoje)
1. ✅ Revisar descrições das tools - **CONCLUÍDO**
2. ✅ Rodar smoke tests extras - **CONCLUÍDO** (ver `exercicios/1-rag_completo.py`)
3. Registrar no journal outputs e raciocínio; atualizar `CONTEXTO_PROXIMO_DIA.md` com handoff.

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

