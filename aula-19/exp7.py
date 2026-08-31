nomes: list[str] = ["Ana","Bruno","Carlos","João"]
pesquisa = "Bruno"
encontrado = False
for i in range (len(nomes)):
    if(nomes[i]==pesquisa):
        encontrado = True
        print("Encontrado:", pesquisa)