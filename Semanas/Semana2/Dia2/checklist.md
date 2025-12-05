# ✅ Checklist - Dia 2 (Terça-feira, 2 Dez 2025)

## 🎯 Objetivo do Dia
Chains e Sequências no LangChain - Criar fluxos de trabalho complexos usando LangChain Expression Language (LCEL).

---

## 📋 FASE 1: PREPARAÇÃO E LEITURA (20min)

### Leitura de Guias
- [ X] Ler `GUIA_CHAINS.md` completo (seções 1-4)
- [ X] Entender o que são Chains e por que usar
- [ X] Entender LangChain Expression Language (LCEL)
- [ X] Revisar conceitos básicos do Dia 1:
  - [ X] Como fazer chamada simples ao LLM
  - [ X] Conceito de Prompt e Messages
  - [ X] Diferença entre código manual e LangChain

**Como fazer:**
1. Abra `GUIA_CHAINS.md` e leia seção por seção
2. Não pule a introdução - ela explica o "porquê" das chains
3. Preste atenção especial na seção sobre LCEL (sintaxe `|`)
4. Anote mentalmente: "Como isso simplifica código complexo?"

**Por que:**
Entender o contexto e propósito é essencial antes de começar a codificar. LCEL é um conceito novo que precisa ser compreendido antes da prática.

**Tempo estimado:** 20 minutos  
**Quando:** Início do dia

---

## 💻 FASE 2: PRIMEIRA CHAIN SEQUENCIAL (40min)

### Entender Exemplo de Referência
- [ X] Abrir arquivo `exemplo_referencia.py`
- [ X] Ler comentários linha por linha
- [ X] Entender cada seção:
  - [ X] Seção 1: Imports e configuração
  - [ X] Seção 2: Chain sequencial simples (usando `|`)
  - [ X] Seção 3: Chain com múltiplas operações
  - [ X] Seção 4: Chain com formatação de saída
- [ X] Executar script: `python exemplo_referencia.py`
- [ X] Verificar resposta e entender fluxo

**Como fazer:**
1. Abra `exemplo_referencia.py` no editor
2. Leia cada comentário cuidadosamente
3. Execute o script e observe a saída
4. Compare mentalmente com código do Dia 1 (chamadas simples)

**Por que:**
Exemplo completo comentado ajuda a entender cada parte do LCEL. Execução prática consolida aprendizado.

**Tempo estimado:** 20 minutos  
**Quando:** Após Fase 1

### Criar Primeira Chain Própria
- [ ] Abrir arquivo `exercicios/1-chain_sequencial.py` OU `template.py` (TODO 1)
- [ ] Completar função `sequencial_chain()` ou TODO 1: Chain sequencial simples
  - [ ] Criar prompt template
  - [ ] Conectar com LLM usando `|`
  - [ ] Invocar chain e imprimir resultado
- [ ] Testar chain criada
- [ ] Modificar prompt para ver diferença

**Como fazer:**
1. **Opção A:** Abra `exercicios/1-chain_sequencial.py` e complete a função
2. **Opção B:** Abra `template.py` e encontre TODO 1
3. Siga as dicas fornecidas no comentário
4. Consulte `exemplo_referencia.py` seção 2 se precisar de ajuda
5. Execute e teste sua chain: `python exercicios/1-chain_sequencial.py` ou `python template.py`

**Por que:**
Prática guiada consolida aprendizado. Criar sua própria chain ajuda a entender o conceito profundamente.

**Tempo estimado:** 20 minutos  
**Quando:** Após entender exemplo de referência

---

## 🔗 FASE 3: CHAINS AVANÇADAS (60min)

### Chains Condicionais
- [ ] Ler seção sobre chains condicionais no `GUIA_CHAINS.md`
- [ ] Completar `exercicios/2-chain_condicional.py` OU TODO 2 no `template.py`:
  - [ ] Criar chain que decide estratégia baseada no tamanho do input
  - [ ] Usar `RunnableBranch` para escolher qual chain usar
  - [ ] Testar com diferentes tamanhos de input
- [ ] Entender quando usar chains condicionais

**Como fazer:**
1. Consulte `GUIA_CHAINS.md` para ver exemplos de condicionais
2. **Opção A:** Complete `exercicios/2-chain_condicional.py`
3. **Opção B:** Complete TODO 2 no `template.py`
4. Teste com diferentes cenários (texto curto vs longo)
5. Compare com código manual equivalente

**Por que:**
Chains condicionais são essenciais para criar aplicações inteligentes que adaptam comportamento baseado em contexto.

**Tempo estimado:** 25 minutos  
**Quando:** Após Fase 2

### Chains Paralelas
- [ X] Ler seção sobre chains paralelas no `GUIA_CHAINS.md`
- [ X] Completar `exercicios/3-chain_paralela.py` OU TODO 3 no `template.py`:
  - [ X] Criar chain que executa múltiplas operações em paralelo
  - [ X] Usar `RunnableParallel` para executar chains simultaneamente
  - [ X] Combinar resultados em um dicionário
- [ X] Entender vantagens de paralelização

**Como fazer:**
1. Consulte `GUIA_CHAINS.md` para ver exemplos de paralelas
2. **Opção A:** Complete `exercicios/3-chain_paralela.py`
3. **Opção B:** Complete TODO 3 no `template.py`
4. Compare tempo de execução sequencial vs paralelo
5. Entenda quando paralelizar faz sentido

**Por que:**
Chains paralelas melhoram performance quando múltiplas operações podem ser executadas simultaneamente.

**Tempo estimado:** 20 minutos  
**Quando:** Após chains condicionais

### Completar Exercícios Guiados
- [ X] Abrir `exercicios.md` para ver instruções detalhadas
- [ X] Completar Exercício 1: `exercicios/1-chain_sequencial.py`
  - [X ] Criar chain sequencial simples
  - [ X] Executar e testar: `python exercicios/1-chain_sequencial.py`
- [ X] Completar Exercício 2: `exercicios/2-chain_condicional.py`
  - [ X] Criar chain condicional com RunnableBranch
  - [ X] Executar e testar: `python exercicios/2-chain_condicional.py`
- [ X] Completar Exercício 3: `exercicios/3-chain_paralela.py`
  - [ X] Criar chain paralela com RunnableParallel
  - [ X] Executar e testar: `python exercicios/3-chain_paralela.py`
- [ X] (Opcional) Exercício 4: `exercicios/4-chain_complexa.py`
  - [ X] Combinar chains sequenciais e paralelas
  - [ X] Executar e testar: `python exercicios/4-chain_complexa.py`

**Como fazer:**
1. Abra `exercicios.md` para ver instruções detalhadas de cada exercício
2. Cada exercício está em um arquivo separado na pasta `exercicios/`
3. Complete a função principal em cada arquivo seguindo os comentários
4. Execute cada arquivo individualmente para testar
5. Não consulte solução antes de tentar
6. Compare sempre com código manual equivalente

**Por que:**
Prática guiada consolida aprendizado. Exercícios progressivos constroem conhecimento gradualmente.

**Tempo estimado:** 15 minutos  
**Quando:** Após chains paralelas

---

## 🔍 FASE 4: COMPARAÇÃO E REFLEXÃO (15min)

### Comparar Abordagens
- [ X] Criar tabela comparativa:
  - [ X] Código manual (Semana 1) vs Chain simples
  - [ X] Código manual vs Chain condicional
  - [ X] Código manual vs Chain paralela
- [ X] Identificar vantagens das chains:
  - [ X] Legibilidade
  - [ X] Reutilização
  - [ X] Composição
  - [ X] Manutenibilidade
- [ X] Identificar casos onde chains são especialmente úteis

**Como fazer:**
1. Abra um script da Semana 1 e uma chain criada hoje lado a lado
2. Compare linha por linha
3. Anote diferenças em um arquivo ou papel
4. Reflita sobre quando usar cada abordagem

**Por que:**
Comparação ajuda a entender valor das chains. Reflexão consolida aprendizado.

**Tempo estimado:** 10 minutos  
**Quando:** Após Fase 3

### Preencher Journal
- [ X] Abrir arquivo `journal.md`
- [ X] Preencher seção "O que foi feito hoje"
- [ X] Preencher seção "O que aprendi hoje"
  - [ X] Conceitos novos aprendidos (Chains, LCEL)
  - [ X] Diferenças entre chains e chamadas simples
  - [ X] Vantagens identificadas
- [ X] Preencher seção "Insights e Reflexões"
  - [ X] O que funcionou bem?
  - [ X] O que foi difícil?
  - [ X] O que quer explorar mais?
- [ X] Adicionar métricas do dia:
  - [ X] Tempo total gasto
  - [ X] Exercícios completados
  - [ X] Chains criadas

**Como fazer:**
1. Abra `journal.md` neste diretório
2. Preencha honestamente cada seção
3. Seja específico sobre aprendizados
4. Inclua exemplos práticos

**Por que:**
Journal consolida aprendizado e cria registro pessoal do progresso. Reflexão ajuda a identificar pontos fortes e fracos.

**Tempo estimado:** 5 minutos  
**Quando:** Final do dia

### Git Commit
- [ X] Adicionar arquivos: `git add .`
- [ X] Commit: `git commit -m "feat: adiciona chains e LCEL - Dia 2 Semana 2"`
- [ X] Push: `git push origin main`

**Tempo estimado:** 5 minutos (incluído no tempo acima)

---

## 🎉 CONCLUSÃO

**Total estimado:** 2h a 2h30min (média de 2h15min)

### ✅ Critérios de Sucesso:
- [ X] Entendeu conceito de Chain e LCEL
- [ X] Criou pelo menos 1 chain sequencial funcional
- [ X] Criou 1 chain condicional ou paralela
- [ X] Completou pelo menos 3 exercícios guiados
- [ X] Consegue explicar diferença entre chain e chamada simples
- [ X] Journal preenchido com reflexões
- [ X] Commit feito no GitHub

### 🎯 Streak: 9/56 dias

**Parabéns por completar o Dia 2 da Semana 2!** 🚀

Você aprendeu:
- ✅ O que são Chains e por que usar
- ✅ LangChain Expression Language (LCEL)
- ✅ Como criar chains sequenciais
- ✅ Como criar chains condicionais
- ✅ Como criar chains paralelas
- ✅ Vantagens das chains sobre código manual

**Próximo passo:** Dia 3 - RAG básico (Quarta-feira)

---

**Última atualização:** 2 Dez 2025

