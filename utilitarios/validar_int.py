from utilitarios.validar_generic import ValidarDadosGeneric


def input_int(numero_range) -> int:
    """
    Valida uma string de data no formato 'DD/MM/AAAA'.

    Args:
        data_str (str): A string representando a data a ser validada.

    Returns:
        datetime: Objeto datetime se a data for válida.

    Raises:
        ValidarDadosGeneric: Se a data não estiver no formato correto ou for inválida.
    """
    while:
        try:
            valor_inteiro = int(valor_inteiro)
            if valor_inteiro in range(numero_range):
                return valor_inteiro

        except ValueError as e:
            print('Digite um número inteiro Válido.')

