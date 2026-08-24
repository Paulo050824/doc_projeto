dia_da_semana = int(input("Informe o dia da semana: (1- Domingo até 7- Sábado)"))
match dia_da_semana:
    case 1:
        print("\n Dia selecionado: Domingo")
    case 2:
        print("\n Dia selecionado: Segunda")
    case 3:
        print("\n Dia selecionado: Terça-feira")
    case 4:
        print("\n Dia selecionado: Quarta-feira")
    case 5:
        print("\n Dia selecionado: Quinta-feira")
    case 6:
        print("\n Dia selecionado: Sexta-feira")
    case 7:
        print("\n Dia selecionado: Sábado")                            
    case _:
        print("Comando inesistente")

print("Programa encerrado!!!")