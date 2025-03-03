#Criação do Menu

menu = """"
    [d]- Depositar
    [s]- Sacar
    [e]- Extrato
    [q]- Sair
    : """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("QUal valor deseja depositar?"))
        if valor > 0:
            saldo +=valor
            extrato += f"Depósito:R${valor:.2f}\n"
        else:
            print("Operação falhou o valor é inválido")

    elif opcao == "s":
        valor = float(input("Quanto deseja sacar?"))
        if valor > saldo:
            print("excedeu o saldo")
        elif valor > limite:
            print("Excedeu o limite")
        elif numero_saques >= LIMITE_SAQUE:  #Para garantir que o limite seja 3, porque o saque começa em 0
            print("excedeu o numero de vezes que pode fazer saque")
        elif valor>0:
            saldo -= valor
            print("Saque realizado com sucesso")
            numero_saques += 1
            extrato += f"saque: R$ {valor:.2f}\n"
        else:
            print("Valor inválido")


    elif opcao == "e":
        print("\n =============Extrato===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor seleciona a opção correcta")


