opcao = int(input("DIgite qual opção você quer "))
match opcao:
    case 1:
        print( "pastel de carne")
    case 2:
        print("pastel de frango com requeijão")
    case 3:
        print("pastel de pizza")
    case 4:
        print("pastel de quatro queijos")
    case _:
        print("sabor não está dentro das especificações!")
print("programa encerrado!")