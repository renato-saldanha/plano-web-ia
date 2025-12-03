# 📅 Dia 2 - Terça-feira (2 Dez 2025)

## 🎯 Contexto para Agentes IA

Este é o **nono dia** do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** Chains e Sequências no LangChain - Criar fluxos de trabalho complexos
- **Duração estimada:** 2h a 2h30min (média de 2h15min)
- **Foco:** Aprender a criar chains (cadeias) de operações com LLMs usando LangChain Expression Language (LCEL)

### 🗺️ Estrutura do Plano:
- **Semana 2:** LangChain + RAG (1 Dez - 7 Dez)
- **Dia 1 (concluído):** LangChain básico - Setup e primeiros exemplos ✅
- **Dia 2 (hoje - Terça):** Chains e sequências - LCEL e fluxos complexos
- **Dia 3 (Quarta):** RAG básico
- **Dia 4 (Quinta):** RAG avançado com vector databases
- **Dia 5 (Sexta):** Agents e tools
- **Dia 6-7 (Sábado-Domingo):** Projeto integrado com LangChain

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python
- `GUIA_CHAINS.md` - Guia completo sobre Chains e LCEL
- `template.py` - Template com TODOs para prática
- `exemplo_referencia.py` - Exemplo completo para consulta
- `exercicios.md` - Exercícios guiados progressivos

### 🎯 O que você vai aprender:
1. **O que são Chains** e por que são fundamentais no LangChain
2. **LangChain Expression Language (LCEL)** - Sintaxe moderna para criar chains
3. **Tipos de chains:** Sequential, Conditional, Parallel
4. **Como criar fluxos complexos** conectando múltiplas operações
5. **Práticas avançadas:** Pipes, Runnables, Streaming com chains

### 💡 Notas Importantes:
- **Baseado em:** Dia 1 (conhecimento básico de LangChain e LLMs)
- **Foco:** Evoluir de chamadas simples para fluxos complexos
- **Nível de Scaffolding:** Nível 2 (Intermediário) - Conceito parcialmente conhecido, aplicação em novo contexto
- **Pré-requisito:** Ter completado Dia 1 e entendido conceitos básicos de LangChain

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Recursos: `../../3-Recursos_E_Links_Uteis.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- Dia 1 (Semana 2): `../Dia1/README.md`
- [LangChain Chains Documentation](https://python.langchain.com/docs/expression_language/)
- [LangChain LCEL Guide](https://python.langchain.com/docs/expression_language/get_started)

---

## 🎓 Por que Chains são importantes?

No **Dia 1**, aprendemos a fazer chamadas simples ao LLM. Mas aplicações reais raramente são tão simples:

- **Exemplo 1:** Gerar conteúdo → Revisar → Formatar → Publicar
- **Exemplo 2:** Pergunta do usuário → Buscar contexto → Gerar resposta → Validar → Responder
- **Exemplo 3:** Texto → Analisar sentimento → Gerar resposta apropriada → Traduzir

**Chains** permitem conectar múltiplas operações de forma elegante e reutilizável. Com **LCEL (LangChain Expression Language)**, você cria chains de forma declarativa e poderosa.

**Vantagens das Chains:**
- ✅ **Composição:** Reutilizar chains em outras chains
- ✅ **Streaming:** Suporte nativo a streaming de respostas
- ✅ **Debugging:** Fácil de debugar e visualizar fluxo
- ✅ **Type Safety:** Type hints completos
- ✅ **Paralelização:** Executar operações em paralelo quando possível

**Não é apenas "chamadas encadeadas":** Chains são uma abstração poderosa que permite criar aplicações complexas de forma simples.

---

## 📚 Pré-requisitos

Antes de começar, certifique-se de:
- ✅ Dia 1 completo (LangChain básico funcionando)
- ✅ Entendeu conceitos básicos: LLMs, Prompts, Messages
- ✅ Consegue fazer chamadas simples ao LLM
- ✅ Python 3.12+ instalado
- ✅ Ambiente virtual configurado
- ✅ LangChain instalado (já feito no Dia 1)

---

**Status:** 🟡 Em progresso  
**Última atualização:** 2 Dez 2025

