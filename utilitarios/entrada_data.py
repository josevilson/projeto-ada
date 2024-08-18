from datetime import datetime

from utilitarios.validar_generic import ValidarDadosGeneric


def validar_data(msg: str) -> dict:
    """
    Valida uma string de data no formato 'DD/MM/AAAA' e retorna um dicionário com dia, mês, ano e a data completa como strings.

    Returns:
        dict: Dicionário contendo dia, mês, ano e a data completa separados como strings.

    Raises:
        ValidarDadosGeneric: Se a data não estiver no formato correto ou for inválida.
    """
    while True:
        try:
            data_str = input(f"{msg} \n")

            data_valida = datetime.strptime(data_str, '%d/%m/%Y')
            
            dia = str(data_valida.day).zfill(2)
            mes = str(data_valida.month).zfill(2)
            ano = str(data_valida.year)
            
            data = f"{dia}/{mes}/{ano}"
            
            data_dict = {
                "data_completa": data,
                "dia": dia,
                "mes": mes,
                "ano": ano  
            }
            
            return data_dict

        except ValueError:
            print('Data inválida. Por favor, digite no formato esperado - Exemplo: 18/01/2024 (DD/MM/AAAA)') 

