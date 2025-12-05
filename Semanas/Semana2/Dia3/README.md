# 📅 Dia 3 - Quarta-feira (3 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **décimo dia** do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** RAG básico - Busca e geração com LangChain
- **Duração estimada:** 2h a 2h30min (média de 2h15min)
- **Foco:** Aprender RAG (Retrieval-Augmented Generation) - buscar informações antes de gerar resposta

### 🗺️ Estrutura do Plano:
- **Semana 2:** LangChain + RAG (1 Dez - 7 Dez)
- **Dia 1 (concluído):** LangChain básico - Setup e primeiros exemplos ✅
- **Dia 2 (concluído):** Chains e sequências - LCEL e fluxos complexos ✅
- **Dia 3 (hoje - Quarta):** RAG básico - Busca e geração
- **Dia 4 (Quinta):** RAG avançado com vector databases
- **Dia 5 (Sexta):** Agents e tools
- **Dia 6-7 (Sábado-Domingo):** Projeto integrado com LangChain

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python
- `GUIA_RAG_BASICO.md` - Guia completo sobre RAG básico
- `template.py` - Template com TODOs para prática
- `exemplo_referencia.py` - Exemplo completo para consulta
- `exercicios.md` - Exercícios guiados progressivos

### 🎯 O que você vai aprender:
1. **O que é RAG** e por que é fundamental para aplicações de IA
2. **Como funciona RAG:** Busca de informações + Geração de resposta
3. **Componentes básicos:** Document Loaders, Text Splitters, Retrievers
4. **Como criar sistema RAG simples** usando LangChain
5. **Práticas:** Buscar em documentos e gerar respostas contextualizadas

### 💡 Notas Importantes:
- **Baseado em:** Dia 1 (LangChain básico) e Dia 2 (Chains)
- **Foco:** Evoluir de geração simples para geração baseada em contexto
- **Nível de Scaffolding:** Nível 2 (Intermediário) - Conceito parcialmente conhecido (já sabe LangChain e Chains), aplicação em novo contexto (RAG)
- **Pré-requisito:** Ter completado Dia 1 e Dia 2, entendido conceitos básicos de LangChain e Chains

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Recursos: `../../3-Recursos_E_Links_Uteis.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Dia 1 (Semana 2): `../Dia1/README.md`
- Dia 2 (Semana 2): `../Dia2/README.md`
- [LangChain RAG Documentation](https://python.langchain.com/docs/use_cases/question_answering/)
- [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)

---

## 🎓 Por que RAG é importante?

No **Dia 1 e Dia 2**, aprendemos a fazer chamadas simples ao LLM e criar chains. Mas LLMs têm limitações:

- **Conhecimento limitado:** LLMs só sabem o que foi treinado até uma data específica
- **Sem acesso a dados privados:** Não podem acessar seus documentos ou banco de dados
- **Alucinações:** Podem inventar informações quando não sabem a resposta

**RAG (Retrieval-Augmented Generation)** resolve isso:

1. **Busca (Retrieval):** Busca informações relevantes em seus documentos/dados
2. **Aumento (Augmentation):** Adiciona essas informações ao prompt
3. **Geração (Generation):** LLM gera resposta baseada no contexto encontrado

**Exemplos práticos:**
- **Chatbot de suporte:** Busca em FAQ antes de responder
- **Assistente de documentos:** Busca em PDFs antes de responder perguntas
- **Sistema de conhecimento:** Busca em base de conhecimento antes de gerar resposta

**Vantagens do RAG:**
- ✅ **Respostas precisas:** Baseadas em dados reais, não apenas treinamento
- ✅ **Atualização fácil:** Adicione novos documentos sem retreinar modelo
- ✅ **Rastreabilidade:** Pode mostrar de onde veio a informação
- ✅ **Menos alucinações:** LLM tem contexto real para trabalhar

**Não é apenas "buscar e colar":** RAG é uma arquitetura completa que combina busca inteligente com geração contextualizada.

---

## 📚 Pré-requisitos

Antes de começar, certifique-se de:
- ✅ Dia 1 completo (LangChain básico funcionando)
- ✅ Dia 2 completo (Chains e LCEL funcionando)
- ✅ Entendeu conceitos básicos: LLMs, Prompts, Chains
- ✅ Consegue criar chains simples com LCEL
- ✅ Python 3.12+ instalado
- ✅ Ambiente virtual configurado
- ✅ LangChain instalado (já feito no Dia 1)

---

**Status:** 🟡 Em progresso  
**Última atualização:** 3 Dez 2025

