import math

raio = float(input("Digite o raio da esfera: "))

volume = (4/3) * math.pi * raio ** 3
area = 4 * math.pi * raio ** 2

print(f"O volume da esfera e {volume:.2f} unidades cubicas.\nA area da esfera e {area:.2f} unidades quadradas ")
