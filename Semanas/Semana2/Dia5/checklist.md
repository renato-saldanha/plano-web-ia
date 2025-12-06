# ✅ Checklist - Dia 5 (Sexta-feira, 5 Dez 2025)

## 🎯 Objetivo do Dia
Criar um Agent ReAct com LangChain v1.0 (`create_agent`) que use tools (calculator + RAG avançado do Dia 4) para responder perguntas de forma autônoma.

---

## 📋 FASE 0: Preparação (5min)
- [ X] Abrir `README.md` e `CONTEXTO_AGENTE.md` para alinhar objetivo.
- [ X] Confirmar `.env` com `GROQ_API_KEY` (ou Gemini/Claude) carregado (`python -c "from dotenv import load_dotenv;load_dotenv();print('ok')"`).
- [ X] Verificar se o vector store persiste em `../Dia4/faiss_index` (recriar se ausente rodando scripts do Dia 4).

**Referências:** `METODOLOGIA_ENSINO.md`, `GUIA_DECISAO_SCAFFOLDING.md`.

---

## 📋 FASE 1: Leitura guiada (20min)
- [ X] Ler `GUIA_AGENTS.md` seções 1-4 (Agents vs Chains, ReAct, Tools, create_agent v1.0).
- [ X] Revisar trecho de tools e middleware em `GUIA_AGENTS.md` (descrições claras).
- [ X] Revisitar `../Dia4/GUIA_RAG_AVANCADO.md` apenas para lembrar retriever/faiss path.

**Saída:** Notas rápidas + dúvidas listadas no journal.  
**Referências:** `GUIA_AGENTS.md`, [LangChain v1.0 Docs](https://docs.langchain.com/oss/python/releases/langchain-v1).

---

## 📋 FASE 2: Construção guiada (90min)

### Parte A (20min) — Tools básicas
- [ X] Implementar tool `calculadora` usando decorator `@tool` conforme `exemplo_completo.py`.
- [ X] Escrever descrições claras (docstrings) deixando explícito quando usar.

### Parte B (35min) — RAG como Tool
- [ X] Reutilizar embeddings e FAISS em `../Dia4/faiss_index` para criar tool `buscar_conhecimento`.
- [ X] Garantir `search_kwargs={"k":3}` e retorno concatenado de docs.
- [ X] Testar isoladamente a tool antes de adicionar ao Agent.

### Parte C (35min) — Agent com create_agent v1.0
- [ X] Importar: `from langchain.agents import create_agent`.
- [ X] Criar Agent: `agent = create_agent(llm, tools=[calculadora, buscar_conhecimento])`.
- [ X] Invocar: `agent.invoke({"messages": [HumanMessage(...)]})`.
- [ X] Testar 2 queries: (a) precisa só calculator; (b) precisa RAG + calculator.

**Referências:** `exemplo_completo.py`, `GUIA_AGENTS.md` seção 4, [create_agent docs](https://reference.langchain.com/python/langchain/agents/).

---

## 📋 FASE 3: Consolidação (25min)
- [ X] Rodar exercícios 1-4 em `exercicios.md` (anotar resultados/dúvidas).
- [ X] Ajustar descrições das tools se o Agent escolher errado.
- [ X] Registrar raciocínio do Agent (iterar sobre `messages`) e salvar exemplos no journal.

---

## 📋 FASE 4: Registro/Handoff (20min)
- [ X] Preencher journal.md (objetivo, o que aprendi, desafios, métricas).
- [ X] Atualizar `CONTEXTO_PROXIMO_DIA.md` com aprendizados e plano para Dia 6.
- [ X] Marcar checklist final e próximos passos.

---

## 📋 Buffer (10min)
- [ X] Usar apenas se algum passo atrasar (priorizar terminar Agent funcional).

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min (5 + 20 + 90 + 25 + 20 + 10)  

### ✅ Critérios de Sucesso:
- [ X] Agent ReAct responde usando calculator quando necessário.
- [ X] Agent ReAct chama RAG (FAISS do Dia 4) quando a pergunta exige contexto.
- [ X] `exercicios.md` executados e dúvidas anotadas.
- [ X] journal.md e `CONTEXTO_PROXIMO_DIA.md` preenchidos.
- [ X] Código usa `create_agent` (API oficial v1.0).

### 🎯 Streak: 12/56 dias

**Parabéns por completar o Dia 5!** 🚀

---

**Última atualização:** 5 Dez 2025

