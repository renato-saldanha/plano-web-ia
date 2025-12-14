# 🎯 Contexto para Construir o Dia 4

## 📚 O que aprendemos hoje (Dia 3)
### Conceitos Principais
- StreamingResponse com async generators
- Formato SSE (`data: ...\n\n`) para tokens
- LangChain/LangGraph com streaming (`astream`)
- Proteção de endpoints com JWT durante streaming

### Habilidades Desenvolvidas
- Implementar endpoint `/api/generate` com SSE
- Ajustar `/chat` para respostas em streaming ou JSON
- Testar SSE via curl e `/docs`

### Código Criado
- `template.py` (TODOs resolvidos) — endpoints `/api/generate` e `/chat`
- `exemplo_referencia.py` — versão completa com LLM streaming
- Configuração de envs para JWT + LLM (`OPENAI_API_KEY`, etc.)

---

## 🔗 Por que o Dia 4 é importante
- Validar estabilidade: testes automatizados e hardening reduzem regressões.
- Rate limiting e observabilidade evitam abuso e ajudam debug em produção.
- Consolida ciclo auth + streaming + testes → base para features avançadas.

---

## 🎯 O que será feito no Dia 4 (proposto)
- **Objetivo:** Testes automatizados (pytest) para login/refresh/streaming e hardening (rate limit por usuário + logs estruturados).
- **Conceitos:** pytest + httpx AsyncClient, fixtures de token, rate limiting (slowapi ou equivalente), logging estruturado.

### Como se relaciona com Dia 3
- Usa `/login` e `/api/generate` implementados hoje.
- Reaproveita `get_current_user` e SSE para criar cenários de teste.
- Exercita limites (429) e métricas sobre endpoints críticos.

---

## 📋 Como Construir o Dia 4
1. Criar estrutura básica `Dia4/` com arquivos obrigatórios (README, CONTEXTO_AGENTE, checklist, journal, requirements, CONTEXTO_PROXIMO_DIA).
2. Nível de scaffolding sugerido: **2** (testes e hardening em contexto conhecido).
3. Arquivos adicionais:
   - `tests/test_auth.py`, `tests/test_stream.py`
   - `template.py` ou `exemplo_referencia.py` focado em testes/logs
   - `GUIA_APRENDIZADO.md` sobre pytest + rate limiting
4. Checklist focado em 160min, cobrindo setup de testes, implementação, execução e registro.

---

## 📚 Recursos de Preparação
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- httpx AsyncClient
- slowapi (rate limiting) ou alternativa leve
- Logging estruturado (pode usar `logging` + JSON)

### Conceitos pré-requisitos
- JWT (Dia 2) e streaming (Dia 3)
- Async/await em Python

---

## 💡 Dicas Importantes
1. Reutilize o código do Dia 3 para fixtures (tokens) e client de teste.
2. Cubra casos de erro: token inválido, ausência de token, modelo inválido.
3. Se o tempo estourar: priorize testes de auth + streaming feliz; hardening extra vai para buffer.

---

**Última atualização:** 11 Dez 2025  
**Status:** 🟡 Pronto como briefing

