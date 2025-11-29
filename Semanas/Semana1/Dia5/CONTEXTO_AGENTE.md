# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** 1 de 8  
**Dia:** 5 de 7 (Sexta-feira, 28 Nov 2024)  
**Diretório:** `Semanas/Semana1/Dia5/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia 1: Setup APIs (Groq, Gemini, Claude) + Hello AI
- ✅ Dia 2: Gerador de conteúdo para blog com Groq
- ✅ Dia 3: Analisador de sentimentos comparando múltiplos LLMs
- ✅ Dia 4: Resumidor de documentos PDF usando múltiplos LLMs

### O que está em progresso:
- 🟡 Dia 5: Refatoração + Documentação

### O que falta fazer (hoje):
- [ ] Revisar código dos scripts dos dias anteriores
- [ ] Adicionar type hints aos scripts
- [ ] Adicionar docstrings completas
- [ ] Melhorar tratamento de erros
- [ ] Refatorar código duplicado (criar funções utilitárias)
- [ ] Criar README principal da Semana 1
- [ ] Criar guias de uso para cada script
- [ ] Organizar estrutura de pastas
- [ ] Preparar estrutura para projeto integrado (Dia 6-7)
- [ ] Preencher journal ao final do dia

---

## 📋 Estrutura de Arquivos

```
Dia5/
├── README.md                    # Visão geral do dia
├── CONTEXTO_AGENTE.md           # Este arquivo
├── checklist.md                 # Checklist detalhado
├── journal.md                   # Journal do dia (preencher)
└── (refatorações nos dias anteriores)
```

**Scripts a refatorar:**
- `../Dia2/gerador_conteudo_blog.py`
- `../Dia3/analisardor_sentimentos.py`
- `../Dia4/resumidor_pdf.py`

**Documentação a criar:**
- `../README.md` (README principal da Semana 1)
- `../GUIA_USO.md` (Guia de uso dos scripts)

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** Python 3.12+
- **APIs:** Groq, Gemini, Claude
- **Ferramentas:** python-dotenv, venv
- **Bibliotecas:** groq, google-generativeai, anthropic, PyPDF2/pdfplumber

### Configuração Necessária:
- Arquivo `.env` com API keys (já configurado)
- Ambiente virtual Python ativado
- Bibliotecas instaladas

### Objetivo do Dia:
Refatorar e documentar os scripts criados nos dias anteriores, melhorando qualidade do código e preparando base sólida para o projeto integrado dos dias 6-7.

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. Seguir checklist.md
2. Revisar código dos scripts anteriores
3. Adicionar type hints e docstrings
4. Melhorar tratamento de erros
5. Refatorar código duplicado
6. Criar documentação completa
7. Organizar estrutura
8. Preencher journal.md

### Próximo Dia (Dia 6 - Sábado):
- Começar projeto integrado: CLI para múltiplas automações
- Integrar os 3 scripts criados
- Criar interface de linha de comando

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
- Python Type Hints: https://docs.python.org/3/library/typing.html
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
- PEP 8: https://pep8.org/
- Markdown Guide: https://www.markdownguide.org/

### Código de Referência:
- Dia 1: `../Dia1/hello_ai_groq.py`
- Dia 2: `../Dia2/gerador_conteudo_blog.py`
- Dia 3: `../Dia3/analisardor_sentimentos.py`
- Dia 4: `../Dia4/resumidor_pdf.py`

---

## ⚠️ Notas Importantes

1. **Segurança:** Nunca commitar arquivo `.env` com API keys
2. **Meta Realista:** 80% de aderência é excelente
3. **Foco:** Qualidade do código e documentação clara
4. **Type Hints:** Adicionar em todas as funções
5. **Docstrings:** Usar formato Google ou NumPy
6. **DRY:** Don't Repeat Yourself - criar funções utilitárias
7. **Documentação:** Deve ser clara para outros desenvolvedores

---

## 🎯 Critérios de Sucesso (Dia 5)

- [ ] Scripts refatorados com type hints
- [ ] Docstrings completas em todas as funções
- [ ] Tratamento de erros melhorado
- [ ] Código duplicado removido (funções utilitárias criadas)
- [ ] README principal da Semana 1 criado
- [ ] Guias de uso criados
- [ ] Estrutura organizada
- [ ] Commit feito no GitHub
- [ ] Journal preenchido
- [ ] Preparação para projeto integrado concluída

---

## 💡 Dicas para Agentes

- **Sempre verificar:** Se o usuário já completou alguma tarefa antes de sugerir
- **Priorizar:** Refatoração incremental (um script por vez)
- **Contexto:** Ler código dos dias anteriores para entender o que precisa ser melhorado
- **Type Hints:** Usar `typing` module para tipos complexos
- **Docstrings:** Incluir descrição, parâmetros, retorno e exemplos
- **Testes:** Considerar adicionar testes básicos (opcional para hoje)

---

## 📝 Exemplo de Refatoração

### Antes:
```python
def gerar_conteudo(tema):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    # código...
```

### Depois:
```python
from typing import Optional
from groq import Groq

def gerar_conteudo(tema: str, tamanho: str = "médio") -> Optional[str]:
    """
    Gera conteúdo de blog sobre um tema específico usando Groq API.
    
    Args:
        tema: Tema do conteúdo a ser gerado
        tamanho: Tamanho do conteúdo ('curto', 'médio', 'longo')
    
    Returns:
        Conteúdo gerado ou None em caso de erro
    
    Raises:
        ValueError: Se tema estiver vazio
        APIError: Se houver erro na API
    
    Example:
        >>> conteudo = gerar_conteudo("Python", "médio")
        >>> print(conteudo)
    """
    if not tema:
        raise ValueError("Tema não pode estar vazio")
    
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        # código...
    except Exception as e:
        logger.error(f"Erro ao gerar conteúdo: {e}")
        return None
```

---

**Última atualização:** 28 Nov 2025  
**Status:** 🟡 Em progresso

