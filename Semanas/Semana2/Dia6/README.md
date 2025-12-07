# 📅 Dia 6 - Sábado (6 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **décimo terceiro dia** do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto
- **Objetivo do Dia:** Projeto integrado — montar um “Knowledge Assistant” combinando prompt base, RAG avançado do Dia 4 e ferramentas do Dia 5, agora orquestrados com **LangGraph** (`langgraph.prebuilt.create_react_agent`).
- **Duração estimada:** 2h30-2h40 (160min exatos).
- **Foco:** Integração de tools e RAG em um fluxo único com LangGraph, adicionando testes rápidos e logging.

### 🗺️ Estrutura do Plano
- **Semana 2:** LangChain + RAG (1 Dez - 7 Dez)
- **Dia 4 (concluído):** RAG avançado com FAISS ✅
- **Dia 5 (concluído):** Agents + tools com LangChain v1.0 (`create_agent`) ✅
- **Dia 6 (hoje):** Projeto integrado em LangGraph (Nível 2) 🟡
- **Dia 7 (próximo):** Consolidação/QA/documentação do projeto (testes rápidos, polish, handoff)

### 📁 Arquivos neste diretório
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist do dia (160min)
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python (obrigatório)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir o Dia 7 (obrigatório)
- `GUIA_APRENDIZADO.md` - Conceitos + passo-a-passo (Nível 2)
- `template.py` - Template com TODOs do mini-projeto (Nível 2)
- `exemplo_referencia.py` - Exemplo completo para consulta
- `exercicios.md` - Exercícios guiados e smoke tests

### 🎯 O que você vai aprender
1. Orquestrar tools + RAG usando LangGraph (`create_react_agent`).
2. Ajustar descrições de tools para boa escolha do agente.
3. Logar e testar rapidamente o fluxo integrado (RAG + cálculo).

### 💡 Notas Importantes
- **Baseado em:** Dia 4 (RAG com FAISS) e Dia 5 (tools/agents).
- **Foco:** Migrar orquestração para LangGraph mantendo as tools existentes.
- **Nível de Scaffolding:** **Nível 2 (Intermediário)** — conceitos já vistos, aplicação integrada. Referência: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`.
- **Pré-requisito:** Index do Dia 4 disponível em `../Dia4/faiss_index` (recriar se ausente). `.env` com `GROQ_API_KEY` (ou Gemini/Claude) carregado.
- **Stack:** Python 3.12 recomendado para evitar avisos do Pydantic; LangChain + LangGraph modernos.

### 🔗 Referências
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- Guia do dia: `GUIA_APRENDIZADO.md`
- Dia 4 (Semana 2): `../Dia4/GUIA_RAG_AVANCADO.md`
- Dia 5 (Semana 2): `../Dia5/GUIA_AGENTS.md`
- LangGraph Docs: https://python.langchain.com/docs/langgraph
- LangChain Overview: https://docs.langchain.com/oss/python/langchain/overview

---

**Status:** 🟡 Em progresso  
**Última atualização:** 6 Dez 2025

