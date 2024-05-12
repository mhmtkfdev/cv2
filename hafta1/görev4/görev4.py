metin = "mum yapay ada kazak "

a = metin.split()
for i in a:
    ters = (i[::-1])
    if ters == i :
        print(f"{ters} palindromdur ")


