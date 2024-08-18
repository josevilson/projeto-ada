def validar_valor():
    while True:
        valor = input("Digite o valor: ")
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print('Digite apenas valores numericos')

def validar_tipo():
    while True:
        tipo = input("Digite o tipo de movimentação (Receita, Despesa ou Investimento): ").capitalize()
        if tipo in ['Receita','Despesa','Investimento']:
            return tipo
        else:
            print('Erro, tipo invalido')

def validar_indice():
    while True:
        try:
            indice = input('digite o indice do registro que deseja excluir: ')
            if 0 <= indice < len(registros):
                return indice
            else:
                print(f'O índice deve estar entre 0 e {len(registros) - 1}')
        except ValueError:
            print('Digite apenas números inteiros')
