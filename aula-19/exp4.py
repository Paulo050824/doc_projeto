nomes: list[str] = []
for i in range(5):
    nome = input("Digite um nome: ")
    print(i+1, "-",nome)
    nomes.append(nome)
print(nomes)