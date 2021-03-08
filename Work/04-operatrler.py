'''
#x = 5
#x += 5   #x = x + 5 demektir
#x //= 2   #x = x / 2 nin bölümünün tam kısmı yani 2 dir cevabı
#x **= 4   #x in 4 üssünü alır x değeri olarak

#print(x)

'''

x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

'''
#Kullanıcının girdiği 2 sayı ile xyz toplamlarınının farkını yazdırdık
a = int(input("sayı giriniz : "))
b = int(input("sayı giriniz : "))

c = a * b
print(c)

d = x + y +z
print(d)

dif = c - d
print(dif)

'''
'''

k = y // x       #y nin x e kalansız bölümü
print(k)

d = x + y +z    # xyz toplamının mod 3 ü
d = d % 3
print(d)

y = y ** x    # y nin x. kuvveti
print(y)

'''


###Karşılaştırma Operatörleri

'''

a, b, c = 5, 5, 10

result = (a == b)  #true yazmasını bekleriz çünkü eşit 
result = (a != b)  # false yazmasını bekleriz çünkü eşit

print(result)

'''
#girilen 2 sayıdan büyük olanı ekrana yazdırır

#a = int(input("vizenot giriniz : "))
#b = int(input("finalnot giriniz : "))

'''
d = max(a, b)   #girilen 2 sayıdan büyük olanı ekrana yazdırır
print(d) 
'''

'''
#vize final notlatını giridirip ortalama hesaplama ve 50 üzerindeyse geçme durumu true yazdırma
vize = (a * 60) / 100
final = (b * 40) /100
ort = vize + final
print(ort)

Gecti = (ort > 50)
print(Gecti)
