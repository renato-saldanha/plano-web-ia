# ✅ Checklist - Dia 1 (Terça-feira, 25 Nov 2024)

## 🎯 Objetivo do Dia
Setup inicial das APIs de IA (Groq, Gemini, Claude) + Primeiro código "Hello AI"

---

## 📋 FASE 1: LEITURA E PLANEJAMENTO (45-60min)

### Leitura Inicial
- [ ] Ler `plano_desenvolvimento_2meses_v2.md` completo
- [ ] Entender as 8 semanas e expectativas REALISTAS (80% aderência)
- [ ] Escolher 1 das 4 opções de projeto final (ver plano, Semana 7)
- [ ] Mentalizar o compromisso de 2 meses

**Tempo estimado:** 45-60 minutos  
**Quando:** Durante almoço ou antes do jantar

---

## 🔧 FASE 2: SETUP TÉCNICO (70min - 17:20-18:30)

### Contas e APIs
- [ ] Criar conta Groq (GRÁTIS!) → [console.groq.com](https://console.groq.com)
  - [ ] Obter API key
  - [ ] Salvar em local seguro
- [ ] Criar conta Google AI Studio (Gemini - GRÁTIS) → [ai.google.dev](https://ai.google.dev)
  - [ ] Obter API key
  - [ ] Salvar em local seguro
- [ ] (Opcional) Criar conta Anthropic (Claude) → [console.anthropic.com](https://console.anthropic.com)
  - [ ] Obter API key ($5 grátis)
  - [ ] Salvar em local seguro

### Ambiente de Desenvolvimento
- [ ] Verificar Python instalado: `python --version` (deve ser 3.12+)
- [ ] Criar ambiente virtual: `python -m venv venv`
- [ ] Ativar venv:
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- [ ] Instalar dependências:
  ```bash
  pip install groq anthropic google-generativeai python-dotenv
  ```

### GitHub e Tracking
- [ ] Criar repositório GitHub "2-month-ai-journey-2025"
- [ ] Clonar ou inicializar git no projeto
- [ ] Instalar WakaTime (tracking automático) → [wakatime.com](https://wakatime.com)
  - [ ] Instalar extensão VS Code/Cursor
  - [ ] Configurar API key do WakaTime

### Organização
- [ ] Criar estrutura de pastas (já criada: Semanas/Semana1/Dia1/)
- [ ] Criar arquivo `.env` (usar `.env.example` como template)
- [ ] Adicionar `.env` ao `.gitignore`

**Tempo estimado:** 70 minutos  
**Quando:** 17:20-18:30

---

## 💻 FASE 3: PRIMEIRO CÓDIGO (60min - 19:00-20:00)

### Hello AI com Groq
- [ ] Abrir arquivo `hello_ai_groq.py`
- [ ] Configurar API key no `.env`:
  ```env
  GROQ_API_KEY=sua_chave_aqui
  ```
- [ ] Executar script: `python hello_ai_groq.py`
- [ ] Verificar resposta do Llama 3.2
- [ ] Testar com diferentes prompts

### Teste Básico
- [ ] Modificar prompt no script
- [ ] Testar novamente
- [ ] Verificar tempo de resposta (Groq é ultra-rápido!)

### Git
- [ ] Adicionar arquivos: `git add .`
- [ ] Commit: `git commit -m "First AI integration with Groq - Hello AI 2025"`
- [ ] Push: `git push origin main`

**Tempo estimado:** 60 minutos  
**Quando:** 19:00-20:00

---

## 📝 FASE 4: FINALIZAÇÃO (30min - 20:00-20:30)

### Journal e Planejamento
- [ ] Abrir arquivo `journal.md`
- [ ] Preencher journal com o que fez hoje
- [ ] Anotar dificuldades encontradas
- [ ] Planejar 3 tarefas para amanhã (Quarta-feira):
  1. 
  2. 
  3. 

### Revisão
- [ ] Revisar código escrito hoje
- [ ] Verificar se tudo está funcionando
- [ ] Confirmar commit no GitHub

**Tempo estimado:** 30 minutos  
**Quando:** 20:00-20:30

---

## 🎉 CONCLUSÃO

**Total estimado:** 3-4 horas

### ✅ Critérios de Sucesso:
- [ ] Contas criadas (Groq, Gemini, opcional Claude)
- [ ] Ambiente Python configurado
- [ ] Primeiro script funcionando
- [ ] Commit feito no GitHub
- [ ] Journal preenchido
- [ ] WakaTime instalado

### 🎯 Streak: 1/56 dias

**Parabéns por completar o Dia 1!** 🚀

---

## 📚 Recursos Úteis
- Groq Docs: https://console.groq.com/docs
- Gemini Docs: https://ai.google.dev/docs
- Claude Docs: https://docs.anthropic.com
- Guia de setup: `setup_apis.md`

---

**Última atualização:** 25 Nov 2024

