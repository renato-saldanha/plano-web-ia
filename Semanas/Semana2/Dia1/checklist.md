# ✅ Checklist - Dia 1 (Segunda-feira, 1 Dez 2025)

## 🎯 Objetivo do Dia
Introdução ao LangChain - Framework profissional para orquestração de LLMs. Aprender conceitos básicos e comparar com código manual da Semana 1.

---

## 📋 FASE 1: PREPARAÇÃO E LEITURA (15min)

### Leitura de Guias
- [ X] Ler `GUIA_LANGCHAIN.md` completo (seções 1-3)
- [ X] Entender o que é LangChain e por que usar
- [ X] Revisar código manual da Semana 1 para comparação:
  - [ X] `../../Semana1/Dia1/hello_ai_groq.py`
  - [ X] `../../Semana1/Dia2/gerador_conteudo_blog.py`
- [ X] Entender diferença entre código manual e LangChain

**Como fazer:**
1. Abra `GUIA_LANGCHAIN.md` e leia seção por seção
2. Não pule a introdução - ela explica o "porquê"
3. Abra os scripts da Semana 1 para ter em mente o código manual
4. Anote mentalmente: "Como isso seria diferente com LangChain?"

**Por que:**
Entender o contexto e propósito é essencial antes de começar a codificar. Comparação com código manual ajuda a ver valor do framework.

**Tempo estimado:** 15 minutos  
**Quando:** Início do dia

---

## 🔧 FASE 2: INSTALAÇÃO E SETUP (15min)

### Instalar LangChain
- [ X] Ativar ambiente virtual (se não estiver ativo):
  ```bash
  # Windows
  venv\Scripts\activate
  
  # Mac/Linux
  source venv/bin/activate
  ```
- [ X] Instalar LangChain e integrações:
  ```bash
  pip install langchain langchain-groq langchain-google-genai langchain-anthropic python-dotenv
  ```
- [ X] Verificar instalação:
  ```bash
  python -c "import langchain; print(langchain.__version__)"
  ```

### Verificar Configuração
- [X ] Verificar arquivo `.env` existe na raiz do projeto
- [X ] Verificar API keys estão configuradas:
  - [X ] `GROQ_API_KEY` (obrigatório)
  - [X ] `GEMINI_API_KEY` (opcional, mas recomendado)
  - [X ] `ANTHROPIC_API_KEY` (opcional)

**Como fazer:**
1. Navegue até a raiz do projeto (`d:\plano web+ia\`)
2. Ative o ambiente virtual
3. Execute comando de instalação
4. Verifique se instalou corretamente

**Por que:**
Setup correto evita erros durante aprendizado. LangChain precisa de integrações específicas para cada LLM.

**Tempo estimado:** 15 minutos  
**Quando:** Após Fase 1

---

## 💻 FASE 3: PRIMEIRO EXEMPLO (45min)

### Executar Exemplo Básico
- [ X] Abrir arquivo `exemplo_langchain_basico.py`
- [ X] Ler comentários linha por linha
- [ X] Entender cada seção:
  - [ X] Seção 1: Imports e configuração
  - [ X] Seção 2: Exemplo básico (equivalente ao hello_ai_groq.py)
  - [ X] Seção 3: Exemplo com prompts estruturados
  - [ X] Seção 4: Comparação com código manual
- [ X] Executar script: `python exemplo_langchain_basico.py`
- [ X] Verificar resposta do LLM

**Como fazer:**
1. Abra `exemplo_langchain_basico.py` no editor
2. Leia cada comentário cuidadosamente
3. Execute o script e observe a saída
4. Compare mentalmente com `hello_ai_groq.py` da Semana 1

**Por que:**
Exemplo completo comentado ajuda a entender cada parte do LangChain. Execução prática consolida aprendizado.

**Tempo estimado:** 45 minutos  
**Quando:** Após Fase 2

### Modificar Exemplo
- [ X] Modificar prompt no exemplo básico
- [ X] Testar com diferentes LLMs (Groq, Gemini)
- [ X] Comparar código LangChain vs código manual:
  - [ X] Quantas linhas cada um tem?
  - [ X] Qual é mais legível?
  - [ X] Qual é mais fácil de manter?

**Como fazer:**
1. Edite o prompt no `exemplo_langchain_basico.py`
2. Mude o LLM de Groq para Gemini (ou vice-versa)
3. Execute novamente
4. Anote diferenças observadas

**Por que:**
Modificar código ajuda a entender como funciona. Comparação mostra valor do LangChain.

**Tempo estimado:** 20 minutos (incluído no tempo acima)

---

## 📚 FASE 4: PRÁTICA GUIADA (45min)

### Completar Exercícios
- [ X] Abrir `exercicios_langchain.md`
- [ X] Completar Exercício 1: Hello LangChain
  - [X ] Criar script próprio usando LangChain
  - [X ] Comparar com `hello_ai_groq.py` da Semana 1
- [ X] Completar Exercício 2: Prompt Template
  - [X ] Criar prompt template simples
  - [X ] Testar com diferentes inputs
- [ X] Completar Exercício 3: Chain Básico
  - X[ ] Criar chain simples
  - [X ] Entender conceito de chain
- [ X] (Opcional) Exercício 4: Comparação Detalhada
  - [ X] Reescrever um script da Semana 1 usando LangChain
  - [ X] Comparar linhas de código, legibilidade, manutenibilidade

**Como fazer:**
1. Abra `exercicios_langchain.md`
2. Siga cada exercício passo a passo
3. Não consulte solução antes de tentar
4. Compare sempre com código manual da Semana 1

**Por que:**
Prática guiada consolida aprendizado. Exercícios progressivos constroem conhecimento gradualmente.

**Tempo estimado:** 45 minutos  
**Quando:** Após Fase 3

---

## 🔍 FASE 5: COMPARAÇÃO E REFLEXÃO (15min)

### Comparar Abordagens
- [ X] Criar tabela comparativa:
  - [ X] Linhas de código (manual vs LangChain)
  - [ X] Legibilidade
  - [ X] Facilidade de manutenção
  - [ X] Flexibilidade (trocar LLM)
- [ X] Identificar vantagens do LangChain:
  - [ X] Quais são?
  - [ X] Quando usar cada abordagem?
- [ X] Identificar quando código manual pode ser melhor:
  - [ X] Existem casos?

**Como fazer:**
1. Abra um script da Semana 1 e um exemplo LangChain lado a lado
2. Compare linha por linha
3. Anote diferenças em um arquivo ou papel
4. Reflita sobre quando usar cada abordagem

**Por que:**
Comparação ajuda a entender valor do LangChain. Reflexão consolida aprendizado.

**Tempo estimado:** 15 minutos  
**Quando:** Após Fase 4

---

## 📝 FASE 6: FINALIZAÇÃO (15min)

### Preencher Journal
- [ X] Abrir arquivo `journal.md`
- [ X] Preencher seção "O que foi feito hoje"
- [ X] Preencher seção "O que aprendi hoje"
  - [ X] Conceitos novos aprendidos
  - [ X] Diferenças entre código manual e LangChain
  - [ X] Vantagens identificadas
- [ X] Preencher seção "Insights e Reflexões"
  - [ X] O que funcionou bem?
  - [ X] O que foi difícil?
  - [ X] O que quer explorar mais?
- [ X] Adicionar métricas do dia:
  - [ X] Tempo total gasto
  - [ X] Exercícios completados
  - [ X] Scripts criados

**Como fazer:**
1. Abra `journal.md` neste diretório
2. Preencha honestamente cada seção
3. Seja específico sobre aprendizados
4. Inclua exemplos práticos

**Por que:**
Journal consolida aprendizado e cria registro pessoal do progresso. Reflexão ajuda a identificar pontos fortes e fracos.

**Tempo estimado:** 15 minutos  
**Quando:** Final do dia

### Git Commit
- [ ] Adicionar arquivos: `git add .`
- [ ] Commit: `git commit -m "feat: adiciona introdução ao LangChain - Dia 1 Semana 2"`
- [ ] Push: `git push origin main`

**Tempo estimado:** 5 minutos (incluído no tempo acima)

---

## 🎉 CONCLUSÃO

**Total estimado:** 2h a 2h30min (média de 2h15min)

### ✅ Critérios de Sucesso:
- [ ] LangChain instalado e funcionando
- [ ] `exemplo_langchain_basico.py` executado com sucesso
- [ ] Entendeu diferença entre código manual e LangChain
- [ ] Completou pelo menos 2 exercícios guiados
- [ ] Journal preenchido com reflexões
- [ ] Commit feito no GitHub

### 🎯 Streak: 8/56 dias

**Parabéns por completar o Dia 1 da Semana 2!** 🚀

Você aprendeu:
- ✅ O que é LangChain e por que usar
- ✅ Como instalar e configurar LangChain
- ✅ Conceitos básicos (LLMs, Prompts, Chains)
- ✅ Primeiros exemplos práticos
- ✅ Comparação com código manual

**Próximo passo:** Dia 2 - Chains e sequências (Terça-feira)

---

**Última atualização:** 1 Dez 2025

