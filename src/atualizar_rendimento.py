from datetime import datetime
from typing import Union


def atualiza_rendimento(registros: list[dict]) -> None: #necessário algumas mudanças
    '''Atualiza o rendimento dos investimentos informados pelo usuário.
    
            A função calcula cada registro de 'investimento' com base na data da aplicação e na taxa juros informada pelo usuário.
            O rendimento será adicionado ao registro 'rendimento'.
    
        Args:
            registros (list[dict]): lista de dicionários que recebe str e float
                Cada dicionário representa um registro financeiro. 
                Cada registro contém as chaves 'valor' (valor do investimento), 'tipo' (tipo do registro),
                e 'data' (data do investimento).
            
         Returns:
            None: 
                Não retorna nenhum valor, apenas atualiza o registro.
    '''

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
            registro['data_atualizacao'] = datetime.now().strftime("%d/%m/%Y")
