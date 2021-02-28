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
