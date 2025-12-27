# ✅ Checklist - Dia 6 (Sábado, 14 Dez 2025)

## 🎯 Objetivo do Dia
Implementar testes automatizados com pytest e exception handlers básicos para a API, alcançando cobertura mínima de 60% e validando funcionalidades críticas.

---

> Todas as fases abaixo devem caber dentro dos **160min totais**, englobando leitura, exercícios/testes e preenchimento dos documentos. Não use autocomplete/IA para escrever o código.

## 📋 FASE 1: Preparação (5min)

### Revisão Inicial
- [ X] Abrir este checklist
- [ X] Ler `README.md` para entender contexto e objetivos
- [ X] Ler `CONTEXTO_AGENTE.md` para detalhes técnicos
- [ X] Verificar que o código do Dia 5 está funcionando (template.py ou exemplo_completo.py)
- [ X] Confirmar que variáveis de ambiente estão configuradas (`.env`)

**Como fazer:**
1. Abra o terminal e navegue até `Semanas/Semana3/Dia6/`
2. Leia os arquivos README.md e CONTEXTO_AGENTE.md
3. Verifique se o código do Dia 5 está disponível (pode copiar template.py do Dia 5)

**Por que:**
Garantir que você entende o contexto e tem o ambiente preparado antes de começar.

**Tempo estimado:** 5 minutos  
**Quando:** Início da sessão

---

## 📋 FASE 2: Leitura Guiada (20min)

### Estudo dos Conceitos
- [ x] Ler `GUIA_PASSO_A_PASSO.md` seção 2: Entender pytest
- [ x] Ler `GUIA_PASSO_A_PASSO.md` seção 3: Entender TestClient
- [ x] Ler `GUIA_PASSO_A_PASSO.md` seção 4: Entender Fixtures
- [ x] Ler `GUIA_PASSO_A_PASSO.md` seção 5: Entender Exception Handlers básicos
- [ x] Ler `GUIA_PASSO_A_PASSO.md` seção 6: Escrever Testes Básicos
- [ x] Anotar dúvidas que serão respondidas na prática

**Como fazer:**
1. Abra `GUIA_PASSO_A_PASSO.md`
2. Leia cada seção cuidadosamente
3. Anote conceitos que não ficaram claros
4. Consulte `exemplo_completo.py` se precisar ver exemplos práticos

**Por que:**
Entender os conceitos de pytest, TestClient e fixtures antes de implementar facilita a criação dos testes.

**Tempo estimado:** 20 minutos  
**Quando:** Após preparação

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção correspondente
- Pytest Documentation: https://docs.pytest.org/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/

---

## 📋 FASE 3: Construção Guiada (90min)

### 3.1: Configurar Ambiente de Testes (10min)
- [ x] Instalar dependências: `pip install -r requirements.txt`
- [ x] Verificar instalação: `pytest --version`
- [ x] Criar estrutura de diretórios `tests/`
- [ x] Criar `tests/__init__.py` (arquivo vazio)

**Como fazer:**
1. No terminal, execute: `pip install -r requirements.txt`
2. Verifique se pytest foi instalado: `pytest --version`
3. Crie a pasta `tests/` se não existir
4. Crie arquivo vazio `tests/__init__.py`

**Tempo estimado:** 10 minutos

---

### 3.2: Criar Fixtures Compartilhadas (15min)
- [ x] Criar `tests/conftest.py`
- [ x] Implementar fixture `client` (TestClient do FastAPI)
- [ x] Implementar fixture `auth_headers` (token de autenticação)
- [ x] Implementar fixture `test_user` (dados de usuário de teste)

**Como fazer:**
1. Crie `tests/conftest.py`
2. Importe `TestClient` do FastAPI
3. Crie fixture `client` que retorna TestClient(app)
4. Crie fixture `auth_headers` que faz login e retorna headers com token
5. Crie fixture `test_user` com dados de usuário padrão

**Dica:** Consulte `GUIA_PASSO_A_PASSO.md` seção 4 e `exemplo_completo.py` para ver exemplos de fixtures.

**Tempo estimado:** 15 minutos

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção 4: Fixtures do pytest
- Consultar `exemplo_completo.py` para ver implementação completa

---

### 3.3: Testes de Autenticação (20min)
- [ x] Criar `tests/test_auth.py`
- [ x] Teste: Login com credenciais válidas
- [ x] Teste: Login com credenciais inválidas
- [ x] Teste: Refresh token válido
- [ x] Teste: Refresh token inválido
- [ x] Teste: Acesso a rota protegida sem token
- [ x] Teste: Acesso a rota protegida com token inválido

**Como fazer:**
1. Crie `tests/test_auth.py`
2. Importe fixtures de `conftest.py`
3. Implemente testes usando `client.post()` e `client.get()`
4. Use `assert` para verificar status codes e respostas

**Dica:** Consulte `GUIA_PASSO_A_PASSO.md` seção 6 e `exemplo_completo.py` para ver exemplos.

**Tempo estimado:** 20 minutos

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção 6: Testes de autenticação
- Consultar `exemplo_completo.py` para ver implementação completa

---

### 3.4: Testes de Chat e Histórico (25min)
- [ x] Criar `tests/test_chat.py`
- [ x] Teste: Criar nova conversa
- [ x] Teste: Enviar mensagem em conversa existente
- [ x] Teste: Listar conversas do usuário
- [ x] Teste: Obter mensagens de uma conversa
- [ ] Teste: Chat com streaming (opcional, se tempo permitir)

**Como fazer:**
1. Crie `tests/test_chat.py`
2. Use fixture `auth_headers` para autenticação
3. Teste fluxo completo: criar conversa → enviar mensagem → listar conversas → obter mensagens
4. Verifique que mensagens são salvas corretamente

**Dica:** Consulte `GUIA_PASSO_A_PASSO.md` seção 6 e `exemplo_completo.py` para ver exemplos.

**Tempo estimado:** 25 minutos

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção 6: Testes de chat básico
- Consultar `exemplo_completo.py` para ver implementação completa

---

### 3.5: Testes de Rate Limiting (10min)
- [ x] Criar `tests/test_rate_limiting.py`
- [ x] Teste: Rate limit de login (5/min)
- [ x] Teste: Rate limit de chat (30/min)
- [ x] Teste: Rate limit por usuário (não compartilhado entre usuários)

**Como fazer:**
1. Crie `tests/test_rate_limiting.py`
2. Faça múltiplas requisições até atingir o limite
3. Verifique que a última requisição retorna 429 (Too Many Requests)
4. Teste que rate limit é por usuário (dois usuários diferentes podem fazer 30 req/min cada)

**Dica:** Use `time.sleep()` ou mock para acelerar testes de rate limiting.

**Tempo estimado:** 10 minutos

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção 6: Testes de rate limiting básico
- Consultar `exemplo_completo.py` para ver implementação completa

---

### 3.6: Testes de Exception Handlers (10min)
- [ x] Criar `tests/test_exceptions.py`
- [ x] Teste: HTTPException retorna JSON padronizado
- [ x] Teste: ValidationError retorna JSON com detalhes
- [ x] Teste: Exception genérica retorna mensagem genérica ao cliente

**Como fazer:**
1. Crie `tests/test_exceptions.py`
2. Teste endpoints que geram erros intencionalmente
3. Verifique que respostas de erro seguem formato JSON padronizado
4. Verifique que Exception genérica não expõe detalhes ao cliente

**Tempo estimado:** 10 minutos

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção 5: Exception Handlers básicos
- Consultar `exemplo_completo.py` para ver implementação completa

---

## 📋 FASE 4: Consolidação (25min)

### 4.1: Executar Testes (10min)
- [ x] Executar todos os testes: `pytest tests/ -v`
- [ x] Verificar que todos os testes passam
- [ x] Corrigir falhas se houver

**Como fazer:**
1. No terminal, execute: `pytest tests/ -v`
2. Analise saída e corrija erros
3. Execute novamente até todos passarem

**Tempo estimado:** 10 minutos

---

### 4.2: Verificar Cobertura (10min)
- [ x] Executar com cobertura: `pytest --cov=template --cov-report=term-missing`
- [ x] Verificar que cobertura está acima de 60%
- [ x] Identificar linhas não cobertas (se houver)
- [ x] Adicionar testes para aumentar cobertura (se necessário e tempo permitir)

**Como fazer:**
1. Execute: `pytest --cov=template --cov-report=term-missing`
2. Analise relatório de cobertura
3. Se cobertura < 60%, adicione testes para funcionalidades críticas não cobertas

**Tempo estimado:** 10 minutos

**Referências:**
- Consultar `GUIA_PASSO_A_PASSO.md` seção 7: Executar Testes e Verificar Cobertura
- Pytest-cov: https://pytest-cov.readthedocs.io/

---

### 4.3: Checklist Parcial (5min)
- [ x] Marcar itens concluídos do checklist
- [ x] Verificar que código está funcionando
- [ x] Anotar dificuldades encontradas

**Tempo estimado:** 5 minutos

---

## 📋 FASE 5: Registro e Handoff (20min)

### 5.1: Checklist Final (5min)
- [ x] Revisar checklist completo
- [ x] Marcar todos os itens concluídos
- [ x] Verificar que todos os testes passam

**Tempo estimado:** 5 minutos

---

### 5.2: Journal (10min)
- [ x] Preencher `journal.md` com:
  - O que foi feito hoje
  - O que foi aprendido
  - Dificuldades enfrentadas
  - Métricas (tempo, cobertura, número de testes)

**Tempo estimado:** 10 minutos

---

### 5.3: CONTEXTO_PROXIMO_DIA (5min)
- [ x] Preencher `CONTEXTO_PROXIMO_DIA.md` com:
  - O que foi aprendido hoje
  - Código criado (estrutura de testes)
  - Por que o Dia 7 é importante
  - Como construir o Dia 7

**Tempo estimado:** 5 minutos

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min no total (inclui leitura dos documentos, execução de testes e preenchimento de checklist + journal, **sem usar autocomplete/IA para gerar código**)

### ✅ Critérios de Sucesso:
- [ ] Todos os testes passam
- [ ] Cobertura de código ≥ 60%
- [ ] Testes cobrem funcionalidades críticas (auth, chat, rate limiting, exceptions)
- [ ] Estrutura de testes está organizada e reutilizável
- [ ] Journal preenchido
- [ ] CONTEXTO_PROXIMO_DIA preenchido

### 🎯 Streak: 18/56 dias

**Parabéns por completar o Dia 6!** 🚀

---

**Última atualização:** 14 Dez 2025
