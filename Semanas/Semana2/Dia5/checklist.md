# ✅ Checklist - Dia 5 (Sexta-feira, 5 Dez 2025)

## 🎯 Objetivo do Dia
Criar um Agent ReAct com LangChain que use tools (calculator + RAG avançado do Dia 4) para responder perguntas de forma autônoma.

---

## 📋 FASE 0: Preparação (5min)
- [ ] Abrir `README.md` e `CONTEXTO_AGENTE.md` para alinhar objetivo.
- [ ] Confirmar `.env` com `GROQ_API_KEY` (ou Gemini/Claude) carregado (`python -c "from dotenv import load_dotenv;load_dotenv();print('ok')"`).
- [ ] Verificar se o vector store persiste em `../Dia4/chroma_db` (recriar se ausente rodando scripts do Dia 4).

**Referências:** `METODOLOGIA_ENSINO.md`, `GUIA_DECISAO_SCAFFOLDING.md`.

---

## 📋 FASE 1: Leitura guiada (20min)
- [ ] Ler `GUIA_AGENTS.md` seções 1-3 (Agents vs Chains, ReAct, Tools).
- [ ] Revisar trecho de tools em `GUIA_AGENTS.md` (descrições claras).
- [ ] Revisitar `../Dia4/GUIA_RAG_AVANCADO.md` apenas para lembrar retriever/chroma path.

**Saída:** Notas rápidas + dúvidas listadas no journal.  
**Referências:** `GUIA_AGENTS.md`, `GUIA_DECISAO_SCAFFOLDING.md`.

---

## 📋 FASE 2: Construção guiada (90min)

### Parte A (20min) — Tools básicas
- [ ] Implementar tool `somar` (calculator) conforme `exemplo_completo.py`.
- [ ] Escrever descrições das tools deixando claro quando usar.

### Parte B (35min) — RAG como Tool
- [ ] Reutilizar embeddings e Chroma em `../Dia4/chroma_db` para criar tool `buscar_conhecimento`.
- [ ] Garantir `search_kwargs={"k":3}` e retorno concatenado de docs.

### Parte C (35min) — Agent ReAct
- [ ] Montar prompt ReAct (mensagens de sistema + Human) igual `exemplo_completo.py`.
- [ ] Criar Agent com `create_react_agent` + `AgentExecutor` (verbose=True).
- [ ] Testar 2 queries: (a) precisa só calculator; (b) precisa RAG + calculator.

**Referências:** `exemplo_completo.py`, `GUIA_AGENTS.md` seção 3, LangChain Agents docs.

---

## 📋 FASE 3: Consolidação (25min)
- [ ] Rodar exercícios 1-4 em `exercicios.md` (anotar resultados/dúvidas).
- [ ] Ajustar descrições das tools se o Agent escolher errado.
- [ ] Registrar raciocínio do Agent (logs) e salvar exemplos no journal.

---

## 📋 FASE 4: Registro/Handoff (20min)
- [ ] Preencher journal.md (objetivo, o que aprendi, desafios, métricas).
- [ ] Atualizar `CONTEXTO_PROXIMO_DIA.md` com aprendizados e plano para Dia 6.
- [ ] Marcar checklist final e próximos passos.

---

## 📋 Buffer (10min)
- [ ] Usar apenas se algum passo atrasar (priorizar terminar Agent funcional).

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min (5 + 20 + 90 + 25 + 20 + 10)  

### ✅ Critérios de Sucesso:
- [ ] Agent ReAct responde usando calculator quando necessário.
- [ ] Agent ReAct chama RAG (vector store do Dia 4) quando a pergunta exige contexto.
- [ ] `exercicios.md` executados e dúvidas anotadas.
- [ ] journal.md e `CONTEXTO_PROXIMO_DIA.md` preenchidos.

### 🎯 Streak: 12/56 dias

**Parabéns por completar o Dia 5!** 🚀

---

**Última atualização:** 5 Dez 2025

