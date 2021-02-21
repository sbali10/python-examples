#and, or, not

'''
#dışardan girilen sayı 5 ile 10 arasıanda ve çift ise aşağıdakiler yapar
x = int(input("rakam giriniz : "))

result = ((x>5) and (x<10) and (x%2==0))

if result == True:
    print("tebrikler")
else:
    print("try again")

'''
#0-100 arasımı girilen sayı kontrolü
#k = int(input("sayı gir : "))    
#result = (0 < k < 100)
#print(result)

#0 dan büyük çift sayı mı konrolü
#k = int(input("sayı gir : "))    
#result = (0 < k ) and (k % 2 == 0)
#print(result)


'''
#VKİ Hesaplama

name = input("Adınız: ")
weight = int(input("Kilonuz: "))
length = int(input("Boyunuz metre cinsinden: "))

k = (weight / (length **2))

if k < 18.5 :
    print(f"{name} is to heavy")
elif 18.5 <= k < 25 :
    print(f"{name} is normal")
elif 25 <= k  :
    print(f"{name} have much kilos ")

########################################################################
x = y [1, 2, 3]
print(x is y)    #false yazar
print(x == y)    #true yazar


x = ['apple', 'banana']    #banana x içinde varsa true yazar
print('banana' in x)    

'''