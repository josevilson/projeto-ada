from datetime import datetime

from src.atualizar_rendimento import atualiza_rendimento
from utilitarios.calcular_tempo import tempo
from utilitarios.entrada_data import validar_data
from utilitarios.validacao import validar_tipo, validar_valor


def atualizar_registro(registros: list[dict]) -> None:
    '''Atualiza um registro já existente conforme solicitação do usuário.
    
            O usuário pode selecionar um registro financeiro de uma lista e atualizar seus valores.
            Também pode optar em alterar o valor já existente, o tipo e a data.
            Se o usuário deixar algum valor em branco, o valor atual do registro será mantido.
         
        Args:
            registros (list[dict]): 
                Recebe uma lista de dicionários onde cada dicionário representa um registro financeiro 
                com as chaves 'valor', 'tipo', e 'data'.

        Returns:
            None: 
                Não retorna nenhum valor, apenas atualiza o registro. 
    '''

    if not registros:
        print("Nenhum registro encontrado.")
        return

    for i, registro in enumerate(registros):
        print(f"{i}: {registro}")
    
    indice = validar_indice(registros)
    novo_valor = validar_valor()
    novo_tipo = validar_tipo('Digite o tipo que deseja alterar. [Receita, Despesa, Investimento]: ')
    nova_data = validar_data('Nova data: ')

    if novo_valor:
        registros[indice]['valor'] = float(novo_valor) if novo_tipo != 'Despesa' else -float(novo_valor)
    if novo_tipo:
        registros[indice]['tipo'] = novo_tipo
    if nova_data:
        registros[indice]['data'] = nova_data
    registros[indice]['data_atualizacao'] = datetime.now().strftime("%d/%m/%Y")

    if novo_tipo == 'Investimento':

        juros = 0.01
        montante_inicial = novo_valor * (1+((juros)))**(tempo(registros[indice]['data']['data_completa']))
        montante = round(montante_inicial, 2)
        rendimento_inicial = montante - novo_valor
        rendimento = round(rendimento_inicial, 2)
        atualiza_rendimento(registros)
