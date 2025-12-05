# 💪 Exercícios Guiados - RAG Básico

Este arquivo contém exercícios progressivos para praticar RAG básico com LangChain.

---

## 📋 Estrutura dos Exercícios

Cada exercício está em um arquivo separado na pasta `exercicios/`. Complete cada exercício antes de passar para o próximo.

---

## 🎯 Exercício 1: RAG Simples

**Arquivo:** `exercicios/1-rag_simples.py`

**Objetivo:** Criar seu primeiro sistema RAG básico funcionando.

**Tarefas:**
1. Carregar um documento de texto simples
2. Dividir o documento em chunks
3. Criar um retriever simples
4. Criar uma chain RAG básica
5. Fazer uma pergunta e ver a resposta

**Dicas:**
- Use o `exemplo_referencia.py` como referência
- Comece com um documento pequeno (2-3 parágrafos)
- Use chunks de 300 caracteres com overlap de 50

**Como testar:**
```bash
python exercicios/1-rag_simples.py
```

**Critérios de sucesso:**
- [ ] Documento carregado com sucesso
- [ ] Chunks criados corretamente
- [ ] Retriever encontra chunks relevantes
- [ ] Chain RAG responde à pergunta usando contexto

---

## 🎯 Exercício 2: RAG com Documentos Reais

**Arquivo:** `exercicios/2-rag_com_pdf.py`

**Objetivo:** Criar sistema RAG que funciona com documentos reais (PDF ou texto mais complexo).

**Tarefas:**
1. Carregar um documento mais complexo (ou PDF se disponível)
2. Ajustar parâmetros de split (tamanho de chunks)
3. Criar sistema RAG otimizado
4. Testar com múltiplas perguntas
5. Comparar qualidade das respostas

**Dicas:**
- Se não tiver PDF, use um documento de texto mais longo
- Experimente diferentes tamanhos de chunks (200, 500, 1000)
- Teste com perguntas que requerem múltiplos chunks

**Como testar:**
```bash
python exercicios/2-rag_com_pdf.py
```

**Critérios de sucesso:**
- [ ] Documento complexo carregado
- [ ] Chunks criados com tamanho apropriado
- [ ] Sistema responde perguntas complexas
- [ ] Respostas são baseadas no contexto fornecido

---

## 🎯 Exercício 3: RAG Completo

**Arquivo:** `exercicios/3-rag_completo.py`

**Objetivo:** Criar sistema RAG completo e funcional com tratamento de erros.

**Tarefas:**
1. Criar sistema RAG com múltiplos documentos
2. Implementar tratamento de erros
3. Adicionar logging para debug
4. Criar função para fazer perguntas facilmente
5. Testar com diferentes cenários (perguntas fáceis, difíceis, sem resposta)

**Dicas:**
- Adicione try/except para tratamento de erros
- Use print() para mostrar progresso
- Crie função `fazer_pergunta(query)` que retorna resposta formatada

**Como testar:**
```bash
python exercicios/3-rag_completo.py
```

**Critérios de sucesso:**
- [ ] Sistema funciona com múltiplos documentos
- [ ] Tratamento de erros implementado
- [ ] Logging ajuda a entender o que está acontecendo
- [ ] Função de perguntas é fácil de usar

---

## 🎯 Exercício 4: RAG Avançado (Opcional)

**Arquivo:** `exercicios/4-rag_avancado.py`

**Objetivo:** Melhorar sistema RAG com otimizações e features extras.

**Tarefas:**
1. Implementar diferentes tipos de chains ("stuff", "map_reduce")
2. Adicionar filtros para melhorar busca
3. Criar sistema que mostra confiança na resposta
4. Implementar cache de respostas (opcional)
5. Comparar performance de diferentes configurações

**Dicas:**
- Este exercício é opcional e mais avançado
- Experimente diferentes chain_types
- Meça tempo de resposta
- Compare qualidade vs velocidade

**Como testar:**
```bash
python exercicios/4-rag_avancado.py
```

**Critérios de sucesso:**
- [ ] Múltiplos tipos de chains implementados
- [ ] Sistema otimizado para melhor performance
- [ ] Comparação de diferentes configurações feita

---

## 💡 Dicas Gerais

### Antes de Começar
1. **Leia o código:** Entenda o que cada parte faz antes de modificar
2. **Execute primeiro:** Execute o exemplo de referência para ver como funciona
3. **Comece simples:** Não tente fazer tudo de uma vez

### Durante o Desenvolvimento
1. **Teste frequentemente:** Execute o código após cada mudança
2. **Use prints:** Adicione prints para ver o que está acontecendo
3. **Consulte documentação:** LangChain tem excelente documentação

### Depois de Completar
1. **Compare:** Compare seu código com o exemplo de referência
2. **Experimente:** Modifique parâmetros para ver diferenças
3. **Reflita:** Pense sobre o que funcionou bem e o que poderia melhorar

---

## 🔍 Troubleshooting

### Erro: "No module named 'langchain_community'"
**Solução:** Instale com `pip install langchain-community`

### Erro: "No chunks found"
**Solução:** Verifique se o documento foi carregado corretamente e se os chunks foram criados

### Respostas não fazem sentido
**Solução:** 
- Verifique se os chunks encontrados são relevantes
- Aumente número de chunks retornados (k)
- Ajuste tamanho dos chunks

### Muito lento
**Solução:**
- Reduza número de chunks retornados
- Use modelo mais rápido (llama-3.1-8b-instant)
- Reduza tamanho dos chunks

---

## 📚 Recursos Adicionais

- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Text Splitters](https://python.langchain.com/docs/modules/data_connection/text_splitters/)

---

**Última atualização:** 3 Dez 2025

