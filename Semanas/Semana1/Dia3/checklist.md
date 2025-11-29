# ✅ Checklist - Dia 3 (Quarta-feira, 26 Nov 2024)

## 🎯 Objetivo do Dia
Criar Script 2 - Analisador de sentimentos de reviews comparando múltiplos LLMs (Groq, Gemini, Claude opcional)

---

## 📋 FASE 1: REVISÃO E PREPARAÇÃO (15min - 17:20-17:35)

### Revisão do Dia Anterior
- [ X] Abrir journal do Dia 2
- [ X] Revisar código `gerador_conteudo_blog.py` do Dia 2
- [ X] Verificar se ambiente virtual está ativado
- [ X] Confirmar que `.env` está configurado com todas as API keys (GROQ_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY)

### Preparação
- [ X] Ler tarefas planejadas (já definidas no Dia 2):
    1. Criar script analisador_sentimentos.py que recebe texto e retorna sentimento (positivo/negativo/neutro) usando Groq
    2. Adicionar função para comparar resultado do Groq com Gemini (mesmo texto, 2 LLMs)
    3. Testar com 5 reviews diferentes e criar tabela comparativa dos resultados
- [ X] Definir objetivo do dia em 1 frase: "Criar analisador de sentimentos que compara múltiplos LLMs"
- [ ] Pesquisar sobre análise de sentimentos com IA (5min - opcional)

**Tempo estimado:** 15 minutos  
**Quando:** 17:20-17:35

---

## 💻 FASE 2: DESENVOLVIMENTO (90min - 17:35-19:05)

### Tarefa 1: Criar Script Base com Groq
- [ X] Criar arquivo `analisador_sentimentos.py`
- [ X] Importar bibliotecas necessárias (groq, google.generativeai, anthropic, dotenv, os)
- [ X] Criar função `analisar_sentimento_groq(texto: str) -> str`
- [ X] Configurar cliente Groq (usar código dos dias anteriores como base)
- [ X] Criar prompt estruturado para análise de sentimentos (retornar: positivo, negativo ou neutro)
- [ X] Testar função com 1 review simples
- [ X] Adicionar tratamento de erros

**Tempo estimado:** 30 minutos

### Tarefa 2: Adicionar Análise com Gemini
- [ X] Criar função `analisar_sentimento_gemini(texto: str) -> str`
- [ X] Configurar cliente Gemini (usar API key do .env)
- [ X] Criar prompt similar ao do Groq para análise de sentimentos
- [ X] Testar função com mesmo review usado no Groq
- [ X] Adicionar tratamento de erros

**Tempo estimado:** 25 minutos

### Tarefa 3: Adicionar Função de Comparação
- [ X] Criar função `comparar_analises(texto: str) -> dict`
  - Retorna sentimento de cada LLM
  - Retorna se há concordância entre eles
  - Retorna tempo de resposta de cada um
- [ X] Criar função para formatar resultado da comparação
- [ X] Testar função de comparação com 1 review

**Tempo estimado:** 20 minutos

### Tarefa 4: Criar Reviews de Teste
- [ X] Criar pasta `reviews_teste/`
- [ X] Criar arquivo `reviews.txt` com 5 reviews diferentes:
  1. Review positivo (ex: "Produto incrível!")
  2. Review negativo (ex: "Péssima qualidade!")
  3. Review neutro (ex: "É ok, nada especial")
  4. Review positivo detalhado
  5. Review negativo detalhado
- [ X] Criar função para ler reviews do arquivo

**Tempo estimado:** 15 minutos

**Tempo total estimado:** 90 minutos  
**Quando:** 17:35-19:05

---

## 🍽️ PAUSA (19:05-19:30)

- [ X] Jantar/Descanso

---

## 📚 FASE 3: TESTES E COMPARAÇÃO (30min - 19:30-20:00)

### Testar com Múltiplos Reviews
- [ X] Testar script com todos os 5 reviews usando Groq
- [ X] Testar script com todos os 5 reviews usando Gemini
- [ X] Executar função de comparação para todos os 5 reviews
- [ X] Verificar se há discordâncias entre os LLMs
- [ X] Anotar qual LLM foi mais rápido

### Criar Tabela Comparativa
- [ X] Criar pasta `resultado_comparacao/`
- [ X] Criar função para gerar tabela comparativa em markdown
- [ X] Gerar tabela com resultados de todos os reviews
- [ X] Adicionar métricas: tempo de resposta, tokens usados, concordância
- [ X] Salvar tabela em `resultado_comparacao/comparacao_llms.md`

**Tempo estimado:** 30 minutos  
**Quando:** 19:30-20:00

---

## 📝 FASE 4: FINALIZAÇÃO (30min - 20:00-20:30)

### Git e Organização
- [ X] Adicionar arquivos: `git add .`
- [ X] Commit: `git commit -m "Dia 3: Analisador de sentimentos com comparação de LLMs"`
- [ X] Push: `git push origin main`

### Journal e Planejamento
- [ X] Abrir arquivo `journal.md`
- [ X] Preencher journal com o que fez hoje
- [ X] Anotar dificuldades encontradas
- [ X] Anotar aprendizados sobre comparação de LLMs
- [ X] Documentar qual LLM foi melhor para análise de sentimentos
- [ X] Planejar 3 tarefas para amanhã (Quinta-feira - Resumidor de PDFs):

**Seu planejamento:**
1. Criar script resumidor_pdf.py que recebe caminho de PDF e retorna resumo usando Groq
2. Adicionar função para extrair texto de PDF (usar biblioteca PyPDF2 ou pdfplumber)
3. Testar com 2-3 PDFs diferentes e salvar resumos em arquivos

**Tempo estimado:** 30 minutos  
**Quando:** 20:00-20:30

---

## 🎉 CONCLUSÃO

**Total estimado:** 3 horas

### ✅ Critérios de Sucesso:
- [ X] Script `analisador_sentimentos.py` criado e funcionando
- [ X] Função de análise funciona com pelo menos 2 LLMs (Groq + Gemini)
- [ X] Testado com 5 reviews diferentes
- [ X] Tabela comparativa criada e salva em arquivo
- [ X] Comparação mostra concordância/discordância entre LLMs
- [ X] Tratamento de erros implementado
- [ X] Commit feito no GitHub
- [ X] Journal preenchido

### 🎯 Streak: 3/56 dias

**Parabéns por completar o Dia 3!** 🚀

---

## 📚 Recursos Úteis
- Groq Docs: https://console.groq.com/docs
- Gemini Docs: https://ai.google.dev/docs
- Claude Docs: https://docs.anthropic.com
- Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- Exemplo do Dia 1: `../Dia1/hello_ai_groq.py`
- Exemplo do Dia 2: `../Dia2/gerador_conteudo_blog.py`

---

## 💡 Dicas

### Prompt para Análise de Sentimentos:
```
Analise o sentimento do seguinte texto e retorne APENAS uma palavra: "positivo", "negativo" ou "neutro".

Texto: {texto}

Sentimento:
```

### Estrutura da Tabela Comparativa:
```markdown
| Review | Groq | Gemini | Claude | Concordância | Tempo Groq | Tempo Gemini |
|--------|------|--------|--------|--------------|------------|--------------|
| Review 1 | positivo | positivo | positivo | ✅ | 150ms | 200ms |
```

### Reviews de Exemplo:
- Positivo: "Este produto é incrível! Funciona perfeitamente."
- Negativo: "Péssima qualidade, não recomendo."
- Neutro: "O produto é ok, nada especial mas funciona."

---

**Última atualização:** 26 Nov 2025

