import math
import sys

n1 = float(input("digite um numero positivo maior que zero:"))

if n1 <= 0:
    print("Animal ja falei que tem que ser maior que zero")
    sys.exit()


n2 = n1 * n1
n3 = math.sqrt(n1)

print("O seu numero ao quadrado e:{}\nA raiz quadrada do seu numero e:{}".format(n2, n3))
