s1 = int(input("Digite quantos segundos: "))

s2 = s1 // 60 # convert seconds to minutes
s3 = s1 % 60 # get the remaining seconds

print("{} segundos dão {} minutos e {} segundos".format(s1, s2, s3))
