# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 3 de 8  
**Dia:** 6 de 7 (Sábado, 14 Dez 2025)  
**Diretório:** `Semanas/Semana3/Dia6/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: API FastAPI básica com endpoint simples
- ✅ Dia 2: Autenticação JWT completa (login, refresh, proteção de rotas)
- ✅ Dia 3: Streaming de respostas com SSE e integração LLM
- ✅ Dia 4: Sistema de histórico de conversas (persistência em memória, gerenciamento de threads)
- ✅ Dia 5: Rate limiting por usuário + Logging estruturado

### O que está em progresso:
- 🟡 Dia 6: Testes automatizados (pytest) com cobertura mínima de 60%

### O que falta fazer (hoje):
- [ ] Configurar ambiente de testes (pytest, pytest-cov)
- [ ] Criar estrutura de testes organizada
- [ ] Implementar testes de autenticação
- [ ] Implementar testes de chat e histórico
- [ ] Implementar testes de rate limiting
- [ ] Implementar testes de exception handlers
- [ ] Alcançar cobertura mínima de 60%
- [ ] Executar todos os testes e garantir que passam

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
- `exemplo_completo.py` - Código completo com testes + exception handlers básicos
- `GUIA_PASSO_A_PASSO.md` - Tutorial detalhado sobre pytest (Nível 1)
- `template.py` - Template com TODOs para testes + exception handlers básicos
- `exercicios.md` - Exercícios de teste para validar implementação

### Estrutura de Testes:
- `tests/__init__.py` - Arquivo vazio para tornar tests um pacote Python
- `tests/conftest.py` - Fixtures compartilhadas (client, tokens, dados de teste)
- `tests/test_auth.py` - Testes de autenticação (login, refresh, proteção de rotas)
- `tests/test_chat.py` - Testes de chat, histórico, streaming
- `tests/test_rate_limiting.py` - Testes de rate limiting
- `tests/test_exceptions.py` - Testes de exception handlers

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12
- **Framework:** FastAPI
- **Bibliotecas de teste:**
  - `pytest` - Framework de testes
  - `pytest-cov` - Cobertura de código
  - `pytest-asyncio` - Suporte a testes assíncronos
  - `httpx` - Cliente HTTP para testes (já incluído no FastAPI TestClient)

### Configuração Necessária:
- Variáveis de ambiente (`.env`):
  - `JWT_SECRET_KEY`
  - `ALGORITHM`
  - `ACCESS_TOKEN_EXPIRE_MINUTES`
  - `REFRESH_TOKEN_EXPIRE_DAYS`
  - `OPENAI_API_KEY` (pode ser mockado nos testes)

### Objetivo do Dia:
Implementar testes automatizados e exception handlers básicos para a API, garantindo que funcionalidades críticas estão funcionando corretamente e alcançando cobertura mínima de 60%.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Ler `GUIA_PASSO_A_PASSO.md` para entender conceitos de pytest, TestClient e fixtures
2. Configurar ambiente de testes (instalar pytest, pytest-cov, pytest-asyncio)
3. Criar `tests/conftest.py` com fixtures compartilhadas
4. Implementar testes de autenticação em `tests/test_auth.py`
5. Implementar testes de chat em `tests/test_chat.py`
6. Implementar testes de rate limiting em `tests/test_rate_limiting.py`
7. Implementar testes de exception handlers em `tests/test_exceptions.py`
8. Executar testes e verificar cobertura (meta: 60%)

### Próximo Dia:
- Dia 7: Configurar Swagger, checklist de deploy e publicar no Railway

---

## 📚 Referências Rápidas

### Pytest:
- Pytest Documentation: https://docs.pytest.org/
- Pytest Fixtures: https://docs.pytest.org/en/stable/fixture.html
- Pytest-asyncio: https://pytest-asyncio.readthedocs.io/

### FastAPI Testing:
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- TestClient: https://fastapi.tiangolo.com/advanced/testing/

### Cobertura:
- Pytest-cov: https://pytest-cov.readthedocs.io/
- Comando: `pytest --cov=template --cov-report=html`

### Estrutura de Testes:
- Organizar por funcionalidade (auth, chat, rate limiting, exceptions)
- Usar fixtures para setup comum (client, tokens, dados de teste)
- Testar casos de sucesso e falha
- Testar edge cases e limites

---

**Última atualização:** 14 Dez 2025  
**Status:** 🟡 Em progresso
