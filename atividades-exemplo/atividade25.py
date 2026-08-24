nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso(kg):"))
altura = float(input("Digite sua altura(m):"))
imc = peso / (altura*altura)

print(nome, "\nimc:", imc, "\n")
print("Seu imc é:", imc)

print("| IMC            | Classificação      |")
print("| -------------- | ------------------ |")

if(imc >= 40):
    print("| 40 ou mais     | Obesidade grau III |")

elif(imc >= 35):
    print("| 35 a 39,9      | Obesidade grau II  |")

elif(imc >= 30):
    print("| 30 a 34,9      | Obesidade grau I   |")

elif(imc >=25):
    print("| 25 a 29,9      | Sobrepeso          |")

elif(imc >=18.59):
    print("| 18,5 a 24,9    | Peso normal        |")

else:
    print("| Menor que 18,5 | Abaixo do peso     |")


    















