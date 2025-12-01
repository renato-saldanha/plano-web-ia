"""
## 📋 Exercício 1: CLI Básico (Nível Iniciante)

### Objetivo
Criar um CLI simples que aceita um argumento e imprime uma mensagem.

### Tarefa
Crie um script `1-cli_simples.py` que:
- Aceita um argumento `--nome` (obrigatório)
- Imprime "Olá, [nome]!"

### Exemplo de uso:
```bash
python 1-cli_simples.py --nome "João"
# Saída: Olá, João!
```
"""

import argparse
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%H:%M:%S',
)

# arg_parser.add_argument("arquivo", type = str, help = "Arquivo a ser processado")
# arg_parser.add_argument("--tema", type = str, help = "Tema do arquivo")

def main():
    """
    Função que recebe o nome e a idade do usuário e mostra uma mensagem de boas-vindas
    :return: None
    """
    
    # Cria o parser principal
    arg_parser = argparse.ArgumentParser(
        description = "Exemplo CLI Simples",
        epilog = "Exemplo de uso: python 1-cli_simples.py --nome 'João' --idade 30"
    )

    # Adiciona os argumentos ao parser
    arg_parser.add_argument("--nome", required = True, type = str, help="Seu nome")
    arg_parser.add_argument("--idade", required = True, type = int, help="Sua idade")

    # Faz o parse dos argumentos
    args = arg_parser.parse_args()

    # Mostra a mensagem de boas-vindas
    logging.info(f"Olá, {args.nome}! Bem-vindo ao exemplo de CLI.")
    logging.info(f"Sua idade é {args.idade} anos.")

# Executa a função principal
if __name__ == "__main__":
    main()