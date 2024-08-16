import csv
import json


def ler_registros(arquivo):
    """Lê os registros financeiros do arquivo JSON."""

    try:
        with open(arquivo, 'r') as f:
            registros = json.load(f)
    except FileNotFoundError:
        print('Ainda não há nenhum registro')
        registros = []  # Cria uma lista vazia se o arquivo não existir

    return registros
