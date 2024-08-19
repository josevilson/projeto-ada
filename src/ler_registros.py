import csv
import json


def ler_registros(arquivo: str) -> list[dict]:
    
    '''
     Lê os registros de um arquivo JSON.

    Essa função tenta abrir os registros a partir de um arquivo JSON.
    Se o arquivo não for encontrado, ela retorna uma lista vazia e exibe uma mensagem de erro.

    Args:
        arquivo (str): 
            O caminho do arquivo a ser lido.

    Returns:
        list[Dict]: 
            Retorna uma lista de dicionários com os registros financeiros.
     '''
    
    try:
        with open(arquivo, 'r') as f:
            registros = json.load(f)
    except FileNotFoundError:
        print('Ainda não há nenhum registro')
        registros = []  # Cria uma lista vazia se o arquivo não existir


    return registros
