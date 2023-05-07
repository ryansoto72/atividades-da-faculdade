s1 = int(input("Digite seu salario: "))
a1 = int(input("Qual e a porcentagem de aumento: "))

linha = ("==================================")

a2 = (s1*a1)/100 
s2 = s1 + a2

print(linha)
print("O seu aumento foi de {} reais".format(a2))
print("O seu salario com o aumento da {} reais".format(s2))
print(linha)

