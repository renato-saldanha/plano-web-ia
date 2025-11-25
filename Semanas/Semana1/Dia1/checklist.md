# ✅ Checklist - Dia 1 (Segunda-feira, 24 Nov 2024)

## 🎯 Objetivo do Dia
Setup inicial das APIs de IA (Groq, Gemini, Claude) + Primeiro código "Hello AI"

---

## 📋 FASE 1: LEITURA E PLANEJAMENTO (45-60min)

### Leitura Inicial
- [ X] Ler `plano_desenvolvimento_2meses_v2.md` completo
- [ X] Entender as 8 semanas e expectativas REALISTAS (80% aderência)
- [ ] Escolher 1 das 4 opções de projeto final (ver plano, Semana 7)
- [ X] Mentalizar o compromisso de 2 meses

**Tempo estimado:** 45-60 minutos  
**Quando:** Durante almoço ou antes do jantar

---

## 🔧 FASE 2: SETUP TÉCNICO (70min - 17:20-18:30)

### Contas e APIs
- [ X] Criar conta Groq (GRÁTIS!) → [console.groq.com](https://console.groq.com)
  - [ X] Obter API key
  - [ X] Salvar em local seguro
- [ X] Criar conta Google AI Studio (Gemini - GRÁTIS) → [ai.google.dev](https://ai.google.dev)
  - [ X] Obter API key
  - [ X] Salvar em local seguro
- [ X] (Opcional) Criar conta Anthropic (Claude) → [console.anthropic.com](https://console.anthropic.com)
  - [ X] Obter API key ($5 grátis)
  - [ X] Salvar em local seguro

### Ambiente de Desenvolvimento
- [ X] Verificar Python instalado: `python --version` (deve ser 3.12+)
- [ X] Criar ambiente virtual: `python -m venv venv`
- [ X] Ativar venv:
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- [ X] Instalar dependências:
  ```bash
  pip install groq anthropic google-generativeai python-dotenv
  ```

### GitHub e Tracking
- [ X] Criar repositório GitHub "2-month-ai-journey-2025"
- [ X] Clonar ou inicializar git no projeto
- [ X] Instalar WakaTime (tracking automático) → [wakatime.com](https://wakatime.com)
  - [ X] Instalar extensão VS Code/Cursor
  - [X ] Configurar API key do WakaTime

### Organização
- [ X] Criar estrutura de pastas (já criada: Semanas/Semana1/Dia1/)
- [ X] Criar arquivo `.env` (usar `.env.example` como template)
- [ X] Adicionar `.env` ao `.gitignore`

**Tempo estimado:** 70 minutos  
**Quando:** 17:20-18:30

---

## 💻 FASE 3: PRIMEIRO CÓDIGO (60min - 19:00-20:00)

### Hello AI com Groq
- [ X] Abrir arquivo `hello_ai_groq.py`
- [ X] Configurar API key no `.env`:
  ```env
  GROQ_API_KEY=sua_chave_aqui
  ```
- [ X] Executar script: `python hello_ai_groq.py`
- [ X] Verificar resposta do Llama 3.2
- [ X] Testar com diferentes prompts

### Teste Básico
- [X] Modificar prompt no script
- [ X] Testar novamente
- [ X] Verificar tempo de resposta (Groq é ultra-rápido!)

### Git
- [ X] Adicionar arquivos: `git add .`
- [ X] Commit: `git commit -m "First AI integration with Groq - Hello AI 2025"`
- [ X] Push: `git push origin main`

**Tempo estimado:** 60 minutos  
**Quando:** 19:00-20:00

---

## 📝 FASE 4: FINALIZAÇÃO (30min - 20:00-20:30)

### Journal e Planejamento
- [ X] Abrir arquivo `journal.md`
- [ X] Preencher journal com o que fez hoje
- [ X] Anotar dificuldades encontradas
- [ X] Planejar 3 tarefas para amanhã (Terça-feira):

  **Seu planejamento:**  
  1. Criar arquivo `gerador_conteudo_blog.py` com função que recebe tema e gera parágrafo introdutório usando Groq API
  2. Testar script com 3 temas diferentes (ex: "IA", "Python", "Web Dev") e salvar resultados
  3. Adicionar tratamento de erros e mensagens informativas ao usuário
  
  *(Veja mais exemplos em: `EXEMPLOS_TAREFAS.md`)*

### Revisão
- [ X] Revisar código escrito hoje
- [ X] Verificar se tudo está funcionando
- [ X] Confirmar commit no GitHub

**Tempo estimado:** 30 minutos  
**Quando:** 20:00-20:30

---

## 🎉 CONCLUSÃO

**Total estimado:** 3-4 horas

### ✅ Critérios de Sucesso:
- [ X] Contas criadas (Groq, Gemini, opcional Claude)
- [ X] Ambiente Python configurado
- [ X] Primeiro script funcionando
- [ X] Commit feito no GitHub
- [ X] Journal preenchido
- [ X] WakaTime instalado

### 🎯 Streak: 1/56 dias

**Parabéns por completar o Dia 1!** 🚀

---

## 📚 Recursos Úteis
- Groq Docs: https://console.groq.com/docs
- Gemini Docs: https://ai.google.dev/docs
- Claude Docs: https://docs.anthropic.com
- Guia de setup: `setup_apis.md`

---

**Última atualização:** 24 Nov 2024

