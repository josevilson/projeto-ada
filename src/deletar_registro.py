def deletar_registro(registros):
    """Deleta um registro financeiro com interação do usuário."""

    if not registros:
        print("Nenhum registro encontrado.")
        return

    for i, registro in enumerate(registros):
        print(f"{i}: {registro}")

    indice = int(input("Índice do registro a ser deletado: "))

    if 0 <= indice <= len(registros):
        del registros[indice]
    else:
        print("Índice inválido.")