# 🎯 Contexto para Construir o Dia 2

## 📚 O que aprendemos hoje (Dia 1)
### Conceitos Principais
- Setup FastAPI com Pydantic v2, CORS básico e logs simples.
- Rotas `/health` e `/chat` com schema validado e eco/placeholder LLM.
- Estrutura para evoluir com JWT, streaming e testes.

### Habilidades Desenvolvidas
- Subir servidor FastAPI com Uvicorn e docs automáticas.
- Validar payloads e respostas com Pydantic.
- Configurar CORS e logs iniciais.

### Código Criado
- `exemplo_completo.py` (rotas básicas, CORS, logs, placeholder LLM).
- `GUIA_PASSO_A_PASSO.md` (setup + comandos de teste).
- `exercicios.md` (tarefas de hardening e streaming esboço).

---

## 🔗 Por que o Dia 2 é importante
- Precisamos adicionar autenticação e proteção mínima antes de expor endpoints.
- JWT será base para `/chat` seguro e para futuras rotas de administração/LLM.
- Hardening inicial evita vazamento de endpoints e configura CORS/env corretamente.

---

## 🎯 O que será feito no Dia 2
### Objetivo Principal
Implementar autenticação JWT básica (login/refresh), middleware de segurança e aplicar proteção em rotas sensíveis.

### Conceitos que serão aprendidos
- Criação e validação de JWT (acess/refresh) com expiração.
- Middlewares/dependencies no FastAPI para rotas protegidas.
- Boas práticas de CORS, headers e tratamento de erros.

### Como se relaciona com Dia 1
- Reutiliza o esqueleto FastAPI e modelos Pydantic.
- Protege `/chat` e prepara estrutura para streaming/LLM autênticado.
- Constrói sobre CORS/logs já configurados.

---

## 📋 Como Construir o Dia 2
### 1. Criar Estrutura Básica
```
Dia2/
├── README.md
├── CONTEXTO_AGENTE.md
├── checklist.md
├── journal.md
├── requirements.txt (mesmo base + lib JWT)
└── (arquivos de scaffolding conforme nível)
```

### 2. Definir Nível de Scaffolding
- JWT é conceito parcialmente conhecido (segurança web), mas novo no contexto FastAPI → **Nível 2** recomendado.
- Arquivos: `template.py`, `GUIA_APRENDIZADO.md`, `exemplo_referencia.py`, `exercicios.md`.

### 3. Criar Arquivos de Aprendizado
- `template.py`: rotas `/login`, `/refresh`, proteção de `/chat`.
- `GUIA_APRENDIZADO.md`: passo a passo JWT, dependências de segurança, exemplos de uso.
- `exemplo_referencia.py`: fluxo completo com tokens e validação.
- `exercicios.md`: hardening (CORS estrito, blacklist claims, clock skew).

### 4. Seguir Checklist
- Preparação → Leitura → Construção → Consolidação → Registro (160min).

---

## 📚 Recursos de Preparação
- FastAPI Security/JWT: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- Pydantic v2: https://docs.pydantic.dev/latest/
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Scaffolding: `../../GUIAS/GUIA_DECISAO_SCAFFOLDING.md`

### Conceitos pré-requisitos
- Noções de HTTP headers, Authorization: Bearer.
- Uso de env vars para secrets (`JWT_SECRET`, `JWT_ALG`).

---

## 💡 Dicas Importantes
1. Reutilizar o app atual e acoplar auth via dependencies/middlewares.
2. Manter CORS estrito (origens conhecidas) e headers mínimos.
3. Planejar testes rápidos com httpie/pytest para tokens válidos e expirados.
4. Se algo ultrapassar 160min, mover para Dia 3 mantendo sequência.

---

**Última atualização:** 9 Dez 2025  
**Status:** 🟡 Pronto como briefing para o Dia 2

