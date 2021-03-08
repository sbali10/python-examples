'''

numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

for a in numbers:
    print('hello')

################################################################
names = ["cll", 'glcn', "brn"]

for name in names:
    print(f"hello my name is {name}")

################################################################
tuple = [(1,2),(1,3),(3,5)]

for a,b in tuple:
    print(a,b)

################################################################
#Key ve değeri karşılıklı alan for döngüsü

d = {'a':1,'b':2,'c':3}

for key,value in d.items():
    print(key,value)

'''



################################################################################################################################
sayilar = [1,3,5,7,9,12,19,21]

'''
for n in sayilar:                  #3 ün katları
    if (n%3==0):
        print(n)



toplam = 0                          #sayıların toplamı
for n in sayilar:
    toplam += n
print('toplam: ',toplam)



for n in sayilar:                   #tek sayıların karesi
    if (n%2==1):
         print(n ** 2)



cities = ["izmir", "istanbul", "diyarbakir", "bitlis", "isparta"]      #5 ve daha az karakterli şehir isimlerini yaz

for sehir in cities:
    if (len(sehir) <= 5):
        print(sehir)


################################################################


urunler = [
    {'name':'s9',  'price':'30'},
    {'name':'s8',  'price':'25'},
    {'name':'s7',  'price':'20'},
    {'name':'s6',  'price':'15'}
]


toplam = 0                                        #tüm ürünlerin fiyatı toplamı
for urun in urunler:
    fyt = int(urun['price'])
    toplam += fyt
print('toplam ürün fiyatı: ', toplam)

 
for urun in urunler:                                #fiyatı 25 den pahalı olan ürünleri yazdır
    if (int(urun['price']) <= 25):
        print(urun['name'])


'''