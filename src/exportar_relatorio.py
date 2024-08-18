import csv
import json


def exportar_relatorio(registros: list[dict], arquivo: str, formato: str = 'csv') -> None:

    '''Exporta o relatório dos registros financeiros para um arquivo nos formatos CSV ou JSON.
    
         Args:
            registros (list[dict]): 
                Recebe uma lista de dicionários onde cada dicionário representa um registro.
            arquivo (str): 
                Nome do arquivo de saída para o relatório.
            formato (str): 
                Formato do arquivo de saída, que pode ser 'csv' ou 'json'.
                
        Returns:
            None: 
                Não retorna nenhum valor, apenas vai exportar os registros para o arquivo especificado.
    '''
    if formato == 'csv':
        try:
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                cabecalho = registros[0].keys() if registros else []
                writer = csv.DictWriter(f, fieldnames=cabecalho)
                writer.writeheader()
                writer.writerows(registros)
            print("Relatório exportado com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar relatório CSV: {e}")
    elif formato == 'json':
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(registros, f, indent=4, ensure_ascii=False)
            print("Relatório exportado com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar relatório JSON: {e}")
    else:
        print("Formato inválido. Use 'csv' ou 'json'.")