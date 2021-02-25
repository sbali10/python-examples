x = 0

'''
while x < 100:               #1 den 100 e kadar sayıları yazdırma
    print(x)
    x += 1
print("Bitti")



while x < 100:                               #tek mi çift mi ayırt edip yaz
    if x % 2 == 1:
        print(f"sayı tek : {x} ")
    else:
        print(f"sayı çifttir : {x}")
    x += 1

print("Bitti")

  
name = ''   #boşken false olur                   #İsmi girene kadar sorar boşluk kabul etmez
while not name.strip():
    name = input("İsminizi giriniz: ")

print(f"Merhaba, {name}")



sayilar = [1,3,5,7,9,12,19,21]


x = 0
while (x < len(sayilar)):                                            #sayiları ekrana yazdırma
    x += 1
    print(sayilar)



say0 = int(input("başlangıç değeri : "))      #girilen 2 sayı arasındaki sayıları yazdırma
say1 = int(input("bitiş değeri : "))

m = min(say0,say1)
b = max(say0,say1)

x = m + 1

while m < x < b:
    print(x)
    x += 1



x = 100                      #100 den geriye sayıları yazdırır

while x > 0:
    print(x)    
    x -= 1


a = int(input("sayi1 : "))                #girilen değerleri liste haline getirir küçükten büyüğe sıralar
b = int(input("sayi2 : "))
c = int(input("sayi3 : "))
d = int(input("sayi4 : "))
e = int(input("sayi5 : "))

k = [a,b,c,d,e]
n = sorted(k)

print(n)

# yada aynı şeyi while ile yaparız

numbers = []

i = 0

while i<5:
    sayi = int(input("sayi"))
    numbers.append(sayi)
    i +=1
numbers.sort()
print(numbers)





urunler = []
adet = int(input("Ürün Sayısı : "))                #girilen ürün sayısı kadar isim ve fiyat bilgisini listele
i = 0

while (i < adet):
    name = input("Ürün ismi: ")    
    price = input("Ürün fiyatı: ")
    urunler.append({
        "name" : name,
        "price" : price

    })
    i += 1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")

'''