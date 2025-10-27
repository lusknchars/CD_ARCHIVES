from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Planilha Financeira"
ws.append(["Tipo de Operação", "Descrição", "Valor"])


def adicionar_transacao(tipo, descricao, valor):
    ws.append([tipo, descricao, valor])
    wb.save("planilha_financeira.xlsx")
    print(f"{tipo} adicionada: {descricao} - R${valor:.2f}")


def calcular_saldo():
    total_entradas = 0
    total_saidas = 0

    for row in ws.iter_rows(min_row=2, values_only=True):
        tipo = row[0]
        valor = row[2]
        if tipo == "Entrada":
            total_entradas += valor
        elif tipo == "Saída":
            total_saidas += valor
    saldo = total_entradas - total_saidas
    return saldo, total_entradas, total_saidas


def mostrar_saldo():
    saldo, entradas, saidas = calcular_saldo()
    print("\n" + "="*40)
    print("Saldo Atual")
    print("="*40)
    print(f"Saldo: R$ {saldo:2f}")
    print("="*40 + "\n")


def mostrar_resumo():
    saldo, entradas, saidas = calcular_saldo()
    print("\n" + "="*40)
    print("Resumo Financeiro")
    print("="*40)
    print(f"Total de Entradas: R$ {entradas:.2f}")
    print(f"Total de Saídas:   R$ {saidas:.2f}")
    print(f"Saldo:             R$ {saldo:.2f}")
    print("="*40 + "\n")


def menu():
    print("\n=== GERENCIADOR FINANCEIRO ===")
    print("1 - Adicionar Entrada")
    print("2 - Adicionar Saída")
    print("3 - Ver Saldo Atual")
    print("4 - Ver Resumo")
    print("5 - Sair")
    return input("Escolha uma opção: ")


while True:
    opcao = menu()

    if opcao == "1":
        descricao = input("Descrição: ")
        valor = float(input("Valor: R$ "))
        adicionar_transacao("Entrada", descricao, valor)

    elif opcao == "2":
        descricao = input("Descrição: ")
        valor = float(input("Valor: R$ "))
        adicionar_transacao("Saída", descricao, valor)

    elif opcao == "3":
        mostrar_saldo()

    elif opcao == "4":
        mostrar_resumo()

    elif opcao == "5":
        print("\nSaindo... Arquivo salvo como 'planilha_financeira.xlsx'")
        break

    else:
        print("Opção inválida!")

wb.save("planilha_financeira.xlsx")
