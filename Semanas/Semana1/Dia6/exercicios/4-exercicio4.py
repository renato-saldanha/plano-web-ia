"""

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

"""

import argparse
import logging
from funcoes import processar_texto

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%H:%M:%S',
)

def main():
    """

    Função principal
    :return: None
    """

    # Cria o parser principal
    arg_parser = argparse.ArgumentParser(
        description = "Integração de funções existentes ao CLI",
        epilog = "Exemplo de uso: python 4-exercicio4.py processar --texto 'Olá, mundo!'"
    )

    # Cria o subparser para as operações matemáticas
    sub_parser = arg_parser.add_subparsers(dest = "tipo", help = "Tipo de processamento")

    # Cria o parser para a operação de processar
    parser_processar = sub_parser.add_parser("processar", help = "Processa o texto")
    parser_processar.add_argument("--texto", required = True, type = str, help = "Texto a ser processado")
    
    # Faz o parse dos argumentos
    args = arg_parser.parse_args()

    # Faz o match da operação matemática
    match args.tipo:
        case "processar":
            resultado = processar_texto(args.texto)
            logging.info(f"Resultado do processamento: {resultado}")
        case _:
            logging.error("Tipo de processamento inválido")
            return


if __name__ == "__main__":
    main()