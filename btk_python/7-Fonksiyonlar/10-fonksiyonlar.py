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

###############################################################################################################

def add(*params):                   #Girilen tüm parametleri toplama
    print(type(params))             #(tuple listesi geleceğinden *(tek yıldız) kullandık)
    print(params)
    return sum((params))

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50))

###############################################################################################################

def displayUser(**params):
    print(type(params))           # (dictionary geleceğinden **(iki yıldız) kullandık)
    for key, value in params.items():
        print("{} is {} ".format(key,value))

displayUser(name= "Serhat", age= 27, city= "Izmir")
displayUser(name= "Baran", age= 23, city= "Izmir", phone= 5512318)

###############################################################################################################

def multiyazdir(t, word):                   #girilen deeğer kadar girilen kellime yazdırma
    i = 1
    while i <= t:
        print(word)
        i += 1


multiyazdir(3, "serhat")

###############################################################################################################

def listeOlustur(*params):              #sınırsız sayıdaki parametre ile liste oluşturma
    liste = []

    for param in params:
        liste.append(param)

    return liste

result = listeOlustur(2, 3, 5, "a")
print(result)

###############################################################################################################
'''

