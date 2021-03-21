def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = (not1+not2+not3)/3

    if ort>90:
        harf = ("AA")
    elif ort >= 85 and ort <= 89:
        harf = ("BA")
    elif ort >= 80 and ort <= 84:
        harf = ("BB")
    elif ort >= 75 and ort <= 79:
        harf = ("CB")
    elif ort >= 70 and ort <= 74:
        harf = ("CC")
    elif ort >= 65 and ort <= 69:
        harf = ("DC")
    elif ort >= 60 and ort <= 64:
        harf = ("DD")
    elif ort >= 50 and ort <= 59:
        harf = ("FD")
    else:
        harf = ("FF")

    return ogrenciAdi + ": " + harf + "\n"
    
    

def ortalamalari_oku():
    with open("Releaseee\obs\sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğr ad: ")
    soyad = input("Öğr soyad: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")

    with open("Releaseee\obs\sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+" "+ soyad+ ":"+not1+","+not2+","+not3+"\n")

def notlari_kaydet():
    with open("Releaseee\obs\sinav_notlari.txt","r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("Releaseee\obs\sonuclar.txt","w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları kayıt et\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kaydet()
    else:
        break

