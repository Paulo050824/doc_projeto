print("\n ---------- AÇÕES ---------\n| 1 - Cadastro \n| 2 - Consulta \n| 3 - Sair ")
cadastro = int(input("Digite qual opção você quer: "))
nome = ""

match cadastro:
    case 1:
        print("---------------Cadastro------------------")
        nome = str(input("Digite seu nome:"))
        idade = int(input("Digite sua idade: "))
        email = input("Digite seu email: ")
        bairro = str(input("Digite seu bairro: "))
        print("Cadastro realizado com sucesso!!")
    case 2:
        print("\n----CONSULTA---")
        if nome:
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"E-mail: {email}")
            print(f"Bairro: {bairro}")
        else:
            print("Nenhum cadastro encontrado!!!")
    case 3:
        print("Saindo...")
    case _:
        print("Opção invalida!")
print("Programa encerrado!")
print("Até a proxima" , nome)