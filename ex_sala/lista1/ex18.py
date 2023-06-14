#h1 = int(input("qual e o tempo de duracao em segundos da festa: "))

#hora = h1/64
#min = hora/64
#seg = min/64

#print(f"A sua festa tem {h1} segundos, isso em horario tem {hora}:{min}:{seg}")

segundos = int(input("Digite o número de segundos que deseja converter: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos.")