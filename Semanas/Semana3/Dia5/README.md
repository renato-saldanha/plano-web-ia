# 📅 Dia 5 - Sexta (13 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **quinto dia** da Semana 3 do plano de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** Implementar rate limiting por usuário e logging estruturado para a API de chat, preparando observabilidade e segurança básica.
- **Duração estimada:** 160min totais (inclui leitura, exercícios/testes e preenchimento de documentos) — **sem autocomplete/IA escrevendo código**.
- **Foco:** Rate limiting por usuário e logging estruturado (conceitos novos).

### 🗺️ Estrutura do Plano:
- **Semana 3:** Backend FastAPI + IA (9-15 Dez)
- **Dia 4 (concluído):** Sistema de histórico de conversas ✅
- **Dia 5 (hoje):** Rate limiting por usuário + Logging estruturado
- **Dia 6:** Testes automatizados (pytest) + Exception Handling básico

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python (obrigatório)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório)
- **Scaffolding Nível 1:** `exemplo_completo.py`, `GUIA_PASSO_A_PASSO.md`, `template.py`, `exercicios.md`

### 🎯 O que você vai aprender:
1. Rate limiting por usuário (usando `slowapi` com função customizada que extrai user_id do JWT)
2. Logging estruturado em formato JSON para facilitar monitoramento
3. Middleware de request logging para rastreabilidade de requisições
4. Uso de módulos compartilhados (`common/logging.py`) para reduzir duplicação

### 💡 Notas Importantes:
- **Baseado em:** Dia 4 (histórico de chat). Reaproveite a estrutura existente e adicione rate limiting e logging.
- **Foco:** Rate limiting por usuário e logging estruturado são conceitos novos que requerem suporte completo (Nível 1).
- **Nível de Scaffolding:** **1 (Iniciante)** - Rate limiting por usuário e logging estruturado são conceitos novos, primeira exposição.
- **Módulos compartilhados:** Use `common/logging.py` para reduzir duplicação de código.

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Recursos: `../../3-recursos_e_links_uteis.md` (se existir)
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- SlowAPI Documentation: https://slowapi.readthedocs.io/
- FastAPI Exception Handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
- Python Logging: https://docs.python.org/3/library/logging.html
- FastAPI Middleware: https://fastapi.tiangolo.com/advanced/middleware/

---

**Status:** 🟡 Em progresso  
**Última atualização:** 13 Dez 2025
