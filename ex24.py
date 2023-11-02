p = input("Introduza uma frase\n")

p = (p.lower())
n = 0
v = 0

for i in p:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        n = n + 1
    elif i.isalpha():
        v = v + 1
    else:
        continue


print("Existem",n,"vogais em",p)
print("Existem",v,"consoantes em",p)