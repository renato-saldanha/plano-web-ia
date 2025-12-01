# 📚 Guia de Aprendizado: CLI (Command Line Interface)

## 🎯 O que você vai aprender

Neste guia, você aprenderá:
1. O que é CLI e por que usar
2. Como criar CLI em Python usando `argparse`
3. Padrões de design para interfaces de linha de comando
4. Como integrar múltiplos scripts em um CLI unificado

---

## 📖 Parte 1: Conceitos Teóricos

### O que é CLI?

**CLI (Command Line Interface)** é uma interface de usuário baseada em texto onde você interage com programas através de comandos escritos no terminal.

**Exemplos de CLIs populares:**
- `git` - Controle de versão
- `docker` - Containerização
- `npm` - Gerenciador de pacotes Node.js
- `pip` - Gerenciador de pacotes Python

### Por que usar CLI?

**Vantagens:**
- ✅ Automatização fácil (scripts, CI/CD)
- ✅ Mais rápido para tarefas repetitivas
- ✅ Funciona em qualquer ambiente (servidor, local)
- ✅ Pode ser integrado em outros sistemas
- ✅ Menos recursos do que interfaces gráficas

**Quando usar:**
- Ferramentas de desenvolvimento
- Scripts de automação
- Ferramentas para servidores
- Utilitários que serão usados em scripts

### Estrutura de um CLI

Um CLI geralmente tem esta estrutura:

```
comando [subcomando] [opções] [argumentos]
```

**Exemplos:**
```bash
git commit -m "mensagem"          # comando + opção + argumento
docker run -d nginx               # comando + subcomando + opções
python script.py --tema "Python"  # script + opção + argumento
```

---

## 📖 Parte 2: argparse - Biblioteca Python para CLI

### O que é argparse?

`argparse` é uma biblioteca **built-in** do Python (não precisa instalar) que facilita a criação de interfaces de linha de comando profissionais.

### Conceitos Básicos

#### 1. ArgumentParser
Cria o parser principal que gerencia todos os argumentos.

```python
import argparse

parser = argparse.ArgumentParser(
    description="Descrição do seu programa",
    epilog="Texto de ajuda adicional"
)
```

#### 2. Argumentos Posicionais
Argumentos obrigatórios que aparecem na ordem especificada.

```python
parser.add_argument('arquivo', help='Caminho do arquivo')
# Uso: python script.py arquivo.txt
```

#### 3. Opções (Flags)
Argumentos opcionais que começam com `--` ou `-`.

```python
parser.add_argument('--tema', help='Tema do conteúdo')
# Uso: python script.py --tema "Python"
```

#### 4. Subcomandos
Comandos diferentes dentro do mesmo programa.

```python
subparsers = parser.add_subparsers(dest='comando')
parser_blog = subparsers.add_parser('blog', help='Gerar conteúdo')
# Uso: python script.py blog --tema "Python"
```

---

## 📖 Parte 3: Passo-a-Passo Básico

### Passo 1: Criar Parser Básico

```python
import argparse

# Criar parser principal
parser = argparse.ArgumentParser(
    description="Meu CLI de exemplo",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Adicionar argumento simples
parser.add_argument('--nome', required=True, help='Seu nome')

# Parsear argumentos
args = parser.parse_args()

# Usar argumentos
print(f"Olá, {args.nome}!")
```

**Teste:**
```bash
python script.py --nome "João"
# Saída: Olá, João!
```

### Passo 2: Adicionar Subcomandos

```python
import argparse

parser = argparse.ArgumentParser(description="CLI com subcomandos")

# Criar subparsers
subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')

# Subcomando 1: blog
parser_blog = subparsers.add_parser('blog', help='Gerar conteúdo para blog')
parser_blog.add_argument('--tema', required=True, help='Tema do blog')

# Subcomando 2: resumir
parser_resumir = subparsers.add_parser('resumir', help='Resumir texto')
parser_resumir.add_argument('--texto', required=True, help='Texto a resumir')

# Parsear e processar
args = parser.parse_args()

if args.comando == 'blog':
    print(f"Gerando conteúdo sobre: {args.tema}")
elif args.comando == 'resumir':
    print(f"Resumindo: {args.texto}")
```

**Teste:**
```bash
python script.py blog --tema "Python"
python script.py resumir --texto "Texto longo aqui"
```

### Passo 3: Menu Interativo (Opcional)

Você pode criar um menu interativo quando nenhum comando é passado:

```python
import argparse

def mostrar_menu():
    print("\n=== Menu ===")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    return input("Escolha: ")

def processar_menu():
    while True:
        escolha = mostrar_menu()
        if escolha == "1":
            # Processar opção 1
            pass
        elif escolha == "2":
            # Processar opção 2
            pass
        elif escolha == "3":
            break

parser = argparse.ArgumentParser()
args = parser.parse_args()

# Se nenhum argumento, mostrar menu
if len(sys.argv) == 1:
    processar_menu()
```

---

## 📖 Parte 4: Padrões de Design CLI

### 1. Mensagens de Ajuda Claras

Sempre forneça ajuda útil:

```python
parser.add_argument(
    '--tema',
    required=True,
    help='Tema do conteúdo a ser gerado (ex: "Python", "IA")'
)
```

### 2. Validação de Entrada

Valide entradas antes de usar:

```python
parser.add_argument('--llm', choices=['groq', 'gemini'], default='groq')
# Só aceita 'groq' ou 'gemini'
```

### 3. Tratamento de Erros

Trate erros de forma amigável:

```python
try:
    args = parser.parse_args()
except SystemExit:
    # argparse já mostra ajuda, apenas sair
    sys.exit(1)
except Exception as e:
    print(f"Erro: {e}")
    sys.exit(1)
```

### 4. Mensagens Informativas

Use logging ou print para feedback:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Processando arquivo...")
logging.error("Erro ao processar!")
```

### 5. Exit Codes

Use códigos de saída apropriados:

```python
import sys

if erro:
    sys.exit(1)  # Erro
else:
    sys.exit(0)  # Sucesso
```

---

## 📖 Parte 5: Integrando Scripts Existentes

### Como Integrar Funções de Outros Scripts

**Opção 1: Importar diretamente**

```python
# No seu CLI
from Semanas.Semana1.Dia2.gerador_conteudo_blog import gerar_conteudo_tema

def comando_blog(tema: str):
    resultado = gerar_conteudo_tema(tema)
    print(resultado)
```

**Opção 2: Criar wrappers**

```python
# Wrapper que adapta a função para o CLI
def comando_blog(tema: str):
    """
    Wrapper para gerar conteúdo de blog via CLI.
    """
    try:
        resultado = gerar_conteudo_tema(tema)
        logging.info("✅ Conteúdo gerado com sucesso!")
        return resultado
    except Exception as e:
        logging.error(f"❌ Erro: {e}")
        sys.exit(1)
```

---

## 📖 Parte 6: Estrutura Completa de um CLI

### Estrutura Recomendada

```python
#!/usr/bin/env python3
"""
CLI Integrado - Descrição
"""

import argparse
import sys
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Importar funções dos scripts anteriores
# from ... import ...

def comando_1(parametro: str) -> None:
    """Processar comando 1"""
    pass

def comando_2(parametro: str) -> None:
    """Processar comando 2"""
    pass

def mostrar_menu() -> str:
    """Mostrar menu interativo"""
    pass

def processar_menu() -> None:
    """Processar escolhas do menu"""
    pass

def criar_parser() -> argparse.ArgumentParser:
    """Criar parser de argumentos"""
    parser = argparse.ArgumentParser(...)
    # Configurar parser
    return parser

def main() -> None:
    """Função principal"""
    parser = criar_parser()
    args = parser.parse_args()
    
    if not args.comando:
        processar_menu()
    else:
        # Processar comando específico
        pass

if __name__ == "__main__":
    main()
```

---

## 🎓 Recursos Adicionais

### Documentação Oficial
- [argparse - Python Docs](https://docs.python.org/3/library/argparse.html)
- [CLI Design Guidelines](https://clig.dev/)

### Exemplos de CLIs Python
- [Click Framework](https://click.palletsprojects.com/) - Alternativa ao argparse
- [Typer](https://typer.tiangolo.com/) - CLI moderno baseado em type hints

### Boas Práticas
- Sempre forneça `--help` automático
- Use mensagens de erro claras
- Valide entradas
- Use logging para feedback
- Documente cada comando

---

## ✅ Checklist de Aprendizado

Antes de começar a implementar, certifique-se de entender:

- [ ] O que é CLI e quando usar
- [ ] Como criar parser básico com argparse
- [ ] Como adicionar argumentos e opções
- [ ] Como criar subcomandos
- [ ] Como criar menu interativo (opcional)
- [ ] Como integrar funções de outros scripts
- [ ] Padrões de design CLI

---

**Próximo passo:** Ver `template_cli.py` para ver estrutura com TODOs, ou `exemplo_cli_simples.py` para exemplo completo comentado.

---

**Última atualização:** 30 Nov 2025

