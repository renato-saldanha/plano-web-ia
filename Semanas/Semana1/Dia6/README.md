# 📅 Dia 6 - Sábado (29 Nov 2024)

## 🎯 Contexto para Agentes IA

Este é o **sexto dia** do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** Criar CLI integrado unificando os 3 scripts dos dias anteriores
- **Duração estimada:** 4-6 horas (meta realista: 3-5h)
- **Foco:** Integrar scripts em uma interface CLI unificada e profissional

### 🗺️ Estrutura do Plano:
- **Semana 1:** Fundamentos de IA Generativa (24 Nov - 30 Nov)
- **Dia 1 (concluído):** Setup APIs + Tutorial básico prompting ✅
- **Dia 2 (concluído):** Script 1 - Gerador de conteúdo para blog ✅
- **Dia 3 (concluído):** Script 2 - Analisador de sentimentos comparando LLMs ✅
- **Dia 4 (concluído):** Script 3 - Resumidor de PDFs ✅
- **Dia 5 (concluído):** Refatoração + Documentação ✅
- **Dia 6 (hoje):** Projeto integrado CLI
- **Dia 7:** Deploy no GitHub + README épico + Review

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia
- `cli_automatizacoes.py` - Script principal do CLI integrado
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python

### 🎯 Funcionalidades do CLI:

O CLI integrado deve permitir:

1. **Gerar conteúdo para blog**
   - Comando: `python cli_automatizacoes.py blog --tema "Python"`
   - Integra: `Dia2/gerador_conteudo_blog.py`

2. **Analisar sentimentos de reviews**
   - Comando: `python cli_automatizacoes.py sentimentos --arquivo reviews.txt`
   - Integra: `Dia3/analisardor_sentimentos.py`

3. **Resumir PDFs**
   - Comando: `python cli_automatizacoes.py resumir --pdf arquivo.pdf --llm groq`
   - Integra: `Dia4/resumidor_pdf.py`

4. **Menu interativo**
   - Comando: `python cli_automatizacoes.py`
   - Mostra menu com opções numeradas

### 💡 Notas Importantes:
- **Baseado nos Dias 2-4:** Integrar os 3 scripts funcionais
- **Foco:** Criar interface CLI profissional e intuitiva
- **Biblioteca recomendada:** `argparse` ou `click` para CLI
- **Boas práticas:** Tratamento de erros, mensagens claras, help text

### 🔗 Referências:
- Plano completo: `../../1-plano_desenvolvimento_2meses_v2.md`
- Recursos: `../../3-recursos_e_links_uteis.md`
- Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Dia 3: `../Dia3/analisardor_sentimentos.py`
- Dia 4: `../Dia4/resumidor_pdf.py`
- Python argparse: https://docs.python.org/3/library/argparse.html
- Python click: https://click.palletsprojects.com/

---

**Status:** 🟡 Em progresso  
**Última atualização:** 29 Nov 2025

