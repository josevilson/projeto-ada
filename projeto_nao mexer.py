import csv
import json
from datetime import datetime


# Função para salvar os dados em um arquivo JSON
def salvar_json(dados, nome_arquivo='dados_financeiros.json'):
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

# Função para carregar os dados de um arquivo JSON
def carregar_json(nome_arquivo='dados_financeiros.json'):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return []

# Funções para validar entradas
def validar_tipo(tipo):
    return tipo.lower() in ['receita', 'despesa', 'investimento']

def validar_valor(valor):
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        return False

def validar_taxa(taxa):
    try:
        taxa = float(taxa)
        return taxa >= 0
    except ValueError:
        return False

def validar_indice(indice, registros):
    try:
        indice = int(indice)
        return 0 <= indice < len(registros)
    except ValueError:
        return False

def validar_formato(formato):
    return formato.lower() in ['csv', 'json']

# Funções para capturar entradas com validação
def capturar_tipo():
    tipo = input("Digite o tipo de movimentação (Receita, Despesa, Investimento): ").strip().lower()
    while not validar_tipo(tipo):
        tipo = input("Tipo inválido. Digite o tipo de movimentação (Receita, Despesa, Investimento): ").strip().lower()
    return tipo

def capturar_valor():
    valor = input("Digite o valor da movimentação: ").strip()
    while not validar_valor(valor):
        print("Valor inválido. Deve ser um número positivo.")
        valor = input("Digite o valor da movimentação: ").strip()
    return float(valor)

def capturar_taxa():
    taxa = input("Digite a taxa de rendimento (em decimal, por exemplo, 0.01 para 1%): ").strip()
    while not validar_taxa(taxa):
        print("Taxa inválida. Deve ser um número não negativo.")
        taxa = input("Digite a taxa de rendimento (em decimal, por exemplo, 0.01 para 1%): ").strip()
    return float(taxa)

def capturar_indice(registros):
    indice = input(f"Digite o índice do registro (0 a {len(registros) - 1}): ").strip()
    while not validar_indice(indice, registros):
        print("Índice inválido.")
        indice = input(f"Digite o índice do registro (0 a {len(registros) - 1}): ").strip()
    return int(indice)

def capturar_formato():
    formato = input("Digite o formato de exportação (csv ou json): ").strip().lower()
    while not validar_formato(formato):
        formato = input("Formato inválido. Digite 'csv' ou 'json': ").strip().lower()
    return formato

# Função para criar um novo registro financeiro
def criar_registro():
    registros = carregar_json()

    tipo = capturar_tipo()
    valor = capturar_valor()

    if tipo == 'despesa':
        valor = -abs(valor)  # Armazena como negativo

    if tipo == 'investimento':
        montante = capturar_valor()
        taxa = capturar_taxa()
        t = (datetime.now() - datetime.now()).days
        valor = montante * (1 + taxa) ** t

    data_atual = datetime.now().strftime("%Y-%m-%d")
    novo_registro = {
        "data": data_atual,
        "tipo": tipo,
        "valor": valor,
        "dia": datetime.now().day,
        "mes": datetime.now().month,
        "ano": datetime.now().year
    }
    
    registros.append(novo_registro)
    salvar_json(registros)
    print("Registro criado com sucesso!")

# Função para ler registros
def ler_registros():
    registros = carregar_json()
    if not registros:
        print("Nenhum registro encontrado.")
        return
    
    filtro = input("Deseja filtrar por data, tipo ou valor? (deixe em branco para ver todos): ").strip().lower()
    valor = None

    if filtro == 'data':
        valor = input("Digite a data no formato AAAA-MM-DD: ").strip()
    elif filtro == 'tipo':
        valor = capturar_tipo()
    elif filtro == 'valor':
        valor = capturar_valor()

    registros_filtrados = [reg for reg in registros if reg[filtro] == valor] if filtro else registros
    for reg in registros_filtrados:
        print(reg)

# Função para atualizar um registro existente
def atualizar_registro():
    registros = carregar_json()
    if not registros:
        print("Nenhum registro encontrado.")
        return

    indice = capturar_indice(registros)
    tipo = capturar_tipo()
    valor = capturar_valor()

    registro = registros[indice]
    registro['tipo'] = tipo
    registro['valor'] = valor if tipo != 'despesa' else -abs(valor)
    registro['data'] = datetime.now().strftime("%Y-%m-%d")
    registro['dia'] = datetime.now().day
    registro['mes'] = datetime.now().month
    registro['ano'] = datetime.now().year

    salvar_json(registros)
    print("Registro atualizado com sucesso!")

# Função para deletar um registro
def deletar_registro():
    registros = carregar_json()
    if not registros:
        print("Nenhum registro encontrado.")
        return

    indice = capturar_indice(registros)
    registros.pop(indice)
    salvar_json(registros)
    print("Registro deletado com sucesso!")

# Função para atualizar rendimentos de investimentos
def atualiza_rendimento():
    registros = carregar_json()
    if not registros:
        print("Nenhum registro encontrado.")
        return
    
    taxa = capturar_taxa()

    for reg in registros:
        if reg['tipo'] == 'investimento':
            data_investimento = datetime.strptime(reg['data'], "%Y-%m-%d")
            dias = (datetime.now() - data_investimento).days
            reg['valor'] = reg['valor'] * (1 + taxa) ** dias
    salvar_json(registros)
    print("Rendimentos atualizados com sucesso!")

# Função para exportar relatório em CSV ou JSON
def exportar_relatorio():
    registros = carregar_json()
    if not registros:
        print("Nenhum registro encontrado.")
        return
    
    formato = capturar_formato()
    nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()

    if formato == 'csv':
        with open(f'{nome_arquivo}.csv', 'w', newline='') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(registros)
        print(f"Relatório exportado como {nome_arquivo}.csv com sucesso!")
    else:
        salvar_json(registros, f'{nome_arquivo}.json')
        print(f"Relatório exportado como {nome_arquivo}.json com sucesso!")

# Função de agrupamento por mês
def agrupamento_por_mes():
    registros = carregar_json()
    if not registros:
        print("Nenhum registro encontrado.")
        return

    agrupamento = {}
    for reg in registros:
        mes_ano = f"{reg['mes']}/{reg['ano']}"
        if mes_ano not in agrupamento:
            agrupamento[mes_ano] = 0
        agrupamento[mes_ano] += reg['valor']

    print("Agrupamento por mês:")
    for mes_ano, total in agrupamento.items():
        print(f"{mes_ano}: {total}")

# Loop principal
def main():
    while True:
        print("\nOpções:")
        print("1 - Criar registro")
        print("2 - Ler registros")
        print("3 - Atualizar registro")
        print("4 - Deletar registro")
        print("5 - Atualizar rendimentos de investimentos")
        print("6 - Exportar relatório")
        print("7 - Agrupar por mês")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            criar_registro()
        elif opcao == '2':
            ler_registros()
        elif opcao == '3':
            atualizar_registro()
        elif opcao == '4':
            deletar_registro()
        elif opcao == '5':
            atualiza_rendimento()
        elif opcao == '6':
            exportar_relatorio()
        elif opcao == '7':
            resultado = agrupar_por_mes(registros)
            if resultado:
                for mes, total in resultado.items():
                    print(f"Total de {mes}: R${total}")
            else:
                print("Nenhum registro encontrado para o mês especificado.")
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
