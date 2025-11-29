# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 1 de 8  
**Dia:** 4 de 7 (Quinta-feira, 27 Nov 2024)  
**Diretório:** `Semanas/Semana1/Dia4/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: Setup APIs (Groq, Gemini, Claude) + Hello AI
- ✅ Dia 2: Gerador de conteúdo para blog com Groq
- ✅ Dia 3: Analisador de sentimentos comparando múltiplos LLMs

### O que está em progresso:
- 🟡 Dia 4: Resumidor de documentos PDF usando múltiplos LLMs

### O que falta fazer (hoje):
- [ ] Criar script `resumidor_pdf.py`
- [ ] Instalar biblioteca para extração de texto de PDF (PyPDF2 ou pdfplumber)
- [ ] Implementar função de extração de texto de PDF
- [ ] Implementar resumo com Groq
- [ ] Implementar resumo com Gemini
- [ ] (Opcional) Implementar resumo com Claude
- [ ] Criar função de comparação de resumos
- [ ] Testar com 2-3 PDFs diferentes
- [ ] Salvar resumos em arquivos
- [ ] Preencher journal ao final do dia

---

## 📋 Estrutura de Arquivos

```
Dia4/
├── README.md                    # Visão geral do dia
├── CONTEXTO_AGENTE.md           # Este arquivo
├── checklist.md                 # Checklist detalhado
├── resumidor_pdf.py             # Script principal (criar)
├── journal.md                   # Journal do dia (preencher)
├── pdfs_teste/                  # Pasta para PDFs de teste (criar)
│   └── exemplo1.pdf             # PDFs para teste
└── resumos/                     # Pasta para resumos gerados (criar)
    └── resumo_exemplo1.md       # Resumos salvos
```

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **APIs:** Groq (prioritário), Gemini, Claude (opcional)
- **Ferramentas:** python-dotenv, venv
- **Bibliotecas:** groq, google-generativeai, anthropic
- **Extração PDF:** PyPDF2 ou pdfplumber (instalar)

### Configuração Necessária:
- Arquivo `.env` com API keys (já configurado nos dias anteriores)
  - `GROQ_API_KEY`
  - `GEMINI_API_KEY`
  - `ANTHROPIC_API_KEY` (opcional)
- Ambiente virtual Python ativado
- Bibliotecas instaladas (ver requirements.txt do Dia 1)
- **Nova biblioteca:** `pip install PyPDF2` ou `pip install pdfplumber`

### Objetivo do Dia:
Criar resumidor de PDFs que extrai texto de documentos PDF e gera resumos usando múltiplos LLMs, comparando a qualidade dos resumos gerados.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Seguir checklist.md
2. Instalar biblioteca de extração de PDF
3. Criar script base `resumidor_pdf.py`
4. Implementar extração de texto de PDF
5. Implementar resumo com Groq
6. Implementar resumo com Gemini
7. Criar função de comparação
8. Testar com 2-3 PDFs diferentes
9. Salvar resumos em arquivos
10. Preencher journal.md

### Próximo Dia (Dia 5 - Sexta-feira):
- Refatorar scripts dos dias anteriores
- Criar documentação completa
- Organizar código
- Preparar para projeto integrado (Dia 6-7)

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
- PyPDF2 Docs: https://pypdf2.readthedocs.io/
- pdfplumber Docs: https://github.com/jsvine/pdfplumber

### Código de Referência:
- Dia 1: `../Dia1/hello_ai_groq.py` - Estrutura básica com Groq
- Dia 2: `../Dia2/gerador_conteudo_blog.py` - Exemplo de uso de API e salvamento de arquivos
- Dia 3: `../Dia3/analisardor_sentimentos.py` - Exemplo de comparação de múltiplos LLMs

---

## ⚠️ Notas Importantes

1. **Segurança:** Nunca commitar arquivo `.env` com API keys
2. **Meta Realista:** 80% de aderência é excelente
3. **Foco:** Extrair texto corretamente e gerar resumos úteis
4. **PDFs grandes:** Considerar dividir PDFs muito grandes em chunks
5. **Limite de tokens:** PDFs grandes podem exceder limite de tokens dos LLMs
6. **Comparação:** Criar métrica de qualidade dos resumos (comprimento, clareza, completude)

---

## 🎯 Critérios de Sucesso (Dia 4)

- [ ] Script `resumidor_pdf.py` criado e funcionando
- [ ] Extração de texto de PDF funcionando
- [ ] Resumo funciona com pelo menos 2 LLMs (Groq + Gemini)
- [ ] Testado com 2-3 PDFs diferentes
- [ ] Resumos salvos em arquivos markdown
- [ ] Comparação de resumos implementada
- [ ] Commit feito no GitHub
- [ ] Journal preenchido
- [ ] Insights sobre qual LLM é melhor para resumos

---

## 💡 Dicas para Agentes

- **Sempre verificar:** Se o usuário já completou alguma tarefa antes de sugerir
- **Priorizar:** Groq + Gemini (gratuitos), Claude é opcional
- **Contexto:** Ler README.md e checklist.md para entender o que fazer
- **Extração PDF:** PyPDF2 é mais simples, pdfplumber é mais robusto para PDFs complexos
- **PDFs grandes:** Se PDF for muito grande, dividir em chunks ou resumir por seções
- **Prompt para resumo:** Deve ser claro sobre o tamanho do resumo desejado (curto, médio, longo)

---

## 📝 Exemplo de PDFs para Teste

Criar pasta `pdfs_teste/` e adicionar:
- PDF curto (1-2 páginas) - artigo ou documento simples
- PDF médio (5-10 páginas) - relatório ou documento técnico
- PDF longo (20+ páginas) - documento completo (opcional, para testar chunking)

**Nota:** Se não tiver PDFs próprios, pode usar documentos públicos ou criar PDFs de teste com texto simples.

---

**Última atualização:** 27 Nov 2025  
**Status:** 🟡 Em progresso

