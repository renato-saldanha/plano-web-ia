import logging
import os


# Função para criar um diretório
def criar_diretorio(caminho: str) -> None:
    """
    Cria um diretório se não existir.
    
    Args:
        caminho: str - O caminho do diretório
    Returns:
        None
    """
    if not os.path.exists(caminho):
        os.makedirs(caminho, exist_ok=True)
        logging.info(f"✅ Diretório criado: {caminho}")


# Função para salvar arquivo
def salvar_arquivo(caminho: str, conteudo: str) -> None:
    """
    Salva um arquivo.
    
    Args:
        caminho: str - O caminho do arquivo
        conteudo: str - O conteúdo do arquivo
    """

    try:
        if os.path.exists(caminho):
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(conteudo)
    except PermissionError:
        raise PermissionError(f"⚠️ Arquivo está aberto ou bloqueado: {caminho}"
                        "\n   Feche o arquivo no editor e tente novamente.")
        return
    