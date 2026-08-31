alunos = int(input("Digite a quantidade de alunos na sala de aula: "))
total = 0

for i in range(alunos + 1):
    notas = float(input("Digite a nota dos aluno: "))
    total = notas / alunos
print("Média da nota da turma é: ", total/alunos)