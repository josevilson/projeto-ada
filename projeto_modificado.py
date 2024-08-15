import json
from datetime import datetime
import csv
from dateutil.relativedelta import relativedelta
import itertools

def tempo(data):
    data_convertido = datetime.strptime(data, '%d/%m/%Y')
    data_referencia = datetime.now()
    diferenca = relativedelta(data_referencia, data_convertido)
    diferenca_meses = diferenca.months
    return diferenca_meses

'''id = itertools.count(1)
def gerador_id():
    return f"{next(id):03}"'''

def criar_registro(): #separar dia, mes e ano
    """Cria um novo registro financeiro com interação do usuário."""

    data = input("Data (dd/mm/aaaa): ")
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
        while True:
            juros = input('Digite o percentual mensal de juros do investimento:')
            try:
                juros = float(juros)
                break
            except ValueError:
                print('Erro, digite apenas números')
        
    montante_inicial = valor *(1+((juros)/100))**(tempo(data))
    montante = round(montante_inicial, 2)
    rendimento_inicial = montante - valor
    rendimento = round(rendimento_inicial, 2)

    registro = {
    ''' 'id': id,''' 
        'data': data,
        'tipo': tipo,
        'valor': valor if tipo != 'Despesa' else -valor, 
        'montante': montante,
        'rendimento': rendimento

        }

    return registro

def ler_registros(arquivo):
    """Lê os registros financeiros do arquivo JSON."""

    try:
        with open(arquivo, 'r') as f:
            registros = json.load(f)
    except FileNotFoundError:
        print('Ainda não há nenhum registro')
        registros = []  # Cria uma lista vazia se o arquivo não existir

    return registros

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
        nova_data = input("Nova data (dd/mm/aaaa, deixe em branco para manter o atual): ")

        if novo_valor:
            registros[indice]['valor'] = float(novo_valor) if novo_tipo != 'Despesa' else -float(novo_valor)
        if novo_tipo:
            registros[indice]['tipo'] = novo_tipo #caso seja Investimento tem que pedir o juros
        if nova_data:
            registros[indice]['data'] = nova_data
    else:
        print("Índice inválido.")

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

def salvar_registros(registros, arquivo):
    """Salva os registros financeiros no arquivo JSON."""

    with open(arquivo, 'w') as f:
        json.dump(registros, f, indent=4)

def atualiza_rendimento(registros): #necessário algumas mudanças
    """Atualiza o rendimento dos investimentos."""

    hoje = datetime.now()

    for registro in registros:
        if registro['tipo'] == 'Investimento':
            data_investimento = datetime.strptime(registro['data'], '%d/%m/%Y')
            dias = (hoje - data_investimento).days
            montante = float(registro['montante'])
            taxa_juros = 0.0005  # o juros deve ser solicitado ao usuário
            rendimento = montante * (1 + taxa_juros) ** dias - montante
            registro['rendimento'] = rendimento

def exportar_relatorio(registros, arquivo, formato='csv'):
    """Exporta um relatório dos registros financeiros."""

    if formato == 'csv':
        try:
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                cabecalho = registros[0].keys() if registros else []
                writer = csv.DictWriter(f, fieldnames=cabecalho)
                writer.writeheader()
                writer.writerows(registros)
            print("Relatório exportado com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar relatório CSV: {e}")
    elif formato == 'json':
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(registros, f, indent=4, ensure_ascii=False)
            print("Relatório exportado com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar relatório JSON: {e}")
    else:
        print("Formato inválido. Use 'csv' ou 'json'.")

def agrupar_por_mes(registros):
    """Agrupa os registros por mês e calcula o total de cada mês."""

    resultado = {}
    for registro in registros:
        mes = datetime.strptime(registro['data'], '%d/%m/%Y').strftime('%m/%Y')
        if mes in resultado:
            resultado[mes] += float(registro['valor'])
        else:
            resultado[mes] = float(registro['valor'])

    return resultado

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
            for mes, total in resultado.items():
                print(f"{mes}: {total}")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
