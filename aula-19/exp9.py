nomes: list[str] = ["Ana", "Ana","Ana","Ana","Ana,","Ana""Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana","Ana"]
pesquisa = "Ana"
posicao = -1
for i in range(len (nomes)):
    if(nomes[i]==pesquisa):
        posicao = i
        print(posicao)
        break