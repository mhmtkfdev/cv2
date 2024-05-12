import random

sayılar = []
i = 0
while i < 5 :
    a = random.randint(0,100)
    sayılar.append(a)
    i += 1

sayılar.sort()
print(sayılar)