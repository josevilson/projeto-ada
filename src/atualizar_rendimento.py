from datetime import datetime


def atualiza_rendimento(registros): #necessário algumas mudanças
    """Atualiza o rendimento dos investimentos."""

    hoje = datetime.now()

    for registro in registros:
        if registro['tipo'] == 'Investimento':
            data_investimento = datetime.strptime(registro['data']['data_completa'], '%d/%m/%Y')
            dias = (hoje - data_investimento).days
            capital = float(registro['valor'])
            taxa_juros = 0.01  # o juros deve ser solicitado ao usuário
            rendimento = capital * (1 + taxa_juros) ** dias - capital
            montante = capital * (1 + taxa_juros) ** dias
            registro['rendimento'] = round(rendimento, 2)
            registro['montante'] = round(montante, 2)
