import csv
import json
from utilitarios.entrada_data import validar_data
from utilitarios.validacao import validar_tipo, validar_valor

def ler_registros_por(arquivo: list[dict]) -> list[dict]:
    
    '''
     Recebe todos os registros e realiza filtros de acordo com os critérios escolhidos.

    Filtra por Data, Tipo ou Valor.

    Args:
        list[Dict]: 
            Todos os registros.

    Returns:
        list[Dict]: 
            Retorna uma lista de dicionários com os registros financeiros.
     '''
    registros = arquivo

    while True:
        print("\n--- Ler registros ---")
        print("1. Por Data")
        print("2. Por Tipo")
        print("3. Por valor")
        print("9. Todos")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nova_data = validar_data('Data pela qual deseja filtrar: ')
            registros_filtrados = []
            for registro in registros:
                if registro['data'] == nova_data:
                    registros_filtrados.append(registro)
            break
        if opcao == '2':
            tipo = validar_tipo('Digite o tipo que deseja filtrar. [Receita, Despesa, Investimento]: ')
            registros_filtrados = []
            for registro in registros:
                if registro['tipo'] == tipo:
                    registros_filtrados.append(registro)
            break
        if opcao == '3':
            novo_valor = validar_valor("Digite o valor pelo qual filtrar: ")
            registros_filtrados = []
            for registro in registros:
                if abs(registro['valor']) == novo_valor:
                    registros_filtrados.append(registro)
            break
        if opcao == '9':
            registros_filtrados = registros
            break
        else:
            print("Escolha uma opção válida")
            continue

    return registros_filtrados
