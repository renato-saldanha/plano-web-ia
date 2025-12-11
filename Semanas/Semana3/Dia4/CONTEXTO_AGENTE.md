# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 3 de 8  
**Dia:** 4 de 7 (Quinta, 12 Dez 2025)  
**Diretório:** `Semanas/Semana3/Dia4/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: FastAPI básico (`/health`, `/chat` inicial, CORS)
- ✅ Dia 2: Autenticação JWT (login, refresh, proteção de rotas)
- ✅ Dia 3: Streaming de respostas (SSE) + integração LLM real

### O que está em progresso:
- 🟡 Dia 4: Sistema de histórico de conversas para `/api/chat`

### O que falta fazer (hoje):
- [ ] Implementar armazenamento de mensagens (em memória ou arquivo JSON)
- [ ] Criar sistema de gerenciamento de conversas/threads
- [ ] Modificar `/api/chat` para incluir histórico no contexto do LLM
- [ ] Criar endpoints para listar conversas e recuperar histórico
- [ ] Validar funcionalidade com exemplos práticos

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- `README.md` - Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- `checklist.md` - Checklist detalhado com fases
- `journal.md` - Template para reflexão
- `requirements.txt` - Dependências Python (obrigatório sempre, mesmo que vazio)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório para todos os dias)

### Arquivos de Aprendizado (Nível 2):
- `template.py` - Template com TODOs para implementação
- `GUIA_APRENDIZADO.md` - Conceitos teóricos + passo-a-passo
- `exemplo_referencia.py` - Exemplo completo para consulta
- `exercicios.md` - Exercícios guiados

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12
- **Framework:** FastAPI
- **APIs:** LangChain/LangGraph (API moderna) para LLM
- **Armazenamento:** Em memória (dict) ou arquivo JSON simples (para simplificar, sem DB ainda)
- **Autenticação:** JWT (herdado do Dia 2)

### Configuração Necessária:
- Variáveis de ambiente do Dia 2-3 (JWT_SECRET_KEY, OPENAI_API_KEY, etc.)
- Reutilizar código de autenticação e streaming do Dia 3

### Objetivo do Dia:
Implementar sistema de histórico de conversas que:
1. Armazena mensagens por usuário e por conversa (thread)
2. Mantém contexto entre mensagens no mesmo thread
3. Permite listar conversas do usuário
4. Permite recuperar histórico de uma conversa específica
5. Integra histórico no contexto enviado ao LLM

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Ler `GUIA_APRENDIZADO.md` sobre persistência e histórico
2. Completar `template.py` com sistema de armazenamento
3. Modificar endpoint `/api/chat` para usar histórico
4. Criar endpoints `/conversations` e `/conversations/{id}/messages`
5. Testar fluxo completo com múltiplas mensagens

### Próximo Dia:
- Rate limiting por usuário
- Tratamento de erros robusto
- Logging estruturado
- Testes automatizados

---

## 📚 Referências Rápidas

- FastAPI Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/
- LangChain Message History: https://python.langchain.com/docs/how_to/message_history
- FastAPI Response Models: https://fastapi.tiangolo.com/tutorial/response-model/
- `../../METODOLOGIA_ENSINO.md` - Metodologia de ensino
- `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md` - Níveis de scaffolding

---

**Última atualização:** 12 Dez 2025  
**Status:** 