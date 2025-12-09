# ✅ Checklist - Dia 1 (Terça, 9 Dez 2025)

## 🎯 Objetivo do Dia
Subir FastAPI básico com `/health` e `/chat` (eco/placeholder LLM), CORS mínimo e logs simples, preparando para JWT e streaming nos próximos dias.

---

> Todas as fases devem caber em **160min** (inclui leitura, testes e preenchimento dos docs). Sem autocomplete/IA escrevendo código.

## 📋 FASE 0: Preparação (5min)
- [ X] Abrir `README.md` e `CONTEXTO_AGENTE.md` para alinhar objetivo e pré-requisitos.
- [ X] Ativar venv e instalar dependências (`pip install -r requirements.txt`).
- [ X] Garantir `.env` disponível se for testar LLM; caso contrário seguir em modo eco.

**Referências:** `METODOLOGIA_ENSINO.md`, `GUIA_DECISAO_SCAFFOLDING.md`.

---

## 📋 FASE 1: Leitura guiada (20min)
- [ X] Ler `GUIA_PASSO_A_PASSO.md` (setup, uvicorn, rotas).
- [ X] Revisar FastAPI docs (seções: Tutorial > First Steps, Response Model).
- [ X] Ler overview LangChain/LangGraph para planejar integração futura.

**Saída:** Notas rápidas + dúvidas no journal.  
**Referências:** `GUIA_PASSO_A_PASSO.md`, FastAPI Docs, LangChain overview.

---

## 📋 FASE 2: Construção guiada (90min)

### Parte A (25min) — Estrutura e saúde
- [ X] Implementar `/health` com status e versão.
- [ X] Adicionar CORS mínimo (origem local, método/headers básicos).
- [ X] Incluir logs iniciais (startup simples).

### Parte B (40min) — `/chat` eco/placeholder LLM
- [ X] Criar modelos Pydantic de entrada/saída (mensagem, metadata).
- [ X] Implementar handler async retornando eco; deixar função stub para LLM.
- [ X] Validar resposta 200 com schema.

### Parte C (25min) — Testes rápidos
- [ ] Rodar `uvicorn exemplo_completo:app --reload` e testar com `curl`/`httpie`.
- [ ] Registrar exemplos de requisição/resposta no journal.
- [ ] Ajustar CORS/headers se necessário.

**Referências:** `exemplo_completo.py`, FastAPI Docs (Body/Response model), `GUIA_PASSO_A_PASSO.md`.

---

## 📋 FASE 3: Consolidação (25min)
- [ X] Revisar código e comentários do `exemplo_completo.py`.
- [ X] Checar consistência de mensagens e validação Pydantic.
- [ X] Atualizar checklist parcial e anotar aprendizados no journal.

---

## 📋 FASE 4: Registro/Handoff (20min)
- [ X] Preencher `journal.md` (tempo, aprendizados, desafios, métricas).
- [ X] Atualizar `CONTEXTO_PROXIMO_DIA.md` com entregas e briefing do Dia 2 (JWT).
- [ X] Marcar checklist final.

---

## 📋 Buffer (10min)
- [ X] Usar apenas se alguma fase atrasar (prioridade: `/chat` + registros).

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min (5 + 20 + 90 + 25 + 20 + 10)  

### ✅ Critérios de Sucesso
- [ X] `/health` responde 200 com payload simples (status/version).
- [ X] `/chat` valida entrada e responde eco conforme schema.
- [ X] CORS mínimo configurado e testes manuais documentados.

### 🎯 Streak: 15/56 dias

**Última atualização:** 9 Dez 2025

