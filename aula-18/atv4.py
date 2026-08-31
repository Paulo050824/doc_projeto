compras = []
qntd_produtos = []
prd1 = str(input("Digite o primeiro produto: "))
prd2 = str(input("Digite o segundo produto: "))
prd3 = str(input("Digite o terceiro produto: "))
compras.append(prd1)
compras.append(prd2)
compras.append(prd3)

print("\n'========LISTA_DE_COMPRAS=========")
print("Produtos: ", compras)
print("Quantidade de produtos:" ,len(compras))
print("Primeiro produto:" , compras[0])
print("Ultimo produto:", compras [len(compras)-1])
