p1 = float(input("Qual e o seu peso atual: "))
a1 = int(input("Qual e a sua altura em CM: "))

if a1 < 120 or p1 <= 60 :
    print("Voce esta no grupo A")

elif a1 < 120 and 60 <= p1 <= 90 :
    print("Voce esta no grupo D")

elif a1 < 120 and p1 > 90 : 
    print("Voce esta no grupo G")

elif a1 <= a1 <= 170 and p1 <= 60 :
    print("Voce esta no grupo B")

elif 120 <= a1 <= 170 and 60 <= p1 <= 90 :
    print("Voce esta no grupo E")

elif 120 <= a1 <= 170 and p1 > 90 :
    print("Voce esta no grupo H")

elif a1 > 170 and p1 <= 60 :
    print("Voce esta no grupo C")

elif a1 > 170 and 60 <= p1 <= 90 :
    print("Voce esta no grupo F")

elif a1 > 170 and p1 >= 90 :
    print("Voce esta no grupo I")