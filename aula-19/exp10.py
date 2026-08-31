numeros: list[int] = [8, 3, 15, 6, 10]
maior = numeros[0]
for i in range(len(numeros)):
    if(numeros[i]>maior):
        maior = numeros[i]
print("Maior valor: ", maior)