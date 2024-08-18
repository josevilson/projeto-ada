from src.atualizar_rendimento import atualiza_rendimento
from utilitarios.entrada_data import validar_data


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

    indice = int(input("Índice do registro a ser atualizado: "))

    if 0 <= indice <= len(registros):
        novo_valor = input("Novo valor (deixe em branco para manter o atual): ")
        novo_tipo = input("Novo tipo (deixe em branco para manter o atual): ")
        nova_data = validar_data('Nova data (deixe em branco para manter o atual): ')

        if novo_valor:
            registros[indice]['valor'] = float(novo_valor) if novo_tipo != 'Despesa' else -float(novo_valor)
        if novo_tipo:
            registros[indice]['tipo'] = novo_tipo #caso seja Investimento tem que pedir o juros
        if nova_data:
            registros[indice]['data'] = nova_data

        atualiza_rendimento(registros)
    else:
        print("Índice inválido.")