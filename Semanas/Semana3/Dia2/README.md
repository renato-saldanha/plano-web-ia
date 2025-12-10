# 📅 Dia 2 - Terça (10 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **segundo dia** da Semana 3 do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** Implementar autenticação JWT básica (login/refresh), middleware de segurança e aplicar proteção em rotas sensíveis
- **Duração estimada:** 160min totais (inclui leitura, exercícios/testes e preenchimento de documentos) — sem autocomplete/IA escrevendo código
- **Foco:** Segurança de APIs com JWT no FastAPI

### 🗺️ Estrutura do Plano:
- **Semana 3:** Backend FastAPI + IA (9-15 Dez)
- **Dia 1 (concluído):** Setup FastAPI básico com `/health`, `/chat`, CORS e Pydantic ✅
- **Dia 2 (hoje):** Autenticação JWT e proteção de rotas
- **Dia 3:** Streaming de respostas + integração LLM

### 📁 Arquivos neste diretório:

**Obrigatórios:**
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia com marcadores [LEIA]/[IMPLEMENTE]/[TESTE]/[DOCUMENTE]
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python (python-jose, passlib)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir Dia 3

**Scaffolding Nível 2:**
- `GUIA_APRENDIZADO.md` - Conceitos JWT + passo-a-passo com seções Teoria e Prática
- `template.py` - Estrutura com TODOs para completar
- `exemplo_referencia.py` - Implementação completa para consulta
- `exercicios.md` - Exercícios de hardening e desafios

### 🎯 O que você vai aprender:
1. JWT (JSON Web Tokens) - access vs refresh tokens
2. FastAPI `Depends()` para rotas protegidas
3. Password hashing seguro com bcrypt
4. Middleware de validação de token
5. CORS e headers de segurança

### 💡 Notas Importantes:
- **Baseado em:** Dia 1 (FastAPI básico, CORS, Pydantic)
- **Foco:** Segurança antes de expor endpoints para LLM
- **Nível de Scaffolding:** 2 (Intermediário) - JWT é parcialmente conhecido, mas novo no contexto FastAPI

### ⚠️ Melhoria aplicada (baseada no feedback do Dia 1):
O aluno relatou dificuldade em entender quando ler documentação vs. quando implementar. 
**Solução:** Cada item do checklist agora tem marcadores explícitos:
- **[LEIA]** - Momento de estudar/ler documentação
- **[IMPLEMENTE]** - Momento de escrever código
- **[TESTE]** - Momento de testar o que foi feito
- **[DOCUMENTE]** - Momento de preencher documentos

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- FastAPI Security/JWT: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- Pydantic v2: https://docs.pydantic.dev/latest/
- python-jose: https://python-jose.readthedocs.io/

---

**Status:** 🟡 Em progresso  
**Última atualização:** 10 Dez 2025


