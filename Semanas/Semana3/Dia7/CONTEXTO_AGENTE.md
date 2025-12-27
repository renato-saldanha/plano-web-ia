# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 3 de 8  
**Dia:** 7 de 7 (Domingo, 15 Dez 2025)  
**Diretório:** `Semanas/Semana3/Dia7/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: API FastAPI básica com endpoint simples
- ✅ Dia 2: Autenticação JWT completa (login, refresh, proteção de rotas)
- ✅ Dia 3: Streaming de respostas com SSE e integração LLM
- ✅ Dia 4: Sistema de histórico de conversas (persistência em memória, gerenciamento de threads)
- ✅ Dia 5: Rate limiting por usuário, tratamento de erros e logging estruturado
- ✅ Dia 6: Testes automatizados (pytest) com cobertura mínima de 60%

### O que está em progresso:
- 🟡 Dia 7: Configurar Swagger/OpenAPI, checklist de deploy e publicar no Railway

### O que falta fazer (hoje):
- [ ] Configurar metadados OpenAPI no FastAPI (title, description, version, contact, license)
- [ ] Adicionar tags e descrições aos endpoints
- [ ] Adicionar exemplos de request/response nos modelos Pydantic
- [ ] Configurar respostas customizadas nos endpoints
- [ ] Criar checklist completo de deploy
- [ ] Configurar variáveis de ambiente para produção
- [ ] Fazer deploy no Railway ou Render
- [ ] Executar smoke tests em produção
- [ ] Validar que Swagger UI está acessível e funcional em produção

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
- `template.py` - Código do Dia 6 herdado + TODOs para configurar Swagger
- `GUIA_APRENDIZADO.md` - Guia sobre Swagger/OpenAPI no FastAPI e deploy em produção (Railway/Render)
- `exemplo_referencia.py` - Código completo do Dia 6 + configuração Swagger completa como referência
- `exercicios.md` - Exercícios de deploy e smoke tests

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12
- **Framework:** FastAPI (gera Swagger automaticamente)
- **Deploy:** Railway (recomendado) ou Render
- **Documentação:** OpenAPI 3.0 (Swagger UI + ReDoc)

### Configuração Necessária:
- Variáveis de ambiente para produção:
  - `JWT_SECRET_KEY` (gerar novo para produção)
  - `ALGORITHM`
  - `ACCESS_TOKEN_EXPIRE_MINUTES`
  - `REFRESH_TOKEN_EXPIRE_DAYS`
  - `OPENAI_API_KEY`
- Conta no Railway (https://railway.app) ou Render (https://render.com)

### Objetivo do Dia:
Configurar documentação interativa (Swagger/OpenAPI) para a API, preparar checklist de deploy e publicar a API em produção (Railway ou Render), validando que tudo funciona corretamente através de smoke tests.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Ler `GUIA_APRENDIZADO.md` seção 1 sobre Swagger/OpenAPI no FastAPI
2. Configurar metadados OpenAPI no `template.py` (title, description, version, contact, license)
3. Adicionar tags aos endpoints (Auth, Chat, Health)
4. Adicionar descrições e exemplos nos modelos Pydantic
5. Configurar respostas customizadas nos endpoints
6. Ler `GUIA_APRENDIZADO.md` seção 2 sobre checklist de deploy
7. Criar checklist de deploy completo
8. Ler `GUIA_APRENDIZADO.md` seção 3 sobre deploy no Railway
9. Configurar variáveis de ambiente no Railway
10. Fazer deploy da API
11. Executar smoke tests em produção
12. Validar Swagger UI em produção

### Próxima Semana:
- **Semana 4:** IA Avançada + Governança + MLFlow (Python)
  - Comparação de performance e DX: FastAPI (Python) vs Hono (Bun)
  - Entender trade-offs e escolher stack preferida para projeto final

---

## 📚 Referências Rápidas

### Swagger/OpenAPI:
- FastAPI OpenAPI: https://fastapi.tiangolo.com/tutorial/metadata/
- Swagger UI: https://swagger.io/tools/swagger-ui/
- OpenAPI Specification: https://swagger.io/specification/

### Deploy:
- Railway Docs: https://docs.railway.app/
- Render Docs: https://render.com/docs
- Railway Quick Start: https://docs.railway.app/deploy/quick-start

### Produção:
- Variáveis de ambiente seguras
- Health checks
- Logging estruturado (já implementado)
- Rate limiting (já implementado)
- Exception handling (já implementado)

---

**Última atualização:** 15 Dez 2025  
**Status:** 🟡 Em progresso

