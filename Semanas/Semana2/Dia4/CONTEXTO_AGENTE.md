# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 2 de 8  
**Dia:** 4 de 7 (Quinta-feira, 4 Dez 2025)  
**Diretório:** `Semanas/Semana2/Dia4/`  
**Dia absoluto:** 11 de 56 dias totais

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ **Semana 1 completa:** APIs diretas, automações, CLI
- ✅ **Dia 1 (Semana 2):** LangChain básico - Setup e primeiros exemplos
- ✅ **Dia 2 (Semana 2):** Chains e LCEL - Sequências complexas
- ✅ **Dia 3 (Semana 2):** RAG básico - Busca por palavras-chave (BM25)

### O que está em progresso:
- 🟡 **Dia 4 (hoje):** RAG avançado - Vector databases e embeddings

### O que falta fazer (hoje):
- [ ] Entender conceito de embeddings (representação vetorial de texto)
- [ ] Aprender sobre vector databases (Chroma, FAISS)
- [ ] Implementar busca semântica com embeddings
- [ ] Criar sistema RAG avançado completo
- [ ] Comparar RAG básico (Dia 3) vs RAG avançado (Dia 4)
- [ ] Documentar aprendizados e próximos passos

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- ✅ `README.md` - Contexto e objetivos do dia
- ✅ `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- 🔄 `checklist.md` - Checklist detalhado com fases (160min)
- 🔄 `journal.md` - Template para reflexão
- 🔄 `requirements.txt` - Dependências Python (obrigatório sempre)
- 🔄 `CONTEXTO_PROXIMO_DIA.md` - Guia para construir Dia 5 (obrigatório)

### Arquivos de Aprendizado (Nível 2 - Intermediário):
- 🔄 `GUIA_RAG_AVANCADO.md` - Conceitos teóricos + passo-a-passo
- 🔄 `template.py` - Template com TODOs para prática guiada
- 🔄 `exemplo_referencia.py` - Exemplo completo para consulta
- 🔄 `exercicios.md` - Exercícios guiados progressivos

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **Framework:** LangChain
- **APIs:** Groq (Llama 3), Google Gemini, Anthropic Claude
- **Vector Databases:** Chroma (principal), FAISS (alternativa)
- **Embeddings:** HuggingFace (sentence-transformers), OpenAI (opcional)

### Configuração Necessária:
- **Ambiente virtual:** Ativado
- **LangChain:** Instalado e funcionando (do Dia 1)
- **Novas dependências:** chromadb, faiss-cpu, sentence-transformers
- **APIs:** Chaves GROQ_API_KEY, GOOGLE_API_KEY em `.env`

### Objetivo do Dia:
Evoluir de RAG básico (busca por palavras-chave) para RAG avançado (busca semântica usando embeddings e vector databases). Entender como embeddings representam texto como vetores numéricos e como vector databases permitem busca eficiente por similaridade semântica.

### Nível de Scaffolding:
**Nível 2 (Intermediário)** - Conceito parcialmente conhecido (RAG básico do Dia 3) aplicado em novo contexto (vector databases e embeddings).

**Arquivos fornecidos:**
- `template.py` com TODOs e dicas
- `exemplo_referencia.py` completo para consulta
- `GUIA_RAG_AVANCADO.md` com teoria + prática
- `exercicios.md` com exercícios guiados

---

## 🔄 Evolução: Dia 3 → Dia 4

### Dia 3: RAG Básico
- **Busca:** BM25 (palavras-chave)
- **Componentes:** TextLoader, RecursiveCharacterTextSplitter, BM25Retriever
- **Limitação:** Busca literal, não entende sinônimos
- **Exemplo:** Query "carro" não encontra documento com "automóvel"

### Dia 4: RAG Avançado
- **Busca:** Semantic Search (embeddings)
- **Componentes:** Embeddings Model, Vector Store (Chroma/FAISS), Semantic Retriever
- **Vantagem:** Busca por significado, entende sinônimos
- **Exemplo:** Query "carro" encontra documentos com "automóvel", "veículo", "transporte"

### Mesma Estrutura, Componentes Melhores:
```
Dia 3: TextLoader → RecursiveCharacterTextSplitter → BM25Retriever → RAG Chain
Dia 4: TextLoader → RecursiveCharacterTextSplitter → VectorStore → Semantic Retriever → RAG Chain
```

**Conclusão:** Não é reaprender RAG, é EVOLUIR o RAG básico para profissional.

---

## 🗺️ Próximos Passos

### Imediato (hoje - 160min):
1. **Preparação (5min):** Revisar README, abrir checklist, confirmar ambiente
2. **Leitura (20min):** Ler `GUIA_RAG_AVANCADO.md` seções 1-3 (conceitos fundamentais)
3. **Construção Parte 1 (30min):** Criar embeddings e calcular similaridade
4. **Construção Parte 2 (30min):** Implementar Chroma vector database
5. **Construção Parte 3 (30min):** Construir sistema RAG completo com busca semântica
6. **Consolidação (25min):** Executar exercícios, comparar RAG básico vs avançado
7. **Registro (20min):** Journal, CONTEXTO_PROXIMO_DIA, commit
8. **Buffer (10min):** Reserva para imprevistos

### Próximo Dia (Dia 5):
- **Foco:** Agents e Tools - Criar agentes autônomos que usam RAG avançado como ferramenta
- **Conexão:** Agents precisarão de RAG avançado para acessar conhecimento
- **Nível:** Provavelmente Nível 1 (conceito novo: Agents)

---

## 📚 Referências Rápidas

### Documentação Oficial:
- [LangChain Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/) - Como usar vector stores
- [LangChain Embeddings](https://python.langchain.com/docs/modules/data_connection/text_embedding/) - Como criar embeddings
- [Chroma Docs](https://docs.trychroma.com/) - Vector database local e gratuita
- [FAISS Docs](https://github.com/facebookresearch/faiss) - Vector database do Facebook

### Arquivos do Projeto:
- `GUIA_RAG_AVANCADO.md` - Teoria completa sobre embeddings e vector databases
- `template.py` - Código com TODOs para completar
- `exemplo_referencia.py` - Código completo funcionando
- `exercicios.md` - Exercícios práticos progressivos
- `../Dia3/GUIA_RAG_BASICO.md` - Para comparação com RAG básico

### Conceitos-Chave:
- **Embeddings:** Representação vetorial de texto (arrays de números)
- **Vector Database:** Banco otimizado para buscar vetores similares
- **Semantic Search:** Busca por significado, não palavras
- **Cosine Similarity:** Medida de similaridade entre vetores
- **Nearest Neighbors:** Algoritmo para encontrar vetores mais próximos

---

## 🔧 Troubleshooting Rápido

### Se embeddings não funcionarem:
1. Verificar instalação: `pip list | grep sentence-transformers`
2. Modelo padrão: `all-MiniLM-L6-v2` (menor e rápido)
3. Alternativa: Usar OpenAI embeddings (requer API key)

### Se Chroma não funcionar:
1. Verificar instalação: `pip list | grep chromadb`
2. Versão mínima: `chromadb>=0.4.22`
3. Alternativa: Usar FAISS (mais rápido, mas menos features)

### Se busca semântica não parecer "inteligente":
1. Modelo de embeddings pode ser fraco (testar modelo maior)
2. Chunks muito grandes ou muito pequenos (ajustar chunk_size)
3. Poucos documentos (adicionar mais exemplos)

### Se performance for lenta:
1. Chroma: Ótimo para desenvolvimento, pode ser lento com muitos docs
2. FAISS: Muito mais rápido, mas requer mais setup
3. Reduzir número de documentos ou chunk_size para testes

---

## 💡 Dicas Importantes

1. **Compare sempre com Dia 3:** Entender a evolução ajuda a valorizar a tecnologia
2. **Embeddings são "mágicos" mas não perfeitos:** Funciona bem 80-90% do tempo
3. **Chunk size importa:** Chunks muito grandes perdem granularidade, muito pequenos perdem contexto
4. **Vector DB é ferramenta, não solução:** RAG bem feito = bons chunks + bom retrieval + bom LLM
5. **Start simple:** Use Chroma primeiro, FAISS depois se precisar performance

---

## 📊 Métricas de Sucesso

Ao final do dia, você deve ser capaz de:
- [ ] Explicar o que são embeddings e como funcionam
- [ ] Criar embeddings de textos e calcular similaridade
- [ ] Configurar e usar Chroma vector database
- [ ] Construir sistema RAG com busca semântica
- [ ] Comparar RAG básico (BM25) vs RAG avançado (embeddings)
- [ ] Entender quando usar cada tipo de RAG

---

**Última atualização:** 4 Dez 2025  
**Status:** 🟡 Pronto para iniciar

