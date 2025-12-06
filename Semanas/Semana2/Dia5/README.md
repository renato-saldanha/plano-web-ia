# 📅 Dia 5 - Sexta-feira (5 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **décimo segundo dia** do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** Agents e Tools — criar um agente ReAct que decide quando usar o RAG avançado (Dia 4) como ferramenta.
- **Duração estimada:** 2h30-2h40 (160min exatos).
- **Foco:** Introduzir Agents com a API oficial `create_agent` (LangChain v1.0) e uso de múltiplas tools (calculator + RAG).

### 🗺️ Estrutura do Plano:
- **Semana 2:** LangChain + RAG (1 Dez - 7 Dez)
- **Dia 1-4 (concluídos):** LangChain básico → Chains/LCEL → RAG básico → RAG avançado ✅
- **Dia 5 (hoje):** Agents e tools com LangChain v1.0 (Nível 1 - conceito novo) 🟡
- **Dia 6-7 (próximos):** Projeto integrado com LangChain e review/deploy

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia (160min)
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python (obrigatório)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório)
- `GUIA_AGENTS.md` - Guia completo sobre Agents com LangChain v1.0 (Nível 1)
- `exemplo_completo.py` - Exemplo completo comentado usando `create_agent` v1.0 (Nível 1)
- `exercicios.md` - Exercícios guiados progressivos

### 🎯 O que você vai aprender:
1. **Agents e ReAct:** Como Agents raciocinam e escolhem ferramentas com `create_agent`.
2. **Tools:** Criar e documentar ferramentas (calculator + RAG como tool).
3. **Orquestração:** Executar um Agent que usa múltiplas tools em sequência.
4. **API v1.0:** Usar a API oficial do LangChain v1.0 para agents.

### 💡 Notas Importantes:
- **Baseado em:** Dia 4 (RAG avançado com FAISS) — o retriever vira uma Tool.
- **Foco:** Autonomia do Agent para decidir quando chamar RAG ou cálculo.
- **Nível de Scaffolding:** **Nível 1 (Iniciante)** — conceito completamente novo (Agents + tools + ReAct). Referência: `GUIAS/GUIA_DECISAO_SCAFFOLDING.md`.
- **Pré-requisito:** RAG avançado do Dia 4 funcionando e persistido em `../Dia4/faiss_index`.
- **API:** LangChain v1.0 com `create_agent` (substitui AgentExecutor clássico e langgraph.prebuilt).

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`
- Guia do dia: `GUIA_AGENTS.md`
- Dia 4 (Semana 2): `../Dia4/README.md` e `../Dia4/GUIA_RAG_AVANCADO.md`
- **LangChain v1.0 Release:** https://docs.langchain.com/oss/python/releases/langchain-v1
- **create_agent Docs:** https://reference.langchain.com/python/langchain/agents/
- ReAct paper: https://arxiv.org/abs/2210.03629

---

**Status:** 🟡 Em progresso  
**Última atualização:** 5 Dez 2025

