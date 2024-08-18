import json


def salvar_registros(registros: list[dict], arquivo: str) -> None:
    '''
    Salva os registros no arquivo JSON.

    Grava uma lista de registros em um arquivo JSON.

    Args:
        registros: list[dict]
            Lista de dicionários que contém os registros a serem salvos.
        arquivo (str): 
            Caminho do arquivo onde os registros serão salvos.

    Returns:
        Não retorna nada, apenas salva os registros.
    '''

    with open(arquivo, 'w') as f:
        json.dump(registros, f, indent=4)
