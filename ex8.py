teste = float(input("Introduza a nota do teste\n"))
trabalho = float(input("Introduza a nota do trabalho\n"))

media = (teste * 0.6) + (trabalho * 0.4)

if media >= 9.5:
    print("O aluno passou com a média de",media,"\n")
else:
    print("O aluno reprovou com a média de",media,"\n")