# ✅ Checklist - Dia 4 (Quinta-feira, 4 Dez 2025)

## 🎯 Objetivo do Dia
Evoluir de RAG básico (busca por palavras-chave) para RAG avançado (busca semântica com embeddings e vector databases).

**Meta:** Criar sistema RAG profissional usando embeddings e vector databases (Chroma/FAISS).

---

## ⏰ FASE 0: Preparação (5min)

### Setup Inicial
- [ X] Abrir este checklist
- [ X] Ler `README.md` completo (contexto do dia)
- [ X] Ler `CONTEXTO_AGENTE.md` (detalhes técnicos)
- [ X] Confirmar ambiente virtual ativado

**Como fazer:**
1. Abrir terminal
3. Ativar ambiente virtual: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)
4. Verificar Python: `python --version` (deve ser 3.12+)

**Por que:**
Preparação adequada evita problemas durante desenvolvimento.

**Tempo estimado:** 5 minutos  
**Quando:** Início da sessão

---

## 📖 FASE 1: Leitura Guiada (20min)

### 1.1 Ler Conceitos Fundamentais (10min)
- [ X] Ler `GUIA_RAG_AVANCADO.md` - Seção 1: "Conceitos Fundamentais"
- [ X] Entender o que são embeddings
- [ X] Entender como vetores representam texto
- [ X] Anotar dúvidas para esclarecer na prática

**Como fazer:**
1. Abrir `GUIA_RAG_AVANCADO.md`
2. Ler seção 1 com atenção
3. Fazer anotações sobre conceitos novos

**Por que:**
Embeddings são a base de tudo que faremos hoje. Entender o conceito antes de implementar é essencial.

**Referência:** `GUIA_RAG_AVANCADO.md` seção "1. Conceitos Fundamentais"

### 1.2 Ler sobre Vector Databases (10min)
- [ X] Ler `GUIA_RAG_AVANCADO.md` - Seção 2: "Vector Databases"
- [ X] Entender o que são vector databases
- [ X] Comparar Chroma vs FAISS
- [ X] Entender busca por similaridade

**Como fazer:**
1. Continuar lendo `GUIA_RAG_AVANCADO.md`
2. Focar em seção 2 (Vector Databases)
3. Comparar com RAG básico do Dia 3

**Por que:**
Vector databases são ferramentas essenciais para RAG em produção. Saber escolher a certa é importante.

**Referência:** `GUIA_RAG_AVANCADO.md` seção "2. Vector Databases"

**Tempo estimado:** 20 minutos  
**Quando:** Após preparação

---

## 🏗️ FASE 2: Construção Guiada (90min)

### 2.1 Criar Embeddings e Calcular Similaridade (30min)

#### 2.1.1 Instalar Dependências (5min)
- [ X] Instalar bibliotecas necessárias
- [ X] Verificar instalação bem-sucedida

**Como fazer:**
```bash
# No terminal com venv ativado
pip install chromadb faiss-cpu sentence-transformers tiktoken
```

**Verificar:**
```bash
pip list | grep -E "chroma|faiss|sentence"
```

**Por que:**
Novas dependências são necessárias para embeddings e vector databases.

**Referência:** `requirements.txt` para lista completa

#### 2.1.2 Trabalhar no Template - Parte 1 (25min)
- [ X] Abrir `template.py`
- [ X] Completar TODO 1: Importar bibliotecas de embeddings
- [ X] Completar TODO 2: Criar modelo de embeddings
- [ X] Testar criação de embeddings de textos simples
- [ X] Calcular similaridade entre embeddings

**Como fazer:**
1. Abrir `template.py` no editor
2. Ler comentários e TODOs com atenção
3. Seguir dicas fornecidas (começam com "Dica:")
4. Consultar `exemplo_referencia.py` se precisar de ajuda
5. Testar código rodando: `python template.py`

**Dicas importantes:**
- Use `HuggingFaceEmbeddings` com modelo `all-MiniLM-L6-v2` (leve e rápido)
- Embeddings são arrays de números (geralmente 384-768 dimensões)
- Similaridade cosine varia de -1 a 1 (quanto maior, mais similar)

**Por que:**
Entender como criar embeddings manualmente ajuda a entender o que vector databases fazem internamente.

**Referência:** `exemplo_referencia.py` seção "Embeddings Básicos"  
**Guia:** `GUIA_RAG_AVANCADO.md` seção "3.1 Criando Embeddings"

**Tempo estimado:** 30 minutos

### 2.2 Implementar Chroma Vector Database (30min)

#### 2.2.1 Setup FAISS (15min)
- [ X] Completar TODO 3: Carregar documentos (reutilizar código do Dia 3)
- [ X] Completar TODO 4: Criar vector store com Chroma
- [ X] Verificar que documentos foram armazenados

**Como fazer:**
1. Reutilizar código de `../Dia3/template.py` para carregar documentos
2. Usar `Chroma.from_documents()` para criar vector store
3. Embeddings serão criados automaticamente para cada documento

**Código de referência:**
```python
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Criar embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Criar vector store (documentos já carregados e divididos)
vectorstore = FAISS.from_documents(
    documents=chunks,  # Do text splitter
    embedding=embeddings,
)

vectorstore.save_local("./faiss_index")
```

**Por que:**
Chroma é simples de usar e ótimo para começar com vector databases.

**Referência:** `GUIA_RAG_AVANCADO.md` seção "3.2 Setup Chroma"  
**Exemplo:** `exemplo_referencia.py` seção "Chroma Setup"

#### 2.2.2 Testar Busca Semântica (15min)
- [ X] Completar TODO 5: Criar retriever do vector store
- [ X] Testar busca semântica com queries diferentes
- [ X] Comparar resultados com busca BM25 do Dia 3

**Como fazer:**
1. Criar retriever: `vectorstore.as_retriever(search_kwargs={"k": 3})`
2. Testar busca: `docs = retriever.invoke("sua query aqui")`
3. Comparar com RAG básico: mesma query, resultados diferentes?

**Testes sugeridos:**
- Query com sinônimos (ex: "automóvel" vs "carro")
- Query conceitual (ex: "transporte rápido" deve encontrar docs sobre carros/aviões)
- Comparar com BM25: qual encontra documentos mais relevantes?

**Por que:**
Busca semântica é o diferencial do RAG avançado. Testar é essencial para entender o poder da tecnologia.

**Referência:** `GUIA_RAG_AVANCADO.md` seção "3.3 Busca Semântica"

**Tempo estimado:** 30 minutos

### 2.3 Construir Sistema RAG Completo (30min)

#### 2.3.1 Criar RAG Chain com LCEL (20min)
- [ X] Completar TODO 6: Criar RAG chain usando LCEL
- [ X] Integrar retriever semântico + LLM
- [ X] Testar com queries complexas

**Como fazer:**
1. Usar LCEL (LangChain Expression Language) aprendido no Dia 2
2. Estrutura similar ao Dia 3, mas com retriever semântico
3. Template de prompt pode ser reutilizado

**Código de referência:**
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Template de prompt (similar ao Dia 3)
template = """Responda baseado apenas no contexto abaixo:

Contexto: {context}

Pergunta: {question}

Resposta:"""

prompt = ChatPromptTemplate.from_template(template)

# RAG chain com LCEL
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Testar
resposta = rag_chain.invoke("Sua pergunta aqui")
```

**Por que:**
RAG chain completa integra retrieval semântico + geração, permitindo criar assistentes inteligentes.

**Referência:** `exemplo_referencia.py` seção "RAG Chain Completa"  
**Guia:** `GUIA_RAG_AVANCADO.md` seção "3.4 RAG Chain com LCEL"

#### 2.3.2 Comparar com RAG Básico (10min)
- [ X] Completar TODO 7: Testar mesmas queries do Dia 3
- [ X] Documentar diferenças nos resultados
- [ X] Avaliar quando usar cada tipo de RAG

**Como fazer:**
1. Pegar 3-5 queries usadas no Dia 3
2. Executar no sistema RAG avançado (Dia 4)
3. Comparar qualidade das respostas
4. Documentar vantagens e desvantagens de cada abordagem

**Pontos de comparação:**
- Relevância dos documentos recuperados
- Qualidade da resposta final
- Velocidade de resposta
- Facilidade de implementação

**Por que:**
Entender quando usar cada tipo de RAG é essencial para escolher tecnologia apropriada em projetos reais.

**Referência:** `GUIA_RAG_AVANCADO.md` seção "4. Comparação RAG Básico vs Avançado"

**Tempo estimado:** 30 minutos

**Total Fase 2:** 90 minutos

---

## 🎯 FASE 3: Consolidação (25min)

### 3.1 Exercícios Práticos (20min)
- [ X] Abrir `exercicios.md`
- [ X] Completar Exercício 1: Embeddings Básicos (5min)
- [ X] Completar Exercício 2: Chroma Vector Store (10min)
- [ X] Completar Exercício 3: RAG Avançado Completo (5min)

**Como fazer:**
1. Abrir `exercicios.md`
2. Seguir instruções de cada exercício
3. Verificar critérios de aceitação
4. Se tempo permitir, tentar desafio opcional

**Por que:**
Exercícios práticos consolidam aprendizado e identificam gaps de conhecimento.

**Referência:** `exercicios.md` para instruções detalhadas

### 3.2 Checklist Parcial (5min)
- [ X] Revisar todos os itens completados até aqui
- [ X] Marcar itens finalizados
- [ X] Identificar pendências críticas
- [ X] Ajustar próximos passos se necessário

**Como fazer:**
1. Reler checklist do início
2. Marcar [x] nos itens completos
3. Se algum item ficou pendente, decidir: fazer agora ou mover para próximo dia?

**Por que:**
Revisão garante que nenhum conceito importante foi pulado.

**Tempo estimado:** 25 minutos

---

## 📝 FASE 4: Registro e Handoff (20min)

### 4.1 Preencher Journal (10min)
- [ X] Abrir `journal.md`
- [ X] Preencher seção "O que foi feito hoje"
- [ X] Preencher seção "O que aprendi hoje"
- [ X] Documentar desafios enfrentados
- [ X] Registrar insights e próximos passos

**Como fazer:**
1. Abrir `journal.md`
2. Preencher cada seção com honestidade
3. Focar em aprendizados, não apenas tarefas

**Perguntas guia:**
- O que aprendi sobre embeddings?
- Como vector databases funcionam?
- Qual diferença prática entre RAG básico e avançado?
- Que dificuldades enfrentei?
- O que farei diferente amanhã?

**Por que:**
Journal é ferramenta de reflexão e aprendizado. Documentar hoje ajuda a revisar depois.

**Referência:** `journal.md` template completo

### 4.2 Criar Contexto para Próximo Dia (10min)
- [ ] Criar `CONTEXTO_PROXIMO_DIA.md`
- [ ] Documentar o que foi aprendido hoje
- [ ] Explicar conexão com Dia 5 (Agents)
- [ ] Listar preparação necessária

**Como fazer:**
1. Usar template de `TEMPLATE_CONTEXTO_PROXIMO_DIA.md` na raiz
2. Resumir conceitos principais do Dia 4
3. Explicar como Agents (Dia 5) usarão RAG avançado
4. Sugerir nível de scaffolding para Dia 5 (provavelmente Nível 1)

**Estrutura sugerida:**
```markdown
# O que aprendemos hoje (Dia 4)
- Embeddings e representação vetorial
- Vector databases (Chroma/FAISS)
- Busca semântica
- RAG avançado completo

# Por que Dia 5 é importante
- Agents são agentes autônomos que usam ferramentas
- RAG avançado será uma das ferramentas do Agent
- Agents decidem quando usar RAG para buscar conhecimento

# Como se conecta
- Dia 4: RAG avançado como sistema isolado
- Dia 5: RAG avançado como ferramenta de Agent
```

**Por que:**
Facilita transição entre dias e ajuda a manter continuidade do aprendizado.

**Referência:** `TEMPLATE_CONTEXTO_PROXIMO_DIA.md` na raiz do projeto

**Tempo estimado:** 20 minutos

---

## 🔄 FASE 5: Buffer (10min)

### Reserva para Imprevistos
- Resolver bloqueios técnicos
- Revisitar conceitos que não ficaram claros
- Ajustar checklist se necessário

**Como usar:**
- Se tudo correu bem: Use para aprofundar exercícios opcionais
- Se teve dificuldades: Use para revisar conceitos ou pedir ajuda
- Se terminou antes: Avance para `exercicios.md` desafio opcional

**Por que:**
Buffer garante que não ultrapassemos 160 minutos mesmo com imprevistos.

**Tempo estimado:** 10 minutos (usar apenas se necessário)

---

## 🎉 CONCLUSÃO

### ✅ Critérios de Sucesso
No final do dia, você deve ter:
- [ ] Sistema RAG avançado funcionando com Chroma
- [ ] Entendimento claro de embeddings e vector databases
- [ ] Comparação documentada: RAG básico vs avançado
- [ ] Template completo com todos os TODOs resolvidos
- [ ] Exercícios práticos finalizados
- [ ] Journal preenchido
- [ ] CONTEXTO_PROXIMO_DIA criado

### 📊 Tempo Total
- Preparação: 5min
- Leitura Guiada: 20min
- Construção Guiada: 90min
- Consolidação: 25min
- Registro/Handoff: 20min
- Buffer: 10min
- **TOTAL: 170min → Ajustar para 160min (usar buffer apenas se necessário)**

### 🎯 Streak: 11/56 dias

**Parabéns por completar o Dia 4!** 🚀

Você evoluiu de RAG básico para RAG profissional. Amanhã aprenderá sobre Agents que usarão este RAG como ferramenta!

---

## 📚 Recursos de Apoio

### Se tiver dúvidas durante o dia:
- **Conceitos teóricos:** Consultar `GUIA_RAG_AVANCADO.md`
- **Código de referência:** Consultar `exemplo_referencia.py`
- **Exercícios práticos:** Consultar `exercicios.md`
- **Comparação:** Revisar `../Dia3/GUIA_RAG_BASICO.md`

### Se travar:
1. **Ler mensagem de erro completa** (geralmente indica o problema)
2. **Consultar `GUIA_RAG_AVANCADO.md` seção "5. Troubleshooting"**
3. **Comparar seu código com `exemplo_referencia.py`**
4. **Revisar conceitos em `GUIA_RAG_AVANCADO.md`**
5. **Testar com exemplo simples primeiro** (poucos documentos, query simples)

### Próximos passos:
- **Amanhã (Dia 5):** Agents e Tools - Criar agentes autônomos
- **Preparação:** Revisar conceitos de RAG avançado, pensar em como agents podem usar ferramentas

---

**Última atualização:** 4 Dez 2025  
**Status:** 🟡 Pronto para iniciar

