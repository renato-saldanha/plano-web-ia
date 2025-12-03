# 📝 Exercícios Guiados: Chains e LCEL

Estes exercícios ajudam a consolidar o aprendizado sobre Chains e LangChain Expression Language (LCEL) através de prática guiada e progressiva.

**Importante:** Tente resolver cada exercício antes de consultar a solução. A prática é essencial para aprender!

---

## 📋 Índice

1. [Exercício 1: Chain Sequencial Simples](#exercício-1-chain-sequencial-simples)
2. [Exercício 2: Chain Condicional](#exercício-2-chain-condicional)
3. [Exercício 3: Chain Paralela](#exercício-3-chain-paralela)
4. [Exercício 4: Chain Complexa](#exercício-4-chain-complexa)

---

## Exercício 1: Chain Sequencial Simples

### Objetivo
Criar uma chain sequencial que gera conteúdo e depois formata em markdown.

### Tarefa
Complete o arquivo `exercicios/1-chain_sequencial.py` que:
1. Recebe um tópico como input
2. Gera uma curiosidade sobre o tópico
3. Retorna o resultado

### Passos Guiados

**Passo 1:** Abrir arquivo `exercicios/1-chain_sequencial.py`

**Passo 2:** O arquivo já contém a estrutura básica. Complete a função `sequencial_chain()` seguindo os comentários no código.

**Passo 3:** Execute o arquivo para testar:
```bash
python exercicios/1-chain_sequencial.py
```

**Como fazer:**
1. Abra `exercicios/1-chain_sequencial.py`
2. Complete a função `sequencial_chain()` seguindo os comentários
3. Execute o arquivo para testar
4. Consulte `exemplo_referencia.py` seção 2 se precisar de ajuda

### Desafio Extra
Modifique o arquivo para adicionar uma segunda etapa que formata o resultado em markdown com título.

### Solução

<details>
<summary>Clique para ver solução completa</summary>

Consulte o arquivo `exercicios/1-chain_sequencial.py` que já contém a solução implementada. O arquivo demonstra:
- Como criar uma chain sequencial simples
- Como usar `ChatPromptTemplate` com variáveis
- Como conectar componentes usando o operador `|`
- Como invocar a chain com um dicionário de entrada

</details>

---

## Exercício 2: Chain Condicional

### Objetivo
Criar uma chain que escolhe qual estratégia usar baseada no tamanho do input.

### Tarefa
Complete o arquivo `exercicios/2-chain_condicional.py` que:
1. Recebe um texto como input
2. Se o texto tiver menos de 50 caracteres: gera resposta curta
3. Se o texto tiver 50 ou mais caracteres: gera resposta detalhada
4. Retorna a resposta apropriada

### Passos Guiados

**Passo 1:** Abrir arquivo `exercicios/2-chain_condicional.py`

**Passo 2:** O arquivo já contém a estrutura básica. Complete a função `conditional_chain()` seguindo os comentários no código.

**Passo 3:** Execute o arquivo para testar:
```bash
python exercicios/2-chain_condicional.py
```

**Como fazer:**
1. Abra `exercicios/2-chain_condicional.py`
2. Complete a função `conditional_chain()` seguindo os comentários
3. Execute o arquivo para testar com diferentes tamanhos de input
4. Consulte `exemplo_referencia.py` seção 4 se precisar de ajuda

### Desafio Extra
Modifique o arquivo para adicionar uma terceira condição: se o texto contém "?", use uma chain que responde como FAQ.

### Solução

<details>
<summary>Clique para ver solução completa</summary>

Consulte o arquivo `exercicios/2-chain_condicional.py` que já contém a solução implementada. O arquivo demonstra:
- Como criar chains diferentes para diferentes condições
- Como usar `RunnableBranch` para escolher qual chain executar
- Como usar lambdas para criar condições
- Como testar com diferentes inputs

</details>

---

## Exercício 3: Chain Paralela

### Objetivo
Criar uma chain que analisa um texto em múltiplas dimensões simultaneamente.

### Tarefa
Complete o arquivo `exercicios/3-chain_paralela.py` que:
1. Recebe um código como input (variável `codebase`)
2. Analisa o código em múltiplas dimensões simultaneamente:
   - Gera resumo do código
   - Analisa o código como System Analyst
   - Extrai palavras-chave
3. Executa todas as análises em paralelo
4. Retorna dicionário com todos os resultados

### Passos Guiados

**Passo 1:** Abrir arquivo `exercicios/3-chain_paralela.py`

**Passo 2:** O arquivo já contém a estrutura básica. Complete a função `parallel_chain()` seguindo os comentários no código.

**Passo 3:** Execute o arquivo para testar:
```bash
python exercicios/3-chain_paralela.py
```

**Como fazer:**
1. Abra `exercicios/3-chain_paralela.py`
2. Complete a função `parallel_chain()` seguindo os comentários
3. Execute o arquivo para testar com o código de exemplo fornecido
4. Consulte `exemplo_referencia.py` seção 5 se precisar de ajuda

### Desafio Extra
Modifique o arquivo para adicionar uma quarta análise: identificar o idioma do código ou adicionar análise de complexidade.

### Solução

<details>
<summary>Clique para ver solução completa</summary>

Consulte o arquivo `exercicios/3-chain_paralela.py` que já contém a solução implementada. O arquivo demonstra:
- Como criar múltiplas chains independentes
- Como usar `RunnableParallel` para executar chains em paralelo
- Como retornar um dicionário com múltiplos resultados
- Como testar com um exemplo de código real

</details>

---

## Exercício 4: Chain Complexa

### Objetivo
Combinar chains sequenciais, condicionais e paralelas em uma pipeline completa.

### Tarefa
Complete o arquivo `exercicios/4-chain_complexa.py` que:
1. Gera um resumo sobre um tópico (chain sequencial)
2. Analisa o resumo gerado em múltiplas dimensões (chain paralela):
   - Análise detalhada do resumo
   - Extração de palavras-chave
3. Combina tudo em uma pipeline completa
4. Retorna dicionário com análise e palavras-chave

### Passos Guiados

**Passo 1:** Abrir arquivo `exercicios/4-chain_complexa.py`

**Passo 2:** O arquivo já contém a estrutura básica. Complete a função `complex_chain()` seguindo os comentários no código.

**Passo 3:** Execute o arquivo para testar:
```bash
python exercicios/4-chain_complexa.py
```

**Como fazer:**
1. Abra `exercicios/4-chain_complexa.py`
2. Complete a função `complex_chain()` seguindo os comentários
3. **Importante:** Lembre-se de converter a string retornada por `generate_chain` em um dicionário antes de passar para `RunnableParallel`
4. Execute o arquivo para testar
5. Consulte `exemplo_referencia.py` seção 6 se precisar de ajuda

### Desafio Extra
Modifique o arquivo para adicionar uma etapa final que formata o resultado em markdown ou adiciona uma chain de revisão.

### Solução

<details>
<summary>Clique para ver solução completa</summary>

Consulte o arquivo `exercicios/4-chain_complexa.py` que já contém a solução implementada. O arquivo demonstra:
- Como combinar chains sequenciais e paralelas
- Como converter tipos entre chains (string → dict)
- Como usar `RunnablePassthrough()` para passar dados entre chains
- Como criar uma pipeline completa que gera e analisa conteúdo

**Dica importante:** Note como o código usa `{"summary": RunnablePassthrough()}` para converter a string retornada por `generate_chain` em um dicionário compatível com `RunnableParallel`.

</details>

---

## 🎯 Critérios de Sucesso

Você completou os exercícios quando:
- [ ] Exercício 1 (`exercicios/1-chain_sequencial.py`) executado com sucesso
- [ ] Exercício 2 (`exercicios/2-chain_condicional.py`) executado com sucesso
- [ ] Exercício 3 (`exercicios/3-chain_paralela.py`) executado com sucesso
- [ ] Exercício 4 (`exercicios/4-chain_complexa.py`) executado com sucesso (ou pelo menos 3 dos 4)
- [ ] Entendeu diferença entre chains sequenciais, condicionais e paralelas
- [ ] Consegue criar suas próprias chains sem consultar exemplos

## 📁 Estrutura dos Arquivos

Os exercícios estão organizados na pasta `exercicios/`:
- `exercicios/1-chain_sequencial.py` - Chain sequencial simples
- `exercicios/2-chain_condicional.py` - Chain condicional com RunnableBranch
- `exercicios/3-chain_paralela.py` - Chain paralela com RunnableParallel
- `exercicios/4-chain_complexa.py` - Chain complexa combinando múltiplas chains

Cada arquivo contém:
- Estrutura completa com imports
- Função principal para implementar
- Código de teste no `if __name__ == "__main__"`
- Comentários explicativos

---

## 💡 Dicas Finais

1. **Comece simples:** Domine chains sequenciais antes de avançar
2. **Teste incrementalmente:** Teste cada parte antes de combinar
3. **Consulte documentação:** LangChain tem excelente documentação
4. **Pratique:** Crie variações dos exercícios para consolidar
5. **Compare:** Sempre compare com código manual equivalente

---

**Boa prática!** 🚀

