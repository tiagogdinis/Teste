from random import randint

n = randint(0,100)

t = 3

while t > 0:
    print("Tentativa Nº",t)
    r = int(input("Introduza a sua tentativa\n"))

    if r == n:
        print("Parabéns! Acertaste o número!")
        break
    else:
        if r > n:
            print("O teu número é muito alto. Tenta um mais baixo.\n")
        elif r < n:
            print("O teu número é muito baixo. Tenta um mais alto.\n")
        t = t - 1

if t == 0:
    print("Acabaram-se as tentativas. Perdeste!")