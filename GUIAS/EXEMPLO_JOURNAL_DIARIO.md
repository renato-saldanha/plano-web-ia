# 📆 EXEMPLO: Journal Diário Preenchido

Este é um exemplo REAL de como preencher o journal diário. Use como referência!

---

# 📆 25 de Novembro de 2024 - Segunda-feira

## ⏰ Horário de Estudo
- Início: 17:45
- Fim: 20:15
- Total: 2h30min

## ✅ Realizações do Dia
- [x] Criei conta Groq e obtive API key gratuita
- [x] Configurei ambiente Python 3.12 com venv
- [x] Instalei bibliotecas: groq, python-dotenv
- [x] Escrevi primeiro script "hello_ai_groq.py"
- [x] Testei integração com Llama 3.2 (funcionou perfeitamente!)
- [x] Fiz primeiro commit no GitHub: "First AI integration with Groq"
- [x] Configurei WakaTime no VS Code

## 🧠 O que Aprendi Hoje
- **Conceito novo:** Tokens são unidades de texto que LLMs processam. 1 token ≈ 4 caracteres em português. Groq processa até 32k tokens por requisição.
- **Tecnologia/Ferramenta:** Groq - API gratuita e ultra-rápida para modelos open-source (Llama 3.2, Mixtral). É 10x mais rápido que OpenAI para testes!
- **Insight importante:** Groq é melhor para desenvolvimento/testes (gratuito e rápido), GPT-4 é melhor para produção quando precisa de máxima qualidade.
- **LLM usado:** Groq (Llama 3.2) - escolhi porque é gratuito, rápido e perfeito para aprender sem gastar dinheiro

## 💻 Código Escrito
- **Projeto:** semana-01-cli-ia (primeiro projeto)
- **Linhas de código:** ~120 linhas (1 arquivo Python: hello_ai_groq.py)
- **Commits:** 1 commit (primeiro commit da jornada!)
- **Link GitHub:** https://github.com/seu-usuario/2-month-ai-journey-2025/tree/main/semana-01-cli-ia
- **WakaTime:** 2h15min (tracking automático)

## ❌ Dificuldades Enfrentadas
- **Problema:** Erro "ModuleNotFoundError: No module named 'groq'" mesmo após pip install groq
- **Tempo perdido:** 30 minutos
- **Como resolvi (ou não):** Descobri que estava usando o Python global ao invés do venv. Ativei o venv correto com `source venv/bin/activate` (Linux) e funcionou perfeitamente.

## 🔍 Recursos Utilizados
- [x] Documentação: Groq API Documentation (https://console.groq.com/docs)
- [x] Tutorial/Vídeo: "Groq vs OpenAI Speed Test 2025" - Fireship (YouTube, 8min)
- [x] Artigo: "Getting Started with Groq API" - Groq Blog
- [ ] Comunidade (pergunta/resposta): Não precisei hoje

## 🎯 Plano para Amanhã
1. Criar segundo script: gerador de conteúdo para blog usando Groq
2. Comparar resposta do Groq com Gemini (criar conta Google AI Studio)
3. Assistir tutorial "Prompt Engineering Basics" (30min)

## 💭 Reflexão
**Como me senti hoje?** (1-10): 8
**Energia após trabalho:** 6 (cansado, mas consegui estudar)
**Foco durante estudo:** 7 (algumas distrações no início, mas depois fiquei focado)
**Motivação:** 9 (muito empolgado com o primeiro dia! Ver o script funcionando foi incrível)

## 🤖 Uso de IA (Novo 2025)
**Usei Cursor/Copilot?** Sim (Cursor)
**Fui copiloto ou piloto?** Piloto - decidi usar Groq e Python, Cursor só ajudou com a sintaxe da requisição HTTP
**Code review do código gerado:** Sim - revisei o código que Cursor sugeriu e entendi cada linha
**Aprendi conceitos ou apenas copiei?** Aprendi - entendi como fazer requisições HTTP para APIs de IA, como usar variáveis de ambiente, e como processar respostas JSON

---
**Frase do dia:**
> "Primeiro commit feito! O começo de uma jornada de 56 dias. Groq é incrível - gratuito e ultra-rápido!"

---

# 📆 26 de Novembro de 2024 - Terça-feira

## ⏰ Horário de Estudo
- Início: 17:30
- Fim: 20:30
- Total: 3 horas

## ✅ Realizações do Dia
- [x] Criei conta Google AI Studio (Gemini - gratuito)
- [x] Escrevi script "gerador_conteudo_blog.py" usando Groq
- [x] Escrevi versão do mesmo script usando Gemini
- [x] Comparei respostas de Groq vs Gemini (qualidade e velocidade)
- [x] Documentei comparação no README
- [x] Fiz 2 commits no GitHub

## 🧠 O que Aprendi Hoje
- **Conceito novo:** Prompt engineering - como estruturar prompts para obter melhores respostas. Few-shot examples melhoram muito a qualidade.
- **Tecnologia/Ferramenta:** Google Gemini 2.0 - API gratuita com 60 requisições/min. Boa qualidade, mas um pouco mais lenta que Groq.
- **Insight importante:** Groq é mais rápido (resposta em 0.5s), mas Gemini tem respostas mais detalhadas e criativas. Para produção, escolheria Gemini para conteúdo criativo.
- **LLM usado:** Groq (Llama 3.2) e Gemini 2.0 - comparei ambos para entender diferenças

## 💻 Código Escrito
- **Projeto:** semana-01-cli-ia
- **Linhas de código:** ~280 linhas (2 arquivos Python novos)
- **Commits:** 2 commits
- **Link GitHub:** https://github.com/seu-usuario/2-month-ai-journey-2025/tree/main/semana-01-cli-ia
- **WakaTime:** 2h50min

## ❌ Dificuldades Enfrentadas
- **Problema:** Gemini API retornava erro 429 (rate limit) mesmo sendo primeira requisição
- **Tempo perdido:** 45 minutos
- **Como resolvi (ou não):** Descobri que precisava criar projeto no Google Cloud Console primeiro, não só no AI Studio. Após criar projeto e ativar API, funcionou.

## 🔍 Recursos Utilizados
- [x] Documentação: Google Gemini API Docs (https://ai.google.dev/docs)
- [x] Tutorial/Vídeo: "Gemini API Tutorial 2025" - Web Dev Cody (YouTube)
- [x] Artigo: "Prompt Engineering Guide" - OpenAI Cookbook
- [x] Comunidade: Perguntei no Discord Rocketseat sobre rate limits do Gemini

## 🎯 Plano para Amanhã
1. Criar script analisador de sentimentos (comparar 3 LLMs: Groq, Gemini, Claude)
2. Criar conta Anthropic (Claude) se necessário
3. Testar com reviews reais de produtos

## 💭 Reflexão
**Como me senti hoje?** (1-10): 7
**Energia após trabalho:** 5 (mais cansado que ontem)
**Foco durante estudo:** 8 (muito focado, especialmente na comparação de LLMs)
**Motivação:** 8 (empolgado com as diferenças entre os modelos!)

## 🤖 Uso de IA (Novo 2025)
**Usei Cursor/Copilot?** Sim
**Fui copiloto ou piloto?** Piloto - decidi comparar os dois LLMs, Cursor ajudou com código de comparação
**Code review do código gerado:** Sim - refatorei função de comparação que Cursor gerou
**Aprendi conceitos ou apenas copiei?** Aprendi - entendi diferenças entre modelos e quando usar cada um

---
**Frase do dia:**
> "Comparar LLMs é fascinante! Groq = velocidade, Gemini = criatividade. Cada um tem seu lugar."

---

# 📆 27 de Novembro de 2024 - Quarta-feira

## ⏰ Horário de Estudo
- Início: 18:00
- Fim: 20:00
- Total: 2 horas

## ✅ Realizações do Dia
- [x] Criei conta Anthropic (Claude) - $5 de créditos grátis
- [x] Escrevi script "analisador_sentimentos.py" comparando 3 LLMs
- [x] Testei com 10 reviews reais de produtos
- [x] Documentei resultados da comparação
- [x] Fiz 1 commit

## 🧠 O que Aprendi Hoje
- **Conceito novo:** Análise de sentimentos com LLMs - como estruturar prompts para classificar sentimentos (positivo/negativo/neutro) com alta precisão.
- **Tecnologia/Ferramenta:** Anthropic Claude 3.5 Sonnet - melhor para análise de texto longo e raciocínio complexo. Mais caro, mas qualidade superior.
- **Insight importante:** Claude é melhor para análise detalhada (mais preciso), Groq é melhor para velocidade (análise rápida), Gemini é meio-termo (boa qualidade, preço justo).
- **LLM usado:** Groq, Gemini e Claude - comparei os 3 para análise de sentimentos

## 💻 Código Escrito
- **Projeto:** semana-01-cli-ia
- **Linhas de código:** ~200 linhas (1 arquivo novo)
- **Commits:** 1 commit
- **Link GitHub:** https://github.com/seu-usuario/2-month-ai-journey-2025/tree/main/semana-01-cli-ia
- **WakaTime:** 1h45min

## ❌ Dificuldades Enfrentadas
- **Problema:** Claude API retornava erro de autenticação mesmo com API key correta
- **Tempo perdido:** 30 minutos
- **Como resolvi (ou não):** Descobri que precisava usar header "x-api-key" ao invés de "Authorization: Bearer". Li a documentação e corrigi.

## 🔍 Recursos Utilizados
- [x] Documentação: Anthropic Claude API Docs (https://docs.anthropic.com)
- [x] Tutorial/Vídeo: "Claude API Tutorial" - AI Jason (YouTube)
- [x] Artigo: "Sentiment Analysis with LLMs" - Dev.to
- [ ] Comunidade: Não precisei hoje

## 🎯 Plano para Amanhã
1. Criar script resumidor de documentos PDF
2. Usar biblioteca PyPDF2 para extrair texto
3. Testar com PDFs de diferentes tamanhos

## 💭 Reflexão
**Como me senti hoje?** (1-10): 6
**Energia após trabalho:** 4 (muito cansado, quase não estudei)
**Foco durante estudo:** 6 (difícil concentrar, mas consegui fazer o script)
**Motivação:** 7 (menos empolgado que ontem, mas ainda motivado)

## 🤖 Uso de IA (Novo 2025)
**Usei Cursor/Copilot?** Sim
**Fui copiloto ou piloto?** Piloto - decidi estrutura do script, Cursor ajudou com parsing de JSON
**Code review do código gerado:** Parcial - revisei parcialmente, estava com pressa
**Aprendi conceitos ou apenas copiei?** Aprendi - entendi como fazer análise de sentimentos com diferentes LLMs

---
**Frase do dia:**
> "Dia difícil, mas completei a tarefa. Progresso de 1% é melhor que 0%!"

---

## 📝 NOTAS IMPORTANTES SOBRE ESTE EXEMPLO:

1. **Não precisa ser perfeito!** - Veja que alguns dias têm mais detalhes que outros. Isso é normal!

2. **Seja honesto** - No dia 27, o usuário estava cansado e estudou menos. Isso é OK! O importante é continuar.

3. **Progresso gradual** - Veja como o conhecimento vai evoluindo dia a dia (tokens → prompt engineering → análise de sentimentos)

4. **Dificuldades são normais** - Cada dia teve algum problema técnico. Isso é esperado e faz parte do aprendizado!

5. **Reflexão honesta** - As notas de energia/foco variam. Isso é realista!

6. **Uso consciente de IA** - O usuário sempre foi "piloto", tomando decisões arquiteturais, e revisou código gerado.

**Use este exemplo como inspiração, mas adapte ao seu estilo!** 🚀

