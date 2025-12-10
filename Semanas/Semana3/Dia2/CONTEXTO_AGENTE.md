# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 3 de 8  
**Dia:** 2 de 7 (Terça, 10 Dez 2025)  
**Diretório:** `Semanas/Semana3/Dia2/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Semana 1: Fundamentos de IA Generativa (CLI funcional + comparação LLMs)
- ✅ Semana 2: LangChain/LangGraph + RAG básico
- ✅ Dia 1 (Semana 3): Setup FastAPI com `/health`, `/chat`, CORS, Pydantic

### O que está em progresso:
- 🟡 Dia 2: Autenticação JWT (login/refresh) e proteção de rotas

### O que falta fazer (hoje):
- [ ] Ler GUIA_APRENDIZADO.md (seções 1-3 sobre JWT)
- [ ] Implementar `/login` com geração de tokens
- [ ] Implementar `/refresh` para renovação de token
- [ ] Proteger `/chat` com dependency de validação
- [ ] Testar fluxo completo com httpie/curl
- [ ] Preencher journal.md e checklist.md

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- `README.md` - Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- `checklist.md` - Checklist detalhado com fases e marcadores
- `journal.md` - Template para reflexão
- `requirements.txt` - Dependências Python (python-jose, passlib)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir Dia 3

### Arquivos de Aprendizado (Nível 2):
- `GUIA_APRENDIZADO.md` - Conceitos JWT + passo-a-passo
- `template.py` - Estrutura com TODOs para completar
- `exemplo_referencia.py` - Implementação completa comentada
- `exercicios.md` - Exercícios de hardening

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12
- **Framework:** FastAPI + Uvicorn
- **Auth:** python-jose (JWT) + passlib (bcrypt)
- **Validação:** Pydantic v2

### Configuração Necessária:
- Arquivo `.env` com:
  - `JWT_SECRET` - Chave secreta para assinar tokens
  - `JWT_ALGORITHM` - Algoritmo (padrão: HS256)
  - `ACCESS_TOKEN_EXPIRE_MINUTES` - Expiração do access token
  - `REFRESH_TOKEN_EXPIRE_DAYS` - Expiração do refresh token

### Objetivo do Dia:
Implementar autenticação JWT completa com:
1. **POST /login** - Valida credenciais, retorna access + refresh tokens
2. **POST /refresh** - Recebe refresh token, retorna novo access token
3. **GET /chat (protegido)** - Requer Bearer token válido no header

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. [LEIA] Estudar GUIA_APRENDIZADO.md seções 1-3 (20 min)
2. [IMPLEMENTE] Completar TODOs no template.py (90 min)
3. [TESTE] Validar endpoints com httpie/curl (25 min)
4. [DOCUMENTE] Preencher journal.md (20 min)

### Próximo Dia (Dia 3):
- Implementar streaming de respostas (`StreamingResponse`)
- Integrar LLM real (Claude/GPT via LangChain)
- Adicionar `/api/generate` com streaming

---

## 📚 Referências Rápidas

### FastAPI Security
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validar token aqui
    pass
```

### JWT com python-jose
```python
from jose import JWTError, jwt
from datetime import datetime, timedelta

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

### Password Hashing
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = pwd_context.hash("senha123")
is_valid = pwd_context.verify("senha123", hashed)
```

---

**Última atualização:** 10 Dez 2025  
**Status:** 🟡 Em progresso


