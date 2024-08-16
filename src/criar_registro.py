from utilitarios.calcular_tempo import tempo
from utilitarios.entrada_data import validar_data #?
from utilitarios.validar_generic import ValidarDadosGeneric #?
from datetime import datetime

def criar_registro():
    """Cria um novo registro financeiro com interação do usuário."""
    while True:
        data = input('Digite a data da movimentação (dd/mm/aaaa): ')
        try:
            data = datetime.strptime(data, '%d/%m/%Y')
            break
        except ValueError:
            print('Erro, digite a data de acordo com o exemplo: 01/01/2000')
    while True:
        tipo = input("Digite o tipo de movimentação (Receita, Despesa ou Investimento): ").capitalize()
        if tipo in ['Receita','Despesa','Investimento']:
            break
        else:
            print('Erro, tipo invalido')
    while True:
        valor = input("Digite o valor: ")
        try:
            valor = float(valor)
            break
        except ValueError:
            print('Digite apenas valores numericos')

    montante = None
    rendimento = None

    if tipo == 'Investimento':
        montante_inicial = valor * (1+0.0005)**(tempo(data))
        montante = round(montante_inicial, 2)
        rendimento_inicial = montante - valor
        rendimento = round(rendimento_inicial, 2)

    registro = {
        'data': { 'data': data, 
                 'dia': f'{data.day:02}',
                 'mês': f'{data.month:02}',
                 'ano':f'{data.year:02}'}
        'tipo': tipo,
        'valor': valor if tipo != 'Despesa' else -valor, 
        'montante': montante,
        'rendimento': rendimento}

    return registro
