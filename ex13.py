n = int(input("Introduza um número\n"))

total = 1

for i in range(1,n+1):
    total = total * i

print("O fatorial de",n,"é",total)