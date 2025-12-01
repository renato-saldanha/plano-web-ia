"""
## 📋 Exercício 2: CLI com Subcomandos (Nível Intermediário)

### Objetivo
Criar um CLI com múltiplos subcomandos.

### Tarefa
Crie um script `2-cli_subcomandos.py` que tenha dois subcomandos:
    1. `somar` - Soma dois números
    2. `multiplicar` - Multiplica dois números

    ### Exemplo de uso:
    ```bash
    python 2-cli_subcomandos.py somar --a 5 --b 3
    # Saída: Resultado: 8

    python 2-cli_subcomandos.py multiplicar --a 4 --b 7
    # Saída: Resultado: 28
    ```
"""

import argparse
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%H:%M:%S',
)

def add_parser_args(parser):
    """
    Adiciona os argumentos ao parser
    :param parser: Parser do argparse
    :return: None
    """
    parser.add_argument("--a", required = True, type = int, help = "Primeiro número")
    parser.add_argument("--b", required = True, type = int, help = "Segundo número")

def main():
    """
    Função principal    
    :return: None
    """

    # Cria o parser principal
    arg_parser = argparse.ArgumentParser(
        description = "Exemplo CLI com multiplos subcomandos",
        epilog = "Exemplo de uso: python 2-cli_subcomandos.py somar --a 10 --b 20"
    )

    # Cria o subparser para as operações matemáticas
    sub_parser = arg_parser.add_subparsers(dest = "operacao", help = "Operação matemática a ser realizada")
    
    # Cria o parser para a operação de soma
    parser_somar = sub_parser.add_parser("somar", help = "Realiza a operação de soma")
    # Adiciona os argumentos ao parser da operação de soma
    add_parser_args(parser_somar)

    # Cria o parser para a operação de subtração
    parser_subtrair = sub_parser.add_parser("subtrair", help = "Realiza a operação de subtração")
    # Adiciona os argumentos ao parser da operação de subtração
    add_parser_args(parser_subtrair)

    parser_multiplicar = sub_parser.add_parser("multiplicar", help = "Realiza a operação de multiplicação")
    add_parser_args(parser_multiplicar)

    parser_dividir = sub_parser.add_parser("dividir", help = "Realiza a operação de divisão")
    add_parser_args(parser_dividir)

    # Faz o parse dos argumentos
    args = arg_parser.parse_args()

    # Faz o match da operação matemática
    match args.operacao:
        case "somar":
            resultado = args.a + args.b
        case "subtrair":
            resultado = args.a - args.b
        case "multiplicar":
            resultado = args.a * args.b
        case "dividir":
            resultado = args.a / args.b
        case _:
            logging.error("Operação inválida")
            return

    logging.info(f"Resultado da operação: {resultado}")


if __name__ == "__main__":
    main()