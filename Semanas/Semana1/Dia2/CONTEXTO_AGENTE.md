# 🤖 Contexto para Agentes IA - Dia 2

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 1 de 8  
**Dia:** 2 de 7 (Terça-feira, 25 Nov 2024)  
**Diretório:** `Semanas/Semana1/Dia2/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: Setup APIs (Groq, Gemini, Claude) + Hello AI
- ✅ Dia 2: Gerador de conteúdo para blog com Groq
- ✅ Dia 3: Analisador de sentimentos comparando múltiplos LLMs
- ✅ Dia 4: Estrutura criada (Resumidor de PDFs)
- ✅ Dia 5: Estrutura criada (Refatoração + Documentação)

### O que está em progresso:
- 🟡 Dia 3: Analisador de sentimentos (em desenvolvimento)
- 🟡 Dia 4: Resumidor de PDFs (estrutura criada, aguardando implementação)
- 🟡 Dia 5: Refatoração (estrutura criada, aguardando implementação)

### O que falta fazer (Dia 2 - se ainda não concluído):
- [ ] Completar script `gerador_conteudo_blog.py`
- [ ] Testar com 3 temas planejados
- [ ] Adicionar tratamento de erros
- [ ] Salvar resultados
- [ ] Preencher journal ao final do dia

---

## 📋 Estrutura de Arquivos

```
Dia2/
├── README.md                    # Visão geral do dia
├── CONTEXTO_AGENTE.md          # Este arquivo
├── checklist.md                 # Checklist detalhado
├── gerador_conteudo_blog.py    # Script principal (criar)
├── journal.md                   # Journal do dia (preencher)
└── resultados/                  # Pasta para salvar conteúdos gerados
```

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **API:** Groq (já configurada no Dia 1)
- **Ferramentas:** python-dotenv, venv
- **Tracking:** WakaTime

### Configuração Necessária:
- Arquivo `.env` com `GROQ_API_KEY` (já configurado no Dia 1)
- Ambiente virtual Python ativado
- Bibliotecas instaladas (groq, python-dotenv)

### Objetivo do Dia:
Criar script funcional que gera conteúdo de blog usando Groq API

### Tarefas Planejadas (do Dia 1):
1. Criar arquivo `gerador_conteudo_blog.py` com função que recebe tema e gera parágrafo introdutório usando Groq API
2. Testar script com 3 temas diferentes (ex: "IA", "Python", "Web Dev") e salvar resultados
3. Adicionar tratamento de erros e mensagens informativas ao usuário

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Seguir checklist.md
2. Criar script base (template já criado)
3. Implementar função de geração
4. Testar e salvar resultados
5. Preencher journal.md

### Próximos Dias:
- ✅ Dia 3: Analisador de sentimentos (em desenvolvimento)
- ✅ Dia 4: Resumidor de PDFs (estrutura criada)
- ✅ Dia 5: Refatoração + Documentação (estrutura criada)

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
- **Dia 1:** `../Dia1/` (código de referência)

### Links Úteis:
- Groq Docs: https://console.groq.com/docs
- Prompt Engineering: https://platform.openai.com/docs/guides/prompt-engineering
- Exemplo Dia 1: `../Dia1/hello_ai_groq.py`

---

## ⚠️ Notas Importantes

1. **Baseado no Dia 1:** Groq já está configurado e funcionando
2. **Foco:** Prompt engineering - aprender a estruturar prompts eficazes
3. **Meta Realista:** 80% de aderência é excelente
4. **Tracking:** WakaTime instalado para métricas automáticas

---

## 🎯 Critérios de Sucesso (Dia 2)

- [ ] Script `gerador_conteudo_blog.py` criado e funcionando
- [ ] Função gera parágrafo introdutório a partir de um tema
- [ ] Testado com 3 temas diferentes
- [ ] Resultados salvos em arquivos
- [ ] Tratamento de erros implementado
- [ ] Commit feito no GitHub
- [ ] Journal preenchido

---

## 💡 Dicas para Agentes

- **Sempre verificar:** Se o usuário já completou alguma tarefa antes de sugerir
- **Referência:** Usar código do Dia 1 (`hello_ai_groq.py`) como base
- **Prompt Engineering:** Focar em criar prompts estruturados e eficazes
- **Ajuda:** Se usuário travar, sugerir consultar documentação de prompt engineering

---

**Última atualização:** 25 Nov 2025  
**Status:** ✅ Concluído (verificar se todas as tarefas foram completadas)

