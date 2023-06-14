import time

print("1: PRECO ANTIGO")
time.sleep(1)
print("2: PRECO NOVO")
time.sleep(1)

ESCOLHA = input("DIGITE QUAL DAS TABELAS VOCE QUER CONSULTAR: ")

if ESCOLHA == "1":
    pa = int(input("Fale o preco antigo do produto: "))

    if pa <= 50:
        p1 = pa / 100
        p2 = pa + (p1 * 5)
        print(f"O novo valor do seu produto vai ser {p2} reais.")

    elif 50 <= pa <= 100:
        p4 = pa + (pa * 10 / 100)
        print(f"O novo valor do seu produto vai ser {p4} reais.")

    elif pa > 100: 
        p5 = pa + (pa * 15 / 100)
        print(f"O novo valor do seu produto vai ser {p5} reais.")

elif ESCOLHA == "2": 
    vp = int(input("Qual e o valor novo do produto: "))

    if vp <= 80:
        print("Esta barato")

    elif 80 <= vp <= 120:
        print("O valor esta normal")

else:
    print("Opcao invalida. Por favor, selecione uma opcao válida (1 ou 2).")
