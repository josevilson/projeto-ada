from src.criar_registro import entradas_novo_registro
from utilitarios.validar_generic import ValidarDadosGeneric

while True:
    try:
        entradas_novo_registro()
    except ValidarDadosGeneric as e:
        print(e)




# criar_registro
# ler_registros
# atualizar_registro
# deletar_registro
# salvar_registros
# atualiza_rendimento
# exportar_relatorio
# agrupar_por_mes