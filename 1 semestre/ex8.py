import math

cateto1 = float(input("Fale o valor do primeiro cateto: "))
cateto2 = float(input("Fale o valor do segundo cateto: "))


c3 = math.sqrt (cateto1**2 + cateto2**2)

print("o valor da hippotenusa e: {:.2f}".format(c3))