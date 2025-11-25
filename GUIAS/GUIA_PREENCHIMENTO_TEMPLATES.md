# 📖 Guia Prático: Como Preencher os Templates de Acompanhamento

Este guia te ajudará a preencher corretamente todos os templates do arquivo `templates_acompanhamento.md`.

---

## 📅 1. JOURNAL DIÁRIO - Como Preencher

### Quando usar?
**TODO DIA**, ao final da sua sessão de estudo (20:00-20:30). Leva apenas 10-15 minutos!

### Estrutura e Exemplos:

#### ⏰ Horário de Estudo
```
- Início: 17:30
- Fim: 20:30
- Total: 3 horas
```
**Dica:** Se você estudou em blocos (ex: 17:30-18:30 e 19:00-20:00), some os períodos.

**Exemplo real:**
```
- Início: 17:45 (cheguei atrasado)
- Fim: 20:15 (parei um pouco antes)
- Total: 2h30min
```

---

#### ✅ Realizações do Dia
**O que colocar aqui?**
- Tarefas concluídas (mesmo que pequenas!)
- Features implementadas
- Bugs resolvidos
- Tutoriais completados
- Commits feitos

**Exemplo real (Dia 1):**
```
- [x] Criei conta Groq e obtive API key
- [x] Configurei ambiente Python com venv
- [x] Escrevi primeiro script "hello_ai_groq.py"
- [x] Testei integração com Llama 3.2 (funcionou!)
- [x] Fiz primeiro commit no GitHub
```

**Exemplo real (Dia 5):**
```
- [x] Implementei endpoint /api/generate com streaming
- [x] Resolvi bug de encoding UTF-8 nas respostas
- [x] Adicionei tratamento de erros para API rate limit
- [x] Escrevi testes para 2 endpoints
- [x] Atualizei documentação Swagger
```

**⚠️ IMPORTANTE:** Marque com `[x]` apenas o que REALMENTE completou. Seja honesto!

---

#### 🧠 O que Aprendi Hoje
**O que colocar aqui?**
- Conceitos novos que você não sabia antes
- Tecnologias/ferramentas que descobriu
- Insights importantes (ex: "Groq é 10x mais rápido que OpenAI")
- Qual LLM usou e POR QUÊ escolheu ele

**Exemplo real (Dia 1):**
```
- **Conceito novo:** Tokens são unidades de texto que LLMs processam. 1 token ≈ 4 caracteres.
- **Tecnologia/Ferramenta:** Groq - API gratuita e ultra-rápida para Llama 3.2
- **Insight importante:** Groq é melhor para testes rápidos (gratuito), GPT-4 é melhor para qualidade final
- **LLM usado:** Groq (Llama 3.2) - escolhi porque é gratuito e rápido para aprender
```

**Exemplo real (Dia 10):**
```
- **Conceito novo:** RAG (Retrieval Augmented Generation) - buscar contexto relevante antes de gerar resposta
- **Tecnologia/Ferramenta:** ChromaDB - vector database local e gratuita
- **Insight importante:** Embeddings transformam texto em números que preservam significado semântico
- **LLM usado:** Claude 3.5 Sonnet - melhor para análise de documentos longos que GPT-4
```

---

#### 💻 Código Escrito
**O que colocar aqui?**
- Nome do projeto/tarefa
- Estimativa de linhas (não precisa ser exato, pode contar arquivos)
- Quantos commits fez
- Link do repositório GitHub
- Horas do WakaTime (se instalou)

**Exemplo real:**
```
- **Projeto:** CLI Automações com IA (semana-01-cli-ia)
- **Linhas de código:** ~350 linhas (3 arquivos Python)
- **Commits:** 5 commits hoje
- **Link GitHub:** https://github.com/seu-usuario/2-month-ai-journey-2025/tree/main/semana-01-cli-ia
- **WakaTime:** 2h45min (tracking automático)
```

**Dica:** Não se preocupe em contar linhas exatas. Uma estimativa é suficiente!

---

#### ❌ Dificuldades Enfrentadas
**O que colocar aqui?**
- Problemas técnicos que travou
- Tempo que perdeu tentando resolver
- Como resolveu (ou se ainda não resolveu)

**Exemplo real:**
```
- **Problema:** Erro "ModuleNotFoundError: No module named 'groq'" mesmo após pip install
- **Tempo perdido:** 45 minutos
- **Como resolvi (ou não):** Descobri que estava usando venv errado. Ativei o venv correto e funcionou.
```

**Exemplo real (problema não resolvido):**
```
- **Problema:** Streaming de respostas não funciona no frontend (NextJS)
- **Tempo perdido:** 1h30min
- **Como resolvi (ou não):** Ainda não resolvi. Vou pesquisar amanhã sobre Vercel AI SDK streaming.
```

**⚠️ IMPORTANTE:** Anotar dificuldades ajuda a não repetir erros e a ver progresso!

---

#### 🔍 Recursos Utilizados
**O que colocar aqui?**
- Documentação oficial que consultou
- Tutoriais/vídeos que assistiu
- Artigos que leu
- Perguntas que fez em comunidades

**Exemplo real:**
```
- [x] Documentação: Groq API Docs (https://console.groq.com/docs)
- [x] Tutorial/Vídeo: "Groq vs OpenAI Speed Test" - Fireship (YouTube)
- [x] Artigo: "Prompt Engineering Guide" - OpenAI Cookbook
- [x] Comunidade: Perguntei no Discord Rocketseat sobre rate limits
```

---

#### 🎯 Plano para Amanhã
**O que colocar aqui?**
- 3 tarefas específicas e realizáveis
- Seja específico (não "estudar IA", mas "implementar endpoint /api/chat")

**Exemplo real:**
```
1. Implementar autenticação JWT no FastAPI
2. Criar endpoint /api/chat com histórico de mensagens
3. Assistir tutorial "FastAPI Authentication" (30min)
```

**Dica:** Escreva isso ANTES de dormir. Seu cérebro vai processar durante a noite!

---

#### 💭 Reflexão
**O que colocar aqui?**
- Avalie honestamente como se sentiu (1-10)
- Não precisa ser sempre 10! Dias difíceis são normais.

**Exemplo real (dia bom):**
```
**Como me senti hoje?** (1-10): 8
**Energia após trabalho:** 6 (cansado, mas consegui estudar)
**Foco durante estudo:** 7 (algumas distrações, mas produtivo)
**Motivação:** 9 (empolgado com o progresso!)
```

**Exemplo real (dia difícil):**
```
**Como me senti hoje?** (1-10): 4
**Energia após trabalho:** 3 (muito cansado)
**Foco durante estudo:** 5 (difícil concentrar)
**Motivação:** 6 (travou em bug, frustrante)
```

**⚠️ IMPORTANTE:** Dias difíceis são NORMAIS! O importante é continuar.

---

#### 🤖 Uso de IA (Novo 2025)
**O que colocar aqui?**
- Se usou Cursor/Copilot
- Se você tomou decisões (piloto) ou só seguiu sugestões (copiloto)
- Se revisou código gerado
- Se aprendeu ou só copiou

**Exemplo real (bom uso):**
```
**Usei Cursor/Copilot?** Sim
**Fui copiloto ou piloto?** Piloto - decidi usar FastAPI, Cursor só ajudou com sintaxe
**Code review do código gerado:** Sim - refatorei 3 funções que Cursor gerou
**Aprendi conceitos ou apenas copiei?** Aprendi - entendi como funciona streaming em FastAPI
```

**Exemplo real (uso ruim - evite!):**
```
**Usei Cursor/Copilot?** Sim
**Fui copiloto ou piloto?** Copiloto - aceitei tudo que Cursor sugeriu sem pensar
**Code review do código gerado:** Não - confiei cegamente
**Aprendi conceitos ou apenas copiei?** Copiei - não entendi o que o código faz
```

**⚠️ LEMBRE-SE:** IA é ferramenta, não substituto do aprendizado!

---

#### Frase do dia
**O que colocar aqui?**
- Uma frase motivacional
- Um aprendizado importante
- Uma reflexão pessoal

**Exemplos:**
```
> "Groq é incrível! Gratuito e 10x mais rápido que OpenAI para testes."
```

```
> "Travou em bug por 1h, mas aprendi muito sobre debugging. Valeu a pena!"
```

```
> "Primeiro commit feito! O começo de uma jornada de 56 dias."
```

---

## 📊 2. REVIEW SEMANAL - Como Preencher

### Quando usar?
**TODO DOMINGO**, ao final da semana (20:00-21:00). Leva 30-45 minutos.

### Passo a Passo:

#### 1️⃣ Preencher Horas Estudadas
**Como fazer:**
1. Abra seus journals diários da semana
2. Some as horas reais de cada dia
3. Compare com o planejado
4. Calcule a aderência: (horas reais / horas planejadas) × 100

**Exemplo real (Semana 1):**
```
| Dia | Horas Planej. | Horas Reais | Atividade Principal | WakaTime |
|-----|---------------|-------------|---------------------|----------|
| Seg | 3h            | 2h45min     | Setup Groq + primeiro script | 2h30min |
| Ter | 3h            | 3h          | Script gerador de conteúdo | 2h50min |
| Qua | 3h            | 2h          | Script analisador de sentimentos | 1h45min |
| Qui | 3h            | 3h15min     | Script resumidor de PDFs | 3h |
| Sex | 3h            | 1h30min     | Refatoração (dia difícil) | 1h15min |
| Sáb | 4-6h          | 4h          | Projeto CLI integrado | 3h45min |
| Dom | 4-6h          | 3h          | Deploy + Review | 2h30min |
| **TOTAL** | **20-24h** | **19h30min** | | **17h35min** |
| **Aderência** | | **82%** | (meta: 80% é excelente!) | |
```

**⚠️ IMPORTANTE:** 80% de aderência é EXCELENTE! Não se culpe se não foi 100%.

---

#### 2️⃣ Sistema de Pontuação
**Como calcular:**

**A) Projetos e Código (40 pontos)**
- Commits: 5 commits = 5 pontos, 3 commits = 3 pontos, 0 commits = 0 pontos
- Projeto completo: Funcionando e deployado = 15 pontos, 80% completo = 12 pontos, 50% = 7 pontos
- Código revisado: Refatorei código = 10 pontos, parcial = 5 pontos, não = 0 pontos
- Testes: 60% coverage = 10 pontos, alguns testes = 5 pontos, nenhum = 0 pontos

**Exemplo real:**
```
- [x] Commits diários no GitHub (5 pts) - 5/5 (fiz 5 commits)
- [x] Projeto semanal completo (15 pts) - 12/15 (80% completo, falta deploy)
- [x] Código revisado e refatorado (10 pts) - 7/10 (refatorei parcialmente)
- [ ] Testes implementados (10 pts) - 0/10 (não fiz testes ainda)
**Subtotal:** 24/40
```

**B) Aprendizado Teórico (25 pontos)**
- Tutoriais: 3 tutoriais completos = 10 pontos, 1 tutorial = 5 pontos
- Documentação: Estudei 3 docs = 5 pontos, 1 doc = 2 pontos
- Anotações: Criei resumos = 5 pontos, anotações soltas = 2 pontos
- Artigo: Escrevi artigo = 5 pontos, rascunho = 2 pontos

**Exemplo real:**
```
- [x] Tutoriais/cursos completados (10 pts) - 8/10 (completei 2 tutoriais)
- [x] Documentação estudada (5 pts) - 5/5 (estudei Groq, Gemini, Claude docs)
- [x] Anotações e resumos criados (5 pts) - 5/5 (criei resumo de LLMs)
- [ ] Artigo técnico escrito (5 pts) - 0/5 (não escrevi ainda)
**Subtotal:** 18/25
```

**C) Qualidade e Boas Práticas (20 pontos)**
- Padrões: Código limpo = 5 pontos, parcial = 3 pontos
- Documentação: README completo = 5 pontos, básico = 2 pontos
- Erros: Tratamento completo = 5 pontos, parcial = 2 pontos
- Performance: Otimizado = 5 pontos, básico = 2 pontos

**Exemplo real:**
```
- [x] Código segue padrões (5 pts) - 4/5 (maioria limpo, alguns trechos confusos)
- [x] Documentação do projeto (5 pts) - 5/5 (README completo com exemplos)
- [x] Tratamento de erros (5 pts) - 3/5 (tratamento básico, falta edge cases)
- [ ] Performance otimizada (5 pts) - 2/5 (funciona, mas não otimizei)
**Subtotal:** 14/20
```

**D) Networking e Comunidade (15 pontos)**
- Post: Postei em comunidade = 5 pontos
- Ajudar: Ajudei alguém = 5 pontos
- Participar: Participei de discussões = 5 pontos

**Exemplo real:**
```
- [x] Post em comunidade/fórum (5 pts) - 5/5 (postei no Discord Rocketseat)
- [ ] Ajudar outro dev (5 pts) - 0/5 (não ajudei ninguém)
- [x] Participar de discussões (5 pts) - 3/5 (comentei em 2 posts)
**Subtotal:** 8/15
```

**TOTAL: 24 + 18 + 14 + 8 = 64/100 pontos**

**Status:** 🟡 Bom (70-84) - Mas você teve 64, então está 🟠 Regular (50-69)

**⚠️ IMPORTANTE:** Não se desanime com pontuação baixa! É normal nas primeiras semanas.

---

#### 3️⃣ Conquistas da Semana
**O que colocar aqui?**
- Top 3 realizações (mesmo que pequenas!)
- Projetos desenvolvidos
- Conceitos aprendidos

**Exemplo real:**
```
### 🏆 Top 3 Realizações
1. Criei primeiro projeto completo com IA (CLI automações)
2. Aprendi a usar 3 LLMs diferentes (Groq, Gemini, Claude)
3. Fiz 5 commits consecutivos no GitHub (streak começando!)

### 💻 Projetos Desenvolvidos
- **Projeto Principal:** CLI Automações com IA
  - Descrição: Scripts Python para gerar conteúdo, analisar sentimentos e resumir PDFs
  - Tecnologias: Python 3.12, Groq API, Gemini API, Claude API
  - Status: Em progresso (80% completo)
  - Link GitHub: https://github.com/seu-usuario/2-month-ai-journey-2025/tree/main/semana-01-cli-ia

### 📚 Conceitos Aprendidos
1. Tokens e como LLMs processam texto
2. Diferenças entre Groq (rápido/gratuito) vs GPT-4 (qualidade/pago)
3. Como fazer streaming de respostas de IA
4. Embeddings e busca semântica (introdução)
5. Prompt engineering básico
```

---

#### 4️⃣ Desafios e Dificuldades
**O que colocar aqui?**
- Principais obstáculos da semana
- Bugs/problemas técnicos difíceis
- Como lidou com eles

**Exemplo real:**
```
### ❌ Principais Obstáculos
1. **Obstáculo:** Erro de encoding UTF-8 nas respostas da API
   - **Impacto:** Perdi 2 horas tentando resolver
   - **Como lidei:** Pesquisei no Stack Overflow, encontrei solução
   - **Lição aprendida:** Sempre especificar encoding ao trabalhar com APIs

2. **Obstáculo:** Cansaço após trabalho (Quinta-feira)
   - **Impacto:** Só estudei 1h30min (meta era 3h)
   - **Como lidei:** Aceitei que foi um dia difícil, retomei na Sexta
   - **Lição aprendida:** Dias difíceis são normais, o importante é não desistir

### 🔧 Bugs/Problemas Técnicos Difíceis
- **Problema:** Streaming não funciona no frontend
  - Tempo gasto: 3h
  - Solução: Ainda não resolvi, vou pesquisar Vercel AI SDK na próxima semana
  - Recurso usado: Documentação Vercel AI SDK, Discord NextJS
```

---

#### 5️⃣ Recursos Consumidos
**O que colocar aqui?**
- Cursos/tutoriais que completou
- Documentação que estudou
- Artigos que leu
- Vídeos que assistiu

**Exemplo real:**
```
### Cursos/Tutoriais Completados
- [x] Título: "Groq API Tutorial" | Duração: 45min | Plataforma: YouTube (Fireship)

### Documentação Estudada
- [x] Groq API Documentation (console.groq.com/docs)
- [x] Google Gemini API Docs (ai.google.dev/docs)

### Artigos/Posts Técnicos Lidos
- [x] "Prompt Engineering Guide" - OpenAI Cookbook
- [x] "LLM Comparison 2025" - Dev.to

### Vídeos do YouTube
- [x] "Groq vs OpenAI Speed Test" - Fireship
- [x] "Python AI Automation" - freeCodeCamp
```

---

#### 6️⃣ Metas vs Realizado
**O que colocar aqui?**
- Compare as metas da semana com o que realmente fez
- Seja honesto!

**Exemplo real:**
```
| Meta da Semana | Status | Observações |
|----------------|--------|-------------|
| Criar 3 scripts de automação | ✅ | Completei todos os 3 scripts |
| Comparar 3 LLMs diferentes | ✅ | Comparei Groq, Gemini e Claude |
| Publicar projeto no GitHub | ⚠️ | Publiquei, mas falta README completo |
| Completar 5 tutoriais | ❌ | Completei apenas 2 tutoriais |

**Taxa de conclusão:** 75% (3/4 metas)
```

---

#### 7️⃣ Reflexão Pessoal
**O que colocar aqui?**
- O que funcionou bem
- O que não funcionou
- Ajustes para próxima semana
- Níveis de energia e motivação

**Exemplo real:**
```
### O que funcionou bem?
- Estudar de manhã (Sábado) foi muito produtivo
- Usar Groq para testes rápidos economizou tempo
- Fazer commits diários me manteve motivado

### O que NÃO funcionou?
- Estudar depois das 21h (muito cansado)
- Tentar aprender tudo de uma vez (sobrecarga)
- Não ter planejado as tarefas do dia antes

### Ajustes necessários para próxima semana
- Planejar tarefas do dia na noite anterior
- Estudar máximo até 20h30 (não forçar depois)
- Focar em 1 conceito por vez (não tentar aprender tudo)

### Nível de energia (1-10)
- Segunda a Sexta: 6 (cansado após trabalho, mas consegui estudar)
- Fim de semana: 8 (mais energia, mais produtivo)

### Nível de motivação (1-10)
- Início da semana: 9 (empolgado para começar!)
- Fim da semana: 7 (alguns dias difíceis, mas ainda motivado)

### 🤖 Avaliação Uso de IA (Novo 2025)
- **Usei IA como copiloto?** Sim (Cursor)
- **Tomei decisões arquiteturais?** Sim - decidi usar Python + FastAPI
- **Revisei código gerado?** Às vezes - preciso melhorar isso
- **Caí em FOMO de tecnologias?** Não - mantive foco em Groq/Gemini/Claude
```

---

#### 8️⃣ Planejamento Semana Próxima
**O que colocar aqui?**
- Objetivos principais
- Projetos a desenvolver
- Conceitos a estudar
- Tempo estimado

**Exemplo real:**
```
### Objetivos Principais
1. Aprender LangChain básico
2. Implementar RAG com ChromaDB
3. Criar chatbot com memória de contexto

### Projetos a Desenvolver
- Personal Knowledge Assistant (chatbot RAG)

### Conceitos a Estudar
- LangChain Expression Language (LCEL)
- Vector databases (ChromaDB)
- Embeddings e busca semântica

### Tempo estimado
- Segunda a Sexta: 15h (3h/dia)
- Fim de semana: 6h (3h Sábado + 3h Domingo)
- **Total:** 21h
```

---

## 🎯 3. CHECKLIST DIÁRIO RÁPIDO - Como Usar

### Quando usar?
**TODO DIA**, antes de começar a estudar. Imprima e deixe na sua mesa!

### Como usar:
1. **Imprima o checklist** (seção do template)
2. **Cole na parede/mesa** de estudos
3. **Marque com caneta** conforme completa cada item
4. **No final do dia**, veja o que faltou

**Dica:** Use um marcador de texto para destacar itens importantes!

---

## 🎮 4. GAMIFICAÇÃO - Sistema de Badges

### Quando usar?
**TODO DOMINGO**, durante o review semanal. Marque os badges que conquistou!

### Como marcar:
```
## 🏆 Minhas Conquistas

### Semana 1
- [x] Iniciante Dedicado 🥉 (estudei 6 dias em 7)
- [x] Primeiro Commit 🎯 (fiz primeiro commit)
- [x] Curioso 🔍 (completei 5 tutoriais)

### Semana 2
- [ ] Maratonista 🥈 (preciso estudar 11 dias em 14)
- [ ] Colecionador 📦 (tenho 12 commits, preciso de 50)
- [ ] Deploy Master 🌐 (ainda não fiz deploy)
```

**Dica:** Crie uma seção no seu Notion/Trello para acompanhar badges visualmente!

---

## 📋 5. PLANILHA DE PROGRESSO (Google Sheets)

### Como criar:
1. Abra Google Sheets
2. Crie uma planilha chamada "Progresso 2 Meses"
3. Copie a estrutura do template
4. Preencha semanalmente (todo Domingo)

### Fórmulas úteis (já estão no template):
- Total de Horas: `=SUM(C2:C9)`
- Aderência: `=D10/C10*100`
- Média de Pontos: `=AVERAGE(E2:E9)`

**Dica:** Use cores para visualizar:
- Verde: ≥80% aderência
- Amarelo: 60-79% aderência
- Vermelho: <60% aderência

---

## 💪 6. DICAS FINAIS PARA MANTER CONSISTÊNCIA

### ✅ Faça:
1. **Preencha o journal TODO DIA** (mesmo que seja rápido, 5min)
2. **Seja honesto** (não minta para si mesmo)
3. **Celebre pequenas vitórias** (cada commit conta!)
4. **Use os templates como ferramenta**, não como obrigação
5. **Revise journals antigos** (ver progresso é motivador!)

### ❌ Evite:
1. **Perfeccionismo** (não precisa preencher tudo perfeitamente)
2. **Culpar-se** por dias difíceis (são normais!)
3. **Comparar-se com outros** (compare com você mesmo de semana passada)
4. **Desistir** se perder alguns dias (retome na próxima semana)

---

## 🚀 PRÓXIMOS PASSOS

1. **HOJE:** Crie seu primeiro journal (`2024-11-25.md` ou data atual)
2. **ESTA SEMANA:** Preencha o journal todo dia
3. **DOMINGO:** Faça seu primeiro review semanal
4. **AJUSTE:** Adapte os templates ao seu estilo (eles são flexíveis!)

---

**Lembre-se:** O objetivo não é perfeição, é **progresso consistente**! 

**80% de aderência é EXCELENTE!** 🎉

Boa jornada! 🚀

