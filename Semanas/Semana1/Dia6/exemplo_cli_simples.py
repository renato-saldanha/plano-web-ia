#!/usr/bin/env python3
"""
Exemplo Simples de CLI - Referência Comentada

Este arquivo mostra um exemplo completo e comentado de como criar um CLI básico.
Use como referência ao implementar seu CLI integrado.

Este exemplo demonstra:
- Como criar parser básico
- Como adicionar subcomandos
- Como criar menu interativo
- Como integrar com funções existentes
"""

import argparse
import sys
import logging

# ============================================================================
# SEÇÃO 1: CONFIGURAÇÃO INICIAL
# ============================================================================

# Configurar logging para feedback ao usuário
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
)

# ============================================================================
# SEÇÃO 2: FUNÇÕES DE COMANDO
# ============================================================================

def comando_saudacao(nome: str) -> None:
    """
    Exemplo de função de comando simples.
    
    Esta função recebe um nome e imprime uma saudação.
    No seu CLI real, você substituiria isso por chamadas às funções
    dos dias anteriores.
    
    Args:
        nome: Nome da pessoa a saudar
    """
    logging.info(f"Processando saudação para: {nome}")
    print(f"Olá, {nome}! 👋")
    logging.info("✅ Saudação processada com sucesso!")


def comando_calcular(operacao: str, a: float, b: float) -> None:
    """
    Exemplo de função de comando com múltiplos argumentos.
    
    Esta função demonstra como processar diferentes tipos de operações.
    No seu CLI real, isso seria substituído por comandos como 'blog', 
    'sentimentos', 'resumir'.
    
    Args:
        operacao: Tipo de operação ('soma', 'subtracao', etc)
        a: Primeiro número
        b: Segundo número
    """
    logging.info(f"Calculando: {a} {operacao} {b}")
    
    try:
        if operacao == 'soma':
            resultado = a + b
        elif operacao == 'subtracao':
            resultado = a - b
        elif operacao == 'multiplicacao':
            resultado = a * b
        elif operacao == 'divisao':
            if b == 0:
                logging.error("❌ Divisão por zero não permitida!")
                sys.exit(1)
            resultado = a / b
        else:
            logging.error(f"❌ Operação inválida: {operacao}")
            sys.exit(1)
        
        print(f"Resultado: {resultado}")
        logging.info("✅ Cálculo realizado com sucesso!")
    
    except Exception as e:
        logging.error(f"❌ Erro ao calcular: {e}")
        sys.exit(1)


# ============================================================================
# SEÇÃO 3: MENU INTERATIVO
# ============================================================================

def mostrar_menu() -> str:
    """
    Mostrar menu interativo e retornar escolha do usuário.
    
    Esta função cria uma interface visual no terminal.
    No seu CLI real, você adaptaria as opções para seus comandos.
    
    Returns:
        Escolha do usuário como string
    """
    print("\n" + "=" * 60)
    print("🤖 CLI de Exemplo")
    print("=" * 60)
    print("\nEscolha uma opção:")
    print("  1. Saudação")
    print("  2. Calcular")
    print("  3. Sair")
    print("\n" + "-" * 60)
    
    escolha = input("\nDigite o número da opção: ").strip()
    return escolha


def processar_menu() -> None:
    """
    Processar escolha do menu interativo.
    
    Esta função cria um loop que mostra o menu e processa escolhas
    até o usuário decidir sair.
    
    No seu CLI real, você adaptaria para chamar seus comandos reais.
    """
    while True:
        escolha = mostrar_menu()
        
        if escolha == "1":
            # Opção 1: Saudação
            nome = input("\nDigite seu nome: ").strip()
            if nome:
                comando_saudacao(nome)
            else:
                print("❌ Nome não pode estar vazio!")
        
        elif escolha == "2":
            # Opção 2: Calcular
            print("\nOperações disponíveis: soma, subtracao, multiplicacao, divisao")
            operacao = input("Digite a operação: ").strip().lower()
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                comando_calcular(operacao, a, b)
            except ValueError:
                print("❌ Números inválidos!")
        
        elif escolha == "3":
            # Opção 3: Sair
            print("\n👋 Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida! Escolha um número de 1 a 3.")
        
        # Pausa antes de mostrar menu novamente
        input("\nPressione Enter para continuar...")


# ============================================================================
# SEÇÃO 4: CONFIGURAÇÃO DO PARSER
# ============================================================================

def criar_parser() -> argparse.ArgumentParser:
    """
    Criar parser de argumentos para o CLI.
    
    Esta função configura todos os argumentos e subcomandos do CLI.
    No seu CLI real, você adaptaria para seus comandos específicos.
    
    Returns:
        Parser configurado com todos os argumentos
    """
    # Criar parser principal
    parser = argparse.ArgumentParser(
        description="CLI de Exemplo - Demonstração de argparse",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  %(prog)s saudacao --nome "João"
  %(prog)s calcular --operacao soma --a 10 --b 5
  %(prog)s  # Menu interativo
        """
    )
    
    # Criar subparsers para diferentes comandos
    subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')
    
    # Subcomando: saudacao
    parser_saudacao = subparsers.add_parser(
        'saudacao',
        help='Saudar uma pessoa'
    )
    parser_saudacao.add_argument(
        '--nome',
        required=True,
        help='Nome da pessoa a saudar'
    )
    
    # Subcomando: calcular
    parser_calcular = subparsers.add_parser(
        'calcular',
        help='Realizar cálculo matemático'
    )
    parser_calcular.add_argument(
        '--operacao',
        required=True,
        choices=['soma', 'subtracao', 'multiplicacao', 'divisao'],
        help='Tipo de operação matemática'
    )
    parser_calcular.add_argument(
        '--a',
        type=float,
        required=True,
        help='Primeiro número'
    )
    parser_calcular.add_argument(
        '--b',
        type=float,
        required=True,
        help='Segundo número'
    )
    
    return parser


# ============================================================================
# SEÇÃO 5: FUNÇÃO PRINCIPAL
# ============================================================================

def main() -> None:
    """
    Função principal do CLI.
    
    Esta função:
    1. Cria o parser
    2. Parseia os argumentos da linha de comando
    3. Se nenhum comando foi passado, mostra menu interativo
    4. Se comando específico foi passado, executa o comando
    5. Trata erros adequadamente
    """
    # Criar parser
    parser = criar_parser()
    
    # Parsear argumentos
    # Se nenhum argumento foi passado, args.comando será None
    args = parser.parse_args()
    
    # Se nenhum comando foi passado, mostrar menu interativo
    if not args.comando:
        processar_menu()
        return
    
    # Processar comando específico
    try:
        if args.comando == 'saudacao':
            comando_saudacao(args.nome)
        
        elif args.comando == 'calcular':
            comando_calcular(args.operacao, args.a, args.b)
        
        else:
            # Se comando não reconhecido, mostrar ajuda
            parser.print_help()
            sys.exit(1)
    
    except KeyboardInterrupt:
        # Usuário pressionou Ctrl+C
        print("\n\n⚠️ Operação cancelada pelo usuário.")
        sys.exit(130)
    
    except Exception as e:
        # Qualquer outro erro
        logging.error(f"❌ Erro ao executar comando: {e}")
        sys.exit(1)


# ============================================================================
# SEÇÃO 6: EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    """
    Por que usamos __name__ == "__main__"?
    
    Isso garante que o código só execute quando o script é rodado diretamente,
    não quando é importado como módulo em outro script.
    
    Isso é uma boa prática em Python.
    """
    main()

