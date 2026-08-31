nomes: list[str] = ["Ana", "Bruno", "Carlos"]
pesquisa = "Carlos"
posicao = -1
for i in range(len(nomes)):
    if(nomes[i]==pesquisa):
        posicao = i
print(posicao)