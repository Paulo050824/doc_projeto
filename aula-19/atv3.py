cidades = []
for i in range(5):
    cidade = input("Digite o nome de uma cidade: ")
    cidades.append(cidade)
for i in range(len(cidades)):
    print(i+1,"-",cidades[i])
