from src.atualizar_rendimento import atualiza_rendimento
from utilitarios.entrada_data import validar_data


def atualizar_registro(registros):
    """Atualiza um registro financeiro existente com interação do usuário."""

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