# ✅ Checklist - Dia 4 (Quinta-feira, 27 Nov 2025)

## 🎯 Objetivo do Dia
Criar Script 3 - Resumidor de documentos PDF usando múltiplos LLMs (Groq, Gemini, Claude opcional)

---

## 📋 FASE 1: REVISÃO E PREPARAÇÃO (10min - 17:20-17:30)

### Revisão do Dia Anterior
- [ X] Abrir journal do Dia 3
- [ X] Revisar código `analisardor_sentimentos.py` do Dia 3
- [ X] Verificar se ambiente virtual está ativado
- [ X] Confirmar que `.env` está configurado com todas as API keys (GROQ_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY)

### Preparação
- [ X] Ler tarefas planejadas (já definidas no Dia 3):
    1. Criar script resumidor_pdf.py que recebe caminho de PDF e retorna resumo usando Groq
    2. Adicionar função para extrair texto de PDF (usar biblioteca PyPDF2 ou pdfplumber)
    3. Testar com 2-3 PDFs diferentes e salvar resumos em arquivos
- [ X] Definir objetivo do dia em 1 frase: "Criar resumidor de PDFs que usa múltiplos LLMs"
- [ ] Pesquisar sobre extração de texto de PDFs (5min - opcional)

**Tempo estimado:** 10 minutos  
**Quando:** 17:20-17:30

---

## 💻 FASE 2: DESENVOLVIMENTO (75min - 17:30-18:45)

### Tarefa 1: Instalar Biblioteca e Criar Script Base 
- [ X] Instalar biblioteca de extração de PDF: `pip install PyPDF2` ou `pip install pdfplumber`
- [ X] Criar arquivo `resumidor_pdf.py`
- [ X] Importar bibliotecas necessárias (groq, google.generativeai, anthropic, dotenv, os, PyPDF2/pdfplumber)
- [ X] Criar função `extrair_texto_pdf(caminho_pdf: str) -> str`
- [ X] Testar função de extração com 1 PDF simples
- [ X] Adicionar tratamento de erros para PDFs corrompidos ou protegidos

**Tempo estimado:** 25 minutos

### Tarefa 2: Implementar Resumo com Groq
- [ X] Criar função `resumir_com_groq(texto: str) -> str`
- [ X] Configurar cliente Groq (usar código dos dias anteriores como base)
- [ X] Criar prompt estruturado para resumo (definir tamanho: curto, médio ou longo)
- [ X] Testar função com texto extraído de 1 PDF
- [ X] Adicionar tratamento de erros
- [ X] Lidar com textos muito longos (dividir em chunks se necessário)

**Tempo estimado:** 30 minutos

### Tarefa 3: Adicionar Resumo com Gemini
- [ X] Criar função `resumir_com_gemini(texto: str) -> str`
- [ X] Configurar cliente Gemini (usar API key do .env)
- [ X] Criar prompt similar ao do Groq para resumo
- [ X] Testar função com mesmo PDF usado no Groq
- [ X] Adicionar tratamento de erros
- [ X] Lidar com textos muito longos (dividir em chunks se necessário)

**Tempo estimado:** 25 minutos

### Tarefa 4: Criar Função Principal e Comparação
- [ X] Criar função `resumir_pdf(caminho_pdf: str, llm: str = "groq") -> dict`
  - Extrai texto do PDF
  - Gera resumo com LLM escolhido
  - Retorna texto original, resumo e metadados
- [ X] Criar função `comparar_resumos(caminho_pdf: str) -> dict`
  - Gera resumo com múltiplos LLMs
  - Compara comprimento, qualidade (subjetiva)
  - Retorna comparação
- [ X] Criar função para salvar resumo em arquivo markdown
- [ X] Testar função completa com 1 PDF

**Tempo estimado:** 20 minutos

**Tempo total estimado:** 75 minutos  
**Quando:** 17:30-18:45

---

## 🍽️ PAUSA (18:45-19:00)

- [ X] Jantar/Descanso

---

## 📚 FASE 3: TESTES E COMPARAÇÃO (20min - 19:00-19:20)

### Testar com Múltiplos PDFs
- [ X] Criar pasta `pdfs/` e adicionar 2-3 PDFs de teste
- [ X] Testar script com PDF curto (1-2 páginas) usando Groq
- [ X] Testar script com PDF curto usando Gemini
- [ X] Testar script com PDF médio (5-10 páginas) usando ambos LLMs
- [ X] Executar função de comparação para todos os PDFs
- [ X] Verificar qualidade dos resumos gerados
- [ X] Anotar qual LLM gerou resumos melhores

### Salvar Resumos
- [ X] Criar pasta `resumos/`
- [ X] Criar função para salvar resumos em arquivos markdown
- [ X] Salvar resumos de todos os PDFs testados
- [ X] Adicionar metadados aos arquivos (data, LLM usado, tamanho original, tamanho resumo)

**Tempo estimado:** 20 minutos  
**Quando:** 19:00-19:20

---

## 📝 FASE 4: FINALIZAÇÃO (15min - 19:20-19:35)

### Git e Organização
- [ ] Adicionar arquivos: `git add .`
- [ ] Commit: `git commit -m "Dia 4: Resumidor de PDFs com múltiplos LLMs"`
- [ ] Push: `git push origin main`

### Journal e Planejamento
- [ ] Abrir arquivo `journal.md`
- [ ] Preencher journal com o que fez hoje
- [ ] Anotar dificuldades encontradas
- [ ] Anotar aprendizados sobre extração de PDFs e resumos
- [ ] Documentar qual LLM foi melhor para resumos
- [ ] Planejar 3 tarefas para amanhã (Sexta-feira - Refatoração + Documentação):

**Seu planejamento:**
1. Refatorar scripts dos dias anteriores (melhorar código, adicionar type hints)
2. Criar documentação completa (README principal, guias de uso)
3. Organizar estrutura de pastas e preparar para projeto integrado (Dia 6-7)

**Tempo estimado:** 15 minutos  
**Quando:** 19:20-19:35

---

## 🎉 CONCLUSÃO

**Total estimado:** 2 horas

### ✅ Critérios de Sucesso:
- [ ] Script `resumidor_pdf.py` criado e funcionando
- [ ] Extração de texto de PDF funcionando corretamente
- [ ] Resumo funciona com pelo menos 2 LLMs (Groq + Gemini)
- [ ] Testado com 2-3 PDFs diferentes
- [ ] Resumos salvos em arquivos markdown
- [ ] Comparação de resumos implementada
- [ ] Tratamento de erros implementado
- [ ] Commit feito no GitHub
- [ ] Journal preenchido

### 🎯 Streak: 4/56 dias

**Parabéns por completar o Dia 4!** 🚀

---

## 📚 Recursos Úteis
- Groq Docs: https://console.groq.com/docs
- Gemini Docs: https://ai.google.dev/docs
- Claude Docs: https://docs.anthropic.com
- PyPDF2 Docs: https://pypdf2.readthedocs.io/
- pdfplumber Docs: https://github.com/jsvine/pdfplumber
- Exemplo do Dia 1: `../Dia1/hello_ai_groq.py`
- Exemplo do Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Exemplo do Dia 3: `../Dia3/analisardor_sentimentos.py`

---

## 💡 Dicas

### Prompt para Resumo:
```
Resuma o seguinte texto de forma clara e concisa. O resumo deve:
- Capturar os pontos principais
- Manter informações importantes
- Ser objetivo e direto
- Tamanho: [curto/médio/longo]

Texto:
{texto}
```

### Estrutura do Arquivo de Resumo:
```markdown
# Resumo: [Nome do PDF]

**Data:** [Data]
**LLM usado:** [Groq/Gemini/Claude]
**Tamanho original:** [X palavras]
**Tamanho resumo:** [Y palavras]

## Resumo

[Resumo gerado aqui]

## Metadados
- Páginas: [N]
- Tempo de processamento: [X segundos]
```

### PDFs de Teste:
- Usar documentos públicos (artigos, relatórios)
- Criar PDFs simples de teste com texto próprio
- Testar com diferentes tamanhos (curto, médio, longo)

---

**Última atualização:** 27 Nov 2025

