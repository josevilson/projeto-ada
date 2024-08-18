from utilitarios.calcular_tempo import tempo
from utilitarios.entrada_data import validar_data
from utilitarios.validacao import validar_indice, validar_tipo, validar_valor
from utilitarios.validar_generic import ValidarDadosGeneric
from datetime import datetime

def criar_registro(): #separar dia, mes e ano
    """Cria um novo registro financeiro com interação do usuário."""

    data = validar_data('Insira uma data no formáto válido, dd/mm/yyyy')
    tipo = validar_tipo()
    valor = validar_valor()

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
        'rendimento': rendimento
        'data_atualizacao': None
        
        }

    return registro
