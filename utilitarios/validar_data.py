from datetime import datetime

from utilitarios.validar_generic import ValidarDadosGeneric


def validar_data(data_str: str) -> datetime:
    """
    Valida uma string de data no formato 'DD/MM/AAAA'.

    Args:
        data_str (str):
        A string representando a data a ser validada.

    Returns:
        datetime:
        Objeto datetime se a data for válida.

    Raises:
        DadosInvalidos:
        Se a data não estiver no formato correto ou  inválida.
    """
    try:
        # Tenta converter a string para um objeto datetime
        data_valida = datetime.strptime(data_str, '%d/%m/%Y')
        return data_valida
    except ValueError as e:
        raise ValidarDadosGeneric('xd')
