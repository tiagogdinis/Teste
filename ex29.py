n = str(input("Introduza o seu nome todo.\n"))

parte = lambda d: d.split()

pn = parte(n)[0]
un = parte(n)[-1]

print("O seu primeiro nome é",pn)
print("O seu último nome é",un)