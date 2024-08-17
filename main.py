import csv

from src import (agrupar_por_mes, atualiza_rendimento, atualizar_registro,
                 criar_registro, deletar_registro, exportar_relatorio,
                 ler_registros, salvar_registros)
from utilitarios.validar_generic import ValidarDadosGeneric


def menu():
    """Exibe o menu interativo e processa as escolhas do usuário."""

    arquivo = 'financas.json'
    registros = ler_registros(arquivo)

    while True:
        print("\n--- Menu ---")
        print("1. Criar registro")
        print("2. Ler registros")
        print("3. Atualizar registro")
        print("4. Deletar registro")
        print("5. Atualizar rendimento")
        print("6. Exportar relatório")
        print("7. Agrupar por mês")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            novo_registro = criar_registro()
            
            registros.append(novo_registro)
            salvar_registros(registros, arquivo)
            print("Registro criado com sucesso!")
        elif opcao == '2':
            if registros:
                for registro in registros:
                    print(registro)
            else:
                print("Nenhum registro encontrado.")
        elif opcao == '3':
            atualizar_registro(registros)
            salvar_registros(registros, arquivo)
        elif opcao == '4':
            deletar_registro(registros)
            salvar_registros(registros, arquivo)
        elif opcao == '5':
            atualiza_rendimento(registros)
            salvar_registros(registros, arquivo)
            print("Rendimento atualizado!")
        elif opcao == '6':
            formato = input("Formato do relatório (csv ou json): ")
            exportar_relatorio(registros, 'relatorio.' + formato, formato)
        elif opcao == '7':
            resultado = agrupar_por_mes(registros) 
            print(resultado)
            if resultado:
                for mes, total in resultado.items():
                    print(f"{mes}: {total}")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

