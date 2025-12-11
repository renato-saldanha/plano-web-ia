# 📅 Dia 4 - Quinta (12 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **quarto dia** da Semana 3 do plano de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** Implementar sistema de histórico de conversas para o endpoint `/api/chat`, permitindo manter contexto entre múltiplas mensagens e listar/recuperar conversas anteriores.
- **Duração estimada:** 160min totais (inclui leitura, exercícios/testes e preenchimento de documentos) — **sem autocomplete/IA escrevendo código**.
- **Foco:** Persistência de mensagens, gerenciamento de conversas e contextos de histórico.

### 🗺️ Estrutura do Plano:
- **Semana 3:** Backend FastAPI + IA (9-15 Dez)
- **Dia 3 (concluído):** Streaming de respostas com SSE e integração LLM ✅
- **Dia 4 (hoje):** Histórico de chat e gerenciamento de conversas
- **Dia 5:** Rate limiting, tratamento de erros e logging estruturado

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python (obrigatório)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório)
- **Scaffolding Nível 2:** `template.py`, `GUIA_APRENDIZADO.md`, `exemplo_referencia.py`, `exercicios.md`

### 🎯 O que você vai aprender:
1. Armazenamento de histórico de mensagens (em memória ou arquivo JSON simples)
2. Gerenciamento de conversas/threads por usuário
3. Envio de contexto completo ao LLM para manter continuidade
4. Endpoints para listar e recuperar conversas anteriores

### 💡 Notas Importantes:
- **Baseado em:** Dia 3 (streaming e `/api/chat`). Reaproveite a estrutura de autenticação JWT e streaming implementados.
- **Foco:** Sistema simples mas funcional de histórico que pode ser evoluído para banco de dados no futuro.
- **Nível de Scaffolding:** 2 (conceito parcialmente conhecido; aplicação de persistência em novo contexto).

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Recursos: `../../3-recursos_e_links_uteis.md` (se existir)
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- FastAPI Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/
- LangChain Message History: https://python.langchain.com/docs/how_to/message_history

---

**Status:** Concluído 
**Última atualização:** 12 Dez 2025