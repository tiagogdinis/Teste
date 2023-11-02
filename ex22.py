print("Máximo e Mínimo")

notas = []
contador = 1

while contador < 5:
    notas.append(float(input("Introduza o Nota do Teste\n")))
    contador = contador + 1

maiornota = max(notas)
menornota = min(notas)
media = sum(notas) / len(notas)

print("A maior nota é",maiornota,"\n")
print("A menor nota é",menornota,"\n")
print("A média é",media,"\n")