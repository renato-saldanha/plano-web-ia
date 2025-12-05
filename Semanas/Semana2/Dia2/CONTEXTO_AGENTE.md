# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 2 de 8  
**Dia:** 2 de 7 (Terça-feira, 2 Dez 2025)  
**Diretório:** `Semanas/Semana2/Dia2/`

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

### O que está em progresso:
- 🟡 Dia 2 (Semana 2): Chains e sequências com LCEL

### O que falta fazer (hoje):
- [ ] Ler GUIA_CHAINS.md completo
- [ ] Entender LangChain Expression Language (LCEL)
- [ ] Criar chains sequenciais simples
- [ ] Criar chains condicionais
- [ ] Criar chains paralelas
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
- `GUIA_CHAINS.md` - Guia completo sobre Chains e LCEL
- `template.py` - Template com TODOs para prática guiada
- `exemplo_referencia.py` - Exemplo completo para consulta

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **Framework:** LangChain (já instalado)
- **Conceito novo:** LangChain Expression Language (LCEL)
- **APIs:** Groq, Gemini, Claude (já configuradas)
- **Ferramentas:** python-dotenv, venv

### Configuração Necessária:
- Ambiente virtual Python ativado
- APIs configuradas (Groq, Gemini, Claude) - já feito
- Arquivo `.env` com API keys (já existe)
- LangChain instalado (já feito no Dia 1)

### Objetivo do Dia:
Aprender a criar chains (cadeias) de operações usando LangChain Expression Language (LCEL). Evoluir de chamadas simples para fluxos complexos e reutilizáveis.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. **Fase 1:** Preparação e Leitura (20min)
   - Ler GUIA_CHAINS.md (seções principais)
   - Entender conceito de LCEL
   - Revisar exemplos básicos do Dia 1

2. **Fase 2:** Primeira Chain Sequencial (40min)
   - Criar chain simples usando LCEL
   - Entender sintaxe `|` (pipe)
   - Executar exemplo_referencia.py
   - Modificar para entender funcionamento

3. **Fase 3:** Chains Avançadas (60min)
   - Chains condicionais (if/else)
   - Chains paralelas (múltiplas operações)
   - Chains com múltiplos LLMs
   - Completar exercícios guiados

4. **Fase 4:** Prática e Reflexão (15min)
   - Preencher journal
   - Comparar chains vs código manual
   - Identificar casos de uso práticos

**Total:** 2h15min (dentro da faixa de 2h-2h30min)

### Próximos Dias:
- Dia 3: RAG básico (usará chains aprendidas hoje)
- Dia 4: RAG avançado com vector databases
- Dia 5: Agents e tools
- Dia 6: Projeto integrado
- Dia 7: Deploy + Review

---

## 📚 Referências Rápidas

### Scripts do Dia 1 (base):
- `../Dia1/exemplo_langchain_basico.py` - Exemplo básico
- `../Dia1/exercicios/3-chain_simples.py` - Chain simples (se existir)

### Documentação LangChain:
- [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
- [LCEL Get Started](https://python.langchain.com/docs/expression_language/get_started)
- [Chains Documentation](https://python.langchain.com/docs/modules/chains/)
- [Runnable Interface](https://python.langchain.com/docs/expression_language/interface)

### Conceitos Importantes:
- **Chain:** Sequência de operações conectadas
- **LCEL:** LangChain Expression Language - sintaxe moderna para chains
- **Runnable:** Interface base para chains no LangChain
- **Pipe (`|`):** Operador para conectar operações em LCEL
- **Streaming:** Capacidade de receber respostas incrementalmente

---

## 💡 Dicas Importantes

1. **LCEL é poderoso:** Sintaxe `|` parece simples, mas permite criar fluxos complexos
2. **Comece simples:** Chain sequencial primeiro, depois avance para condicionais
3. **Pratique:** Modifique exemplos para entender como funciona
4. **Visualize:** Pense no fluxo de dados através da chain
5. **Reutilize:** Chains podem ser compostas em outras chains

---

## 🎯 Critérios de Sucesso (Dia 2)

- [ ] Entendeu conceito de Chain e LCEL
- [ ] Criou pelo menos 1 chain sequencial funcional
- [ ] Criou 1 chain condicional ou paralela
- [ ] Completou pelo menos 3 exercícios guiados
- [ ] Consegue explicar diferença entre chain e chamada simples
- [ ] Journal preenchido com reflexões

---

**Última atualização:** 2 Dez 2025  
**Status:** 🟡 Em progresso

