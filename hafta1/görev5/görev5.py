while True:
    işlem=input("""
    lütfen yapılacak işlemi seçin
    toplama için 1
    çıkarma için 2
    çarpma için 3
    bölme için 4

        """
                     )
    sayı1=int(input("1. sayıyı gir"))
    sayı2=int(input("2. sayıyı gir"))
    sonuc1=sayı1+sayı2
    sonuc2=sayı1-sayı2
    sonuc3=sayı1*sayı2
    sonuc4=sayı1/sayı2
    if işlem=="1":
        print("girdiğiniz sayıların toplamı=",sonuc1)
    elif işlem=="2":
        print("girdiğiniz sayıların farkı=",sonuc2)
    elif işlem=="3":
        print("girdiğiniz sayıların çarpımı=",sonuc3)
    elif işlem=="4":
        print("girdiğiniz sayıların bölümü=",sonuc4)