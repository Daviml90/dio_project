menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar usuário
[f] Criar conta corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = {}
numero_conta = 1

def saque(*, saldo1=saldo, valor, extrato1=extrato, limite=limite, numero_saques1=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES):
        global saldo
        global extrato
        global numero_saques
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
            
def deposito(valor,saldo2=saldo, extrato2=extrato,/):
    global saldo
    global extrato
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
        
def extrato_func(saldo3=saldo, /, *, extrato3=extrato):
    global saldo
    global extrato
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuario():
    global usuarios
    nome = input("Nome: ")
    nascimento = input("Data de nascimento: ")
    cpf0 = input("CPF: ")
    cpf = ""
    for c in cpf0:
        if c.isdigit() == True:
            cpf += c
    endereco = input("Endereço (logradouro, nro, bairro, cidade/sigla estado): ")
    
    if cpf in usuarios:
        return print("CPF já existe")
    
    else:
        usuarios.update({cpf: {"nome": nome, "data de nascimento": nascimento, "cpf": cpf, "endereco": endereco, "contas": []}})

    print(usuarios)

def criar_conta(cpf):
    global numero_conta
    if cpf not in usuarios:
        return print("CPF não encontrado")
    else:
        conta = "0001-"+str(numero_conta)
        usuarios[cpf]["contas"].append(conta) 
        numero_conta += 1
        print(f"Sua nova conta é: {conta}")
    

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        deposito(valor)


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saque(valor=valor)

    elif opcao == "e":
        extrato_func()
    
    elif opcao == "c":
        criar_usuario()

    elif opcao == "f":
        cpf0 = input("CPF: ")
        cpf = ""
        for c in cpf0:
            if c.isdigit() == True:
                cpf += c
                
        criar_conta(cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
