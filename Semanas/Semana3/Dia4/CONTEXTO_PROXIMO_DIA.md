# 🎯 Contexto para Construir o Dia 5

## 📚 O que aprendemos hoje (Dia 4)

### Conceitos Principais
- Armazenamento de histórico de mensagens em memória (dict estruturado)
- Gerenciamento de conversas/threads por usuário
- Integração de histórico no contexto do LLM (lista de HumanMessage/AIMessage)
- Endpoints REST para listar e recuperar conversas

### Habilidades Desenvolvidas
- Implementar sistema de persistência simples (em memória)
- Construir contexto completo para LLM mantendo histórico
- Criar endpoints RESTful para gerenciar recursos (conversas, mensagens)
- Validar isolamento por usuário (segurança)

### Código Criado
- `template.py` (TODOs resolvidos) — sistema de histórico completo
- Funções auxiliares: `get_or_create_conversation()`, `add_message()`, `get_messages()`, `list_conversations()`
- Endpoints: `/chat` (modificado), `/conversations`, `/conversations/{id}/messages`
- Modelos Pydantic: `Message`, `ConversationSummary`

---

## 🔗 Por que o Dia 5 é importante

O sistema de chat agora tem histórico funcional, mas falta:
- **Rate limiting robusto:** Proteger contra abuso (por usuário, não só por IP)
- **Tratamento de erros:** Capturar e logar erros de forma estruturada
- **Observabilidade:** Logging estruturado para debug e monitoramento

Estes elementos são essenciais para produção e completam o backend antes de testes automatizados.

---

## 🎯 O que será feito no Dia 5

### Objetivo Principal
Implementar rate limiting por usuário, tratamento de erros robusto e logging estruturado para a API de chat.

### Conceitos que serão aprendidos
- Rate limiting por usuário (usando `slowapi` ou middleware custom)
- Tratamento de exceções global (exception handlers do FastAPI)
- Logging estruturado (formato JSON) com contexto
- Middleware de logging para requests

### Como se relaciona com Dia 4
- Usa sistema de histórico implementado hoje
- Adiciona camadas de segurança e observabilidade
- Prepara código para produção e testes automatizados

---

## 📋 Como Construir o Dia 5

### 1. Criar Estrutura Básica
```
Dia5/
├── README.md
├── CONTEXTO_AGENTE.md
├── checklist.md
└── journal.md
```

**Ordem sugerida:**
1. Criar pasta `Dia5/`
2. Copiar templates de `TEMPLATE_ESTRUTURA_DIA.md`
3. Preencher README.md com contexto do próximo dia
4. Criar CONTEXTO_AGENTE.md
5. Criar checklist.md detalhado

### 2. Definir Nível de Scaffolding

**Nível recomendado:** **2** (conceitos parcialmente conhecidos: rate limiting e logging são aplicações de conceitos conhecidos em novo contexto)

**Arquivos necessários:**
- `template.py` (herdar código do Dia 4, adicionar rate limiting e logging)
- `GUIA_APRENDIZADO.md` (rate limiting, exception handling, logging estruturado)
- `exemplo_referencia.py` (implementação completa como referência)
- `exercicios.md` (exercícios de teste)

### 3. Criar Arquivos de Aprendizado

**GUIA_APRENDIZADO.md deve cobrir:**
- Rate limiting por usuário vs por IP
- Exception handlers globais no FastAPI
- Logging estruturado (JSON format)
- Middleware de request logging

**template.py deve ter TODOs para:**
- Rate limiter por usuário (usando `slowapi` com função customizada)
- Exception handler global (HTTPException, ValidationError, Exception genérica)
- Configuração de logging estruturado
- Middleware para logar requests (método, path, status, tempo)

**exemplo_referencia.py deve mostrar:**
- Implementação completa de rate limiting por usuário
- Exception handlers configurados
- Logging estruturado funcionando
- Middleware de request logging

### 4. Seguir Checklist

Dividir em fases:
- Preparação (5min)
- Leitura guiada (20min) — GUIA_APRENDIZADO.md
- Construção guiada (90min) — implementar rate limiting, exception handlers, logging
- Consolidação (25min) — testar cenários de erro e rate limit
- Registro (20min) — journal e CONTEXTO_PROXIMO_DIA

---

## 📚 Recursos de Preparação

### O que revisar antes de começar:
- [ ] Código do Dia 4 (`template.py` ou `exemplo_referencia.py`)
- [ ] Conceitos de rate limiting básico (Dia 2 tinha rate limiting por IP)
- [ ] FastAPI exception handling: https://fastapi.tiangolo.com/tutorial/handling-errors/

### Recursos úteis para ler:
- SlowAPI documentation: https://slowapi.readthedocs.io/
- Python logging (structured): https://docs.python.org/3/library/logging.html
- FastAPI middleware: https://fastapi.tiangolo.com/advanced/middleware/

### Conceitos pré-requisitos:
- Rate limiting básico (já visto no Dia 2)
- Exception handling em Python
- Logging básico em Python
- Middleware em FastAPI (SecurityHeadersMiddleware do Dia 3)

---

## 💡 Dicas Importantes

1. **Rate limiting por usuário:** Usar `slowapi` com função customizada que extrai `user_id` do token JWT
2. **Exception handlers:** Criar handlers para `HTTPException`, `ValidationError` e `Exception` genérica
3. **Logging estruturado:** Usar formato JSON para facilitar parsing (ex: `{"level": "INFO", "message": "...", "user_id": "...", "path": "..."}`)
4. **Testes:** Testar rate limit (429) e diferentes tipos de erro (400, 404, 500)
5. **Se o tempo estourar:** Priorizar rate limiting + exception handlers básicos; logging pode ser simplificado

---

## 🎯 Objetivos do Dia 5 (Resumo)

1. Implementar rate limiting por usuário (não só por IP)
2. Adicionar exception handlers globais
3. Configurar logging estruturado
4. Criar middleware de request logging
5. Testar cenários de erro e rate limit

---

**Última atualização:** 12 Dez 2025  
**Status:** 🟡 Pronto como briefing
