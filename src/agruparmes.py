from datetime import datetime

from utilitarios.validacao import validar_tipo


def agrupar_por(registros: list[dict]) -> None:
    '''
    Agrupa os registros por mês e tipo, calculando o total de cada um.

    Args:
        registros (List[Dict]): 
            Lista de dicionários contendo os registros financeiros.
            Cada registro contém uma chave 'data' com outra chave 'data_completa',
            e uma chave 'tipo' para categorizar o registro.

    Returns:
        None: 
           Imprime o resultado dos agrupamentos, mas não retorna nenhum valor.
    '''
    
    tipo_desejado = validar_tipo('Digite o tipo que deseja agrupar. [Receita, Despesa, Investimento]: ')
    while True:
        mes_desejado = input('Digite o mês e ano que deseja agrupar (mm/aaaa): ')
        try:
            mes_desejado = datetime.strptime(mes_desejado, '%m/%Y').strftime('%m/%Y')
            break
        except ValueError:
            print('Digite o mês e o ano de acordo com o exemplo: 05/2000')

    total_rendimento = 0
    valor = 0

    nenhum_registro = True

    for registro in registros:
        mes = datetime.strptime(registro['data']['data_completa'], '%d/%m/%Y').strftime('%m/%Y')
        if mes == mes_desejado and registro['tipo'] == tipo_desejado:
            nenhum_registro = False
            if tipo_desejado == 'Investimento':
                valor += float(registro['valor'])
                total_rendimento += float(registro.get('rendimento', 0))
            else:
                valor += float(registro['valor'])

    if nenhum_registro:
        print(f'Nenhum registro encontrado para {mes_desejado} com o tipo {tipo_desejado}.')
    else:
        if tipo_desejado == 'Investimento':
            print(f'Total investido em {mes_desejado}: {valor}')
            print(f'Total do rendimento em {mes_desejado}: {total_rendimento}')
        else:
            print(f'Total para {mes_desejado} ({tipo_desejado}): {valor}')
