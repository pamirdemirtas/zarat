while True:
    zar = input ("Komut giriniz : ")
    from random import randint
    if zar == '/zarat':
        while True:
            try:
                kacYuz = input("Kaç yüzlü zar atmak istersin? ?: ")
                intzar = int(kacYuz)
                yuz = randint(1, intzar)
                print(f"{intzar} yüz'lü zar'dan gelen sayı : {yuz}")
                input("Çıkış için 'Enter' tuşuna basabilirsin.")
                break
            except:
                print("Hatalı girdi. Lütfen sayı gir!")
    else:
        print('Hatalı girdi.')
        pass