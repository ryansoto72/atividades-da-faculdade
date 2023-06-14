import math

def volume_lata(raio, altura):
    volume = math.pi * raio ** 2 * altura
    return volume

raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))

volume = volume_lata(raio, altura)
print(f"o volume da lata e {volume:.2f}.")
