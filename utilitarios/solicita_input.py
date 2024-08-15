from utilitarios.validar_generic import ValidarDadosGeneric
from utilitarios.validar_data import validar_data
from typing import Callable


def solicitar_input(tipo_input: str, *args: any) -> any:
    """
    Solicita ao usuário que insira uma data no formato 'DD/MM/AAAA' e valida a entrada.

    Returns:
        datetime: Objeto datetime correspondente à data inserida e validada.
    """
    while True:

        data_msg = {
            'data': 'Digite a data no formato DD/MM/AAAA: ',
            'entrada': 'Por favor, digite um número inteiro Válido: '
        }

        valor_input = input(data_msg[tipo_input])

        data_func = {
            'data': validar_data
            'entrada': print
        }


        try:
            return data_func[tipo_input](valor_input)
        except ValidarDadosGeneric as e:
            print(e)


if __name__ == '__main__':
    solicitar_input('data')
