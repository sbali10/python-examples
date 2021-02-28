'''
list = [1,2,3]

#list.append(4)    #liste sonuna 4 ekler
#lit.pop()         #listenin  son elemanını siler
#print(type(list))    #listenin classının yazdırr burda list mesela
 
print(list)

###############################################################################################################

def sayHello(name = "user"):               #Hello + girilen isimi yazan fonksiyon
    print("Hello " + name)

sayHello('Serhat')    #name yerine atanır
#sayHello()            #name yerine birşey girilmezse "user" kelimesini otomatik atar

###############################################################################################################

def total(num1,num2):       #İki sayıyıyı toplayan fonskiyon
    return num1 + num2

result = total(10,20)
print(result)

'''

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