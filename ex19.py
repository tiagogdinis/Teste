p = input("Introduza uma palavra\n")

p = (p.lower())
n = 0

for i in p:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        n = n + 1

print("Existem",n,"vogais em",p)