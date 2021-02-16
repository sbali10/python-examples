'''
###Kullanıcıdan maaş değerini girdirip vergi sonrası kalan net tutarı yazdıran fonksiyon

maasA = int(input('Maaşınızı giriniz: '))
vergi = 0.27
Net_Maas = print(int(maasA - (maasA * vergi)))

'''

'''

### Yarıçapı dışardan girdirerek daire alanı ve çeveresi hesaplama

r = float(input("Yarıcapi giriniz : "))
pi = 3.14

alan = (pi * (r ** 2))
print("Daire_Alani: "+ str(alan)  )


cevre = float(2 * pi * (r ** 2))
print("Daire_Çevresi: "+ str(cevre))

'''
'''
###Textin çeşitli özelliklerini yazdırma

name = 'Serhat'
surname = "Bali"
age = 27

about = 'My name is '+ name + ' ' + surname + ' and  \nI am '+ str(age) + ' years old'
length = len(about)

print(about)
print(about[0])
print(about[3])
print(about[length-1])
print(about[-1])
print(about[3:7])
print(about[3:])
print(about[:17])
print(about[2:40:3])

'''
'''
###Dışardan girilen değişkenleri cümle içine farklı şekillerde atayıp output olarak yazdırma

name = input('İsminizi giriniz: ')
surname = input('Soyadınızı giriniz: ')
age = input('Yaşınzı giriniz: ')

#print('My name is {} {} '.format(name, surname))
#print("My name is {n} {s}, and I'm {a} years old.  ".format(n=name, s=surname , a=age))
print(f"My name is {name} {surname}, and I'm {age} years old.")

'''