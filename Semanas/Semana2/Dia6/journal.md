# 📝 Journal - Dia 6 (Sábado, 6 Dez 2025)

## 🎯 Objetivo do Dia
Integrar tools (calculator + RAG do Dia 4) em um agent ReAct com LangGraph (`create_react_agent`) para formar um “Knowledge Assistant”.

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [ X] Tool `calculadora` validada
- [ X] Tool `buscar_conhecimento` validada (FAISS Dia 4)
- [ X] Agent LangGraph testado (cálculo, RAG, pergunta mista)

### Detalhes das Tarefas
- Concluído leitura dos documento.
- template.py ajustado e executado.
- Exercícios executados no template.py.
- Feitos exercícios adicionais.
- Solicitado exercício 3 para estudo - RAG avançado com busca híbrida, reranker e agent opcionais.


## 🎓 O que aprendi hoje?

### Conceitos Novos
- Agentic RAG - Conceitos de Tools, como restringir ao máximo o modelo para que busque somente dados do RAG
- Busca híbrida - Permite o RAG uma precisão maior no retorno da informação, efetuando busca semântica e exata.
- Reranker - Após a busca híbrida, reorganiza os indices com base nas mais similares.

### Ferramentas Utilizadas
- Python
- LangChain
- FAISS
- ChatOpenAI

### Desafios Enfrentados
- Escrita consistente das Docstrings, não possibilitando o modelo associar a tool. Fui testando até que me trouxe resultados consistentes.
- Ao entrar no RAG não encontrada a pergunta. Melhora na Docstring.
- Entendimento da estrutura de um chain usando HumanMessage. Pedi ao modelo para me explicar como é uma estrutura feita com HumanMessage usando um SYSTEM_MESSAGE junto.

---

## 💡 Insights e Reflexões

### O que funcionou bem?
- 

### O que poderia ser melhorado?
- 

### Próximos Passos
- 

---

## 📊 Métricas do Dia
- **Tempo total:** 6 horas (meta 2h30-2h40)  
- **Commits:** 1  
- **Erros do agent resolvidos:** 10+

---

## 🔗 Links e Referências Úteis
- 

---

## 📝 Notas Adicionais
_(Espaço livre para anotações)_  

---

**Data:** 6 Dez 2025  
**Status:** 🟡 Em progresso

