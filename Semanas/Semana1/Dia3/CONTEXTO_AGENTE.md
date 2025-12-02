# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 1 de 8  
**Dia:** 3 de 7 (Quarta-feira, 26 Nov 2025)  
**Diretório:** `Semanas/Semana1/Dia3/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: Setup APIs (Groq, Gemini, Claude) + Hello AI
- ✅ Dia 2: Gerador de conteúdo para blog com Groq
- ✅ Dia 3: Analisador de sentimentos comparando múltiplos LLMs
- ✅ Dia 4: Resumidor de PDFs usando múltiplos LLMs
- ✅ Dia 5: Refatoração + Documentação
- ✅ Dia 6: CLI integrado unificando todos os scripts
- ✅ Dia 7: Deploy no GitHub + README épico + Review

### O que está em progresso:
- Nenhum - Semana 1 completa! ✅

### O que falta fazer (hoje):
- [ ] Criar script `analisador_sentimentos.py`
- [ ] Implementar análise com Groq
- [ ] Implementar análise com Gemini
- [ ] (Opcional) Implementar análise com Claude
- [ ] Criar função de comparação
- [ ] Testar com 5 reviews diferentes
- [ ] Criar tabela comparativa
- [ ] Salvar resultados em arquivo
- [ ] Preencher journal ao final do dia

---

## 📋 Estrutura de Arquivos

```
Dia3/
├── README.md                    # Visão geral do dia
├── CONTEXTO_AGENTE.md           # Este arquivo
├── checklist.md                 # Checklist detalhado
├── analisador_sentimentos.py    # Script principal (criar)
├── journal.md                   # Journal do dia (preencher)
├── resultado_comparacao/        # Pasta para resultados (criar)
│   └── comparacao_llms.md       # Tabela comparativa
└── reviews_teste/               # Pasta para reviews de teste (criar)
    └── reviews.txt              # Reviews para teste
```

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **APIs:** Groq (prioritário), Gemini, Claude (opcional)
- **Ferramentas:** python-dotenv, venv
- **Bibliotecas:** groq, google-generativeai, anthropic

### Configuração Necessária:
- Arquivo `.env` com API keys (já configurado nos dias anteriores)
  - `GROQ_API_KEY`
  - `GEMINI_API_KEY`
  - `ANTHROPIC_API_KEY` (opcional)
- Ambiente virtual Python ativado
- Bibliotecas instaladas (ver requirements.txt do Dia 1)

### Objetivo do Dia:
Criar analisador de sentimentos que usa múltiplos LLMs e compara os resultados para entender qual é melhor para análise de sentimentos.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Seguir checklist.md
2. Criar script base `analisador_sentimentos.py`
3. Implementar análise com Groq
4. Implementar análise com Gemini
5. Criar função de comparação
6. Testar com 5 reviews diferentes
7. Gerar tabela comparativa
8. Preencher journal.md

### Próximo Dia (Dia 4 - Quinta-feira):
- ✅ Estrutura criada (README, CONTEXTO_AGENTE, checklist, journal)
- Criar script resumidor de documentos PDF
- Usar múltiplos LLMs para resumir

### Próxima Semana:
- Semana 2: LangChain + RAG
- Semana 3: FastAPI Backend
- Semana 4: Bun + Hono
- Semana 5-6: NextJS Frontend
- Semana 7-8: Projeto Final

---

## 📚 Referências Rápidas

### Documentos Principais:
- **Plano Completo:** `../../1-plano_desenvolvimento_2meses_v2.md`
- **Recursos:** `../../3-recursos_e_links_uteis.md`
- **Templates:** `../../2-templates_acompanhamento.md`
- **Começar Aqui:** `../../0-COMECE_AQUI.md`

### Links Úteis:
- Groq Docs: https://console.groq.com/docs
- Gemini Docs: https://ai.google.dev/docs
- Claude Docs: https://docs.anthropic.com
- Prompt Engineering para Sentiment Analysis: https://platform.openai.com/docs/guides/prompt-engineering

### Código de Referência:
- Dia 1: `../Dia1/hello_ai_groq.py` - Estrutura básica com Groq
- Dia 2: `../Dia2/gerador_conteudo_blog.py` - Exemplo de uso de API e salvamento de arquivos

---

## ⚠️ Notas Importantes

1. **Segurança:** Nunca commitar arquivo `.env` com API keys
2. **Meta Realista:** 80% de aderência é excelente
3. **Foco:** Comparar diferentes LLMs, não apenas usar um
4. **Análise de Sentimentos:** Prompt deve ser claro para retornar: positivo, negativo ou neutro
5. **Comparação:** Criar métrica de concordância entre LLMs

---

## 🎯 Critérios de Sucesso (Dia 3)

- [ ] Script `analisador_sentimentos.py` criado e funcionando
- [ ] Análise funciona com pelo menos 2 LLMs (Groq + Gemini)
- [ ] Testado com 5 reviews diferentes
- [ ] Tabela comparativa criada e salva
- [ ] Commit feito no GitHub
- [ ] Journal preenchido
- [ ] Insights sobre qual LLM é melhor para análise de sentimentos

---

## 💡 Dicas para Agentes

- **Sempre verificar:** Se o usuário já completou alguma tarefa antes de sugerir
- **Priorizar:** Groq + Gemini (gratuitos), Claude é opcional
- **Contexto:** Ler README.md e checklist.md para entender o que fazer
- **Prompt para análise de sentimentos:** Deve ser claro e pedir apenas 3 opções: positivo, negativo, neutro
- **Comparação:** Criar função que mostra concordância/discordância entre LLMs

---

## 📝 Exemplo de Reviews para Teste

Criar arquivo `reviews_teste/reviews.txt` com reviews de exemplo:

```
Review 1: Este produto é incrível! Funciona perfeitamente e superou minhas expectativas.
Review 2: Péssima qualidade, não recomendo. Quebrei após 2 dias de uso.
Review 3: O produto é ok, nada especial mas funciona como esperado.
Review 4: Estou muito satisfeito com a compra. Entrega rápida e produto de qualidade.
Review 5: Decepcionado. O produto não corresponde ao que foi prometido na descrição.
```

---

**Última atualização:** 30 Nov 2025  
**Status:** ✅ Concluído

