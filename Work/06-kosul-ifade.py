'''
#kullanıcı bilgilerini girdirip hatanın nerde olduğunu yazdırma

username = input("entry your username : ")
password = input("entry your password : ")


#username = "sbali"
#password = "1234"

if (username == "sbali"):
    if (password == "1234"):
        print("tebrikler")
    else:
        print("parola yanlış")
else:
    print("username yanlış")    

#elif example

num = int(input("Sayı : "))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print("sayı negatif")
else:
    print("sayı sıfırdır")    

'''
'''

#İsim,yaş,eğitim bilgisi girdirip ehliyet alabilme durumu sorgulama

name = input("İsim : ")
age = int(input("yaş : "))
education = str(input("eğitim bilgisini seçiniz \n lise \n üniversite \n Tercihiniz ? : "))
print(education)

if (age >= 18):

    if (education == 'lise') or (education == 'üniversite'):
        print(f"Sayın {name} ehliyet alma süreciniz başlamıştır")
    else:
        print(f"Sayın {name} eğitim durumunuz ehliyet için yetersiz")

else:
    print(f"Sayın {name} ehliyet alamazsın, yaşın küçük ")


#Sınav notu girdisini hesaplama

exam1 = int(input("1. yazılı notunuzu giriniz : "))
exam2 = int(input("2. yazılı notunuzu giriniz : "))
fnlexam = int(input("Final notunuzu giriniz : "))

k = ((exam1 + exam2 + fnlexam) / 3)

if k < 25:
    print("Notunuz 0")
elif 25 <= k < 45 :
    print("Notunuz 1")
elif 45 <= k < 55 :
    print("Notunuz 2")
elif 55 <= k < 70 :
    print("Notunuz 3")         
elif 70 <= k < 85 :
    print("Notunuz 4")
elif 85 <= k < 100 :
    print("Notunuz 5")
else:
    print("geçersiz giriş")

'''

'''
#Araç bakım süresi hesaplama

import datetime

date = input("Aracınız ne zaman trafiğe çıktı? YYYY/AA/GG olarak giriniz ")
date = date.split('/')
firstDrive = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))

yet = datetime.datetime.now()

fark = yet - firstDrive
days = fark.days
print(days)

if days <= 730:
    print("2 yıl doldu 1.kontol için servise")
elif days > 730 and days < 1095:
    print("3 yıl doldu 2. kez servise")

'''