import time

print("eu vou calcular a soma de quatro numeros para voce")
time.sleep(2)

n1 = int(input("Qual e o primeiro numero: "))
n2 = int(input("Qual e o segundo: "))
n3 = int(input("qual e o terceiro "))
n4 = int(input("e qual e o ultimo: "))

soma = n1+n2+n3+n4
media = soma/4

print("a soma dos numeros que voce falou da {} e a media de todos eles da {:.0f}".format(soma, media))
