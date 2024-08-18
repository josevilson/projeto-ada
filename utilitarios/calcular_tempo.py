from datetime import datetime, timedelta


def tempo(data: str) -> int:
    '''
    Faz o cálculo da diferença em dias entre a data fornecida e a data atual,
    baseado na conversão do formato 'dd/mm/aaaa' para 'datetime'.

    Args:
        data (str): 
            Recebe a data em formato de string no (dd/mm/aaaa).

    Returns:
        int: 
            Retorna a diferença em dias entre a data fornecida e a data atual.
    '''
    data_convertido = datetime.strptime(data, '%d/%m/%Y')
    data_referencia = datetime.now()
    diferenca = data_referencia - data_convertido
    diferenca_days = diferenca.days
    return diferenca_days
