fak = int(input("faktöriyeli alınacak sayıyı giriniz: "))

if fak==0:
    print("Girdiğiniz sayı 0 olduğundan faktöriyeli de 0'dır.")
elif fak==1:
    print("Girdiğiniz sayı 1 olduğundan faktöriyeli de 1 olacaktır.")
else:
    for i in range (1,fak):
        fak = fak*i
    print(f"Girdiğiniz sayının faktöriyeli {fak} dır.")
