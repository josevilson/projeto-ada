from datetime import datetime

from utilitarios.calcular_tempo import tempo
from utilitarios.entrada_data import validar_data
from utilitarios.validacao import validar_indice, validar_tipo, validar_valor
from utilitarios.validar_generic import ValidarDadosGeneric


def criar_registro() -> dict:
    '''
    Cria um novo registro financeiro com interação do usuário.

    Solicita ao usuário que digite uma data, tipo de movimentação (Receita, Despesa ou Investimento),
    e o valor. 
    Se o usuário selecionar 'Investimento' ela irá calcular o montante e o rendimento com base em um percentula de juros fixo.

    Returns:
        Dict
        Retorna um dicionário representando o registro financeiro que contém as chaves:
        'id', 'data', 'tipo', 'valor', 'montante', e 'rendimento'.
    '''
    data = validar_data('Insira uma data no formáto válido, dd/mm/yyyy')
    tipo = validar_tipo('Digite o tipo que deseja criar. [Receita, Despesa, Investimento]: ')
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
        
        'data': data,
        'tipo': tipo,
        'valor': valor if tipo != 'Despesa' else -valor, 
        'montante': montante,
        'rendimento': rendimento,
        'data_atualizacao': None
        
        }

    return registro
