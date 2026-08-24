saldo_da_conta = 2500
saque = float(input("Digite o valor que deseja sacar:" ))
if (saque <= saldo_da_conta):
    print("Saque realizado com sucesso!" , "\nAguarde as notas sairem!")
    print("Seu saldo atual é de: R$" , (saldo_da_conta - saque))
else:
    print("Saldo da conta indisponivel!")
    print("Seu saldo atual é de: R$" , saldo_da_conta)
   