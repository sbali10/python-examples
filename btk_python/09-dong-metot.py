''''
name = "Serhat"

for a in name:
    if a == "r":                 #break dönüyü o değerde keser
        break                   #name içerisinde r ye gelene kadar harfleri yazdırır r de kesilir 
    print(a)                     

for a in name:
    if a == "r":                    #continue döngüde o değeri atlar devam eder
        continue                   #r harfini atlar dönüye devam eder 
    print(a)



x = 0

while x < 5:                           #2 yi atlar döngüye devam eder
    x += 1
    if x == 2:
        continue
    print(x)



x = 1                                  #1 den 100 e kdar olan sayıların toplamı
result = 0

while x <= 100:
    result += x
    x += 1
print(f"toplam: {result}")



x = 0                                  #1 den 100 e kdar olan çift sayıların toplamı
result = 0

while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x
print(f"Çift sayıların toplamı: {result}")



for item in range(10):                  #10 a kadar döngüdeki tüm sayıları yazdırır
    print(item)

for item in range(22,60,4):              #20 ile 60 arası 4 er artaratk gider
    print(item)



index = 0                                       #hangi indexte hangi karakterin olduğunu yazdırır
greeting = 'Hello'

for letter in greeting:
    print(f"index : {index}, letter : {greeting[index]} ")
    index += 1


                                 
greeting = 'Hello'                              #hangi indexte hangi karakterin olduğunu enumerate ile yazdırma

for item in enumerate(greeting):
    print(item)


list1 = [1,2,3,4,5]                               
list2 = ["a","b","c","d","e"]
list3 = ['x','y','z','r','t']


print(list(zip(list1, list2, list3)))           #3 listedeki elemanları index numaralarını baz alarak eşleştirir ve yanyana yazdırır


for item in zip(list1, list2, list3):           #3 listedeki elemanları index numaralarını baz alarak eşleştirir ve alt alta yazdırır
    print(item)


numbers = [x for x in range(10)]                  #10 a kdar olan sayılardan dizi oluşturur
print(numbers)


myString = "Hello"                                 #myString elemenlarını liste olarak teker teker yazdırır
myList = []

for letter in myString:
    myList.append(letter)
print(myList)


years = [1960, 1970, 1994, 1998]                   #listedeki yılları döngüye sokup günümüzle aradaki farkı buluruz
age = [2021-year for year in years]
print(age)


results = [x if x%2==0 else "TEK" for x in range(1,10)]    #döngüdeki sayılar tek mi string TEK çiftse değeri yzdırma
print(results)


result = []                                      #2 for iç içe liste haline getirir

for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)



numbers = [(x,y) for x in range(3) for y in range(3)]     #2 for iç içe liste haline getirir üsttekinin aynısı farklı gösterim
print(numbers)


#prime number checker (asal sayı kontrolör)

n = int(input("Input a number: "))
asalmi = True

if n == 1:
    print("1 asal değildir")

for i in range(2, n):
    if (n % i == 0):
        asalmi = False
        break

if asalmi:
    print("Sayı asaldir")

else:
    print("Sayı asal değildir")

'''