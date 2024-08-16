from datetime import datetime


def atualiza_rendimento(registros): #necessário algumas mudanças
    """Atualiza o rendimento dos investimentos."""

    hoje = datetime.now()

    for registro in registros:
        if registro['tipo'] == 'Investimento':
            data_investimento = datetime.strptime(registro['data'], '%d/%m/%Y')
            dias = (hoje - data_investimento).days
            montante = float(registro['montante'])
            taxa_juros = 0.0005  # o juros deve ser solicitado ao usuário
            rendimento = montante * (1 + taxa_juros) ** dias - montante
            registro['rendimento'] = rendimento