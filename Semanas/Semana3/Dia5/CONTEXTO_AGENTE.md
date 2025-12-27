# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 3 de 8  
**Dia:** 5 de 7 (Sexta, 13 Dez 2025)  
**Diretório:** `Semanas/Semana3/Dia5/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: API FastAPI básica com endpoint simples
- ✅ Dia 2: Autenticação JWT completa (login, refresh, proteção de rotas)
- ✅ Dia 3: Streaming de respostas com SSE e integração LLM
- ✅ Dia 4: Sistema de histórico de conversas (persistência em memória, gerenciamento de threads)

### O que está em progresso:
- 🟡 Dia 5: Rate limiting por usuário e logging estruturado

### O que falta fazer (hoje):
- [ ] Implementar rate limiting por usuário (usando `slowapi` com função customizada)
- [ ] Configurar logging estruturado usando módulos compartilhados (`common/logging.py`)
- [ ] Criar middleware de request logging
- [ ] Testar cenários de rate limit

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- `README.md` - Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- `checklist.md` - Checklist detalhado com fases
- `journal.md` - Template para reflexão
- `requirements.txt` - Dependências Python (obrigatório sempre, mesmo que vazio)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório para todos os dias)

### Arquivos de Aprendizado (Nível 1):
- `exemplo_completo.py` - Código completo comentado (Rate Limiting + Logging)
- `GUIA_PASSO_A_PASSO.md` - Tutorial detalhado passo-a-passo (Nível 1)
- `template.py` - Estrutura com TODOs para implementar rate limiting e logging
- `exercicios.md` - Exercícios de teste para validar implementação

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12
- **Framework:** FastAPI
- **Bibliotecas principais:**
  - `slowapi` - Rate limiting
  - `logging` (stdlib) - Logging estruturado
  - `pydantic` - Validação de dados
  - `jose` - JWT tokens
  - `langchain_openai` - Integração com LLM

### Configuração Necessária:
- Variáveis de ambiente (`.env`):
  - `JWT_SECRET_KEY`
  - `ALGORITHM`
  - `ACCESS_TOKEN_EXPIRE_MINUTES`
  - `REFRESH_TOKEN_EXPIRE_DAYS`
  - `OPENAI_API_KEY`

### Objetivo do Dia:
Adicionar camadas de segurança (rate limiting por usuário) e observabilidade (logging estruturado) à API. Exception handling será abordado no Dia 6 junto com testes.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Ler `GUIA_PASSO_A_PASSO.md` para entender conceitos de rate limiting e logging
2. Implementar rate limiting por usuário no `template.py`
3. Configurar logging estruturado usando módulos compartilhados (`common/logging.py`)
4. Criar middleware de request logging
5. Testar cenários de rate limit

### Próximo Dia:
- Dia 6: Testes automatizados (pytest) + Exception handlers básicos (Nível 1)

---

## 📚 Referências Rápidas

### Rate Limiting:
- SlowAPI: https://slowapi.readthedocs.io/
- Rate limiting por usuário: usar função customizada que extrai `user_id` do token JWT

### Módulos Compartilhados:
- `common/logging.py` - JSONFormatter, log_structured, setup_logger
- `common/auth.py` - Funções de autenticação JWT
- `common/models.py` - Modelos Pydantic compartilhados
- `common/conversations.py` - Funções de gerenciamento de histórico

### Logging:
- Python Logging: https://docs.python.org/3/library/logging.html
- Logging estruturado: usar formato JSON para facilitar parsing
- Middleware: logar método, path, status, tempo de resposta

---

**Última atualização:** 13 Dez 2025  
**Status:** 🟡 Em progresso
