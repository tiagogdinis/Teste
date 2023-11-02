alunos = int(input("Introduza o número de alunos\n"))

mt = 0
tep = 0
ten = 0
trp = 0
trn = 0

for i in range(1,alunos+1):
    teste = float(input("Introduza a nota do teste do aluno\n"))
    if teste >= 50:
        tep = tep + 1
    else:
        ten = ten + 1
    
    trabalho = float(input("Introduza a nota do trabalho\n"))
    if trabalho >= 50:
        trp = trp + 1
    else:
        trn = trn + 1
    
    ma = teste*0.5+trabalho*0.5

    print("A média do aluno",i,"é",ma,"\n\n")

    mt = mt + ma

print("A média da turma é",mt/alunos)
print("Houveram",tep,"testes positivos e",ten,"testes negativos")
print("Houveram",trp,"trabalhos positivos e",trn,"trabalhos negativos")