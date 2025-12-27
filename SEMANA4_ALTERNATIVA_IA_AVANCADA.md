# 🔄 Semana 4 - Alternativa: IA Avançada + Governança

**Substituição proposta:** Trocar Bun + Hono (JavaScript) por tópicos avançados de IA do plano DIO

---

## 🎯 **SEMANA 4 (16-22 Dez): IA Avançada + Governança + MLFlow**

### **Objetivos:**
- Explorar modelos open-source com Hugging Face
- Entender Transfer Learning e fine-tuning básico
- Implementar governança de IA (segurança, ética, compliance)
- Gerenciar ciclo de vida de modelos com MLFlow
- Aplicar estratégias de produtos digitais com IA

### **Justificativa da Substituição:**
- ✅ **Mais relevante para carreira em IA:** Hugging Face é padrão da indústria
- ✅ **Mantém foco em Python:** Não precisa aprender JavaScript/TypeScript
- ✅ **Conhecimento estratégico:** Governança é diferencial competitivo
- ✅ **Produção-ready:** MLFlow é essencial para ML em produção
- ✅ **Complementa Semana 3:** Aprofunda backend Python (FastAPI)

---

## 📅 **Sequência (7 sessões de ≤2h (120min)):**

### **Dia 1: Hugging Face - Fundamentos e Modelos**
**Duração:** 2h (120min)

**Objetivos:**
- Entender o ecossistema Hugging Face (Hub, Transformers, Datasets)
- Explorar modelos pré-treinados (BERT, GPT-2, T5)
- Carregar e usar modelos localmente

**Estrutura:**
- **Preparação (5min):** Revisar checklist e contexto
- **Leitura guiada (20min):** 
  - Hugging Face Documentation: "Getting Started"
  - Artigo: "Hugging Face Transformers em 2025"
- **Construção guiada (90min):**
  - Setup: `pip install transformers datasets accelerate`
  - Carregar modelo pré-treinado (ex: `distilbert-base-uncased`)
  - Pipeline de NLP (sentiment analysis, text classification)
  - Comparar com API de IA (Groq/Gemini) - quando usar cada um
- **Consolidação (20min):** Testes rápidos, documentar diferenças
- **Registro (15min):** Journal + próximos passos

**Entregáveis:**
- ✅ Script Python usando Hugging Face Transformers
- ✅ Comparação: Hugging Face vs APIs (quando usar cada um)
- ✅ Anotações sobre modelos disponíveis

**Recursos:**
- 🔗 [Hugging Face Docs](https://huggingface.co/docs/transformers)
- 🔗 [Hugging Face Hub](https://huggingface.co/models)
- 📺 YouTube: "Hugging Face Transformers Tutorial 2025"

---

### **Dia 2: Hugging Face - Fine-tuning Básico**
**Duração:** 2h (120min)

**Objetivos:**
- Entender conceitos de Transfer Learning
- Fine-tuning de modelo para tarefa específica
- Avaliar performance do modelo ajustado

**Estrutura:**
- **Preparação (5min):** Revisar código do Dia 1
- **Leitura guiada (20min):**
  - Artigo: "Transfer Learning em NLP: Guia Prático"
  - Hugging Face: "Fine-tuning Tutorial"
- **Construção guiada (90min):**
  - Preparar dataset customizado (ex: reviews de produtos)
  - Fine-tuning de modelo de sentimentos
  - Treinar modelo (usar GPU se disponível, senão CPU)
  - Avaliar métricas (accuracy, F1-score)
- **Consolidação (20min):** Comparar modelo original vs fine-tuned
- **Registro (15min):** Journal + documentar aprendizados

**Entregáveis:**
- ✅ Modelo fine-tuned funcional
- ✅ Script de treinamento documentado
- ✅ Métricas de avaliação

**Recursos:**
- 🔗 [Hugging Face Fine-tuning Guide](https://huggingface.co/docs/transformers/training)
- 🔗 [Hugging Face Datasets](https://huggingface.co/docs/datasets)
- 📺 YouTube: "Fine-tuning BERT Tutorial 2025"

---

### **Dia 3: Web Scraping + Preparação de Dados**
**Duração:** 2h (120min)

**Objetivos:**
- Coletar dados da web para treinamento
- Limpar e preparar dados para ML
- Criar pipeline de dados

**Estrutura:**
- **Preparação (5min):** Revisar conceitos de dados
- **Leitura guiada (20min):**
  - Artigo: "Web Scraping Ético com Python"
  - BeautifulSoup/Scrapy basics
- **Construção guiada (90min):**
  - Web scraping básico (BeautifulSoup ou Scrapy)
  - Limpeza de dados (remover HTML, normalizar texto)
  - Preparação para Hugging Face (formato Dataset)
  - Validação de qualidade dos dados
- **Consolidação (20min):** Testar pipeline completo
- **Registro (15min):** Journal + próximos passos

**Entregáveis:**
- ✅ Script de web scraping funcional
- ✅ Pipeline de preparação de dados
- ✅ Dataset limpo e pronto para uso

**Recursos:**
- 🔗 [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- 🔗 [Scrapy Documentation](https://scrapy.org/)
- 📺 YouTube: "Web Scraping Python Tutorial 2025"

---

### **Dia 4: Governança de IA - Fundamentos**
**Duração:** 2h (120min)

**Objetivos:**
- Entender princípios de governança de IA
- Implementar segurança básica (variáveis de ambiente, logging)
- Criar política de uso de IA

**Estrutura:**
- **Preparação (5min):** Revisar segurança da Semana 3
- **Leitura guiada (20min):**
  - Artigo: "Governança de IA: Guia Prático para Desenvolvedores"
  - Princípios: Transparência, Justiça, Privacidade, Segurança
- **Construção guiada (90min):**
  - Implementar logging de uso de IA (quem, quando, quanto)
  - Sistema de rate limiting por usuário (evitar abuso)
  - Política de retenção de dados (GDPR básico)
  - Documentação de decisões de IA (explicabilidade)
- **Consolidação (20min):** Testar sistema de governança
- **Registro (15min):** Journal + checklist de governança

**Entregáveis:**
- ✅ Sistema de logging de IA implementado
- ✅ Política de governança documentada
- ✅ Checklist de segurança e ética

**Recursos:**
- 🔗 [AI Governance Framework (Microsoft)](https://www.microsoft.com/en-us/ai/responsible-ai)
- 🔗 [GDPR para Desenvolvedores](https://gdpr.eu/)
- 📺 YouTube: "AI Governance for Developers 2025"

---

### **Dia 5: MLFlow - Gerenciamento de Modelos**
**Duração:** 2h (120min)

**Objetivos:**
- Entender ciclo de vida de modelos ML
- Implementar tracking de experimentos com MLFlow
- Versionar modelos e métricas

**Estrutura:**
- **Preparação (5min):** Revisar modelo do Dia 2
- **Leitura guiada (20min):**
  - MLFlow Documentation: "Getting Started"
  - Artigo: "MLOps Básico com MLFlow"
- **Construção guiada (90min):**
  - Setup: `pip install mlflow`
  - Integrar MLFlow no pipeline de treinamento (Dia 2)
  - Logging de métricas, parâmetros, artefatos
  - Registrar modelo no MLFlow Model Registry
  - Interface web do MLFlow (visualizar experimentos)
- **Consolidação (20min):** Comparar versões de modelos
- **Registro (15min):** Journal + próximos passos

**Entregáveis:**
- ✅ Pipeline de treinamento com MLFlow integrado
- ✅ Modelo versionado no MLFlow
- ✅ Dashboard de experimentos funcionando

**Recursos:**
- 🔗 [MLFlow Documentation](https://mlflow.org/docs/latest/index.html)
- 🔗 [MLFlow Tutorials](https://mlflow.org/docs/latest/tutorials-and-examples/index.html)
- 📺 YouTube: "MLFlow Tutorial Python 2025"

---

### **Dia 6: Estratégias em Produtos Digitais com IA**
**Duração:** 2h (120min)

**Objetivos:**
- Entender como aplicar IA em produtos reais
- Criar estratégia de produto com IA
- Definir métricas de sucesso

**Estrutura:**
- **Preparação (5min):** Revisar projetos anteriores
- **Leitura guiada (20min):**
  - Artigo: "IA em Produtos Digitais: Estratégias Práticas"
  - Case studies: ChatGPT, GitHub Copilot, Notion AI
- **Construção guiada (90min):**
  - Análise de produto existente (escolher 1 dos 4 da Semana 7)
  - Definir features de IA (quais adicionar valor real)
  - Estratégia de custos (quando usar Hugging Face vs APIs)
  - Métricas de sucesso (engagement, accuracy, custo)
  - Roadmap de implementação
- **Consolidação (20min):** Validar estratégia
- **Registro (15min):** Journal + estratégia documentada

**Entregáveis:**
- ✅ Estratégia de produto com IA documentada
- ✅ Análise de custos (Hugging Face vs APIs)
- ✅ Roadmap de features

**Recursos:**
- 🔗 [Product Strategy with AI (a16z)](https://a16z.com/tag/ai/)
- 📺 YouTube: "AI Product Strategy 2025"
- 📚 Livro: "The AI Product Manager's Handbook"

---

### **Dia 7: Integração e Projeto Consolidado**
**Duração:** 2h (120min)

**Objetivos:**
- Integrar todos os conceitos da semana
- Criar projeto demonstrativo
- Documentar aprendizados

**Estrutura:**
- **Preparação (5min):** Revisar toda a semana
- **Leitura guiada (15min):** Revisar documentação criada
- **Construção guiada (90min):**
  - Projeto: "Sistema de Análise de Sentimentos com Fine-tuning"
    - Web scraping de reviews
    - Fine-tuning de modelo Hugging Face
    - Tracking com MLFlow
    - API FastAPI integrando modelo
    - Governança (logging, rate limiting)
  - Deploy modelo no Hugging Face Hub (opcional)
- **Consolidação (20min):** Testes end-to-end
- **Registro (20min):** 
  - Journal completo da semana
  - README do projeto
  - Artigo curto: "Hugging Face vs APIs: Quando Usar Cada Um"

**Entregáveis:**
- ✅ Projeto completo integrando todos os conceitos
- ✅ README documentado
- ✅ Artigo técnico publicado (Dev.to ou LinkedIn)

**Recursos:**
- 🔗 [Hugging Face Model Hub](https://huggingface.co/models)
- 🔗 [MLFlow Model Serving](https://mlflow.org/docs/latest/models.html)

---

## 📊 **Comparação: Semana 4 Original vs Alternativa**

| **Aspecto** | **Original (Bun + Hono)** | **Alternativa (IA Avançada)** |
|-------------|---------------------------|-------------------------------|
| **Linguagem** | JavaScript/TypeScript | Python (mantém consistência) |
| **Foco** | Performance backend | IA + Governança + MLOps |
| **Relevância Carreira** | Opcional (já tem FastAPI) | **Alto** (diferencial competitivo) |
| **Complexidade** | Média (nova linguagem) | Média-Alta (conceitos avançados) |
| **Aplicabilidade** | Comparação de stacks | **Direto em produção** |
| **Alinhamento DIO** | ❌ Não | ✅ **Sim (Nível 2-3)** |

---

## ✅ **Vantagens da Substituição:**

1. **✅ Mantém foco em Python:**
   - Não precisa aprender JavaScript/TypeScript
   - Aproveita conhecimento da Semana 3 (FastAPI)

2. **✅ Mais relevante para IA:**
   - Hugging Face é padrão da indústria
   - Transfer Learning é conhecimento essencial

3. **✅ Diferencial competitivo:**
   - Governança de IA é raro em desenvolvedores
   - MLFlow é essencial para ML em produção

4. **✅ Complementa projeto final:**
   - Conhecimento aplicável na Semana 7-8
   - Estratégia de produtos ajuda na escolha

5. **✅ Alinhado com plano DIO:**
   - Cobre Nível 2 (Hugging Face, Transfer Learning)
   - Cobre Nível 3 (Governança, Estratégias, MLFlow)

---

## ⚠️ **Considerações:**

### **Desvantagens:**
- ❌ Perde comparação FastAPI vs Bun (mas não é essencial)
- ❌ Não aprende JavaScript/TypeScript (mas pode aprender depois)
- ⚠️ Mais conceitos teóricos (mas com prática)

### **Mitigações:**
- ✅ FastAPI já cobre backend Python (suficiente)
- ✅ JavaScript pode ser aprendido depois (não é crítico)
- ✅ Todos os conceitos têm prática (não é só teoria)

---

## 🎯 **Métricas de Sucesso (Semana 4 Alternativa):**

- ✅ Modelo Hugging Face fine-tuned funcionando
- ✅ Pipeline de dados (web scraping + preparação)
- ✅ Sistema de governança implementado
- ✅ MLFlow tracking configurado
- ✅ Estratégia de produto documentada
- ✅ Projeto integrado completo
- ✅ Artigo técnico publicado

---

## 📚 **Recursos Adicionais:**

### **Hugging Face:**
- 🔗 [Transformers Library](https://huggingface.co/docs/transformers)
- 🔗 [Hugging Face Course](https://huggingface.co/learn/nlp-course) (GRATUITO!)
- 🔗 [Model Hub](https://huggingface.co/models)

### **MLFlow:**
- 🔗 [MLFlow Documentation](https://mlflow.org/docs/latest/index.html)
- 🔗 [MLFlow Examples](https://github.com/mlflow/mlflow-examples)

### **Governança:**
- 🔗 [Responsible AI (Microsoft)](https://www.microsoft.com/en-us/ai/responsible-ai)
- 🔗 [AI Ethics Guidelines](https://www.partnershiponai.org/)

---

## 🚀 **Próximos Passos:**

1. [ ] Revisar proposta e aprovar substituição
2. [ ] Criar estrutura de arquivos para Semana 4
3. [ ] Preparar templates e exemplos
4. [ ] Atualizar `1-Plano_Desenvolvimento.md` com alternativa
5. [ ] Começar Dia 1 (Hugging Face Fundamentos)

---

**Última atualização:** 2025  
**Status:** 📝 Proposta para aprovação

