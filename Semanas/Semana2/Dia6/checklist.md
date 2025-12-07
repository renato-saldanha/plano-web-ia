# ✅ Checklist - Dia 6 (Sábado, 6 Dez 2025)

## 🎯 Objetivo do Dia
Integrar tools (calculator + RAG do Dia 4) em um agent ReAct usando **LangGraph** (`create_react_agent`) para formar um “Knowledge Assistant” com testes rápidos e logging.

---

## 📋 FASE 0: Preparação (5min)
- [ x] Abrir `README.md` e `CONTEXTO_AGENTE.md` para alinhar objetivos.
- [ x] Confirmar `.env` com `GROQ_API_KEY` (ou Gemini/Claude) carregado.
- [ x] Verificar se `../Dia4/faiss_index` existe; recriar com scripts do Dia 4 se faltar.

**Referências:** `METODOLOGIA_ENSINO.md`, `GUIA_DECISAO_SCAFFOLDING.md`.

---

## 📋 FASE 1: Leitura guiada (20min)
- [ x] Ler `GUIA_APRENDIZADO.md` (seções LangGraph + fluxo do dia).
- [ x] Revisar `../Dia5/GUIA_AGENTS.md` focando descrições de tools.
- [ x] Revisar `../Dia4/GUIA_RAG_AVANCADO.md` para relembrar retriever/FAISS.

**Saída:** Notas rápidas + dúvidas listadas no journal.  
**Referências:** `GUIA_APRENDIZADO.md`, LangGraph Docs (prebuilt agent).

---

## 📋 FASE 2: Construção guiada (90min)

### Parte A (20min) — Setup + prompt base
- [ X] Copiar/ajustar prompt base (tom e foco) no `template.py`.
- [ X] Garantir imports e carregamento do retriever (FAISS) no template.

### Parte B (35min) — Tools
- [ X] Implementar `calculadora` com `@tool`, docstring clara e validação simples.
- [ X] Implementar `buscar_conhecimento` usando retriever FAISS (`search_kwargs={"k":3}`).
- [ X] Testar cada tool de forma isolada (chamada direta) e registrar resultados.

### Parte C (35min) — Agent com LangGraph
- [ X] Criar agent com `create_agent(llm, tools=[...])`.
- [ X] Invocar: `agent.invoke({"messages": [HumanMessage(content=...)]}, config={"recursion_limit": 8})`.
- [ X] Testar 3 queries: (a) só cálculo; (b) só RAG; (c) pergunta mista (RAG + cálculo).
- [ X] Registrar raciocínio (`messages`) e ajustar descrições se escolher tool errada.

**Referências:** `template.py`, `exemplo_referencia.py`, `GUIA_APRENDIZADO.md`, LangGraph Docs.

---

## 📋 FASE 3: Consolidação (25min)
- [ X] Rodar exercícios de `exercicios.md` (smoke tests) e anotar resultados.
- [ X] Ajustar prompt/descrições se o agent errar a escolha de tool.
- [ X] Registrar trechos de output e raciocínio no journal.

---

## 📋 FASE 4: Registro/Handoff (20min)
- [ X] Preencher `journal.md` (objetivo, aprendizados, desafios, métricas).
- [ X] Atualizar `CONTEXTO_PROXIMO_DIA.md` com entregas e foco do Dia 7.
- [ X] Marcar checklist final e próximos passos.

---

## 📋 Buffer (10min)
- [ X] Usar apenas se algum passo atrasar (prioridade: agent funcional + smoke tests).

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min (5 + 20 + 90 + 25 + 20 + 10)  

### ✅ Critérios de Sucesso
- [ X] Agent responde usando calculator quando necessário.
- [ X] Agent chama RAG (FAISS do Dia 4) quando a pergunta exige contexto.
- [ X] Smoke tests de `exercicios.md` executados e observações anotadas.
- [ X] journal.md e `CONTEXTO_PROXIMO_DIA.md` preparados/preenchidos.
- [ X] Uso de `langchain.agents.create_agent` com `@tool`.

### 🎯 Streak: 13/56 dias

**Parabéns por completar o Dia 6!** 🚀

---

**Última atualização:** 6 Dez 2025

