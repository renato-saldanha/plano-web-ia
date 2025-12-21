# ✅ Checklist - Dia 7 (Domingo, 15 Dez 2025)

## 🎯 Objetivo do Dia
Configurar Swagger/OpenAPI para documentação interativa, completar checklist de deploy e publicar a API em produção (Railway/Render).

---

> Todas as fases abaixo devem caber dentro dos **160min totais**, englobando leitura, exercícios/testes e preenchimento dos documentos. Não use autocomplete/IA para escrever o código.

## 📋 FASE 1: Preparação (5min)

### Revisão Inicial
- [ ] Abrir este checklist
- [ ] Ler `README.md` para entender contexto e objetivos
- [ ] Ler `CONTEXTO_AGENTE.md` para detalhes técnicos
- [ ] Verificar que o código do Dia 6 está funcionando (template.py ou exemplo_referencia.py)
- [ ] Confirmar que variáveis de ambiente estão configuradas (`.env` local)

**Como fazer:**
1. Abra o terminal e navegue até `Semanas/Semana3/Dia7/`
2. Leia os arquivos README.md e CONTEXTO_AGENTE.md
3. Verifique se o código do Dia 6 está disponível (pode copiar template.py do Dia 6)

**Por que:**
Garantir que você entende o contexto e tem o ambiente preparado antes de começar.

**Tempo estimado:** 5 minutos  
**Quando:** Início da sessão

---

## 📋 FASE 2: Leitura Guiada (20min)

### Estudo dos Conceitos
- [ ] Ler `GUIA_APRENDIZADO.md` seção 1: Swagger/OpenAPI no FastAPI
- [ ] Ler `GUIA_APRENDIZADO.md` seção 2: Checklist de Deploy
- [ ] Ler `GUIA_APRENDIZADO.md` seção 3: Deploy no Railway
- [ ] Ler `GUIA_APRENDIZADO.md` seção 4: Deploy no Render (alternativa)
- [ ] Ler `GUIA_APRENDIZADO.md` seção 5: Smoke Tests em Produção
- [ ] Anotar dúvidas que serão respondidas na prática

**Como fazer:**
1. Abra `GUIA_APRENDIZADO.md`
2. Leia cada seção cuidadosamente
3. Anote conceitos que não ficaram claros
4. Consulte `exemplo_referencia.py` (quando criado) se precisar ver exemplos práticos

**Por que:**
Entender os conceitos antes de implementar facilita o processo e evita erros.

**Tempo estimado:** 20 minutos  
**Quando:** Após preparação

---

## 📋 FASE 3: Construção Guiada (90min)

### 3.1: Configurar Swagger no template.py (30min)

#### Copiar código do Dia 6
- [ ] Copiar `template.py` do Dia 6 para o Dia 7
- [ ] Verificar que o código funciona localmente (`uvicorn template:app --reload`)

#### Configurar Metadados OpenAPI
- [ ] Adicionar `title` personalizado
- [ ] Adicionar `description` detalhada da API
- [ ] Adicionar `version` (ex: "1.0.0")
- [ ] Adicionar `contact` (nome e email)
- [ ] Adicionar `license_info` (opcional)

**Dica:** Consulte `GUIA_APRENDIZADO.md` seção 1.3 para exemplo.

#### Adicionar Tags aos Endpoints
- [ ] Tag "Auth" para endpoints de autenticação (`/login`, `/refresh`)
- [ ] Tag "Chat" para endpoints de chat (`/chat`, `/conversations`, `/api/generate`)
- [ ] Tag "Health" para endpoint de health check (`/health`)

**Dica:** Adicione `tags=["NomeDaTag"]` ao decorator do endpoint.

#### Adicionar Descrições
- [ ] Adicionar docstrings detalhadas em cada endpoint
- [ ] Adicionar descrições nos modelos Pydantic usando `Field(description="...")`
- [ ] Adicionar exemplos nos modelos usando `Field(example="...")`

**Tempo estimado:** 30 minutos

---

### 3.2: Testar Swagger Localmente (10min)

#### Verificar Documentação
- [ ] Iniciar servidor local (`uvicorn template:app --reload`)
- [ ] Acessar `http://localhost:8000/docs` no navegador
- [ ] Verificar que metadados aparecem corretamente
- [ ] Verificar que tags organizam endpoints
- [ ] Verificar que descrições e exemplos aparecem
- [ ] Testar um endpoint no Swagger UI (ex: `/health`)

**Tempo estimado:** 10 minutos

---

### 3.3: Preparar Checklist de Deploy (15min)

#### Listar Variáveis de Ambiente
- [ ] Criar lista completa de variáveis necessárias
- [ ] Documentar cada variável (o que faz, exemplo de valor)
- [ ] Identificar quais precisam ser geradas/alteradas para produção

**Variáveis necessárias:**
- `JWT_SECRET_KEY` (gerar nova para produção!)
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `REFRESH_TOKEN_EXPIRE_DAYS`
- `OPENAI_API_KEY`

#### Verificar Configurações
- [ ] CORS configurado corretamente (origins permitidas)
- [ ] Headers de segurança implementados (já feito no Dia 5)
- [ ] Health check funcionando (`/health`)
- [ ] Logging estruturado funcionando (já feito no Dia 5)

**Tempo estimado:** 15 minutos

---

### 3.4: Fazer Deploy no Railway (25min)

#### Configurar Projeto no Railway
- [ ] Criar conta no Railway (https://railway.app)
- [ ] Criar novo projeto
- [ ] Conectar repositório GitHub (ou fazer upload manual)

#### Configurar Variáveis de Ambiente
- [ ] Adicionar `JWT_SECRET_KEY` (gerar nova chave forte)
- [ ] Adicionar `ALGORITHM`
- [ ] Adicionar `ACCESS_TOKEN_EXPIRE_MINUTES`
- [ ] Adicionar `REFRESH_TOKEN_EXPIRE_DAYS`
- [ ] Adicionar `OPENAI_API_KEY`

**Dica:** Railway gera `$PORT` automaticamente, não precisa configurar.

#### Configurar Start Command
- [ ] Configurar start command: `uvicorn template:app --host 0.0.0.0 --port $PORT`
- [ ] Verificar que `requirements.txt` está na raiz do projeto

#### Fazer Deploy
- [ ] Fazer push do código (ou deploy manual no Railway)
- [ ] Aguardar build completar
- [ ] Verificar logs para erros
- [ ] Anotar URL de produção gerada

**Tempo estimado:** 25 minutos

**Alternativa:** Se Railway não funcionar, usar Render seguindo `GUIA_APRENDIZADO.md` seção 4.

---

### 3.5: Testar Deploy (10min)

#### Verificar URL de Produção
- [ ] Acessar URL gerada no navegador
- [ ] Verificar que retorna 404 ou redireciona (esperado para rota raiz)

#### Testar Swagger UI
- [ ] Acessar `https://sua-url.railway.app/docs`
- [ ] Verificar que Swagger UI carrega
- [ ] Verificar que todos os endpoints aparecem
- [ ] Verificar que metadados estão corretos

**Tempo estimado:** 10 minutos

---

## 📋 FASE 4: Consolidação (25min)

### 4.1: Smoke Tests em Produção (20min)

#### Testar Endpoints Críticos
- [ ] Testar `/health` (esperado: 200 OK)
- [ ] Testar `/docs` (esperado: Swagger UI carregando)
- [ ] Testar `/login` (esperado: token retornado)
- [ ] Testar endpoint protegido com token (esperado: resposta válida)

**Como fazer:**
1. Use `curl` ou Postman
2. Ou crie script Python seguindo `GUIA_APRENDIZADO.md` seção 5.3

#### Verificar Funcionalidades
- [ ] Autenticação funcionando
- [ ] Rate limiting funcionando (testar muitas requisições)
- [ ] Exception handlers funcionando (testar requisição inválida)
- [ ] Logs aparecendo no painel do Railway

**Tempo estimado:** 20 minutos

---

### 4.2: Documentar Deploy (5min)

#### Anotar Informações
- [ ] URL de produção: `https://...`
- [ ] URL do Swagger: `https://.../docs`
- [ ] Variáveis de ambiente configuradas (listar)
- [ ] Problemas encontrados e soluções (se houver)

**Tempo estimado:** 5 minutos

---

## 📋 FASE 5: Registro e Handoff (20min)

### 5.1: Preencher Journal (10min)
- [ ] Preencher `journal.md` com:
  - O que foi feito hoje
  - O que foi aprendido
  - Desafios enfrentados
  - Métricas (URL de produção, endpoints documentados, etc.)
  - Links úteis

**Tempo estimado:** 10 minutos

---

### 5.2: Criar CONTEXTO_PROXIMO_DIA (10min)
- [ ] Preencher `CONTEXTO_PROXIMO_DIA.md` com:
  - Resumo do que foi aprendido (Swagger, deploy, produção)
  - Transição para Semana 4 (Backend Alternativo - Bun + Hono)
  - Como o aprendizado de FastAPI será aplicado no contexto alternativo

**Tempo estimado:** 10 minutos

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min no total (inclui leitura dos documentos, execução de exercícios/testes e preenchimento de checklist + journal, **sem usar autocomplete/IA para gerar código**)

### ✅ Critérios de Sucesso:
- [ ] Swagger UI acessível e funcional em produção
- [ ] Metadados da API configurados corretamente
- [ ] Endpoints documentados com tags e descrições
- [ ] Checklist de deploy completo
- [ ] API em produção (Railway ou Render)
- [ ] Smoke tests passando em produção
- [ ] Journal preenchido
- [ ] CONTEXTO_PROXIMO_DIA criado

### 🎯 Streak: X/56 dias

**Parabéns por completar o Dia 7 e a Semana 3!** 🚀

---

**Última atualização:** 15 Dez 2025

