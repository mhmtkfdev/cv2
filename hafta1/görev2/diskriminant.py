import math

def diskriminant():
    a = int(input("İkinci dereceden denkleminizin 'a' katsayısını giriniz: "))
    b = int(input("İkinci dereceden denkleminizin 'b' katsayısını giriniz: "))
    c = int(input("İkinci dereceden denkleminizin 'c' katsayısını giriniz: "))

    diskriminant = math.pow(b,2)-(4*a*c)

    if diskriminant>0:
        x1 = (-b+(math.sqrt(diskriminant)))/2*a
        x2 = (-b-(math.sqrt(diskriminant)))/2*a
        print(f"İkinci dereceden denklem sisteminizin kökleri {x1} ve {x2} dir.")
    elif diskriminant==0:
        sonuc = -b/2*a
        print(f"İkinci dereceden denklem sisteminizin iki tane birbirine eşit kökü vardır ve nu kök {sonuc} dir.")
    else:
        print("İkinci dereceden denklem sisteminizin reel kökü yoktur.")

    print(f"{a}x²+({b})x+({c}) denklemimizdir.")