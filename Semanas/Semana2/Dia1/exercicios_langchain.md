# 📝 Exercícios Guiados: LangChain Básico

Estes exercícios ajudam a consolidar o aprendizado do LangChain através de prática guiada e progressiva.

**Importante:** Tente resolver cada exercício antes de consultar a solução. A prática é essencial para aprender!

---

## 📋 Índice

1. [Exercício 1: Hello LangChain](#exercício-1-hello-langchain)
2. [Exercício 2: Prompt Template](#exercício-2-prompt-template)
3. [Exercício 3: Chain Básico](#exercício-3-chain-básico)
4. [Exercício 4: Comparação Detalhada](#exercício-4-comparação-detalhada)

---

## Exercício 1: Hello LangChain

### Objetivo
Criar seu primeiro script usando LangChain, equivalente ao `hello_ai_groq.py` da Semana 1.

### Tarefa
Crie um script chamado `meu_hello_langchain.py` que:
1. Usa LangChain com Groq
2. Envia um prompt simples
3. Imprime a resposta

### Passos Guiados

**Passo 1:** Criar arquivo `meu_hello_langchain.py`

**Passo 2:** Adicionar imports necessários
```python
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
```

**Passo 3:** Carregar variáveis de ambiente
```python
load_dotenv()
```

**Passo 4:** Criar instância do LLM
```python
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)
```

**Passo 5:** Criar mensagem e invocar LLM
```python
message = HumanMessage(content="Olá! Me apresente em 2 frases.")
response = llm.invoke([message])
print(response.content)
```

### Teste
Execute o script:
```bash
python meu_hello_langchain.py
```

Deve imprimir uma resposta do LLM.

### Comparação
Compare com `hello_ai_groq.py` da Semana 1:
- Quantas linhas cada um tem?
- Qual é mais legível?
- Qual é mais fácil de entender?

### Solução

<details>
<summary>Clique para ver solução completa</summary>

```python
#!/usr/bin/env python3
"""
Meu Hello LangChain
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Carregar variáveis de ambiente
load_dotenv()

# Criar LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Criar mensagem
message = HumanMessage(content="Olá! Me apresente em 2 frases.")

# Invocar LLM
response = llm.invoke([message])

# Imprimir resposta
print(response.content)
```

</details>

---

## Exercício 2: Prompt Template

### Objetivo
Criar um script que usa prompts dinâmicos (com variáveis).

### Tarefa
Crie um script chamado `gerador_explicacao.py` que:
1. Recebe um tópico como variável
2. Gera uma explicação sobre o tópico
3. Usa SystemMessage para definir comportamento

### Passos Guiados

**Passo 1:** Criar arquivo `gerador_explicacao.py`

**Passo 2:** Adicionar imports
```python
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
```

**Passo 3:** Criar função que recebe tópico
```python
def gerar_explicacao(topic: str):
    # Seu código aqui
    pass
```

**Passo 4:** Criar SystemMessage
```python
system_message = SystemMessage(
    content="Você é um professor experiente. "
            "Explique conceitos de forma clara e didática."
)
```

**Passo 5:** Criar HumanMessage com tópico
```python
user_message = HumanMessage(
    content=f"Explique o que é {topic} em 3 frases."
)
```

**Passo 6:** Invocar LLM e retornar resposta
```python
llm = ChatGroq(model="llama-3.1-8b-instant")
response = llm.invoke([system_message, user_message])
return response.content
```

### Teste
```python
if __name__ == "__main__":
    explicacao = gerar_explicacao("Python")
    print(explicacao)
```

Execute e teste com diferentes tópicos:
- "Python"
- "Machine Learning"
- "Web Development"

### Desafio Extra
Modifique para aceitar número de frases como parâmetro:
```python
def gerar_explicacao(topic: str, num_frases: int = 3):
    # Modifique para usar num_frases no prompt
    pass
```

### Solução

<details>
<summary>Clique para ver solução completa</summary>

```python
#!/usr/bin/env python3
"""
Gerador de Explicações com LangChain
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

def gerar_explicacao(topic: str, num_frases: int = 3):
    """
    Gera explicação sobre um tópico usando LangChain.
    
    Args:
        topic: Tópico a explicar
        num_frases: Número de frases na explicação
    
    Returns:
        str: Explicação gerada
    """
    # Criar LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
    )
    
    # Criar SystemMessage
    system_message = SystemMessage(
        content="Você é um professor experiente. "
                "Explique conceitos de forma clara e didática."
    )
    
    # Criar HumanMessage com tópico
    user_message = HumanMessage(
        content=f"Explique o que é {topic} em {num_frases} frases."
    )
    
    # Invocar LLM
    response = llm.invoke([system_message, user_message])
    
    return response.content

if __name__ == "__main__":
    # Testar com diferentes tópicos
    topicos = ["Python", "Machine Learning", "Web Development"]
    
    for topico in topicos:
        print(f"\n{'='*60}")
        print(f"Tópico: {topico}")
        print('='*60)
        explicacao = gerar_explicacao(topico)
        print(explicacao)
```

</details>

---

## Exercício 3: Chain Básico

### Objetivo
Entender o conceito de Chain no LangChain (sequência de operações).

### Tarefa
Crie um script chamado `chain_simples.py` que:
1. Cria uma chain simples usando o operador `|`
2. Aplica a chain em um prompt
3. Entende como chains funcionam

### Conceito: Chains

**O que é uma Chain?**
Uma chain é uma sequência de operações conectadas. No LangChain, você pode criar chains usando o operador `|` (pipe).

**Exemplo básico:**
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Criar prompt template
prompt = ChatPromptTemplate.from_template("Explique {topic}")

# Criar LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

# Criar chain: prompt → llm
chain = prompt | llm

# Usar chain
response = chain.invoke({"topic": "Python"})
```

### Passos Guiados

**Passo 1:** Criar arquivo `chain_simples.py`

**Passo 2:** Adicionar imports
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
```

**Passo 3:** Criar prompt template
```python
prompt = ChatPromptTemplate.from_template(
    "Explique o que é {conceito} em {num_frases} frases."
)
```

**Passo 4:** Criar LLM
```python
llm = ChatGroq(model="llama-3.1-8b-instant")
```

**Passo 5:** Criar chain
```python
chain = prompt | llm
```

**Passo 6:** Usar chain
```python
response = chain.invoke({
    "conceito": "Python",
    "num_frases": 3
})
print(response.content)
```

### Teste
Execute e teste com diferentes conceitos e números de frases.

### Por que Chains são Úteis?
- **Reutilizáveis:** Crie uma vez, use muitas vezes
- **Combináveis:** Conecte múltiplas operações
- **Legíveis:** Código mais claro e intuitivo

### Solução

<details>
<summary>Clique para ver solução completa</summary>

```python
#!/usr/bin/env python3
"""
Exemplo de Chain Básico com LangChain
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Criar prompt template
prompt = ChatPromptTemplate.from_template(
    "Explique o que é {conceito} em {num_frases} frases."
)

# Criar LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Criar chain: prompt → llm
chain = prompt | llm

# Usar chain
if __name__ == "__main__":
    conceitos = [
        {"conceito": "Python", "num_frases": 3},
        {"conceito": "Machine Learning", "num_frases": 5},
        {"conceito": "Web Development", "num_frases": 2}
    ]
    
    for entrada in conceitos:
        print(f"\n{'='*60}")
        print(f"Conceito: {entrada['conceito']}")
        print('='*60)
        response = chain.invoke(entrada)
        print(response.content)
```

</details>

---

## Exercício 4: Comparação Detalhada

### Objetivo
Reescrever um script da Semana 1 usando LangChain e comparar.

### Tarefa
Escolha um script da Semana 1 (ex: `gerador_conteudo_blog.py`) e:
1. Reescreva usando LangChain
2. Compare linhas de código
3. Compare legibilidade
4. Compare facilidade de manutenção

### Scripts da Semana 1 para Escolher

- `Semana1/Dia1/hello_ai_groq.py` - Hello AI básico
- `Semana1/Dia2/gerador_conteudo_blog.py` - Gerador de conteúdo
- `Semana1/Dia3/analisador_sentimentos.py` - Analisador (mais complexo)

### Passos Guiados

**Passo 1:** Escolher script da Semana 1

**Passo 2:** Ler e entender código manual

**Passo 3:** Reescrever usando LangChain

**Passo 4:** Criar tabela comparativa:

| Aspecto | Código Manual | LangChain |
|---------|---------------|-----------|
| Linhas de código | ? | ? |
| Legibilidade | ? | ? |
| Facilidade de manutenção | ? | ? |
| Trocar LLM | ? | ? |

**Passo 5:** Anotar vantagens e desvantagens

### Exemplo: Reescrever hello_ai_groq.py

**Código Manual (Semana 1):**
```python
from groq import Groq
client = Groq(api_key=api_key)
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Olá!"}],
    model="llama-3.1-8b-instant"
)
print(response.choices[0].message.content)
```

**Código LangChain:**
```python
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

llm = ChatGroq(model="llama-3.1-8b-instant")
message = HumanMessage(content="Olá!")
response = llm.invoke([message])
print(response.content)
```

**Comparação:**
- Linhas: Similar (~5-6 linhas cada)
- Legibilidade: LangChain mais intuitivo
- Trocar LLM: LangChain muito mais fácil

### Desafio Extra
Reescreva `gerador_conteudo_blog.py` usando LangChain com:
- SystemMessage para definir estilo
- Prompt template para diferentes temas
- Chain para simplificar código

### Solução Parcial

<details>
<summary>Clique para ver exemplo de reescrita</summary>

```python
#!/usr/bin/env python3
"""
Gerador de Conteúdo para Blog - Versão LangChain
Reescrito do Semana1/Dia2/gerador_conteudo_blog.py
"""

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

def gerar_conteudo_blog(tema: str):
    """
    Gera conteúdo para blog usando LangChain.
    
    Args:
        tema: Tema do conteúdo
    
    Returns:
        str: Conteúdo gerado
    """
    # Criar LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7
    )
    
    # SystemMessage define estilo
    system_message = SystemMessage(
        content="Você é um escritor profissional de blog. "
                "Escreva conteúdo claro, envolvente e informativo."
    )
    
    # HumanMessage com tema
    user_message = HumanMessage(
        content=f"Escreva um parágrafo introdutório sobre {tema} "
                f"para um blog. Seja claro e envolvente."
    )
    
    # Invocar LLM
    response = llm.invoke([system_message, user_message])
    
    return response.content

if __name__ == "__main__":
    tema = "Inteligência Artificial"
    conteudo = gerar_conteudo_blog(tema)
    print(conteudo)
```

</details>

---

## ✅ Checklist de Conclusão

Complete os exercícios e marque:

- [ ] Exercício 1: Hello LangChain criado e funcionando
- [ ] Exercício 2: Prompt Template criado e testado
- [ ] Exercício 3: Chain básico entendido e implementado
- [ ] Exercício 4: Comparação detalhada feita
- [ ] Todos os scripts executam sem erros
- [ ] Comparação com código manual documentada

---

## 🎯 Próximos Passos

Após completar os exercícios:

1. **Reflita:** O que você aprendeu?
2. **Compare:** Qual abordagem prefere? Por quê?
3. **Pratique:** Crie seu próprio script usando LangChain
4. **Prepare:** Dia 2 - Chains e sequências mais avançadas

---

## 💡 Dicas

1. **Não tenha pressa:** Leia cada exercício cuidadosamente
2. **Tente primeiro:** Não consulte solução antes de tentar
3. **Experimente:** Modifique exemplos para entender melhor
4. **Compare sempre:** Sempre compare com código manual da Semana 1
5. **Documente:** Anote suas descobertas no journal

---

**Última atualização:** 1 Dez 2025  
**Boa prática!** 🚀

