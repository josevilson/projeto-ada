def validar_valor(msg: str = "Digite o valor: ") -> float:
    '''
    Valida a entrada de um valor numérico inserida pelo usuário.
    
    Returns:
        float: 
            Retorna o valor validado.
    '''
    while True:
        valor = input(msg).replace(',', '.')
        try: 
            valor = float(valor)
            if valor < 0:
                raise ValueError('Digite apenas valores numericos e positivos')
            return valor
        except ValueError:
            print('Digite apenas valores numericos e positivos')

def validar_tipo(msg: str) -> str:
    '''
    Valida a entrada de um tipo de movimentação inserida pelo usuário.

    Returns:
        str: 
            Retorna o tipo de movimentação validado ('Receita', 'Despesa' ou 'Investimento').
    '''
    while True:
        tipo = input(msg).capitalize()
        if tipo in ['Receita','Despesa','Investimento']:
            return tipo
        else:
            print('Erro, tipo invalido')

def validar_indice(registros: list[dict]) -> int:
    '''
    Valida a entrada de um índice para exclusão de registros financeiros.

    Args:
        registros (list[dict]): 
            Lista de registros financeiros para verificar o índice válido.

    Returns:
        int: 
            O índice validado.
    '''
    while True:
        try:
            indice = int(input('digite o indice: '))
            if 0 <= indice < len(registros):
                return indice
            else:
                print(f'Digite índices de 0 a {len(registros) - 1}')
        except ValueError:
            print('Digite apenas números inteiros')
