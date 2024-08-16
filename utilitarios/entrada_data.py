from datetime import datetime

from utilitarios.validar_generic import ValidarDadosGeneric


def validar_data() -> datetime:
    """
    Valida uma string de data no formato 'DD/MM/AAAA'.

    Args:
        data_str (str): A string representando a data a ser validada.

    Returns:
        datetime: Objeto datetime se a data for válida.

    Raises:
        ValidarDadosGeneric: Se a data não estiver no formato correto ou for inválida.
    """
    while True:
        try:
            data_str = input('Digite uma data em um formato válido.')
            data_valida = datetime.strptime(data_str, '%d/%m/%Y')
            return data_valida

        except ValueError as e:
            print('Data inválida, por favor. Digite no formato esperado - Exemplo: 18/01/2024 (dd/mm/yyyy)')
