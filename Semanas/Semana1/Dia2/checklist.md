# ✅ Checklist - Dia 2 (Terça-feira, 25 Nov 2025)

## 🎯 Objetivo do Dia
Criar Script 1 - Gerador de conteúdo para blog usando Groq API

---

## 📋 FASE 1: REVISÃO E PREPARAÇÃO (10min - 17:20-17:30)

### Revisão do Dia Anterior
- [ X] Abrir journal do Dia 1
- [ X] Revisar código `hello_ai_groq.py` do Dia 1
- [ X] Verificar se ambiente virtual está ativado
- [ X] Confirmar que `.env` está configurado com `GROQ_API_KEY`

### Preparação
- [ X] Ler tarefas planejadas (já definidas no Dia 1)
    1. Criar arquivo gerador_conteudo_blog.py com função que recebe tema e gera parágrafo introdutório usando Groq
    2. Testar script com 3 temas diferentes (ex: "Inteligência Artificial", "Python", "Web Development")
    3. Adicionar tratamento de erros e salvar resultado em arquivo .txt
- [ X] Definir objetivo do dia em 1 frase: "Criar script que gera conteúdo de blog"

**Tempo estimado:** 10 minutos  
**Quando:** 17:20-17:30

---

## 💻 FASE 2: DESENVOLVIMENTO (75min - 17:30-18:45)

### Tarefa 1: Criar Script Base
- [ X] Criar arquivo `gerador_conteudo_blog.py`
- [ X] Importar bibliotecas necessárias (groq, dotenv, os)
- [ X] Criar função `gerar_conteudo_blog(tema: str) -> str`
- [ X] Configurar cliente Groq (usar código do Dia 1 como base)
- [ X] Criar prompt estruturado para gerar parágrafo introdutório
- [ X] Testar função com 1 tema simples

**Tempo estimado:** 45 minutos

### Tarefa 2: Testar e Salvar Resultados
- [ X] Testar script com tema "Inteligência Artificial"
- [ X] Testar script com tema "Python para Iniciantes"
- [ X] Testar script com tema "Desenvolvimento Web Moderno"
- [ X] Criar função para salvar resultado em arquivo `.txt` ou `.md`
- [ X] Salvar os 3 resultados em arquivos separados
- [ X] Verificar qualidade do conteúdo gerado

**Tempo estimado:** 30 minutos

### Tarefa 3: Melhorias e Tratamento de Erros
- [ X] Adicionar tratamento de erros (try/except)
- [ X] Adicionar mensagens informativas ao usuário
- [ X] Adicionar validação de entrada (verificar se tema não está vazio)
- [ X] Melhorar prompt para gerar conteúdo mais estruturado
- [ X] Adicionar opção de escolher tamanho do conteúdo (curto/médio/longo) (feito limitando os tokens)

**Tempo estimado:** 15 minutos

**Tempo total estimado:** 75 minutos  
**Quando:** 17:30-18:45

---

## 🍽️ PAUSA (18:45-19:00)

- [ X] Jantar/Descanso

---

## 📚 FASE 3: APRENDIZADO E REFINAMENTO (20min - 19:00-19:20)

### Prompt Engineering
- [ X] Pesquisar sobre "Prompt Engineering para geração de conteúdo"
- [ X] Testar diferentes estruturas de prompt:
  - Prompt simples
  - Prompt com contexto
  - Prompt com exemplos (few-shot)
- [ X] Comparar resultados e escolher melhor abordagem

### Refinamento
- [ X] Ajustar prompt baseado no aprendizado(já tinha conhecimento da definiçaõ de persona, contexto e few shot e foi oq ue apliquei)
- [ X] Testar novamente com 1 tema
- [ X] Verificar se conteúdo melhorou

**Tempo estimado:** 20 minutos  
**Quando:** 19:00-19:20

---

## 📝 FASE 4: FINALIZAÇÃO (15min - 19:20-19:35)

### Git e Organização
- [ X] Adicionar arquivos: `git add .`
- [ X] Commit: `git commit -m "Dia 2: Gerador de conteúdo para blog funcionando"`
- [ X] Push: `git push origin main`

### Journal e Planejamento
- [ X] Abrir arquivo `journal.md`
- [ X] Preencher journal com o que fez hoje
- [ X] Anotar dificuldades encontradas
- [ X] Anotar aprendizados sobre prompt engineering
- [ X] Planejar 3 tarefas para amanhã (Quarta-feira - Analisador de sentimentos):
  

**Tempo estimado:** 15 minutos  
**Quando:** 19:20-19:35

---

## 🎉 CONCLUSÃO

**Total estimado:** 2 horas

### ✅ Critérios de Sucesso:
- [ X] Script `gerador_conteudo_blog.py` criado e funcionando
- [ X] Função gera parágrafo introdutório a partir de um tema
- [ X] Testado com 3 temas diferentes
- [ X] Resultados salvos em arquivos
- [ X] Tratamento de erros implementado
- [ X] Commit feito no GitHub
- [ X] Journal preenchido

### 🎯 Streak: 2/56 dias

**Parabéns por completar o Dia 2!** 🚀

---

## 📚 Recursos Úteis
- Groq Docs: https://console.groq.com/docs
- Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- Exemplo do Dia 1: `../Dia1/hello_ai_groq.py`

---

## 💡 Dicas

- **Prompt estruturado:** Use formato como "Escreva um parágrafo introdutório sobre [TEMA] para um blog. O parágrafo deve ser..."
- **Teste iterativamente:** Teste com 1 tema, ajuste prompt, teste novamente
- **Salve versões:** Salve diferentes versões do prompt para comparar resultados

---

**Última atualização:** 25 Nov 2025

