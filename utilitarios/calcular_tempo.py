from datetime import datetime, timedelta


def tempo(data):
    data_convertido = datetime.strptime(data, '%d/%m/%Y')
    data_referencia = datetime.now()
    diferenca = data_referencia - data_convertido
    diferenca_days = diferenca.days
    return diferenca_days
