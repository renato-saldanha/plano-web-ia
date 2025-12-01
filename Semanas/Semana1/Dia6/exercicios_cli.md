# 🏋️ Exercícios: CLI em Python

Estes exercícios são progressivos - comece pelo primeiro e avance conforme se sentir confortável.

---

## 📋 Exercício 1: CLI Básico (Nível Iniciante)

### Objetivo
Criar um CLI simples que aceita um argumento e imprime uma mensagem.

### Tarefa
Crie um script `exercicio1.py` que:
- Aceita um argumento `--nome` (obrigatório)
- Imprime "Olá, [nome]!"

### Exemplo de uso:
```bash
python exercicio1.py --nome "João"
# Saída: Olá, João!
```

### Dica
Consulte `GUIA_CLI.md` seção "Passo 1: Criar Parser Básico"

### Solução
<details>
<summary>Clique para ver solução</summary>

```python
import argparse

parser = argparse.ArgumentParser(description="CLI básico")
parser.add_argument('--nome', required=True, help='Seu nome')
args = parser.parse_args()

print(f"Olá, {args.nome}!")
```
</details>

---

## 📋 Exercício 2: CLI com Subcomandos (Nível Intermediário)

### Objetivo
Criar um CLI com múltiplos subcomandos.

### Tarefa
Crie um script `exercicio2.py` que tenha dois subcomandos:
1. `somar` - Soma dois números
2. `multiplicar` - Multiplica dois números

### Exemplo de uso:
```bash
python exercicio2.py somar --a 5 --b 3
# Saída: Resultado: 8

python exercicio2.py multiplicar --a 4 --b 7
# Saída: Resultado: 28
```

### Dica
Consulte `GUIA_CLI.md` seção "Passo 2: Adicionar Subcomandos"

### Solução
<details>
<summary>Clique para ver solução</summary>

```python
import argparse

parser = argparse.ArgumentParser(description="CLI com subcomandos")
subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')

# Subcomando somar
parser_somar = subparsers.add_parser('somar', help='Somar dois números')
parser_somar.add_argument('--a', type=float, required=True)
parser_somar.add_argument('--b', type=float, required=True)

# Subcomando multiplicar
parser_mult = subparsers.add_parser('multiplicar', help='Multiplicar dois números')
parser_mult.add_argument('--a', type=float, required=True)
parser_mult.add_argument('--b', type=float, required=True)

args = parser.parse_args()

if args.comando == 'somar':
    resultado = args.a + args.b
    print(f"Resultado: {resultado}")
elif args.comando == 'multiplicar':
    resultado = args.a * args.b
    print(f"Resultado: {resultado}")
```
</details>

---

## 📋 Exercício 3: Menu Interativo (Nível Intermediário)

### Objetivo
Criar um menu interativo quando nenhum comando é passado.

### Tarefa
Modifique `cli_menu_interativo.py` para que:
- Se nenhum comando for passado, mostre um menu interativo
- O menu permita escolher entre somar ou multiplicar
- O menu continue até o usuário escolher sair

### Exemplo de uso:
```bash
python cli_menu_interativo.py
# Mostra menu interativo
```

### Dica
Consulte `GUIA_CLI.md` seção "Passo 3: Menu Interativo"

### Solução
<details>
<summary>Clique para ver solução</summary>

```python
import argparse

def mostrar_menu():
    print("\n=== Menu ===")
    print("1. Somar")
    print("2. Multiplicar")
    print("3. Sair")
    return input("Escolha: ")

def processar_menu():
    while True:
        escolha = mostrar_menu()
        if escolha == "1":
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a + b}")
        elif escolha == "2":
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a * b}")
        elif escolha == "3":
            break
        input("\nPressione Enter para continuar...")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='comando')
# ... (subcomandos do exercício anterior)

args = parser.parse_args()

if not args.comando:
    processar_menu()
else:
    # Processar comando da linha de comando
    pass
```
</details>

---

## 📋 Exercício 4: Integração com Função Existente (Nível Avançado)

### Objetivo
Integrar uma função de outro script no CLI.

### Tarefa
1. Crie um arquivo `funcoes.py` com uma função:
   ```python
   def processar_texto(texto: str) -> str:
       return texto.upper()
   ```

2. Crie um CLI `exercicio4.py` que:
   - Importa a função de `funcoes.py`
   - Tem um comando `processar` que aceita `--texto`
   - Chama a função e mostra o resultado

### Exemplo de uso:
```bash
python exercicio4.py processar --texto "olá mundo"
# Saída: OLÁ MUNDO
```

### Dica
Consulte `GUIA_CLI.md` seção "Parte 5: Integrando Scripts Existentes"

### Solução
<details>
<summary>Clique para ver solução</summary>

```python
import argparse
from funcoes import processar_texto

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='comando')

parser_processar = subparsers.add_parser('processar', help='Processar texto')
parser_processar.add_argument('--texto', required=True)

args = parser.parse_args()

if args.comando == 'processar':
    resultado = processar_texto(args.texto)
    print(resultado)
```
</details>

---

## 📋 Exercício 5: CLI Completo - Desafio Final (Nível Avançado)

### Objetivo
Criar um CLI completo integrando os scripts dos dias anteriores.

### Tarefa
Crie um CLI `cli_automatizacoes.py` que:
1. Tem 3 subcomandos: `blog`, `sentimentos`, `resumir`
2. Integra funções dos dias 2, 3 e 4
3. Tem menu interativo quando nenhum comando é passado
4. Trata erros adequadamente
5. Usa logging para feedback

### Requisitos:
- Comando `blog --tema "Python"` → chama função do Dia 2
- Comando `sentimentos --arquivo reviews.txt` → chama funções do Dia 3
- Comando `resumir --pdf arquivo.pdf --llm groq` → chama função do Dia 4
- Menu interativo com todas as opções

### Dica
Use `template_cli.py` como base e preencha os TODOs.

### Solução
<details>
<summary>Clique para ver solução (após tentar primeiro!)</summary>

Consulte `cli_automatizacoes.py` na pasta `solucoes/` (se disponível) ou implemente baseado nos exercícios anteriores.
</details>

---

## ✅ Checklist de Progresso

Marque conforme completar:

- [ X] Exercício 1 completo
- [ X] Exercício 2 completo
- [ X] Exercício 3 completo
- [ X] Exercício 4 completo
- [ X] Exercício 5 completo (desafio final)

---

## 💡 Dicas Gerais

1. **Sempre teste:** Execute cada exercício após completar
2. **Consulte recursos:** Use `GUIA_CLI.md` e `exemplo_cli_simples.py` quando necessário
3. **Trate erros:** Adicione tratamento de erros desde o início
4. **Use logging:** Facilita debug e feedback ao usuário
5. **Documente:** Adicione docstrings e comentários úteis

---

## 🎯 Próximo Passo

Após completar os exercícios, você está pronto para implementar o CLI integrado usando `template_cli.py`!

---

**Última atualização:** 30 Nov 2025

