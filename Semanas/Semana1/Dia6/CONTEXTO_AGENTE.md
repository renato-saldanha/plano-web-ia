# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 1 de 8  
**Dia:** 6 de 7 (Sábado, 29 Nov 2024)  
**Diretório:** `Semanas/Semana1/Dia6/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: Setup APIs (Groq, Gemini, Claude) + Hello AI
- ✅ Dia 2: Gerador de conteúdo para blog com Groq
- ✅ Dia 3: Analisador de sentimentos comparando múltiplos LLMs
- ✅ Dia 4: Resumidor de documentos PDF usando múltiplos LLMs
- ✅ Dia 5: Refatoração + Documentação completa

### O que está em progresso:
- 🟡 Dia 6: CLI integrado unificando os 3 scripts

### O que falta fazer (hoje):
- [ ] Criar estrutura do CLI integrado
- [ ] Integrar script do Dia 2 (gerador de conteúdo)
- [ ] Integrar script do Dia 3 (analisador de sentimentos)
- [ ] Integrar script do Dia 4 (resumidor de PDFs)
- [ ] Criar menu interativo
- [ ] Adicionar tratamento de erros unificado
- [ ] Criar help text e documentação inline
- [ ] Testar todas as funcionalidades
- [ ] Preencher journal ao final do dia

---

## 📋 Estrutura de Arquivos

```
Dia6/
├── README.md                    # Visão geral do dia
├── CONTEXTO_AGENTE.md           # Este arquivo
├── checklist.md                 # Checklist detalhado
├── cli_automatizacoes.py        # Script principal do CLI
├── journal.md                   # Journal do dia (preencher)
└── requirements.txt             # Dependências Python
```

**Scripts a integrar:**
- `../Dia2/gerador_conteudo_blog.py` → Comando `blog`
- `../Dia3/analisardor_sentimentos.py` → Comando `sentimentos`
- `../Dia4/resumidor_pdf.py` → Comando `resumir`

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **APIs:** Groq, Gemini, Claude
- **CLI:** `argparse` (built-in) ou `click` (opcional)
- **Ferramentas:** python-dotenv, venv
- **Bibliotecas:** groq, google-generativeai, pdfplumber

### Configuração Necessária:
- Arquivo `.env` com API keys (já configurado)
- Ambiente virtual Python ativado
- Bibliotecas instaladas
- Scripts dos dias anteriores funcionando

### Objetivo do Dia:
Criar uma interface CLI profissional que integre os 3 scripts criados nos dias anteriores, permitindo acesso fácil e unificado a todas as funcionalidades de automação com IA.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Seguir checklist.md
2. Criar estrutura básica do CLI com argparse
3. Integrar cada script como subcomando
4. Criar menu interativo opcional
5. Adicionar tratamento de erros unificado
6. Testar todas as funcionalidades
7. Preencher journal.md

### Próximo Dia (Dia 7 - Domingo):
- Deploy no GitHub
- Criar README épico com documentação completa
- Review da semana completa
- Preparar para Semana 2

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
- Python argparse: https://docs.python.org/3/library/argparse.html
- Python click: https://click.palletsprojects.com/
- CLI Design Best Practices: https://clig.dev/

### Código de Referência:
- Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Dia 3: `../Dia3/analisardor_sentimentos.py`
- Dia 4: `../Dia4/resumidor_pdf.py`

---

## ⚠️ Notas Importantes

1. **Segurança:** Nunca commitar arquivo `.env` com API keys
2. **Meta Realista:** 80% de aderência é excelente
3. **Foco:** CLI intuitivo e profissional
4. **Reutilização:** Importar funções dos scripts anteriores, não duplicar código
5. **Tratamento de Erros:** Mensagens claras e úteis para o usuário
6. **Help Text:** Documentação inline clara em cada comando

---

## 🎯 Critérios de Sucesso (Dia 6)

- [ ] CLI funcional com 3 comandos principais
- [ ] Menu interativo opcional funcionando
- [ ] Todos os scripts integrados corretamente
- [ ] Tratamento de erros unificado
- [ ] Help text completo e claro
- [ ] Testes básicos realizados
- [ ] Código organizado e documentado
- [ ] Commit feito no GitHub
- [ ] Journal preenchido

---

## 💡 Dicas para Agentes

- **Sempre verificar:** Se o usuário já completou alguma tarefa antes de sugerir
- **Priorizar:** Criar estrutura básica primeiro, depois integrar cada script
- **Contexto:** Ler código dos dias anteriores para entender como integrar
- **CLI Design:** Seguir padrões comuns (--help, mensagens claras, exit codes)
- **Reutilização:** Importar funções dos scripts anteriores, não copiar código
- **Testes:** Testar cada comando após integrar

---

## 📝 Exemplo de Estrutura CLI

### Com argparse (built-in):
```python
import argparse

parser = argparse.ArgumentParser(description='CLI de Automações com IA')
subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')

# Comando blog
parser_blog = subparsers.add_parser('blog', help='Gerar conteúdo para blog')
parser_blog.add_argument('--tema', required=True, help='Tema do blog')

# Comando sentimentos
parser_sentimentos = subparsers.add_parser('sentimentos', help='Analisar sentimentos')
parser_sentimentos.add_argument('--arquivo', required=True, help='Arquivo com reviews')

# Comando resumir
parser_resumir = subparsers.add_parser('resumir', help='Resumir PDF')
parser_resumir.add_argument('--pdf', required=True, help='Caminho do PDF')
parser_resumir.add_argument('--llm', choices=['groq', 'gemini'], default='groq')

args = parser.parse_args()
```

### Menu Interativo:
```python
def mostrar_menu():
    print("\n=== CLI de Automações com IA ===")
    print("1. Gerar conteúdo para blog")
    print("2. Analisar sentimentos")
    print("3. Resumir PDF")
    print("4. Sair")
    return input("\nEscolha uma opção: ")
```

---

**Última atualização:** 29 Nov 2025  
**Status:** 🟡 Em progresso

