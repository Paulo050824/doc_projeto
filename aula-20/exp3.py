numeros: list[list[int]] = [
    [10,20],
    [30,40]
]
print("Antes:")
print("------------------------")
print(numeros[0])
print(numeros[1])
numeros[1][0] = 100
print("------------------------")
print("Depois")
print(numeros[0])
print(numeros[1])