from utilitarios.validar_data import validar_data
from utilitarios.validar_generic import ValidarDadosGeneric


def solicitar_input(tipo_input: str, *args: any) -> any:
    """
    Solicita ao usuário que insira uma data no formato 'DD/MM/AAAA' e valida a entrada.
    Returns:
        datetime: Objeto datetime correspondente à data inserida e validada.
    """
    data_func = {
        'data': {
            'func': validar_data,
            'msg':'Digite a data no formato DD/MM/AAAA: '}}
    
    
    
    try:
        valor_input = data_func[tipo_input]['func'](valor_input, args)
        print(args)
        return valor_input
    except ValidarDadosGeneric as e:
        print(e)


if __name__ == '__main__':
    solicitar_input('data')
