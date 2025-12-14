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
- 🟡 Dia 5: Rate limiting por usuário, tratamento de erros e logging estruturado

### O que falta fazer (hoje):
- [ ] Implementar rate limiting por usuário (usando `slowapi` com função customizada)
- [ ] Criar exception handlers globais (HTTPException, ValidationError, Exception genérica)
- [ ] Configurar logging estruturado (formato JSON)
- [ ] Criar middleware de request logging
- [ ] Testar cenários de erro e rate limit

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
- `template.py` - Estrutura com TODOs para implementar rate limiting, exception handlers e logging
- `GUIA_APRENDIZADO.md` - Conceitos teóricos + passo-a-passo sobre rate limiting, exception handling e logging estruturado
- `exemplo_referencia.py` - Implementação completa como referência
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
Adicionar camadas de segurança (rate limiting por usuário) e observabilidade (logging estruturado) à API, além de tratamento robusto de erros para preparar o código para produção.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Ler `GUIA_APRENDIZADO.md` para entender conceitos de rate limiting, exception handling e logging
2. Implementar rate limiting por usuário no `template.py`
3. Criar exception handlers globais
4. Configurar logging estruturado
5. Criar middleware de request logging
6. Testar cenários de erro e rate limit

### Próximo Dia:
- Dia 6: Foco em testes automatizados (pytest) com cobertura mínima de 60%

---

## 📚 Referências Rápidas

### Rate Limiting:
- SlowAPI: https://slowapi.readthedocs.io/
- Rate limiting por usuário: usar função customizada que extrai `user_id` do token JWT

### Exception Handling:
- FastAPI Exception Handlers: https://fastapi.tiangolo.com/tutorial/handling-errors/
- Tratar: `HTTPException`, `ValidationError`, `Exception` genérica

### Logging:
- Python Logging: https://docs.python.org/3/library/logging.html
- Logging estruturado: usar formato JSON para facilitar parsing
- Middleware: logar método, path, status, tempo de resposta

---

**Última atualização:** 13 Dez 2025  
**Status:** 🟡 Em progresso
