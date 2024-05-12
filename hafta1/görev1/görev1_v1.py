dönem_ort = float(input("Not ortalamanızı giriniz: "))
vize = int(input("Vize notunuzu giriniz: "))
vize_katsayı = float(input("Vizenin katsayısını girin: "))
final = int(input("final notunuzu giriniz: "))
final_katsayi = float(input("Final notunuzun katsayısını girin: "))
lab_kontrol = str(input("Dersinizin laboratuvarı var mı? "))

def nothesapla ():
    if lab_kontrol == "evet":
        lab = int(input("Laboratuvar notunuzu giriniz: "))
        lab_katsayı = float(input("Laboratuvar notunuzun katsayısını girin: "))
        global ortalama
        ortalama = ((vize*vize_katsayı)+(final*final_katsayi)+(lab*lab_katsayı))
    else:
        ortalama = ((vize*vize_katsayı)+(final*final_katsayi))
    return ortalama

def harf_notu(ortalama):
    if 90<=ortalama<100:
        print(f"Ortalamanız {ortalama} ve harf notunuz: AA")
    elif 80<=ortalama<=89:
        print(f"Ortalamanız {ortalama} ve harf notunuz: BA")
    elif 75<=ortalama<=79:
        print(f"Ortalamanız {ortalama} ve harf notunuz: BB")
    elif 70<=ortalama<=74:
        print(f"Ortalamanız {ortalama} ve harf notunuz: CB")
    elif 60<=ortalama<=69:
        print(f"Ortalamanız {ortalama} ve harf notunuz: CC")
    elif 50<=ortalama<=59:
        print(f"Ortalamanız {ortalama} ve harf notunuz: DC")
    else:
        print(f"Kaldınız ve maalesef ki harf notunuz FF :(")
        
cevap = nothesapla()
harf_notu(cevap)