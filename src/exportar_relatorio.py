import csv
import json
def exportar_relatorio(registros, arquivo, formato='csv'):
    """Exporta um relatório dos registros financeiros."""

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