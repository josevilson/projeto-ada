from datetime import datetime
from utilitarios.validar_generic import ValidarDadosGeneric


def validar_data(data_str: str, *args: any) -> datetime:
    """
    Valida uma string de data no formato 'DD/MM/AAAA'.

    Args:
        data_str (str): A string representando a data a ser validada.

    Returns:
        datetime: Objeto datetime se a data for válida.

    Raises:
        ValidarDadosGeneric: Se a data não estiver no formato correto ou for inválida.
    """
    try:
        data_valida = datetime.strptime(data_str, '%d/%m/%Y')
        return data_valida
    except ValueError:
        raise ValidarDadosGeneric(f"\n\n ******************************* \n Data inválida: \n Você digitou: {data_str} \n Esperando o formato DD/MM/AAAA \n Exemplo: 31/01/2024. \n******************************* \n\n")