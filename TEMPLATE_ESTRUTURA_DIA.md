# 📋 Template: Estrutura Padrão de um Dia

Este template deve ser usado como base para criar novos dias no plano de desenvolvimento. Adapte conforme o nível de scaffolding necessário.

---

## 📁 Estrutura de Arquivos

```
DiaX/
├── README.md                    # Contexto e objetivos do dia (OBRIGATÓRIO)
├── CONTEXTO_AGENTE.md           # Informações técnicas detalhadas (OBRIGATÓRIO)
├── checklist.md                 # Tarefas práticas divididas em fases (OBRIGATÓRIO)
├── journal.md                   # Template para reflexão (OBRIGATÓRIO)
├── requirements.txt             # Dependências Python (OBRIGATÓRIO - mesmo que vazio)
├── CONTEXTO_PROXIMO_DIA.md      # Guia para construir próximo dia (OBRIGATÓRIO)
│
├── GUIA_APRENDIZADO.md          # Conceitos teóricos + passo-a-passo (Nível 2)
├── GUIA_CONCEITOS.md            # Conceitos teóricos resumidos (Nível 3)
│
├── template.py                  # Estrutura básica com TODOs (Nível 2)
├── exemplo_referencia.py         # Exemplo completo comentado (Nível 1-2)
├── especificacoes.md             # Requisitos e objetivos (Nível 3)
│
└── exercicios.md                 # Exercícios guiados e desafios
```

**⚠️ IMPORTANTE - Ordem Padrão:**
Os arquivos obrigatórios devem seguir esta ordem lógica de uso:
1. README.md (contexto inicial)
2. CONTEXTO_AGENTE.md (detalhes técnicos)
3. checklist.md (tarefas práticas)
4. journal.md (reflexão)
5. requirements.txt (dependências)
6. CONTEXTO_PROXIMO_DIA.md (transição)

> **Regra de tempo:** se algum conceito ou exercício não couber em 160 minutos, divida-o em um novo dia seguindo o método de scaffolding (exposição guiada → prática assistida → autonomia). O limite de 160min inclui **toda leitura dos documentos do dia, execução de testes/exercícios e preenchimento dos arquivos obrigatórios**, e o código deve ser escrito **sem autocomplete/IA gerando trechos**.

---

## ⏰ Métricas de Tempo Padrão

### ⚠️ IMPORTANTE: Tempo Máximo = 2h40 (160min)

| Fase | Duração | Atividades típicas | Saídas obrigatórias |
|------|---------|--------------------|---------------------|
| Preparação | 5min | Abrir checklist, revisar `README.md`, validar ambiente | Pré-requisitos marcados |
| Leitura guiada | 20min | Ler guias/documentos do dia, destacar pontos-chave | Notas rápidas + dúvidas registradas |
| Construção guiada | 90min | Trabalhar no `template.py`, exercícios ou código principal | TODOs resolvidos ou dúvidas comentadas |
| Consolidação | 25min | Testes rápidos, refino e checklist parcial | Código executando + checklist atualizado |
| Registro/handoff | 20min | Checklist final, journal, `CONTEXTO_PROXIMO_DIA.md` | Documentos preenchidos |
| Buffer | 10min | Resolver imprevistos ou mover item para próximo dia | Deve permanecer livre se tudo der certo |

- **Total diário:** 160 minutos (não extrapole) e **sem uso de autocomplete/IA para escrever código**.
- **Fins de semana:** mesma estrutura em horário alternativo.
- **Conceito maior que 160 minutos?** Converta o excedente em um novo dia e ajuste o scaffolding (Nível 1 → 2 → 3).

---

## 📝 Conteúdo de Cada Arquivo

### README.md

```markdown
# 📅 Dia X - [Dia da Semana] ([Data])

## 🎯 Contexto para Agentes IA

Este é o **[número] dia** do plano de desenvolvimento de 2 meses em Desenvolvimento Web + IA Generativa.

### 📋 O que foi proposto:
- **Objetivo do Dia:** [Objetivo claro e específico]
- **Duração estimada:** [160min totais (inclui leitura, exercícios/testes e preenchimento de documentos) — sem autocomplete/IA escrevendo código]
- **Foco:** [Foco principal do aprendizado]

### 🗺️ Estrutura do Plano:
- **Semana X:** [Nome da semana] ([Datas])
- **Dia X-1 (concluído):** [Resumo do dia anterior] ✅
- **Dia X (hoje):** [Objetivo do dia atual]
- **Dia X+1:** [Próximo dia]

### 📁 Arquivos neste diretório:
- `README.md` - Este arquivo (contexto)
- `CONTEXTO_AGENTE.md` - Contexto detalhado para agentes IA
- `checklist.md` - Checklist detalhado do dia
- `journal.md` - Journal do dia (preencher ao final)
- `requirements.txt` - Dependências Python (obrigatório, mesmo que vazio)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório)
- [Outros arquivos específicos do dia conforme nível de scaffolding]

### 🎯 O que você vai aprender:
1. [Conceito/Habilidade 1]
2. [Conceito/Habilidade 2]
3. [Conceito/Habilidade 3]

### 💡 Notas Importantes:
- **Baseado em:** [Dias anteriores ou conceitos pré-requisitos]
- **Foco:** [Foco específico]
- **Nível de Scaffolding:** [1, 2 ou 3 - ver METODOLOGIA_ENSINO.md]

### 🔗 Referências:
- Plano completo: `../../1-Plano_Desenvolvimento.md`
- Recursos: `../../3-recursos_e_links_uteis.md`
- Metodologia: `../../METODOLOGIA_ENSINO.md`
- [Referências específicas do dia]

---

**Status:** 🟡 Em progresso  
**Última atualização:** [Data]
```

### CONTEXTO_AGENTE.md

```markdown
# 🤖 Contexto para Agentes IA

Este arquivo fornece contexto essencial para agentes IA que precisam entender o estado atual do projeto e próximos passos.

---

## 📍 Localização Atual

**Projeto:** Plano de Desenvolvimento - 2 Meses em Web + IA  
**Semana:** X de 8  
**Dia:** X de 7 ([Dia da semana], [Data])  
**Diretório:** `Semanas/SemanaX/DiaX/`

---

## 🎯 Estado Atual do Projeto

### O que foi feito:
- ✅ Dia X-1: [Resumo]
- ✅ Dia X-2: [Resumo]

### O que está em progresso:
- 🟡 Dia X: [Objetivo atual]

### O que falta fazer (hoje):
- [ ] [Tarefa 1]
- [ ] [Tarefa 2]
- [ ] [Tarefa 3]

---

## 📋 Estrutura de Arquivos

### Arquivos Obrigatórios (ordem padrão):
- `README.md` - Contexto e objetivos do dia
- `CONTEXTO_AGENTE.md` - Este arquivo (contexto técnico)
- `checklist.md` - Checklist detalhado com fases
- `journal.md` - Template para reflexão
- `requirements.txt` - Dependências Python (obrigatório sempre, mesmo que vazio)
- `CONTEXTO_PROXIMO_DIA.md` - Guia para construir próximo dia (obrigatório para todos os dias)

### Arquivos de Aprendizado (conforme nível de scaffolding):
[Listar arquivos específicos do nível: exemplo_completo.py, template.py, GUIA_APRENDIZADO.md, etc.]

---

## 🔑 Informações Importantes

### Stack Tecnológica:
- **Linguagem:** [Python/TypeScript/etc]
- **APIs:** [APIs utilizadas]
- **Ferramentas:** [Ferramentas necessárias]

### Configuração Necessária:
- [Configurações específicas]

### Objetivo do Dia:
[Objetivo detalhado]

---

## 🗺️ Próximos Passos

### Imediato (hoje):
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

### Próximo Dia:
- [O que será feito no próximo dia]

---

## 📚 Referências Rápidas

[Links e recursos úteis]

---

**Última atualização:** [Data]  
**Status:** 🟡 Em progresso
```

### checklist.md

```markdown
# ✅ Checklist - Dia X ([Dia da semana], [Data])

## 🎯 Objetivo do Dia
[Objetivo claro e específico]

---

> Todas as fases abaixo devem caber dentro dos **160min totais**, englobando leitura, exercícios/testes e preenchimento dos documentos. Não use autocomplete/IA para escrever o código.

## 📋 FASE 1: [Nome da Fase] ([Tempo estimado])

### [Subfase 1]
- [ ] [Tarefa específica e mensurável]
- [ ] [Tarefa específica e mensurável]

**Como fazer:**
[Instruções passo-a-passo detalhadas]

**Por que:**
[Explicação do propósito]

**Tempo estimado:** [X] minutos  
**Quando:** [Momento do dia]

---

## 📋 FASE 2: [Nome da Fase] ([Tempo estimado])

[Repetir estrutura da Fase 1]

---

## 🎉 CONCLUSÃO

**Total estimado:** 160min no total (inclui leitura dos documentos, execução de exercícios/testes e preenchimento de checklist + journal, **sem usar autocomplete/IA para gerar código**)

### ✅ Critérios de Sucesso:
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

### 🎯 Streak: X/56 dias

**Parabéns por completar o Dia X!** 🚀

---

**Última atualização:** [Data]
```

### journal.md

```markdown
# 📝 Journal - Dia X ([Dia da semana], [Data])

## 🎯 Objetivo do Dia
[Objetivo do dia]

---

## ✅ O que foi feito hoje?

### Manhã/Tarde
- [ ] [Tarefa 1]
- [ ] [Tarefa 2]

### Detalhes das Tarefas
_(Preencher ao longo do dia)_

---

## 🎓 O que aprendi hoje?

### Conceitos Novos
- 

### Ferramentas Utilizadas
- 

### Desafios Enfrentados
- 

---

## 💡 Insights e Reflexões

### O que funcionou bem?
- 

### O que poderia ser melhorado?
- 

### Próximos Passos
- 

---

## 📊 Métricas do Dia

- **Tempo total:** ___ horas
- **Commits:** ___
- **Linhas de código:** ___
- [Outras métricas relevantes]

---

## 🔗 Links e Referências Úteis

- 

---

## 📝 Notas Adicionais

_(Espaço livre para anotações)_

---

**Data:** [Data]  
**Status:** 🟡 Em progresso
```

### CONTEXTO_PROXIMO_DIA.md

```markdown
# 🎯 Contexto para Construir o Dia X+1

## 📚 O que aprendemos hoje (Dia X)

### Conceitos Principais
- [Conceito 1]
- [Conceito 2]
- [Conceito 3]

### Habilidades Desenvolvidas
- [Habilidade 1]
- [Habilidade 2]

### Código Criado
- [Arquivo/Funcionalidade 1]
- [Arquivo/Funcionalidade 2]

---

## 🔗 Por que o Dia X+1 é importante

[Explicação de como o próximo dia se relaciona com o aprendizado atual]

---

## 🎯 O que será feito no Dia X+1

### Objetivo Principal
[Objetivo do próximo dia]

### Conceitos que serão aprendidos
- [Conceito 1]
- [Conceito 2]

### Como se relaciona com Dia X
[Explicação da conexão]

---

## 📋 Como Construir o Dia X+1

### 1. Criar Estrutura Básica
```
DiaX+1/
├── README.md
├── CONTEXTO_AGENTE.md
├── checklist.md
└── journal.md
```

**Ordem sugerida:**
1. Criar pasta `DiaX+1/`
2. Copiar templates de `TEMPLATE_ESTRUTURA_DIA.md`
3. Preencher README.md com contexto do próximo dia
4. Criar CONTEXTO_AGENTE.md
5. Criar checklist.md detalhado

### 2. Definir Nível de Scaffolding

**Nível recomendado:** [1, 2 ou 3]

**Arquivos necessários:**
- [Listar arquivos específicos do nível]

### 3. Criar Arquivos de Aprendizado

**Se Nível 1:**
- Criar `exemplo_completo.py` com código completo comentado
- Criar `GUIA_PASSO_A_PASSO.md` muito detalhado

**Se Nível 2:**
- Criar `template.py` com TODOs
- Criar `GUIA_APRENDIZADO.md` com conceitos + passo-a-passo
- Criar `exemplo_referencia.py` para consulta

**Se Nível 3:**
- Criar `especificacoes.md` com requisitos
- Criar `GUIA_CONCEITOS.md` com conceitos teóricos
- Criar `exercicios.md` com desafios

### 4. Seguir Checklist

[Referência ao checklist.md do próximo dia]

---

## 📚 Recursos de Preparação

### O que revisar antes de começar:
- [ ] [Conceito/Arquivo 1]
- [ ] [Conceito/Arquivo 2]

### Recursos úteis para ler:
- [Link 1] - [Descrição]
- [Link 2] - [Descrição]

### Conceitos pré-requisitos:
- [Conceito 1]
- [Conceito 2]

---

## 💡 Dicas Importantes

1. **Consistência:** Seguir estrutura padrão definida em `TEMPLATE_ESTRUTURA_DIA.md`
2. **Scaffolding:** Usar nível apropriado conforme `METODOLOGIA_ENSINO.md`
3. **Contexto:** Sempre incluir relação com dias anteriores
4. **Clareza:** Objetivos devem ser claros e mensuráveis

---

**Última atualização:** [Data]
```

---

## 🎓 Níveis de Scaffolding - Arquivos Específicos

**⚠️ IMPORTANTE:** Os níveis de scaffolding são determinados pelo **CONCEITO**, não pela posição temporal (dia/semana). Cada conceito novo começa no Nível 1, independente de ser Dia 1 da Semana 1 ou Dia 1 da Semana 2.

**Regra de Decisão:**
- **Nível 1:** Conceito completamente novo, primeira exposição
- **Nível 2:** Conceito parcialmente conhecido, aplicação em novo contexto
- **Nível 3:** Conceitos conhecidos, aplicação independente

**Exemplos práticos:**
- Semana 1, Dia 1: Nível 1 (conceito novo: usar APIs diretamente)
- Semana 2, Dia 1: Nível 1 (conceito novo: LangChain)
- Semana 2, Dia 2: Nível 2 (conceito parcialmente conhecido: já sabe LangChain básico, agora aplica em chains)

### Nível 1: Iniciante
**Quando usar:** Conceitos completamente novos, primeira exposição

**Arquivos adicionais:**
- `exemplo_completo.py` - Código completo comentado linha por linha
- `GUIA_PASSO_A_PASSO.md` - Tutorial muito detalhado

**Estrutura do exemplo_completo.py:**
```python
#!/usr/bin/env python3
"""
[Nome do Script]

Este script demonstra [conceito principal].

Uso:
    python exemplo_completo.py [argumentos]
"""

# ============================================================================
# SEÇÃO 1: IMPORTS
# ============================================================================
# Por que precisamos destes imports:
# - [Biblioteca 1]: Para [propósito]
# - [Biblioteca 2]: Para [propósito]

import os  # Operações com sistema de arquivos
from dotenv import load_dotenv  # Carregar variáveis de ambiente

# ============================================================================
# SEÇÃO 2: CONFIGURAÇÃO
# ============================================================================
# PASSO 1: Carregar variáveis de ambiente
load_dotenv()  # Carrega arquivo .env na raiz do projeto

# PASSO 2: [Outra configuração]
# [Explicação]

# ============================================================================
# SEÇÃO 3: FUNÇÕES
# ============================================================================
def minha_funcao(parametro: str) -> str:
    """
    [Descrição da função]
    
    Por que esta função é necessária: [Explicação]
    
    Args:
        parametro: [Descrição]
    
    Returns:
        str: [Descrição]
    
    Example:
        >>> resultado = minha_funcao("teste")
        >>> print(resultado)
    """
    # PASSO 1: [O que este passo faz]
    resultado = f"Processando: {parametro}"
    
    # PASSO 2: [O que este passo faz]
    # [Mais código comentado]
    
    return resultado

# ============================================================================
# SEÇÃO 4: EXECUÇÃO PRINCIPAL
# ============================================================================
if __name__ == "__main__":
    # Por que usamos __name__ == "__main__": [Explicação]
    resultado = minha_funcao("exemplo")
    print(resultado)
```

### Nível 2: Intermediário
**Quando usar:** Conceitos parcialmente conhecidos, aplicação em novo contexto

**Arquivos adicionais:**
- `template.py` - Estrutura com TODOs
- `GUIA_APRENDIZADO.md` - Conceitos + passo-a-passo
- `exemplo_referencia.py` - Exemplo completo para consulta
- `exercicios.md` - Exercícios guiados

**Estrutura do template.py:**
```python
#!/usr/bin/env python3
"""
[Nome do Script] - Template

TODO: Preencher docstring explicando o propósito do script
"""

# TODO: Importar bibliotecas necessárias
# Dica: Consulte exemplo_referencia.py para ver quais imports são necessários

# TODO: Configurar ambiente
# Dica: Use load_dotenv() para carregar variáveis de ambiente

def minha_funcao(parametro: str) -> str:
    """
    TODO: Escrever docstring completa
    
    Args:
        parametro: TODO - Descrever parâmetro
    
    Returns:
        str: TODO - Descrever retorno
    
    Dica: Consulte exemplo_referencia.py se precisar de ajuda
    """
    # TODO: Implementar lógica aqui
    # Dica 1: [Dica específica]
    # Dica 2: [Outra dica]
    pass

if __name__ == "__main__":
    # TODO: Implementar execução principal
    pass
```

### Nível 3: Avançado
**Quando usar:** Conceitos conhecidos, aplicação independente

**Arquivos adicionais:**
- `especificacoes.md` - Requisitos e objetivos
- `GUIA_CONCEITOS.md` - Conceitos teóricos resumidos
- `exercicios.md` - Desafios independentes

**Estrutura do especificacoes.md:**
```markdown
# Especificações - [Nome do Projeto]

## Objetivo
[Objetivo claro e específico]

## Requisitos Funcionais
1. [Requisito 1]
2. [Requisito 2]
3. [Requisito 3]

## Requisitos Técnicos
- [Requisito técnico 1]
- [Requisito técnico 2]

## Referências
- Ver exemplo em: [caminho para exemplo]
- Conceitos em: GUIA_CONCEITOS.md
- Padrões em: [referência]

## Desafio
Implemente [objetivo] seguindo as especificações acima.
```

---

## ✅ Checklist para Criar Novo Dia

- [ ] Criar pasta `DiaX/`
- [ ] Copiar templates deste arquivo
- [ ] Preencher README.md com contexto específico
- [ ] Criar CONTEXTO_AGENTE.md
- [ ] Criar checklist.md detalhado
- [ ] Criar journal.md
- [ ] Definir nível de scaffolding (usar `GUIAS/GUIA_DECISAO_SCAFFOLDING.md`)
- [ ] Criar arquivos específicos do nível escolhido
- [ ] Criar CONTEXTO_PROXIMO_DIA.md usando `TEMPLATE_CONTEXTO_PROXIMO_DIA.md` (OBRIGATÓRIO para todos os dias)
- [ ] Criar requirements.txt (OBRIGATÓRIO, mesmo que vazio)
- [ ] Revisar consistência com dias anteriores

**📚 Guia Completo:** Consulte `GUIAS/GUIA_CRIAR_NOVO_DIA.md` para processo passo-a-passo detalhado.

---

**Última atualização:** 2 Dez 2025  
**Versão:** 2.0

