from utilitarios.calcular_tempo import tempo
from utilitarios.entrada_data import validar_data
from utilitarios.validar_generic import ValidarDadosGeneric


def criar_registro(): #separar dia, mes e ano
    """Cria um novo registro financeiro com interação do usuário."""

    data = validar_data('Insira uma data no formáto válido, dd/mm/yyyy')
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

        juros = 0.01

        montante_inicial = valor * (1+((juros)))**(tempo(data['data_completa']))
        montante = round(montante_inicial, 2)
        rendimento_inicial = montante - valor
        rendimento = round(rendimento_inicial, 2)

    registro = {
        'id': 0,
        'data': data,
        'tipo': tipo,
        'valor': valor if tipo != 'Despesa' else -valor, 
        'montante': montante,
        'rendimento': rendimento}

    return registro
