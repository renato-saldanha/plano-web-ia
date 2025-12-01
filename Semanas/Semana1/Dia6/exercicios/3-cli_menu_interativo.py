"""
## 📋 Exercício 3: Menu Interativo (Nível Intermediário)

### Objetivo
Criar um menu interativo quando nenhum comando é passado.

### Tarefa
Modifique `3-cli_menu_interativo.py` para que:
- Se nenhum comando for passado, mostre um menu interativo
- O menu permita escolher entre somar ou multiplicar
- O menu continue até o usuário escolher sair

### Exemplo de uso:
```bash
python 3-cli_menu_interativo.py
# Mostra menu interativo
"""

import argparse
import logging
import sys

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
    return None

def mostrar_menu():
    """
    Mostra o menu interativo
    :return: None
    """
    logging.info("Menu ------")
    logging.info("1. Somar")
    logging.info("2. Subtrair")
    logging.info("3. Multiplicar")
    logging.info("4. Dividir")
    logging.info("0. Sair")
    logging.info("--------------------------------")
    return int(input("Selecione a operação: "))

def processar_operacao(sub_parser):
    """
    Processa a operação matemática
    :param sub_parser: Subparser do argparse
    :return: None
    """

    # Loop infinito para mostrar o menu interativo
    while True:        
        opcao = mostrar_menu()
        if opcao == 0:
            break
        elif opcao == 1:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            resultado = a + b
            logging.info(f"Resultado da operação: {resultado}")
        elif opcao == 2:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            resultado = a - b
            logging.info(f"Resultado da operação: {resultado}")
        elif opcao == 3:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            resultado = a * b
            logging.info(f"Resultado da operação: {resultado}")
        elif opcao == 4:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            resultado = a / b
            logging.info(f"Resultado da operação: {resultado}")
        else:
            logging.error("Operação inválida")

    logging.info("=" * 40)


def main():
    """
    Função principal
    :return: None
    """

    # Cria o parser principal
    arg_parser = argparse.ArgumentParser(
        description = "Exemplo de CLI com menu interativo",
        epilog = "Exemplo de uso: python 3-cli_menu_interativo.py"
    )

    # Cria o subparser para as operações matemáticas
    sub_parser = arg_parser.add_subparsers(dest = "operacao", help = "Operação matemática a ser realizada")

    # Se nenhum comando for passado, mostra o menu interativo
    if len(sys.argv) == 1:
        processar_operacao(sub_parser)
        return
    else:
        # Adiciona os argumentos ao parser
        arg_parser.add_argument("--a", required = True, type = int, help = "Primeiro número")
        arg_parser.add_argument("--b", required = True, type = int, help = "Segundo número")
        
    # Cria o parser para a operação de soma
    parser_somar = sub_parser.add_parser("somar", help = "Realiza a operação de soma")
    add_parser_args(parser_somar)

    # Cria o parser para a operação de subtração
    parser_subtrair = sub_parser.add_parser("subtrair", help = "Realiza a operação de subtração")
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

    # Mostra o resultado da operação
    logging.info(f"Resultado da operação: {resultado}")
    

# Executa a função principal
if __name__ == "__main__":
    main()