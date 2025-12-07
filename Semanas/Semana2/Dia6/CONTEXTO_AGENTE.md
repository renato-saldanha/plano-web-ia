# 🤖 Contexto para Agentes IA

Este arquivo resume estado, stack e próximos passos para o Dia 6.

---

## 📍 Localização Atual
- **Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
- **Semana:** 2 de 8  
- **Dia:** 6 de 7 (Sábado, 6 Dez 2025)  
- **Diretório:** `Semanas/Semana2/Dia6/`

---

## 🎯 Estado Atual do Projeto
### O que foi feito
- ✅ Dia 4: RAG avançado com FAISS e embeddings (armazenado em `../Dia4/faiss_index`).
- ✅ Dia 5: Tools + Agents com LangChain v1.0 (`create_agent`) e descrições melhoradas.

### O que está em progresso
- 🟡 Dia 6: Projeto integrado em LangGraph, reusando tools (calculator + RAG) em um fluxo único.

### O que falta fazer (hoje)
- [ ] Garantir acesso ao index FAISS do Dia 4 e `.env` carregado.
- [ ] Configurar tools com docstrings claras e tipagem (`@tool`).
- [ ] Montar agent ReAct com `langgraph.prebuilt.create_react_agent`.
- [ ] Testar queries mistas (só cálculo, só RAG, RAG + cálculo) e registrar no journal.

---

## 📋 Estrutura de Arquivos
### Arquivos obrigatórios
- `README.md` — Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` — Este arquivo
- `checklist.md` — Checklist 160min dividido em fases
- `journal.md` — Registro diário
- `requirements.txt` — Dependências (Python 3.12, LangChain + LangGraph)
- `CONTEXTO_PROXIMO_DIA.md` — Handoff para o Dia 7

### Arquivos de aprendizado (Nível 2)
- `GUIA_APRENDIZADO.md`
- `template.py` (TODOs)
- `exemplo_referencia.py`
- `exercicios.md`

---

## 🔑 Informações Importantes
### Stack Tecnológica
- **Linguagem:** Python 3.12
- **Orquestração:** LangGraph (`langgraph.prebuilt.create_react_agent`)
- **LLM sugerido:** Groq (Llama 3) via `langchain-groq` (gratuito); fallback Gemini/Claude
- **Vector store:** FAISS carregado de `../Dia4/faiss_index` (HuggingFace embeddings)
- **Observabilidade:** `verbose=True` e iteração sobre `messages` para inspecionar raciocínio

### Configuração Necessária
- Variáveis de ambiente em `.env`: `GROQ_API_KEY` (ou `GOOGLE_API_KEY`/`ANTHROPIC_API_KEY` para fallback)
- Garantir que o diretório `../Dia4/faiss_index` exista; recriar com scripts do Dia 4 se preciso.
- Dependências: ver `requirements.txt` (langchain/langgraph/langchain-community/langchain-groq/embeddings/faiss).

### Objetivo do Dia
Integrar tools (calculator + RAG) em um agente ReAct com LangGraph, fornecendo fluxo único de assistência (“Knowledge Assistant”) e testes rápidos.

---

## 🗺️ Próximos Passos
### Imediato (hoje)
1. Validar ambiente e index FAISS (Preparação/Leitura).
2. Ajustar tools com docstrings explícitas (quando usar).
3. Montar agent com `create_react_agent` e testar 3 queries (cálculo, RAG conceitual, pergunta mista).

### Próximo Dia (Dia 7)
- Consolidar: QA rápido, testes adicionais, documentação curta e polimento do fluxo.

---

## 📚 Referências Rápidas
- `README.md` (contexto)
- `GUIA_APRENDIZADO.md` (passo-a-passo do dia)
- Dia 4: `../Dia4/GUIA_RAG_AVANCADO.md`
- Dia 5: `../Dia5/GUIA_AGENTS.md`
- LangGraph Docs: https://python.langchain.com/docs/langgraph

---

**Última atualização:** 6 Dez 2025  
**Status:** 🟡 Em progresso

