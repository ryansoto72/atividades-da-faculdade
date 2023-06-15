print(" 1:SOMA 2:SUBTRAÇAO 3:MULTIPLICAÇAO 4:DIVISAO qual voce deseja usar: ")

ESCOLHA = int(input("qual voce deseja usar:"))


if ESCOLHA == 1:
    s1 = int(input("Digite o primeiro numero da soma: "))
    s2 = int(input("Digite o segundo numero da soma: "))

    s3 = s1+s2

    print(f"A sua soma deu {s3}")

elif ESCOLHA == 2:
    su1 = int(input("Digite o primeiro numero da subtracao: "))
    su2 = int(input("Digite o segundo numero da subtracao: "))
    
    su3 = su1 - su2 

    print(f"O resultado da sua subtracao da {su3}")

elif ESCOLHA == 3:
    mu1 = int(input("Digite o primeiro numero da multiplicacao: "))
    mu2 = int(input("Digite o segundo numero da multiplicacao: "))

    mu3 = mu1 * mu2

    print(f"O resultado da sua multiplicacao deu {mu3}")

elif ESCOLHA == 4:
    di1 = int(input("Digite o primeiro numero da divisao: "))
    di2 = int(input("Digite o segundo numero da divisao: "))

    di3 = di1 / di2

    print(f"O resultado da sua divisao deu {di3}")

else:
    print("Digite um numero vallido")