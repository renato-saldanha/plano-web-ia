# 📝 Journal - Dia 5 (Sexta, 13 Dez 2025)

## 🎯 Objetivo do Dia
Implementar rate limiting por usuário, tratamento de erros robusto e logging estruturado para a API de chat, preparando o código para produção.

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [ X] Implementação de rate limiting por usuário
- [ X] Criação de exception handlers globais
- [ X] Configuração de logging estruturado
- [ X] Criação de middleware de request logging
- [ X] Testes e validação das funcionalidades

### Detalhes das Tarefas
_(Preencher ao longo do dia)_

**Rate Limiting:**
- Criado metodo de validação de rate limiting por user_id(caso não tiver usda fallback pelo IP). Implementado método de rate limiting no endpoint do chat com limite de 30 requisições por minuto. log estruturado no início da conversa e se case gerar erro. Login permanece a mesma regra, 5 por minuto.

**Exception Handlers:**
- Criado excessões com retornos padronizados para HTTP, validações do pydantic e genéricas.

**Logging:**
- Criado metodo de log estruturado. Permitindo a centralização dos logs em um só local, facilitando a legibilidade e manutenção.

**Middleware:**
- Criado middleware de segurança contendo 3 validações no header:
  Previnir ataques de upload de arquivos perigosos.
  Impedir que sites incorporem a pagina.
  Adicionar segurança de conteúdo(navegadores antigos).
  Adicionar segurança de conteúdo(navegadores novos).
  Forçar HTTPS.
  Limitar informações enviadas.
  Desabilitar recursos sinsíveis.
  
---

## 🎓 O que aprendi hoje?

### Conceitos Novos
- Rate Limiter por user_id com fallback.
- Logging estruturado

### Ferramentas Utilizadas
- SlowAPI para rate limiting
- Python logging para logging estruturado
- FastAPI exception handlers
- Middleware customizado

### Desafios Enfrentados
- Erros de digitação. A cada execução uma correção.
- Dificuldade em lembrar algumas lógicas usadas com suas ferramentas. Foi consutlado no GUIA_APRENDIZADO.MD

---

## 💡 Insights e Reflexões

### O que funcionou bem?
- 

### O que poderia ser melhorado?
- GUIA_APRENDIZADO.md ter exemplos de uso diferentes do template.py e exercicios.md

### Próximos Passos
- Dia 6: Implementar testes automatizados com pytest

---

## 📊 Métricas do Dia

- **Tempo total:** 2 horas
- **Commits:** 1
- **Linhas de código:** 738
- **Testes realizados:** 3
- **Rate limit testado:** 31 requisições

---

## 🔗 Links e Referências Úteis

- SlowAPI Documentation: https://slowapi.readthedocs.io/
- FastAPI Exception Handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
- Python Logging: https://docs.python.org/3/library/logging.html

---

## 📝 Notas Adicionais

_(Espaço livre para anotações)_

---

**Data:** 13 Dez 2025  
**Status:** 🟡 Em progresso
