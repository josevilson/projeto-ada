from datetime import datetime


def agrupar_por_mes(registros):
    """Agrupa os registros por mês e calcula o total de cada mês."""

    resultado = {}
    for registro in registros:
        mes = datetime.strptime(registro['data'], '%d/%m/%Y').strftime('%m/%Y')
        if mes in resultado:
            resultado[mes] += float(registro['valor'])
        else:
            resultado[mes] = float(registro['valor'])

    return resultado