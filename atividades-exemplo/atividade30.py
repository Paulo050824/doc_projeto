metros = int(input("Digite o número que deseja acessar(Sendo eles 1- centimetros 2- Quilometros 3- milimetros): "))
print("|------Conversão-------| \n|   Centimetros   |     \n|   Quilometros   |    \n|   Melimetros    |")
conversao = int(input("Digite a opção que deseja fazer a conversão!: "))

match conversao:
    case 1:
        centimetros = metros *100
        print(f"\nAqui está o valor da conversão em centimetros: {centimetros}cm:")
    case 2:
        quilometros = metros / 1000
        print(f"\nA conversão em quilometros é: {quilometros}km")
    case 3:
        melimetros = metros * 1000
        print(f"\nA conversão em melimetros é: {melimetros}mm")
    case _ :
        print("opção inesistente!!")
print("Sessão encerrada")