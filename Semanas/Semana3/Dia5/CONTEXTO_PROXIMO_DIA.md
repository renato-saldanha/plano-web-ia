# 🎯 Contexto para Construir o Dia 6

## 📚 O que aprendemos hoje (Dia 5)

### Conceitos Principais
- Rate limiting por usuário usando `slowapi` com função customizada
- Exception handlers globais no FastAPI (HTTPException, ValidationError, Exception genérica)
- Logging estruturado em formato JSON para facilitar monitoramento
- Middleware de request logging para rastreabilidade completa

### Habilidades Desenvolvidas
- Implementar rate limiting baseado em user_id extraído do token JWT
- Criar exception handlers que retornam respostas JSON padronizadas
- Configurar logging estruturado com formato JSON
- Criar middleware customizado para logar todas as requisições
- Garantir que erros sejam logados completamente no servidor, mas retornem mensagens genéricas ao cliente

### Código Criado
- `template.py` (TODOS resolvidos) — sistema completo com rate limiting, exception handling e logging
- Função `get_user_id_for_rate_limit()` para extrair user_id do token JWT
- Exception handlers globais para todos os tipos de erro
- Classe `JSONFormatter` para logging estruturado
- Função helper `log_structured()` para facilitar logging
- Middleware `RequestLoggingMiddleware` para logar todas as requisições

---

## 🔗 Por que o Dia 6 é importante

A API agora está robusta e pronta para produção com rate limiting, tratamento de erros e observabilidade. No entanto, falta **testes automatizados** para garantir que tudo funciona corretamente e prevenir regressões futuras.

O Dia 6 focará em:
- **Testes automatizados com pytest:** Garantir que funcionalidades críticas estão funcionando
- **Cobertura de testes:** Alcançar pelo menos 60% de cobertura (meta realista)
- **Testes de integração:** Validar fluxos completos (login → chat → histórico)
- **Testes de rate limiting e exception handling:** Garantir que segurança e tratamento de erros funcionam

---

## 🎯 O que será feito no Dia 6

### Objetivo Principal
Implementar testes automatizados com pytest para a API, alcançando cobertura mínima de 60% e validando funcionalidades críticas.

### Conceitos que serão aprendidos
- Estrutura de testes com pytest
- TestClient do FastAPI para testes de endpoints
- Fixtures do pytest para setup e teardown
- Testes de autenticação e autorização
- Testes de rate limiting
- Testes de exception handlers
- Cálculo de cobertura de código (pytest-cov)

### Como se relaciona com Dia 5
- Testará as funcionalidades implementadas hoje (rate limiting, exception handling, logging)
- Garantirá que mudanças futuras não quebrem funcionalidades existentes
- Validará que rate limiting, exception handlers e logging estão funcionando corretamente

---

## 📋 Como Construir o Dia 6

### 1. Criar Estrutura Básica
```
Dia6/
├── README.md
├── CONTEXTO_AGENTE.md
├── checklist.md
├── journal.md
├── requirements.txt
├── CONTEXTO_PROXIMO_DIA.md
├── template.py (herdar código do Dia 5)
├── tests/
│   ├── __init__.py
│   ├── conftest.py (fixtures compartilhadas)
│   ├── test_auth.py (testes de autenticação)
│   ├── test_chat.py (testes de chat)
│   ├── test_rate_limiting.py (testes de rate limiting)
│   └── test_exceptions.py (testes de exception handlers)
├── GUIA_APRENDIZADO.md (pytest, TestClient, fixtures, cobertura)
├── exemplo_referencia.py (código completo com testes)
└── exercicios.md (exercícios de teste)
```

**Ordem sugerida:**
1. Criar pasta `Dia6/` e subpasta `tests/`
2. Copiar código do Dia 5 para `template.py`
3. Criar arquivos obrigatórios (README, CONTEXTO_AGENTE, checklist, journal)
4. Criar `GUIA_APRENDIZADO.md` sobre pytest
5. Criar testes seguindo o checklist

### 2. Definir Nível de Scaffolding

**Nível recomendado:** **2** (conceitos parcialmente conhecidos: testes são aplicação de conceitos conhecidos em novo contexto)

**Arquivos necessários:**
- `template.py` (herdar código do Dia 5)
- `GUIA_APRENDIZADO.md` (pytest, TestClient, fixtures, cobertura)
- `exemplo_referencia.py` (código completo com testes de exemplo)
- `exercicios.md` (exercícios de teste)
- `tests/` (estrutura de testes)

### 3. Criar Arquivos de Aprendizado

**GUIA_APRENDIZADO.md deve cobrir:**
- Introdução ao pytest
- TestClient do FastAPI
- Fixtures do pytest (setup, teardown, dependências)
- Testes de autenticação (login, refresh, proteção de rotas)
- Testes de endpoints (chat, histórico)
- Testes de rate limiting
- Testes de exception handlers
- Cálculo de cobertura (pytest-cov)

**Estrutura de testes sugerida:**
- `conftest.py`: Fixtures compartilhadas (client, tokens, etc.)
- `test_auth.py`: Testes de login, refresh, autenticação
- `test_chat.py`: Testes de chat, histórico, streaming
- `test_rate_limiting.py`: Testes de rate limiting
- `test_exceptions.py`: Testes de exception handlers

**template.py:**
- Herdar código completo do Dia 5 (sem modificações, apenas para referência)

**exemplo_referencia.py:**
- Código completo do Dia 5 + testes completos como referência

### 4. Seguir Checklist

Dividir em fases:
- Preparação (5min)
- Leitura guiada (20min) — GUIA_APRENDIZADO.md
- Construção guiada (90min) — criar testes seguindo estrutura sugerida
- Consolidação (25min) — executar testes, verificar cobertura, corrigir falhas
- Registro (20min) — journal e CONTEXTO_PROXIMO_DIA

---

## 📚 Recursos de Preparação

### O que revisar antes de começar:
- [ ] Código do Dia 5 (`template.py` ou `exemplo_referencia.py`)
- [ ] Conceitos básicos de testes unitários (se necessário)
- [ ] Documentação do pytest: https://docs.pytest.org/
- [ ] TestClient do FastAPI: https://fastapi.tiangolo.com/tutorial/testing/

### Recursos úteis para ler:
- Pytest Documentation: https://docs.pytest.org/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- Pytest Fixtures: https://docs.pytest.org/en/stable/fixture.html
- Pytest-cov (cobertura): https://pytest-cov.readthedocs.io/

### Conceitos pré-requisitos:
- Estrutura básica de testes (assert, setup, teardown)
- Autenticação JWT (já implementado)
- Rate limiting (já implementado)
- Exception handling (já implementado)

---

## 💡 Dicas Importantes

1. **Estrutura de testes:** Organizar testes por funcionalidade (auth, chat, rate limiting, etc.)
2. **Fixtures:** Usar fixtures para setup comum (client, tokens, dados de teste)
3. **Cobertura:** Focar em funcionalidades críticas primeiro (auth, chat, rate limiting)
4. **Testes de integração:** Testar fluxos completos (login → chat → histórico)
5. **Testes de rate limiting:** Usar `time.sleep()` ou mock para testar limites
6. **Se o tempo estourar:** Priorizar testes de funcionalidades críticas (auth, chat básico)

---

## 🎯 Objetivos do Dia 6 (Resumo)

1. Configurar ambiente de testes (pytest, pytest-cov)
2. Criar estrutura de testes organizada
3. Implementar testes de autenticação
4. Implementar testes de chat e histórico
5. Implementar testes de rate limiting
6. Implementar testes de exception handlers
7. Alcançar cobertura mínima de 60%
8. Executar todos os testes e garantir que passam

---

**Última atualização:** 13 Dez 2025  
**Status:** 🟡 Pronto como briefing
