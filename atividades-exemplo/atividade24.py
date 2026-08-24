velocidade_veiculo = float(input("Informe a sua velocidade atual:"))

if(velocidade_veiculo >=81):
    print("Multado")
elif(velocidade_veiculo >= 61 <= 80):
    print("Atenção")
else:
    print("Velocidade permitida")