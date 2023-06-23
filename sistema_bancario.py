menu = """
Escolha uma opção:

[1] Sacar
[2] Depositar
[3] Ver Extrato 
[4] Sair

"""

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    exit = 0
    opcao = input(menu)

    if opcao == "1":
        if numero_saques >= LIMITE_SAQUES:
            print("Excedeu o limite de saques diários")
        else:
            while True:
                while True:
                    quantia_saque = input("Quanto deseja sacar? ")
                    try:
                        quantia_saque = int(quantia_saque)
                    except ValueError:
                        print('Quantia inválida')
                    else:
                        break
                
                if quantia_saque > limite:
                    print("Execedeu o limite máximo por saque: R$500")
                    continue
                elif quantia_saque <= saldo:
                    saldo -= quantia_saque
                    extrato += f"Saque.......(- R${format(quantia_saque, '.2f')}) \n"
                    numero_saques += 1
    
                    print("Saque realizado com sucesso")
                    break
                else:
                    print("Saldo insuficiente")

    elif opcao == "2":
        while True:
            quantia_deposito = input("Quanto deseja depositar? ")
            try:
                quantia_deposito = int(quantia_deposito)
            except ValueError:
                print('Quantia inválida')
            else:
                break
        
        saldo += quantia_deposito

        print("Depósito realizado com sucesso")

        extrato += f"Depósito....(+ R${format(quantia_deposito, '.2f')}) \n"

    elif opcao == "3":
         print(extrato)
         print(f"Saldo = R${format(float(saldo), '.2f')}")

    elif opcao == "4":
        print("Volte sempre!")
        break
    else:
        print("Opção inválida") 
      
