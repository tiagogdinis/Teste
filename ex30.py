import random

l = [random.randint(0,100) for _ in range(20)]
p = 0
i = 0

for n in l:
    if n%2==0:
        p = p + n
    elif n%2!=0:
        i = i + n

print(l)
print("Soma dos Pares:",p)
print("Soma dos Ímpares:",i)