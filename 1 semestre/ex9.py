h1 = float(input("Insira a quantidade de horas trabalhadas: "))

s1 = float(input("Fale qual e o salario minimo: "))

ht = s1/2
st = ht*h1
imposto = st * 0.03
#im2 = imposto * 0.03
salario_a_receber = st - imposto
print("o seu salario vai ser de {:.2f} reais.".format(salario_a_receber))
