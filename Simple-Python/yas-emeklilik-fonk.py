def yasHesapla(dogumYili):            

    '''
    DOCSTRING: Yaş hesaplama fonskiyonu
    INPUT: Dogum yili
    OUTPUT: yas
    '''
    return 2021 - dogumYili

ageSerhat = yasHesapla(1994)
print(ageSerhat)
help(yasHesapla)                            #tırnakların arasındaki fonksiyonu detaylı açıklayan ksımı görebilmek için


def EmeklilikKalan(dogumYili, isim):

    '''
    DOCSTRING: Yaş hesaplama fonskiyonunuda kullanarak emeklilik hesaplama
    INPUT: Yas ve Isim
    OUTPUT: Kalan Yil

    '''          
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")

EmeklilikKalan(1994, "Serhat")
EmeklilikKalan(1960, "Celal")
help(EmeklilikKalan)                          #tırnakların arasındaki fonksiyonu detaylı açıklayan ksımı görebilmek için