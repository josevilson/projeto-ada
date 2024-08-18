def deletar_registro(registros: list[dict])-> None:
    
    '''Deleta um registro financeiro, se solicitado pelo usuário.

            Essa função vai exibir uma lista de registros e permitir que o usuário delete o registro que escolher.
            Se a lista estiver vazia uma mensagem será exibida informando que nenhum registro foi encontrado.
            Se a informação fornecida pelo usuário estiver incorreta, a função também notificará.
        
        Args:
            registros (list[dict]):
                Recebe uma lista de dicionários, cada dicinário representa um registro.

        Returns:
            None: 
                Não retorna nenhum valor, apenas deleta o registro da lista.
    '''
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