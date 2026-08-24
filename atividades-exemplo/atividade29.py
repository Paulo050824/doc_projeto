banco = float(input("Digite um numero de 1 a 5 sendo(1-Saldo 2-Saque 3-Depósito 4-Pix e 5 Sair)"))
saldo_da_conta = 2550.54

match banco:
    case 1:
        print(f"Saldo da conta: R${saldo_da_conta}")
    case 2:
        saque = float(input("Digite o valor de quanto deseja sacar: "))
        if saque > saldo_da_conta:
            print("Saldo indisponivel")
        else:
            saldo_da_conta -= saque
        print("Seu saldo atual é de: R$" , (saldo_da_conta - saque))
    case 3:
        deposito = float(input("Digite o valor a ser depositado: "))
        print("Valor sendo depositado! Aguarde...")
        print("Valor depositado!")
        print("Seu saldo agora é de:R$" , (saldo_da_conta + deposito))
    case 4:
        print("pix")
    case 5:
        print("Sair")
    case _:
        print("Digito invalido!")
print("Cessão encerrada!")
print("Obrigado!")



