n1 = int(input("Introduza o primeiro número\n"))
n2 = int(input("Introlduza o segundo número\n"))
op = int(input("Introduza a operação:\n 1 - Adição\n 2 - Subração\n 3 - Multiplicação\n 4 - Divisão"))

match op:
    case 1:
        print("A adição de",n1,"com",n2,"é",n1+n2)
    case 2:
        print("A subtração de",n1,"com",n2,"é",n1-n2)
    case 3:
        print("A multiplicação de",n1,"com",n2,"é",n1*n2)
    case 4:
        print("A divisão de",n1,"com",n2,"é",n1/n2)
        