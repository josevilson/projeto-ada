from datetime import datetime

def agrupar_por_mes(registros):
    """Agrupa os registros por mês e calcula o total de cada mês."""
    while True:
        mes_desejado = input('Digite o mês e ano que deseja agrupar (mm/aaaa): ')
        try:
            mes_desejado = datetime.strptime(mes_desejado, '%m/%Y').strftime('%m/%Y')
            break
        except ValueError:
            print('Digite o mês e o ano de acordo com o exmeplo: 05/2000')

    resultado = {}
    
    for registro in registros:
        mes = datetime.strptime(registro['data'], '%d/%m/%Y').strftime('%m/%Y')
        if mes == mes_desejado:
            if mes in resultado:
                resultado[mes] += float(registro['valor'])
            else:
                resultado[mes] = float(registro['valor'])

    if not resultado:
        return print(f'Nenhum registro encontrado para {mes_desejado}.')
    else:
        return resultado
