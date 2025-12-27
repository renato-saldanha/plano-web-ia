# 🎯 Contexto para Construir a Semana 4 - Dia 1

## 📚 O que aprendemos hoje (Dia 7 - Semana 3)

### Conceitos Principais
- **Swagger/OpenAPI:** Documentação interativa automática gerada pelo FastAPI
- **Metadados OpenAPI:** Configuração de title, description, version, contact, license
- **Tags:** Organização de endpoints em grupos no Swagger UI
- **Descrições e Exemplos:** Melhorar documentação com Field(description) e Field(example)
- **Deploy em Produção:** Publicar API em plataformas cloud (Railway/Render)
- **Smoke Tests:** Testes básicos para validar API em produção
- **Variáveis de Ambiente:** Configuração segura de secrets em produção

### Habilidades Desenvolvidas
- Configurar documentação OpenAPI completa no FastAPI
- Personalizar Swagger UI com metadados e tags
- Adicionar descrições e exemplos aos modelos Pydantic
- Criar checklist completo de deploy
- Fazer deploy de API Python em produção (Railway/Render)
- Executar smoke tests para validar deploy
- Documentar URL de produção e endpoints

### Código Criado
- `template.py` - API com configuração Swagger completa
- `exemplo_referencia.py` - Código completo com todos os metadados OpenAPI
- Documentação Swagger acessível em `/docs`
- API em produção com URL pública

---

## 🔗 Por que a Semana 4 é importante

A Semana 3 consolidou o aprendizado de backend com **FastAPI (Python)**. A Semana 4 aprofunda em **IA Avançada + Governança + MLFlow (Python)**.

### Evolução do Aprendizado
- **Semana 3:** Backend em Python (FastAPI) - robusto, maduro, amplamente usado
- **Semana 4:** IA Avançada (Hugging Face, MLFlow, Governança) - aprofundamento em IA
- **Resultado:** Conhecimento avançado em IA aplicada, diferencial competitivo

### O que será aprendido na Semana 4
- **Hugging Face:** Modelos open-source, padrão da indústria
- **Transfer Learning:** Fine-tuning de modelos
- **Governança de IA:** Segurança, ética, compliance
- **MLFlow:** Gerenciamento de ciclo de vida de modelos
- **Estratégias:** Aplicar IA em produtos digitais

---

## 🎯 O que será feito na Semana 4 - Dia 1

### Objetivo Principal
Hugging Face - Fundamentos e Modelos (carregar e usar modelos pré-treinados)

### Conceitos que serão aprendidos
- Ecossistema Hugging Face (Hub, Transformers, Datasets)
- Modelos pré-treinados (BERT, GPT-2, T5)
- Carregar e usar modelos localmente
- Comparação: Hugging Face vs APIs (quando usar cada um)

### Nível de Scaffolding
**Nível 1** (conceito completamente novo)

### Consultar
**OBRIGATÓRIO:** `1-Plano_Desenvolvimento.md` seção "SEMANA 4" para detalhes completos

### Como se relaciona com Dia 7
- Aprendemos a criar API Python com FastAPI
- Agora vamos aprofundar em IA: modelos open-source, fine-tuning, governança
- Conhecimento aplicável diretamente no projeto final (Semana 7-8)

---

## 📋 Como Construir a Semana 4 - Dia 1

### ⚠️ OBRIGATÓRIO: Consultar documentação

1. **Consultar `1-Plano_Desenvolvimento.md` seção "SEMANA 4"** para estrutura completa
2. **Seguir estrutura abaixo**

### 1. Criar Estrutura Básica
```
Semana4/
├── Dia1/
│   ├── README.md
│   ├── CONTEXTO_AGENTE.md
│   ├── checklist.md
│   ├── journal.md
│   ├── requirements.txt (transformers, datasets, accelerate)
│   ├── CONTEXTO_PROXIMO_DIA.md
│   ├── exemplo_completo.py (Nível 1 - conceito novo)
│   └── GUIA_PASSO_A_PASSO.md (tutorial Hugging Face detalhado)
```
**Consultar `1-Plano_Desenvolvimento.md` seção "SEMANA 4" para:**
- Níveis de scaffolding pré-definidos (Dia 1: Nível 1)
- Estrutura de tempo detalhada (120min: 5+15+60+20+15+5)
- Objetivos e entregáveis específicos
- Recursos e referências

**Ordem sugerida:**
1. Criar pasta `Semana4/Dia1/`
2. Copiar templates de `TEMPLATE_ESTRUTURA_DIA.md` na raiz
3. **Se Opção B:** Consultar `SEMANA4_ALTERNATIVA_CORRIGIDA.md` para detalhes
4. Preencher README.md com contexto específico da Semana 4
5. Criar CONTEXTO_AGENTE.md
5. Criar checklist.md detalhado

**Como fazer:**
- Consultar `TEMPLATE_ESTRUTURA_DIA.md` para estrutura completa
- Adaptar templates para contexto TypeScript/JavaScript
- Manter consistência com Semana 3, mas adaptando para nova stack
- Garantir que o dia inteiro caiba em **160min**, incluindo leitura, execução e preenchimento de docs

**Por que:**
Estrutura consistente facilita navegação e aprendizado, mesmo mudando de linguagem.

---

### 2. Definir Nível de Scaffolding

**Nível recomendado:** **1** (Iniciante)

**Justificativa:**
- **Conceito novo:** Hugging Face é primeira exposição a modelos open-source
- **Contexto novo:** Transfer Learning e fine-tuning (conceitos novos)
- **Primeira vez:** Trabalhar com modelos pré-treinados localmente

**Arquivos necessários (Nível 1):**
- `exemplo_completo.py` - Código completo comentado linha por linha
- `GUIA_PASSO_A_PASSO.md` - Tutorial muito detalhado sobre Hugging Face
- Consultar `1-Plano_Desenvolvimento.md` seção "SEMANA 4" para estrutura completa

**Como fazer:**
- Consultar `METODOLOGIA_ENSINO.md` para entender níveis
- Verificar que conceitos completamente novos sempre começam no Nível 1
- Garantir que exemplo_completo.ts tenha explicações detalhadas

**Por que:**
Nível adequado garante aprendizado efetivo sem sobrecarga. Conceito novo = Nível 1.

---

### 3. Criar Arquivos de Aprendizado

**⚠️ OBRIGATÓRIO:** Consultar `SEMANA4_ALTERNATIVA_CORRIGIDA.md` para estrutura completa de arquivos.

#### exemplo_completo.py (Nível 1)
**Estrutura sugerida:**
```python
# SEÇÃO 1: IMPORTS
# transformers, datasets, accelerate

# SEÇÃO 2: CARREGAR MODELO
# Usar pipeline do Hugging Face

# SEÇÃO 3: USAR MODELO
# Exemplos práticos (sentiment analysis, text classification)

# SEÇÃO 4: COMPARAR COM APIs
# Quando usar Hugging Face vs APIs (Groq/Gemini)
```

**Explicações detalhadas:**
- Cada linha deve ter comentário explicando o que faz
- Comparações com APIs de IA (quando usar cada um)
- Explicar vantagens de modelos locais vs APIs

#### GUIA_PASSO_A_PASSO.md
**Conteúdo sugerido:**
1. **Introdução ao Hugging Face**
   - O que é Hugging Face
   - Ecossistema (Hub, Transformers, Datasets)
   - Por que usar modelos open-source
   - Comparação com APIs pagas

2. **Modelos Pré-treinados**
   - BERT, GPT-2, T5
   - Como escolher modelo adequado
   - Carregar modelos do Hub

3. **Pipelines de NLP**
   - Sentiment analysis
   - Text classification
   - Question answering

4. **Primeiro Uso**
   - Instalar transformers
   - Carregar modelo simples
   - Fazer primeira predição

---

### 4. Criar Checklist Detalhado

**⚠️ IMPORTANTE: Tempo Padronizado**

**Fases (total 120min):**
- **Preparação (5min):** Revisar Semana 3, entender objetivo da Semana 4
- **Leitura guiada (15min):** Ler GUIA_PASSO_A_PASSO.md sobre Hugging Face
- **Construção guiada (60min):** 
  - Instalar transformers, datasets, accelerate
  - Carregar modelo pré-treinado
  - Usar pipeline de NLP
  - Comparar com APIs (Groq/Gemini)
- **Consolidação (20min):** Testar modelo, documentar diferenças
- **Registro/handoff (15min):** Preencher journal e CONTEXTO_PROXIMO_DIA
- **Buffer (5min):** Resolver bloqueios

**Referências:**
- Hugging Face Documentation: https://huggingface.co/docs/transformers
- Hugging Face Hub: https://huggingface.co/models
- Consultar `SEMANA4_ALTERNATIVA_CORRIGIDA.md` para detalhes completos

---

## 📚 Recursos de Preparação

### O que revisar antes de começar:
- [ ] Semana 1-2 (integração com APIs de IA) - para comparar
- [ ] Semana 3 (backend FastAPI) - para entender contexto
- [ ] Conceitos básicos de Python e ML (se necessário)

### Recursos úteis para ler:
- [Hugging Face Documentation](https://huggingface.co/docs/transformers) - Introdução ao Hugging Face
- [Hugging Face Hub](https://huggingface.co/models) - Explorar modelos disponíveis
- [1-Plano_Desenvolvimento.md](../../1-Plano_Desenvolvimento.md) seção "SEMANA 4" - Estrutura completa
- YouTube: "Hugging Face Transformers Tutorial 2025"

### Conceitos pré-requisitos:
- **Python básico:** Variáveis, funções, imports (já consolidado)
- **APIs de IA:** Entender uso de LLMs (já aprendido na Semana 1-2)
- **Machine Learning básico:** Conceitos de modelos e predição (será aprendido)

---

## 💡 Dicas Importantes

1. **Comparação constante:** Sempre comparar com APIs de IA da Semana 1-2
2. **Modelos locais vs APIs:** Entender quando usar cada um
3. **Foco em conceitos:** Transfer Learning, fine-tuning, embeddings
4. **Python mantido:** Continuar usando Python (sem mudar linguagem)
5. **Tempo:** Respeitar 120min (leitura/testes/docs inclusos)

---

## ✅ Checklist de Preparação para Semana 4 - Dia 1

Antes de começar, certifique-se de:

- [ ] Semana 3 está completa (Dia 7 concluído)
- [ ] API FastAPI está em produção e funcionando
- [ ] Entende uso de APIs de IA (já aprendido na Semana 1-2)
- [ ] Tem Python 3.12 instalado e funcionando
- [ ] Tem pip funcionando para instalar pacotes
- [ ] Regra dos 120min confirmada

---

## 🔄 Transição Suave

A Semana 4 é uma **expansão natural** do aprendizado em IA:

- **Semana 1-2:** APIs de IA (Groq, Gemini, Claude) - uso de LLMs via API ✅
- **Semana 3:** Backend Python (FastAPI) - API completa e em produção ✅
- **Semana 4:** IA Avançada (Hugging Face, MLFlow, Governança) - aprofundamento em IA

O objetivo é **aprender modelos open-source** e **governança**:
- Quando usar modelos locais vs APIs?
- Como fazer fine-tuning?
- Como gerenciar ciclo de vida de modelos?

---

## 📝 Notas Finais

A Semana 4 é uma oportunidade de:
- **Aprender modelos open-source:** Hugging Face é padrão da indústria
- **Aprofundar em IA:** Transfer Learning, fine-tuning, governança
- **Diferencial competitivo:** Governança de IA é conhecimento raro e valioso
- **Aplicar em produção:** MLFlow para gerenciar modelos em produção

---

**Última atualização:** 15 Dez 2025  
**Criado em:** Dia 7 - Semana 3

