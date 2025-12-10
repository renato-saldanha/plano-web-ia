# ✅ Checklist - Dia 2 (Terça, 10 Dez 2025)

## 🎯 Objetivo do Dia
Implementar autenticação JWT básica (login/refresh), middleware de segurança e aplicar proteção em rotas sensíveis.

---

> ⚠️ **IMPORTANTE:** Cada item tem um marcador de ação:
> - **[LEIA]** = Momento de estudar/ler (não escreva código ainda)
> - **[IMPLEMENTE]** = Momento de escrever código
> - **[EXECUTE]** = Momento de rodar comandos no terminal
> - **[TESTE]** = Momento de testar o que foi feito
> - **[DOCUMENTE]** = Momento de preencher documentos

---

## 📋 FASE 1: Preparação (5 min)

### 1.1 Revisar contexto
- [ ] **[LEIA]** Abrir e ler `README.md` deste diretório (2 min)
- [ ] **[LEIA]** Verificar se entendeu a conexão com Dia 1

### 1.2 Preparar ambiente
- [ ] **[EXECUTE]** Ativar venv: `.\venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)
- [ ] **[EXECUTE]** Instalar dependências: `pip install -r requirements.txt`
- [ ] **[EXECUTE]** Verificar instalação: `pip list | grep -E "jose|passlib"`

**Tempo estimado:** 5 minutos  
**Saída esperada:** Ambiente pronto com python-jose e passlib instalados

---

## 📋 FASE 2: Leitura Guiada (20 min)

### 2.1 Estudar conceitos JWT
- [ ] **[LEIA]** Abrir `GUIA_APRENDIZADO.md`
- [ ] **[LEIA]** Ler **Seção 1: O que é JWT** (5 min)
  - Entender estrutura: header.payload.signature
  - Entender diferença access vs refresh token
- [ ] **[LEIA]** Ler **Seção 2: JWT no FastAPI** (5 min)
  - Entender OAuth2PasswordBearer
  - Entender Depends() para proteção
- [ ] **[LEIA]** Ler **Seção 3: Password Hashing** (5 min)
  - Entender por que não guardar senhas em texto
  - Entender bcrypt

### 2.2 Revisar exemplo
- [ ] **[LEIA]** Abrir `exemplo_referencia.py` e dar uma olhada geral (5 min)
  - NÃO copie o código ainda
  - Apenas entenda a estrutura geral

**Tempo estimado:** 20 minutos  
**Saída esperada:** Compreensão dos conceitos JWT antes de implementar

---

## 📋 FASE 3: Construção Guiada (90 min)

> 💡 **AGORA SIM você vai escrever código!** Abra o `template.py` e complete os TODOs.

### 3.1 Configuração inicial (15 min)
- [ ] **[IMPLEMENTE]** Abrir `template.py` no editor
- [ ] **[IMPLEMENTE]** Completar TODO 1: Importar bibliotecas JWT
- [ ] **[IMPLEMENTE]** Completar TODO 2: Carregar variáveis de ambiente
- [ ] **[IMPLEMENTE]** Completar TODO 3: Configurar CryptContext para bcrypt

**Dica:** Se travar, consulte `exemplo_referencia.py` seção de imports

### 3.2 Modelos Pydantic (10 min)
- [ ] **[IMPLEMENTE]** Completar TODO 4: Criar modelo `Token` (access_token, refresh_token, token_type)
- [ ] **[IMPLEMENTE]** Completar TODO 5: Criar modelo `LoginRequest` (username, password)

**Dica:** Use `str` para tokens e `Literal["bearer"]` para token_type

### 3.3 Funções de Token (25 min)
- [ ] **[IMPLEMENTE]** Completar TODO 6: Função `create_access_token(data, expires_delta)`
  - Copiar dados, adicionar "exp", usar jwt.encode()
- [ ] **[IMPLEMENTE]** Completar TODO 7: Função `create_refresh_token(data)`
  - Similar ao access, mas com expiração maior
- [ ] **[IMPLEMENTE]** Completar TODO 8: Função `verify_token(token)`
  - Decodificar com jwt.decode(), tratar JWTError

**Dica:** Consulte GUIA_APRENDIZADO.md seção "Criando Tokens"

### 3.4 Dependency de Autenticação (15 min)
- [ ] **[IMPLEMENTE]** Completar TODO 9: Configurar `OAuth2PasswordBearer`
- [ ] **[IMPLEMENTE]** Completar TODO 10: Função `get_current_user(token)`
  - Usar Depends(oauth2_scheme)
  - Chamar verify_token()
  - Retornar usuário ou HTTPException 401

### 3.5 Endpoints (25 min)
- [ ] **[IMPLEMENTE]** Completar TODO 11: Endpoint `POST /login`
  - Validar credenciais (use usuário fake por enquanto)
  - Gerar access + refresh tokens
  - Retornar modelo Token
- [ ] **[IMPLEMENTE]** Completar TODO 12: Endpoint `POST /refresh`
  - Receber refresh_token no body
  - Validar token
  - Gerar novo access_token
- [ ] **[IMPLEMENTE]** Completar TODO 13: Proteger endpoint `/chat`
  - Adicionar `current_user: dict = Depends(get_current_user)`

**Tempo estimado:** 90 minutos  
**Saída esperada:** Arquivo `template.py` completo e funcional

---

## 📋 FASE 4: Consolidação (25 min)

### 4.1 Subir servidor
- [ ] **[EXECUTE]** Rodar: `uvicorn template:app --reload --port 8000`
- [ ] **[TESTE]** Verificar se servidor subiu sem erros

### 4.2 Testar login
- [ ] **[TESTE]** Abrir http://localhost:8000/docs no navegador
- [ ] **[TESTE]** Testar `POST /login` com credenciais fake:
  ```bash
  curl -X POST http://localhost:8000/login \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "admin123"}'
  ```
- [ ] **[TESTE]** Verificar se retornou `access_token` e `refresh_token`

### 4.3 Testar rota protegida
- [ ] **[TESTE]** Testar `/chat` SEM token (deve dar 401):
  ```bash
  curl http://localhost:8000/chat
  ```
- [ ] **[TESTE]** Testar `/chat` COM token (deve funcionar):
  ```bash
  curl http://localhost:8000/chat \
    -H "Authorization: Bearer SEU_ACCESS_TOKEN_AQUI"
  ```

### 4.4 Testar refresh
- [ ] **[TESTE]** Testar `POST /refresh`:
  ```bash
  curl -X POST http://localhost:8000/refresh \
    -H "Content-Type: application/json" \
    -d '{"refresh_token": "SEU_REFRESH_TOKEN_AQUI"}'
  ```
- [ ] **[TESTE]** Verificar se retornou novo access_token

**Tempo estimado:** 25 minutos  
**Saída esperada:** Todos os endpoints funcionando corretamente

---

## 📋 FASE 5: Registro e Handoff (20 min)

### 5.1 Preencher documentos
- [ ] **[DOCUMENTE]** Abrir `journal.md` e preencher:
  - O que foi feito hoje
  - Conceitos novos aprendidos
  - Desafios enfrentados
  - Tempo total gasto
- [ ] **[DOCUMENTE]** Marcar todos os itens concluídos neste checklist

### 5.2 Commit
- [ ] **[EXECUTE]** `git add .`
- [ ] **[EXECUTE]** `git commit -m "feat(auth): implementar JWT login/refresh e proteção de rotas"`

### 5.3 Preparar próximo dia
- [ ] **[LEIA]** Ler `CONTEXTO_PROXIMO_DIA.md` para entender o que vem no Dia 3

**Tempo estimado:** 20 minutos  
**Saída esperada:** Journal preenchido, commit feito, próximo dia entendido

---

## 📋 FASE 6: Buffer (10 min)

> ⚠️ Use este tempo APENAS se precisou de mais tempo em alguma fase anterior.
> Se terminou tudo, pode começar os exercícios extras em `exercicios.md`.

- [ ] Resolver pendências
- [ ] OU iniciar exercício extra de hardening

---

## 🎉 CONCLUSÃO

**Total estimado:** 160 minutos (5 + 20 + 90 + 25 + 20 + 10 = 170, buffer incluso)

### ✅ Critérios de Sucesso:
- [ ] `POST /login` retorna access + refresh tokens
- [ ] `POST /refresh` renova o access token
- [ ] `/chat` está protegido (401 sem token, 200 com token)
- [ ] Senhas são hasheadas com bcrypt
- [ ] Journal preenchido com reflexões
- [ ] Commit feito no Git

### 🎯 Streak: 16/56 dias

**Parabéns por completar o Dia 2!** 🚀

---

**Última atualização:** 10 Dez 2025


