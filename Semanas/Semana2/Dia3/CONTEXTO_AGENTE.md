# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 2 de 8  
**Dia:** 3 de 7 (Quarta-feira, 3 Dez 2025)  
**Diretório:** `Semanas/Semana2/Dia3/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Semana 1 completa: Scripts de automação com APIs diretas
  - Dia 1: Hello AI com Groq
  - Dia 2: Gerador de conteúdo para blog
  - Dia 3: Analisador de sentimentos (3 LLMs)
  - Dia 4: Resumidor de PDFs
  - Dia 5: Refatoração
  - Dia 6: CLI integrado
  - Dia 7: Deploy + Review
- ✅ Dia 1 (Semana 2): Introdução ao LangChain básico
  - LangChain instalado e funcionando
  - Conceitos básicos aprendidos (LLMs, Prompts, Messages)
  - Exemplos básicos executados
  - Comparação com código manual feita
- ✅ Dia 2 (Semana 2): Chains e sequências com LCEL
  - LangChain Expression Language (LCEL) aprendido
  - Chains sequenciais criadas
  - Chains condicionais criadas
  - Chains paralelas criadas
  - Exercícios completados

### O que está em progresso:
- 🟡 Dia 3 (Semana 2): RAG básico

### O que falta fazer (hoje):
- [ ] Ler GUIA_RAG_BASICO.md completo
- [ ] Entender conceito de RAG (Retrieval-Augmented Generation)
- [ ] Entender componentes básicos: Document Loaders, Text Splitters
- [ ] Criar sistema RAG simples com busca em documentos
- [ ] Criar chain RAG completa (busca + geração)
- [ ] Completar exercícios guiados
- [ ] Preencher journal ao final do dia

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- `README.md` - Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- `checklist.md` - Checklist detalhado com fases
- `journal.md` - Template para reflexão
- `requirements.txt` - Dependências Python (obrigatório sempre, mesmo que vazio)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório para todos os dias)

### Arquivos de Aprendizado (Nível 2 - Intermediário):
- `GUIA_RAG_BASICO.md` - Guia completo sobre RAG básico
- `template.py` - Template com TODOs para prática guiada
- `exemplo_referencia.py` - Exemplo completo para consulta
- `exercicios.md` - Exercícios guiados progressivos

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **Framework:** LangChain (já instalado)
- **Conceito novo:** RAG (Retrieval-Augmented Generation)
- **Componentes:** Document Loaders, Text Splitters, Retrievers
- **APIs:** Groq, Gemini, Claude (já configuradas)
- **Ferramentas:** python-dotenv, venv

### Configuração Necessária:
- Ambiente virtual Python ativado
- APIs configuradas (Groq, Gemini, Claude) - já feito
- Arquivo `.env` com API keys (já existe)
- LangChain instalado (já feito no Dia 1)
- Bibliotecas adicionais: `langchain-community` (para document loaders)

### Objetivo do Dia:
Aprender a criar sistemas RAG básicos usando LangChain. Evoluir de geração simples para geração baseada em contexto encontrado em documentos.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. **Fase 1:** Preparação e Leitura (20min)
   - Ler GUIA_RAG_BASICO.md (seções principais)
   - Entender conceito de RAG
   - Entender componentes básicos (Loaders, Splitters)
   - Revisar chains do Dia 2

2. **Fase 2:** Primeiro Sistema RAG (50min)
   - Carregar documentos simples (texto)
   - Dividir documentos em chunks
   - Criar sistema de busca simples
   - Criar chain RAG completa
   - Executar exemplo_referencia.py
   - Modificar para entender funcionamento

3. **Fase 3:** RAG com Documentos Reais (60min)
   - Carregar documentos de diferentes formatos (texto, PDF)
   - Criar sistema RAG funcional
   - Testar com perguntas reais
   - Completar exercícios guiados

4. **Fase 4:** Prática e Reflexão (15min)
   - Preencher journal
   - Comparar RAG vs geração simples
   - Identificar casos de uso práticos

**Total:** 2h25min (dentro da faixa de 2h-2h30min)

### Próximos Dias:
- Dia 4: RAG avançado com vector databases (usará RAG básico aprendido hoje)
- Dia 5: Agents e tools
- Dia 6: Projeto integrado
- Dia 7: Deploy + Review

---

## 📚 Referências Rápidas

### Scripts dos Dias Anteriores (base):
- `../Dia1/exemplo_langchain_basico.py` - Exemplo básico LangChain
- `../Dia2/exemplo_referencia.py` - Exemplo de chains
- `../Dia2/exercicios/1-chain_sequencial.py` - Chain sequencial

### Documentação LangChain:
- [RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Text Splitters](https://python.langchain.com/docs/modules/data_connection/text_splitters/)
- [Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/)

### Conceitos Importantes:
- **RAG:** Retrieval-Augmented Generation - buscar informações antes de gerar resposta
- **Document Loader:** Carrega documentos de diferentes fontes (texto, PDF, web, etc.)
- **Text Splitter:** Divide documentos grandes em chunks menores
- **Retriever:** Busca chunks relevantes baseado em query
- **Chain RAG:** Chain que combina retriever + LLM para gerar resposta contextualizada

---

## 💡 Dicas Importantes

1. **RAG é poderoso:** Permite criar sistemas que respondem baseados em seus próprios dados
2. **Comece simples:** RAG básico primeiro (busca simples), depois avance para vector databases
3. **Pratique:** Modifique exemplos para entender como funciona
4. **Visualize:** Pense no fluxo: Documento → Chunks → Busca → Contexto → Geração
5. **Teste:** Sempre teste com perguntas reais para verificar qualidade

---

## 🎯 Critérios de Sucesso (Dia 3)

- [ ] Entendeu conceito de RAG e por que usar
- [ ] Entendeu componentes básicos (Loaders, Splitters, Retrievers)
- [ ] Criou pelo menos 1 sistema RAG simples funcional
- [ ] Criou chain RAG completa (busca + geração)
- [ ] Completou pelo menos 3 exercícios guiados
- [ ] Consegue explicar diferença entre RAG e geração simples
- [ ] Journal preenchido com reflexões

---

**Última atualização:** 3 Dez 2025  
**Status:** 🟡 Em progresso

