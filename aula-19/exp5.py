alunos: list[str] = []
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    print(i+1, "-", nome)
    alunos.append(nome)
print("=======ALUNOS==========")
for i in range (len(alunos)):
    print(i+1, "-", alunos[i])
    