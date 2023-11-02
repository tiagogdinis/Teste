l1 = []
l2 = []

cont = 1

while cont <= 5:
    l1.append(int(input("Introduza um número para a lista 1\n")))
    cont = cont + 1

cont = 1

while cont <= 5:
    l2.append(int(input("Introduza um número para a lista 2\n")))
    cont = cont + 1

c = 0

for i in range(0,5):
    for n in range(0,5):
        if l1[i] == l2[n]:
            c = c + 1

print("Existem",c,"números iguais")