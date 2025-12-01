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
- `checklist.md` - Checklist detalhado com guias passo-a-passo
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python
- `cli_automatizacoes.py` - CLI integrando os exercícios dos dias 2, 3 e 4

### Exemplos de uso
python
``` 
python cli_automatizacoes.py blog --tema "Python"
python cli_automatizacoes.py sentimentos --arquivo reviews/reviews.txt
python cli_automatizacoes.py resumir --pdf pdfs/arquivo.pdf --llm groq
python cli_automatizacoes.py  # Menu interativo
```

### 📚 Arquivos de Aprendizado:
- `GUIA_CLI.md` - Guia completo de conceitos e passo-a-passo de CLI
- `template_cli.py` - Template com TODOs para você preencher
- `exemplo_cli_simples.py` - Exemplo completo comentado para referência
- `exercicios_cli.md` - Exercícios progressivos para praticar

### 🎯 Arquivo de Transição:
- `CONTEXTO_PROXIMO_DIA.md` - Guia completo para construir o Dia 7

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
- **Nível de Scaffolding:** Nível 2 (Intermediário) - Template com TODOs
- **Baseado nos Dias 2-4:** Integrar os 3 scripts funcionais
- **Foco:** Aprender criando, não copiando código pronto
- **Metodologia:** Scaffolding + Progressive Disclosure (ver `../../METODOLOGIA_ENSINO.md`)
- **Biblioteca:** `argparse` (built-in do Python, não precisa instalar)
- **Boas práticas:** Tratamento de erros, mensagens claras, help text

### 🎓 Como Usar Este Dia:

1. **Leia primeiro:** `GUIA_CLI.md` para entender conceitos
2. **Veja exemplo:** `exemplo_cli_simples.py` para ver estrutura completa
3. **Use template:** `template_cli.py` como base e preencha TODOs
4. **Pratique:** Complete exercícios em `exercicios_cli.md` se necessário
5. **Siga checklist:** `checklist.md` tem guias passo-a-passo detalhados

### 🔗 Referências:

**Documentação do Projeto:**
- Metodologia de Ensino: `../../METODOLOGIA_ENSINO.md`
- Template de Estrutura: `../../TEMPLATE_ESTRUTURA_DIA.md`
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Recursos: `../../3-recursos_e_links_uteis.md`

**Scripts dos Dias Anteriores:**
- Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Dia 3: `../Dia3/analisador_sentimentos.py`
- Dia 4: `../Dia4/resumidor_pdf.py`

**Documentação Externa:**
- Python argparse: https://docs.python.org/3/library/argparse.html
- CLI Design Best Practices: https://clig.dev/
- Python click (alternativa): https://click.palletsprojects.com/

---

**Status:** 🟡 Em progresso  
**Nível de Scaffolding:** 2 (Intermediário)  
**Última atualização:** 30 Nov 2025

---

## 🎯 Próximo Passo

Após completar este dia, consulte `CONTEXTO_PROXIMO_DIA.md` para entender como construir o Dia 7 (Deploy + Documentação + Review).


