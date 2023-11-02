par = 0
impar = 0

while True:
    n = float(input("Introduza um número\n"))

    if n==0:
        break
    else:
        if n%2==0:
            par = par + 1
        elif n%2!=0:
            impar = impar + 1

print("Foram introduzidos",par,"números pares")
print("Foram introduzidos",impar,"números ímpares")