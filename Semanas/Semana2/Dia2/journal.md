# 📝 Journal - Dia 2 (Terça-feira, 2 Dez 2025)

## 🎯 Objetivo do Dia
Chains e Sequências no LangChain - Criar fluxos de trabalho complexos usando LangChain Expression Language (LCEL).

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [ X] Leitura do GUIA_CHAINS.md
- [ X] Execução do exemplo_referencia.py
- [ X] Criação de chains sequenciais
- [ X] Criação de chains condicionais
- [ X] Criação de chains paralelas
- [ X] Completar exercícios guiados

### Detalhes das Tarefas
- Estudado GUIA_CHAINS.md
- Lido e compreendido os exercícios propostos
- Inicio e conclusão dos exercícios
- Preenchimento do checklist e journal
- Commitado

## 🎓 O que aprendi hoje?

### Conceitos Novos
- **Chains:**
  - O que são: São um conjunto de funcionalidades percententes ao LangChain que permite encadear diversas chamadas com diversas configurações.
  - Por que usar: Para fazer chamadas e gerenciamento de vários processos.
  - Quando usar: Na necessidade de ter vários procesos em uma mesma chamada.

- **LangChain Expression Language (LCEL):**
  - O que é: É um recurso que permite criar Chains usando o pipe |.
  - Como funciona: Basta instânciar as Chains na ordem correta, Ex: chain = (template | llm | StrOutputParser) 
  - Sintaxe `|` (pipe): É o que permite usar o recurso LCEL.

- **Chains Sequenciais:**
  - Como criar: chain = (template | llm | StrOutputParser)
  - Quando usar: Quando necessitar de instânciar uma Chain simples.
  - Exemplo prático: Ao ter uma Chain que só peça um resumo de um texto.

- **Chains Condicionais:**
  - Como criar: chain = RunnableBranch((idade > 53, old_chain), young_chain)
  - Quando usar: Quando há necessidade de uma validação.
  - Exemplo prático: Caso o prompt de entrada passe de 50 caracteres, retorne um texto longo e detalhado senão então retorne um texto resumido e curto.

- **Chains Paralelas:**
  - Como criar: 
  parallel = RunnableParallel({
    "summary": summary,
    "context": context,
  })
  - Quando usar: Na necessidade de ter processos que precisam de que o retorno sejam obtidos juntos.
  - Vantagens: Mais rapidez por ter N processos sendo feitos simultaneamente.

### Ferramentas Utilizadas
- LangChain versão: 1.1.0
- Conceitos utilizados: Chains sequenciais, condicionais, paralelos e complexos.
- LLMs testados: Groq

### Desafios Enfrentados
- De início foi entender a estrutura dos tipos diferentes de chain

---

## 💡 Insights e Reflexões

### O que funcionou bem?
- Os códigos rodaram de primeira, tive que ajustar o paralelo e complexo por conta de como estava sendo passado a estrutura do Chain já composto.

### O que poderia ser melhorado?
- Usar um colorama
- Aplicar tratamentos de exceptions
- Aplicar Logging para melhorar a captura de mensagens importântes

### Comparação: Chamadas Simples vs Chains

**Chamadas Simples (Dia 1):**
- Linhas de código: 60.
- Legibilidade: Códigos longos mas sem muita complexidade para ler.
- Reutilização: Pouca.
- Complexidade: Nenhuma.

**Chains (Dia 2):**
- Linhas de código: 51.
- Legibilidade: Boa.
- Reutilização: Desacoplado.
- Complexidade: Nenhuma.

**Vantagens das Chains:**
1. Maior desacoplamento de código. 
2. Melhora o gerenciamento dos processos
3. Permite efetuar processos que uma chamada normal geraria muito código e pouca legibilidade.

**Quando usar cada abordagem:**
- Chamadas simples: Quando for fazer um processo de teste.
- Chains: Quando necessitar de uma certa complexidade.

### Próximos Passos
- 

---

## 📊 Métricas do Dia

- **Tempo total:** 2:30 horas (meta: 2h a 2h30min)
- **Exercícios completados:** 4 / 4
- **Chains criadas:** 4
- **Commits:** 1
- **Linhas de código:** 51, 58, 87, 70

---

## 🔗 Links e Referências Úteis

- [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
- [LCEL Get Started](https://python.langchain.com/docs/expression_language/get_started)
- 

---

---

**Data:** 2 Dez 2025  
**Status:** 🟡 Em progresso

