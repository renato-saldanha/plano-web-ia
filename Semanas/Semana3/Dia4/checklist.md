# ✅ Checklist - Dia 4 (Quinta, 12 Dez 2025)

## 🎯 Objetivo do Dia
Implementar sistema de histórico de conversas para o endpoint `/api/chat`, permitindo manter contexto entre mensagens e gerenciar conversas por usuário.

---

> Todas as fases abaixo devem caber dentro dos **160min totais**, englobando leitura, exercícios/testes e preenchimento dos documentos. Não use autocomplete/IA para escrever o código.

## 📋 FASE 1: Preparação (5min)

### Configuração Inicial
- [ ] Abrir `README.md` e ler contexto do dia
- [ ] Revisar `CONTEXTO_AGENTE.md` para entender objetivo técnico
- [ ] Ativar ambiente virtual Python (venv)
- [ ] Verificar se variáveis de ambiente do Dia 3 estão configuradas (JWT, API keys)
- [ ] Abrir `checklist.md` (este arquivo) para acompanhar progresso

**Como fazer:**
1. Navegar até `Semanas/Semana3/Dia4/`
2. Ler README.md e CONTEXTO_AGENTE.md rapidamente
3. Ativar venv: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Verificar `.env` tem JWT_SECRET_KEY, OPENAI_API_KEY, etc.

**Por que:**
Garantir ambiente configurado antes de começar evita bloqueios durante a implementação.

**Tempo estimado:** 5 minutos  
**Quando:** Início da sessão

---

## 📋 FASE 2: Leitura Guiada (20min)

### Leitura de Documentação
- [ ] Ler `GUIA_APRENDIZADO.md` (seção 1: Conceitos de Histórico)
- [ ] Ler `GUIA_APRENDIZADO.md` (seção 2: Armazenamento em Memória)
- [ ] Ler `GUIA_APRENDIZADO.md` (seção 3: Integração com LLM)
- [ ] Consultar `exemplo_referencia.py` para entender estrutura esperada
- [ ] Anotar dúvidas sobre persistência e formato de dados

**Como fazer:**
1. Abrir `GUIA_APRENDIZADO.md` e ler seções sobre histórico
2. Abrir `exemplo_referencia.py` e entender a estrutura de dados
3. Anotar pontos-chave: estrutura de Conversation/Message, formato de armazenamento

**Por que:**
Entender conceitos antes de implementar reduz erros e aumenta qualidade do código.

**Tempo estimado:** 20 minutos  
**Quando:** Logo após preparação

---

## 📋 FASE 3: Construção Guiada (90min)

### Implementação do Sistema de Histórico

#### Subfase 3.1: Estrutura de Dados (15min)
- [ ] Abrir `template.py`
- [ ] Criar modelos Pydantic: `Message`, `Conversation`, `ConversationList`
- [ ] Definir estrutura de armazenamento (dict em memória ou função helper)

**Como fazer:**
1. Consultar `exemplo_referencia.py` para ver modelos esperados
2. Implementar TODOs em `template.py` relacionados a modelos
3. Definir formato: `{user_id: {conversation_id: [messages]}}`

**Por que:**
Modelos bem definidos facilitam validação e manutenção do código.

**Tempo estimado:** 15 minutos

---

#### Subfase 3.2: Funções de Armazenamento (20min)
- [ ] Implementar `get_or_create_conversation(user_id, conversation_id=None)`
- [ ] Implementar `add_message(user_id, conversation_id, role, content)`
- [ ] Implementar `get_messages(user_id, conversation_id)`
- [ ] Implementar `list_conversations(user_id)`

**Como fazer:**
1. Seguir TODOs em `template.py`
2. Usar estrutura em memória: `conversations = {}`
3. Gerar IDs únicos com `uuid.uuid4()` se necessário

**Por que:**
Funções auxiliares encapsulam lógica de armazenamento, facilitando testes e manutenção.

**Tempo estimado:** 20 minutos

---

#### Subfase 3.3: Modificar Endpoint /api/chat (25min)
- [ ] Adicionar parâmetro `conversation_id` (opcional) ao `ChatRequest`
- [ ] Recuperar histórico da conversa (se existir)
- [ ] Construir lista de mensagens com histórico + nova mensagem
- [ ] Enviar contexto completo ao LLM usando `ChatPromptTemplate` ou lista de `HumanMessage`/`AIMessage`
- [ ] Salvar resposta do LLM no histórico

**Como fazer:**
1. Modificar modelo `ChatRequest` para incluir `conversation_id: Optional[str]`
2. Na função `/api/chat`, buscar histórico antes de chamar LLM
3. Construir lista: `[HumanMessage(...), AIMessage(...), ..., HumanMessage(nova)]`
4. Após resposta do LLM, salvar ambas mensagens (user + assistant)

**Por que:**
Manter histórico permite ao LLM ter contexto completo da conversa, melhorando respostas.

**Tempo estimado:** 25 minutos

---

#### Subfase 3.4: Novos Endpoints (20min)
- [ ] Criar `GET /conversations` para listar conversas do usuário
- [ ] Criar `GET /conversations/{conversation_id}/messages` para recuperar histórico
- [ ] Criar `POST /conversations` (opcional) para criar nova conversa explicitamente

**Como fazer:**
1. Seguir TODOs em `template.py` para novos endpoints
2. Usar `Depends(get_current_user)` para obter `user_id`
3. Retornar lista formatada conforme modelos Pydantic

**Por que:**
Endpoints RESTful permitem gerenciar conversas de forma clara e padronizada.

**Tempo estimado:** 20 minutos

---

#### Subfase 3.5: Testes Manuais Básicos (10min)
- [ ] Testar login e obter token
- [ ] Enviar mensagem ao `/api/chat` sem `conversation_id` (cria nova)
- [ ] Enviar segunda mensagem com mesmo `conversation_id`
- [ ] Verificar se LLM recebe contexto da primeira mensagem
- [ ] Listar conversas via `GET /conversations`
- [ ] Recuperar mensagens via `GET /conversations/{id}/messages`

**Como fazer:**
1. Usar `/docs` do FastAPI ou curl/Postman
2. Verificar que segunda mensagem referencia primeira (ex: "Como mencionei antes...")
3. Validar formato de resposta dos novos endpoints

**Por que:**
Testes manuais rápidos garantem que implementação básica funciona antes de consolidação.

**Tempo estimado:** 10 minutos

---

## 📋 FASE 4: Consolidação (25min)

### Validação e Ajustes
- [ ] Revisar código implementado no `template.py`
- [ ] Verificar se TODOs foram resolvidos
- [ ] Testar fluxo completo: criar conversa → enviar 3-4 mensagens → verificar histórico
- [ ] Verificar tratamento de erros (conversation_id inválido, etc.)
- [ ] Validar que streaming funciona com histórico
- [ ] Atualizar checklist parcial (marcar itens concluídos)

**Como fazer:**
1. Executar servidor: `uvicorn template:app --reload`
2. Fazer requisições sequenciais testando diferentes cenários
3. Verificar logs do servidor para erros

**Por que:**
Consolidação garante que funcionalidades básicas estão operacionais antes do registro.

**Tempo estimado:** 25 minutos  
**Quando:** Após construção guiada

---

## 📋 FASE 5: Registro e Handoff (20min)

### Documentação
- [ ] Preencher `journal.md` com aprendizados do dia
- [ ] Atualizar `checklist.md` marcando todas as fases concluídas
- [ ] Preencher `CONTEXTO_PROXIMO_DIA.md` descrevendo:
  - O que foi implementado hoje
  - Conceitos aprendidos
  - Dificuldades enfrentadas
  - O que será feito no Dia 5 (rate limiting, erros, logging)
- [ ] Fazer commit do código (se usando git)

**Como fazer:**
1. Abrir `journal.md` e preencher seções: "O que aprendi", "Desafios", "Próximos passos"
2. Abrir `CONTEXTO_PROXIMO_DIA.md` e documentar estado atual
3. Commit: `git add . && git commit -m "feat: adiciona sistema de histórico de chat"`

**Por que:**
Registro documenta progresso e facilita retomada no próximo dia.

**Tempo estimado:** 20 minutos  
**Quando:** Final da sessão

---

## 📋 FASE 6: Buffer (10min)

### Espaço para Imprevistos
- [ ] Se houver tempo, refatorar código ou adicionar validações extras
- [ ] Se houver bloqueios, anotar no journal para revisar depois
- [ ] Se tudo correu bem, buffer fica livre

**Por que:**
Buffer previne extrapolação do tempo e dá flexibilidade para resolver imprevistos.

**Tempo estimado:** 10 minutos  
**Quando:** Se necessário

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min no total (inclui leitura dos documentos, execução de exercícios/testes e preenchimento de checklist + journal, **sem usar autocomplete/IA para gerar código**)

### ✅ Critérios de Sucesso:
- [ ] Sistema de histórico armazena mensagens por usuário e conversa
- [ ] Endpoint `/api/chat` usa histórico para manter contexto
- [ ] Endpoints `/conversations` e `/conversations/{id}/messages` funcionam
- [ ] LLM recebe contexto completo da conversa
- [ ] Código testado manualmente e funcionando
- [ ] `journal.md` e `CONTEXTO_PROXIMO_DIA.md` preenchidos

### 🎯 Streak: X/56 dias

**Parabéns por completar o Dia 4!** 🚀

---

**Última atualização:** 12 Dez 2025