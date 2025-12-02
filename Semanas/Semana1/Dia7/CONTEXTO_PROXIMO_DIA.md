# 🎯 Contexto para Construir a Semana 2, Dia 1

## 📚 O que aprendemos na Semana 1

### Conceitos Principais
- **APIs de IA Generativa:** Como integrar Groq, Gemini e Claude APIs
- **Prompts e Engenharia de Prompt:** Como criar prompts efetivos para diferentes tarefas
- **Comparação de LLMs:** Entender diferenças entre modelos e quando usar cada um
- **Automação com Python:** Criar scripts práticos para tarefas do dia a dia
- **CLI (Command Line Interface):** Criar interfaces de linha de comando profissionais
- **Documentação Técnica:** Como documentar projetos de forma profissional
- **Versionamento Git:** Controle de versão e deploy no GitHub

### Habilidades Desenvolvidas
- Configuração de ambiente Python e APIs
- Criação de scripts de automação funcionais
- Tratamento de erros e logging
- Extração de texto de PDFs
- Criação de CLI com argparse
- Documentação de projetos
- Deploy no GitHub

### Código Criado
- `hello_ai_groq.py` - Hello AI básico
- `gerador_conteudo_blog.py` - Gerador de conteúdo para blog
- `analisador_sentimentos.py` - Analisador comparando 3 LLMs
- `resumidor_pdf.py` - Resumidor de documentos PDF
- `cli_automatizacoes.py` - CLI integrado unificando todos os scripts

---

## 🔗 Por que a Semana 2 é importante

A Semana 2 marca a transição de **scripts simples** para **aplicações mais sofisticadas** usando **LangChain**.

### O que é LangChain?
LangChain é um framework Python que facilita:
- **Orquestração de LLMs:** Gerenciar múltiplos modelos de forma unificada
- **Chains:** Conectar múltiplas operações de IA em sequência
- **RAG (Retrieval-Augmented Generation):** Buscar informações relevantes antes de gerar resposta
- **Agents:** Criar agentes autônomos que podem tomar decisões

### Por que aprender LangChain?
1. **Padrão da Indústria:** Framework mais usado para aplicações de IA
2. **Produtividade:** Reduz código boilerplate significativamente
3. **Escalabilidade:** Facilita criar aplicações complexas
4. **Flexibilidade:** Funciona com qualquer LLM (Groq, OpenAI, Gemini, etc.)
5. **Preparação:** Base para projetos mais avançados nas semanas seguintes

### Como se relaciona com Semana 1
- **Semana 1:** Aprendemos a usar APIs diretamente (método manual)
- **Semana 2:** Aprendemos a usar LangChain (método profissional)
- **Benefício:** Código mais limpo, manutenível e escalável

---

## 🎯 O que será feito na Semana 2

### Objetivo Principal
Aprender LangChain e criar aplicações mais sofisticadas com RAG (Retrieval-Augmented Generation).

### Tarefas Principais da Semana

1. **Dia 1: LangChain Básico**
   - Setup de LangChain
   - Primeiros exemplos práticos
   - Comparar código manual vs LangChain

2. **Dia 2: Chains e Sequências**
   - Criar chains simples
   - Conectar múltiplas operações
   - Exemplos práticos

3. **Dia 3: RAG Básico**
   - Introdução ao RAG
   - Criar sistema de busca simples
   - Integrar com LLM

4. **Dia 4: RAG Avançado**
   - Vector databases básicos
   - Embeddings
   - Busca semântica

5. **Dia 5: Agents**
   - Criar agentes simples
   - Tools e funções
   - Exemplos práticos

6. **Dia 6: Projeto Integrado**
   - Projeto completo usando LangChain
   - Integração de conceitos aprendidos

7. **Dia 7: Deploy + Review**
   - Deploy do projeto
   - Review da semana
   - Preparação para Semana 3

### Conceitos que serão aprendidos
- **LangChain:** Framework de orquestração de LLMs
- **Chains:** Sequências de operações de IA
- **RAG:** Retrieval-Augmented Generation
- **Embeddings:** Representações vetoriais de texto
- **Vector Databases:** Armazenamento de embeddings
- **Agents:** Agentes autônomos de IA
- **Tools:** Funções que agentes podem usar

### Como se relaciona com Semana 1
- **Base sólida:** Semana 1 forneceu conhecimento de APIs e Python
- **Evolução natural:** LangChain é próximo passo lógico
- **Aplicação prática:** Usaremos conhecimento de Semana 1 em contexto mais avançado

---

## 📋 Como Construir a Semana 2, Dia 1

### 1. Criar Estrutura Básica

```
Semana2/
├── README.md                  # Visão geral da semana
├── Dia1/
│   ├── README.md
│   ├── CONTEXTO_AGENTE.md
│   ├── checklist.md
│   ├── journal.md
│   ├── requirements.txt
│   │
│   ├── GUIA_LANGCHAIN.md      # Guia completo de LangChain
│   ├── exemplo_langchain_basico.py  # Exemplo completo comentado
│   └── exercicios_langchain.md
```

**Ordem sugerida:**
1. Criar pasta `Semana2/` e `Semana2/Dia1/`
2. Copiar templates de `TEMPLATE_ESTRUTURA_DIA.md` na raiz
3. Preencher README.md com contexto específico
4. Criar CONTEXTO_AGENTE.md
5. Criar checklist.md detalhado

### 2. Definir Nível de Scaffolding

**Nível recomendado:** **Nível 1 (Iniciante)**

**Justificativa:**
- LangChain é conceito completamente novo
- Framework complexo com muitos conceitos
- Primeira exposição ao tópico
- Muitas dependências novas

**Arquivos necessários:**
- `GUIA_LANGCHAIN.md` - Guia muito detalhado passo-a-passo
- `exemplo_langchain_basico.py` - Código completo comentado linha por linha
- `exercicios_langchain.md` - Exercícios guiados progressivos

### 3. Criar Arquivos de Aprendizado

#### GUIA_LANGCHAIN.md
Conteúdo sugerido:
- O que é LangChain e por que usar
- Instalação e setup
- Conceitos básicos (LLMs, Prompts, Chains)
- Primeiros exemplos práticos
- Comparação com código manual da Semana 1
- Recursos para aprofundamento

#### exemplo_langchain_basico.py
Estrutura sugerida:
```python
#!/usr/bin/env python3
"""
Exemplo Básico de LangChain

Este script demonstra uso básico do LangChain para criar
aplicações com LLMs de forma mais simples que código manual.
"""

# Seção 1: Imports e configuração
# Seção 2: Exemplo básico (equivalente ao hello_ai_groq.py)
# Seção 3: Exemplo com prompts estruturados
# Seção 4: Comparação com código manual
```

#### exercicios_langchain.md
Exercícios sugeridos:
1. Exercício 1: Hello LangChain (equivalente ao Dia 1 Semana 1)
2. Exercício 2: Prompt template simples
3. Exercício 3: Chain básico
4. Exercício 4: Comparar com código manual

### 4. Criar Checklist Detalhado

**⚠️ IMPORTANTE: Tempo Padronizado**

**Todos os Dias:**
- **Total:** 2h a 2h30min (média de 2h15min)

O checklist do Dia 1 deve incluir:

**Fase 1: Preparação (15min)**
- Ler GUIA_LANGCHAIN.md (seções principais)
- Instalar LangChain
- Configurar ambiente

**Fase 2: Primeiro Exemplo (45min)**
- Executar exemplo_langchain_basico.py
- Entender cada linha
- Comparar com código manual

**Fase 3: Prática Guiada (60min)**
- Completar exercícios
- Criar primeiro script próprio
- Testar diferentes LLMs

**Fase 4: Reflexão (15min)**
- Preencher journal
- Comparar abordagens
- Identificar vantagens

**Total:** 2h15min (dentro da faixa de 2h-2h30min)

---

## 📚 Recursos de Preparação

### O que revisar antes de começar:
- [ ] Estrutura de chamadas de API da Semana 1
- [ ] Como funcionam prompts (Dia 1-4 Semana 1)
- [ ] Tratamento de erros em Python
- [ ] Variáveis de ambiente (.env)

### Recursos úteis para ler:
- [LangChain Documentation](https://python.langchain.com/) - Documentação oficial
- [LangChain Quickstart](https://python.langchain.com/docs/get_started/introduction) - Guia rápido
- [LangChain Tutorials](https://python.langchain.com/docs/tutorials) - Tutoriais práticos
- [LangChain YouTube](https://www.youtube.com/@LangChain) - Vídeos oficiais

### Conceitos pré-requisitos:
- **Python básico/intermediário** - Já aprendido na Semana 1
- **APIs de IA** - Já usado na Semana 1
- **Prompts** - Já criados na Semana 1
- **Variáveis de ambiente** - Já configurado na Semana 1

---

## 💡 Dicas Importantes

1. **Comparação é chave:** Sempre compare código LangChain com código manual da Semana 1
2. **Comece simples:** Não tente aprender tudo de uma vez
3. **Pratique:** Execute exemplos e modifique para entender
4. **Documentação:** LangChain tem excelente documentação, use-a
5. **Paciência:** Framework tem curva de aprendizado, mas vale a pena

---

## ✅ Checklist de Preparação para Semana 2, Dia 1

Antes de começar a Semana 2, Dia 1, certifique-se de:

- [ ] Semana 1 está completa (todos os scripts funcionando)
- [ ] Repositório GitHub está atualizado
- [ ] Ambiente Python está configurado
- [ ] APIs estão funcionando (Groq, Gemini, Claude)
- [ ] Entendeu estrutura de chamadas de API da Semana 1
- [ ] Tem tempo dedicado para aprendizado (2h a 2h30min)

---

## 🔄 Transição Suave

A Semana 2 é uma **evolução natural** da Semana 1:

- **Semana 1:** Aprendemos a usar APIs diretamente (método manual, mais código)
- **Semana 2:** Aprendemos a usar LangChain (método profissional, menos código, mais poder)

**Não é começar do zero:** Todo conhecimento da Semana 1 será aplicado, apenas de forma mais eficiente.

---

## 📝 Notas Finais

A Semana 2 é uma oportunidade de:
- **Evoluir:** De scripts simples para aplicações profissionais
- **Aprender:** Framework usado pela indústria
- **Aplicar:** Conhecimentos da Semana 1 em contexto mais avançado
- **Preparar:** Base para projetos mais complexos nas semanas seguintes

É um passo importante, mas com base sólida da Semana 1, será uma transição suave.

---

**Última atualização:** 30 Nov 2025  
**Criado em:** Dia 7, Semana 1  
**Status:** ✅ Completo

