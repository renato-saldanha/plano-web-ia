# 📝 Journal - Dia 2 (Terça, 10 Dez 2025)

## 🎯 Objetivo do Dia
Implementar autenticação JWT básica (login/refresh), middleware de segurança e aplicar proteção em rotas sensíveis.

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [ X] Estudei conceitos de JWT no GUIA_APRENDIZADO.md
- [ X] Implementei endpoint `/login` com geração de tokens
- [ X] Implementei endpoint `/refresh` para renovação
- [ X] Protegi endpoint `/chat` com dependency de autenticação
- [ ] Testei fluxo completo com curl/httpie

### Detalhes das Tarefas


## 🎓 O que aprendi hoje?

### Conceitos Novos
- Rate Limiter - Limita acessos excessivos, protegente de ataques de força bruta.
- Middleware de Segurança - Habilita a restrição de acesso à API somente pelas origens permitidas.
- JWT com refresh token e blacklist - Validação básica de token JWT com blacklist usada para efetuar o logout.
- BCrypt - Encryptador de textos para dar segurança as senhas.

### Ferramentas Utilizadas
- Python
- FastAPI
- python-jose (JWT)
- passlib (bcrypt)
- 

### Desafios Enfrentados
- Configuração do middleware. Estava sendo chamado no local errado, peguei como base o exemplo do exercicio.
- Assimilar onde cada algoritmo se encaixa. Estudando e praticando para acostumar.

---

## 💡 Insights e Reflexões

### O que funcionou bem?
- Rate Limiter funcinou bem

### O que poderia ser melhorado?
- Praticar mais para ter mais expertise.

### Próximos Passos
- 

---

## 📊 Métricas do Dia

- **Tempo total:** 170 minutos (meta: 160)
- **Commits:** 2
- **Testes manuais:** `/login`, `/refresh`, `/chat` protegido

---

## 🔗 Links e Referências Úteis

- FastAPI Security/JWT: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- python-jose: https://python-jose.readthedocs.io/
- passlib: https://passlib.readthedocs.io/

---

## 📝 Notas Adicionais

_(Espaço livre para anotações)_

---

**Data:** 10 Dez 2025  
**Status:** 🟡 Em progresso


