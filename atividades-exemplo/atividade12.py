nome = input("Nome do funcionario: ")
salario_base = float(input("Digite o valor do salário base: "))
horas_extras = float(input("Digite o total de horas extras: "))
desconto = float(input("Valor descontado: "))
salario_final = (salario_base + horas_extras) - desconto

print("Nome funcionario:", nome, "\nValor do salário final: R$", salario_final)