#import math as islem

#value = dir(math)
#value = help(math.factorial)
#value = math.sqrt(49)
#value = math.factorial(5)
#value = math.floor(5.9)
#value = islem.factorial(5)

#####################################################
# def sqrt(x):                 #bu fonksiyonu importun altına alsaydık x : DEĞER yazırrıdı sadece
#     print("x : " + str(x))


# from math import *      #modülü bu şekilde çağırrısak math.factorial demeye gerek kalmaz direk fonk adı ile çağrılabilir

# value = factorial(4)
# value = sqrt(21)

# print(value)


#####################################################

import random

#result = random.random()   # 0.0 ile 1.0 arası random değer üretir
#result = random.random * 100
#result = random.uniform(1,10)   # verilen aralıkta sayı üretir
#result = int(random.uniform(1,10))   # verilen aralıkta tamsayı üretir, virgülden sonrasını atar
#result = random.randint(10,21)   # verilen aralıkta tamsayı üretir



names = ["ali","veli","selami"]
# result = names[random.randint(0,len(names)-1)]    #names içerisine girilen değer sayısı farketmeksizin random yazdırır
# result = random.choice(names)                      #liste içerisinde random değer seçer ve yazdırır



# liste = list(range(10))   #0-10 arası liste oluşturur
# random.shuffle(liste)    #listedeki değerleri ratgele sıralar
# result = liste   



liste = range(100)
#result = random.sample(liste, 3)         #liste içerisinde random 3 değer getirir
result = random.sample(names, 2)          #names içerisinde rastgele 2 değeri yazdırır
print(result)
