# ✅ Checklist - Dia 5 (Sexta, 13 Dez 2025)

## 🎯 Objetivo do Dia
Implementar rate limiting por usuário, tratamento de erros robusto e logging estruturado para a API de chat, preparando o código para produção.

---

> Todas as fases abaixo devem caber dentro dos **160min totais**, englobando leitura, exercícios/testes e preenchimento dos documentos. Não use autocomplete/IA para escrever o código.

## 📋 FASE 1: Preparação (5min)

### Revisão Inicial
- [ X] Abrir este checklist
- [ X] Ler `README.md` para entender contexto e objetivos
- [ X] Ler `CONTEXTO_AGENTE.md` para detalhes técnicos
- [ X] Verificar que o código do Dia 4 está funcionando (template.py ou exemplo_referencia.py)
- [ X] Confirmar que variáveis de ambiente estão configuradas (`.env`)

**Como fazer:**
1. Abra o terminal e navegue até `Semanas/Semana3/Dia5/`
2. Leia os arquivos README.md e CONTEXTO_AGENTE.md
3. Verifique se o servidor do Dia 4 ainda está rodando ou se precisa iniciar

**Por que:**
Garantir que você entende o contexto e tem o ambiente preparado antes de começar.

**Tempo estimado:** 5 minutos  
**Quando:** Início da sessão

---

## 📋 FASE 2: Leitura Guiada (20min)

### Estudo dos Conceitos
- [ X] Ler `GUIA_APRENDIZADO.md` seção 1: Rate Limiting por Usuário
- [ X] Ler `GUIA_APRENDIZADO.md` seção 2: Exception Handlers Globais
- [ X] Ler `GUIA_APRENDIZADO.md` seção 3: Logging Estruturado
- [ X] Ler `GUIA_APRENDIZADO.md` seção 4: Middleware de Request Logging
- [ X] Anotar dúvidas que serão respondidas na prática

**Como fazer:**
1. Abra `GUIA_APRENDIZADO.md`
2. Leia cada seção cuidadosamente
3. Anote conceitos que não ficaram claros
4. Consulte `exemplo_referencia.py` se precisar ver exemplos práticos

**Por que:**
Entender os conceitos antes de implementar facilita a resolução dos TODOs e evita erros comuns.

**Tempo estimado:** 20 minutos  
**Quando:** Após preparação

---

## 📋 FASE 3: Construção Guiada (90min)

### Implementação do Rate Limiting por Usuário
- [ X] Abrir `template.py` (herdar código do Dia 4)
- [ X] TODO 1: Criar função `get_user_id_for_rate_limit()` que extrai `user_id` do token JWT
- [ X] TODO 2: Configurar `slowapi.Limiter` com `key_func=get_user_id_for_rate_limit`
- [ X] TODO 3: Aplicar rate limit ao endpoint `/chat` (ex: 30 requisições/minuto por usuário)
- [ X] Testar rate limiting: fazer múltiplas requisições e verificar retorno 429

**Como fazer:**
1. Copie o código do Dia 4 (`template.py` ou `exemplo_referencia.py`) para `template.py` do Dia 5
2. Consulte `GUIA_APRENDIZADO.md` seção 1 para entender como criar função customizada
3. Consulte `exemplo_referencia.py` se precisar de referência
4. Implemente a função `get_user_id_for_rate_limit()` que:
   - Extrai o token do header Authorization
   - Decodifica o JWT
   - Retorna o `user_id` (username)
5. Configure o limiter com a função customizada
6. Aplique o decorator `@limiter.limit("30/minute")` ao endpoint `/chat`
7. Teste fazendo 31 requisições rápidas e verificando se a 31ª retorna 429

**Por que:**
Rate limiting por usuário é mais seguro que por IP, pois previne abuso mesmo quando múltiplos usuários compartilham o mesmo IP.

**Tempo estimado:** 25 minutos

---

### Implementação de Exception Handlers Globais
- [ X] TODO 4: Criar exception handler para `HTTPException`
- [ X] TODO 5: Criar exception handler para `ValidationError` (Pydantic)
- [ X] TODO 6: Criar exception handler para `Exception` genérica (catch-all)
- [ ] Testar handlers: forçar erros e verificar respostas formatadas

**Como fazer:**
1. Consulte `GUIA_APRENDIZADO.md` seção 2
2. Use `@app.exception_handler()` para registrar handlers
3. Handler para `HTTPException`: retornar JSON com `detail` e `status_code`
4. Handler para `ValidationError`: retornar JSON com lista de erros de validação (status 422)
5. Handler para `Exception`: logar erro completo e retornar mensagem genérica (status 500)
6. Teste forçando erros:
   - Endpoint inexistente (404)
   - Dados inválidos no request (422)
   - Erro interno (500)

**Por que:**
Exception handlers globais garantem que todos os erros sejam tratados de forma consistente e retornem respostas JSON padronizadas.

**Tempo estimado:** 25 minutos

---

### Configuração de Logging Estruturado
- [ X] TODO 7: Configurar logging com formato JSON
- [ X] TODO 8: Criar função helper `log_structured()` para facilitar logging
- [ X] TODO 9: Adicionar logs em pontos críticos (login, chat, erros)
- [ X] Testar logs: verificar formato JSON no console

**Como fazer:**
1. Consulte `GUIA_APRENDIZADO.md` seção 3
2. Configure `logging.basicConfig()` com formato JSON
3. Crie função `log_structured(level, message, **kwargs)` que:
   - Cria dict com `level`, `message`, `timestamp`, e campos extras
   - Serializa para JSON e loga
4. Adicione logs em:
   - Login bem-sucedido (INFO)
   - Início de chat (INFO com user_id, conversation_id)
   - Erros (ERROR com detalhes)
5. Teste fazendo requisições e verificando logs no console

**Por que:**
Logging estruturado facilita análise e monitoramento em produção, permitindo filtrar e buscar logs por campos específicos.

**Tempo estimado:** 20 minutos

---

### Criação de Middleware de Request Logging
- [ X] TODO 10: Criar middleware `RequestLoggingMiddleware`
- [ X] TODO 11: Logar método, path, status_code, tempo de resposta
- [ X] TODO 12: Registrar middleware na aplicação
- [ X] Testar middleware: fazer requisições e verificar logs

**Como fazer:**
1. Consulte `GUIA_APRENDIZADO.md` seção 4
2. Crie classe `RequestLoggingMiddleware(BaseHTTPMiddleware)`
3. No método `dispatch()`:
   - Capture tempo inicial
   - Chame `await call_next(request)`
   - Capture tempo final e calcule duração
   - Logue método, path, status_code, duração (usando `log_structured()`)
4. Registre middleware com `app.add_middleware(RequestLoggingMiddleware)`
5. Teste fazendo requisições e verificando logs de cada request

**Por que:**
Middleware de request logging fornece visibilidade completa de todas as requisições, facilitando debug e monitoramento de performance.

**Tempo estimado:** 20 minutos

---

## 📋 FASE 4: Consolidação (25min)

### Testes e Validação
- [ X] Testar rate limiting: fazer 31 requisições rápidas ao `/chat` e verificar 429
- [ X] Testar exception handlers: forçar erros e verificar respostas JSON
- [ X] Verificar logs estruturados: confirmar formato JSON e campos corretos
- [ X] Verificar middleware: confirmar que todas as requisições são logadas
- [ X] Revisar código: garantir que não há TODOs pendentes
- [ ] Comparar com `exemplo_referencia.py` se necessário

**Como fazer:**
1. Use `curl`, Postman ou script Python para testar rate limiting
2. Force erros intencionalmente (endpoint inexistente, dados inválidos)
3. Verifique logs no console (devem estar em formato JSON)
4. Faça requisições a diferentes endpoints e verifique se todas são logadas
5. Revise o código completo procurando por TODOs não resolvidos

**Por que:**
Testes garantem que todas as funcionalidades estão funcionando corretamente antes de finalizar o dia.

**Tempo estimado:** 25 minutos  
**Quando:** Após construção guiada

---

## 📋 FASE 5: Registro e Handoff (20min)

### Documentação e Reflexão
- [ X] Preencher `journal.md` com:
  - O que foi feito hoje
  - O que foi aprendido
  - Dificuldades enfrentadas
  - Próximos passos
- [ X] Preencher `CONTEXTO_PROXIMO_DIA.md` com:
  - Resumo do que foi aprendido
  - Contexto para o Dia 6 (testes automatizados)
- [ x] Marcar checklist como completo
- [ X] Fazer commit do código (se aplicável)

**Como fazer:**
1. Abra `journal.md` e preencha todas as seções
2. Abra `CONTEXTO_PROXIMO_DIA.md` e preencha com base no que foi implementado hoje
3. Revise este checklist e marque todos os itens concluídos
4. Se estiver usando git, faça commit das mudanças

**Por que:**
Documentação e reflexão consolidam o aprendizado e facilitam a transição para o próximo dia.

**Tempo estimado:** 20 minutos  
**Quando:** Final da sessão

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min no total (inclui leitura dos documentos, execução de exercícios/testes e preenchimento de checklist + journal, **sem usar autocomplete/IA para gerar código**)

### ✅ Critérios de Sucesso:
- [ ] Rate limiting por usuário funcionando (retorna 429 após limite)
- [ ] Exception handlers globais tratando todos os tipos de erro
- [ ] Logging estruturado em formato JSON funcionando
- [ ] Middleware de request logging registrando todas as requisições
- [ ] Código testado e funcionando
- [ ] Journal e CONTEXTO_PROXIMO_DIA preenchidos

### 🎯 Streak: 19/56 dias

**Parabéns por completar o Dia 5!** 🚀

---

**Última atualização:** 13 Dez 2025
