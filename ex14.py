alunos = int(input("Introduza o número de alunos\n"))

mt = 0

for i in range(1,alunos+1):
    teste = float(input("Introduza a nota do teste do aluno\n"))
    trabalho = float(input("Introduza a nota do trabalho\n"))
    ma = teste*0.5+trabalho*0.5

    print("A média do aluno",i,"é",ma,"\n\n")

    mt = mt + ma

print("A média da turma é",mt/alunos)