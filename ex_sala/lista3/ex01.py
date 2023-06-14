id = int(input("Digite sua idade:"))
tb = int(input("Quanto tempo voçe ja trabalhou:"))

if id > 64:
    print("Aposentado")
    
elif tb > 29:
    print("Aposentado")

elif tb > 24 or id > 59:
    print("Aposentado")

else:
    print("ainda nao aposentado")

