# ✅ Checklist - Dia 7 (Domingo, 7 Dez 2025)

## 🎯 Objetivo do Dia
Polir o “Knowledge Assistant” do Dia 6: reforçar descrições das tools, validar escolhas de tool com smoke tests extras, melhorar mensagens de erro e registrar evidências/handoff.

---

## 📋 FASE 0: Preparação (5min)
- [X ] Abrir `README.md` e `CONTEXTO_AGENTE.md` para alinhar objetivos e pré-requisitos.
- [X ] Confirmar `.env` carregado (`GROQ_API_KEY` ou `GOOGLE_API_KEY`/`ANTHROPIC_API_KEY`).
- [ X] Validar acesso a `../Dia4/faiss_index`; recriar com scripts do Dia 4 se faltar.

**Referências:** `METODOLOGIA_ENSINO.md`, `GUIA_DECISAO_SCAFFOLDING.md`.

---

## 📋 FASE 1: Leitura guiada (20min)
- [ X] Ler `GUIA_CONCEITOS.md` (QA/polish) para critérios de teste.
- [ X] Revisar `../Dia5/GUIA_AGENTS.md` focando docstrings de tools e prompts.
- [ X] Revisar `../Dia4/GUIA_RAG_AVANCADO.md` (retriever/FAISS) e LangGraph Docs (prebuilt agent).

**Saída:** Notas rápidas + dúvidas no journal.  
**Referências:** `GUIA_CONCEITOS.md`, LangGraph Docs, `GUIA_AGENTS.md`.

---

## 📋 FASE 2: Construção guiada (90min)

### Parte A (20min) — Docstrings e prompt
- [ X] Ajustar docstrings das tools (`template.py` ou `exemplo_referencia.py` do Dia 6) deixando claro “quando usar / quando NÃO usar”.
- [ X] Revisar prompt base do agent para reforçar prioridades (usar RAG antes de alucinar, só usar calculator para aritmética direta).

### Parte B (35min) — Smoke tests adicionais
- [ X] Testar 4 casos: (a) só cálculo; (b) só RAG conceitual; (c) pergunta mista; (d) entrada ambígua/ruidosa.
- [ X] Registrar outputs e raciocínio (`messages`) no journal; notar se escolheu tool errada.
- [ X] Ajustar descrições/prompt até passar os 4 casos.

### Parte C (35min) — UX e erros
- [ X] Padronizar mensagens de erro amigáveis (ex.: falta de index, falta de chave).
- [ X] Garantir `recursion_limit` adequado (6-10) e logging enxuto (`verbose=True` só em debug).
- [ X] Documentar passos mínimos de uso (inputs/outputs esperados) para handoff.

**Referências:** `GUIA_CONCEITOS.md`, `especificacoes.md`, LangGraph Docs.

---

## 📋 FASE 3: Consolidação (25min)
- [ X] Repetir smoke tests após ajustes e anotar resultados finais.
- [ X] Revisar critérios em `especificacoes.md` e marcar o que foi atendido.
- [ X] Atualizar notas no journal com evidências (prompt, outputs).

---

## 📋 FASE 4: Registro/Handoff (20min)
- [ X] Preencher `journal.md` (tempo, aprendizados, desafios, métricas).
- [ X] Atualizar `CONTEXTO_PROXIMO_DIA.md` com entregas de QA e briefing para o Dia 8.
- [ X] Marcar checklist final e próximos passos.

---

## 📋 Buffer (10min)
- [ X] Usar apenas se alguma fase atrasar (prioridade: smoke tests + handoff).

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min (5 + 20 + 90 + 25 + 20 + 10)  

### ✅ Critérios de Sucesso
- [ X] Agent escolhe calculator para aritmética simples e RAG para consultas conceituais.
- [ X] Pergunta mista é resolvida com cadeia tool → resposta final coerente.
- [ X] Mensagens de erro estão claras (falta de index/chaves) e registradas.
- [ X] Evidências de testes registradas no journal e handoff pronto.

### 🎯 Streak: 14/56 dias

**Última atualização:** 7 Dez 2025

