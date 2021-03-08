'''

website = "https://github.com/sbali10"
course = "Python Denemeler"

name, surname, age, job = 'Serhat', 'Bali', 27, "engineer"

#length = len(course)
#print(length)   #course karakter sayısı

#print(website[0:5])   #website ın ilk 5 karakteri

#print(website[15:18])  #website ın com'lı kısmı

#print(course[:15])    #ilk 15
#print(course[15:])    #son 15

#print(course[::-1])   #tersten yazdırma

#print(f"My name is {name} {surname} and I'am {age} years old. I work as a {job}")  #değişkenleri setleyerek çıktı yazdırma

#d = "hello world"
#result = d.replace('w','N')         #replace methodu kullanımı w görülen yerleri N ile değştirir


#k = "abc"    #3 kere arkad arakaya abc yazdırma
#result = k * 3

#result = "  Hello World  ".strip()   #baştaki ve sondaki boşlukları siler
#result = "  Hello World  ".lstrip()  #soldaki boşlukları siler
#result = "  Hello World  ".rstrip()  #sağdaki boşlukları siler


#result = "www.github.com".strip('w.moc')   #baştaki ve sondaki karakterleri siler sadece github kısmı kalır

#result = website.count('j')  #kaç adet j karakteri var onu yazdırır
#result = website.count('sbali')  #sbali ifadesi varmı onu yazdırır
#result = website.count('github',0,19)  #0 ile 10 arasında github değeri varmı ona bakar

#result = website.find('com')   #com değerini arar ve var ise index numarasını değerin ilk karakterinin  çıktı olarak verir
#result = website.find('com'0,10) #0 ile 10 arasonda com değerinin arar

#result = course.isalpha()   #course ifadesindeki değerler alfabetik ise true verir
#result = 'Helllo'.isalpha()  #Hello ifadesindeki karakterler alfabetik sıralı ise bize true verir
#result = course.isdigit()   #course içindeki değerler sayısal ise true verir
#result = '123'.isdigit() #123 değerleri sayısal olduğundan true verir

#result = 'Merhaba'.center(50)   #başta ve sonda boşluk olacak şekilde 50 merkeze atarak Merhabayı 50 karakteri yazdrır
#result = 'Merhaba'.center(50, '*') #başa ve sona yıldız ekleyerek 50 karakteri tamamlar
#result = 'Merhaba'.ljust(50, '*')  #sola yaslar kalan kısıma * koyar
#result = "Merhaba".rjust(50, '*') #sağa yaslar ve başına yıldız koyar

print(result)
##############################################################################################################
'''
message = "Hello World, safe World"

#message = message.upper()    #tüm harfler büyük
#message = message.lower()   #tüm harfler küçük
#message = message.title()  #her kelimenin ilk harfi büyük
#message = message.capitalize()  #Sadece cümlenin ilk harfi büyük

#message = message.strip()  #baştaki ve sondaki boşluklar gider
#message = message.split()  #boşluk olan tüm kelimeleri ayırı dizi oluşturur
#message= '---'.join(message)  ###tüm boşlıkları --- ile doldurur

#index = message.find("safe")   #safe kelimesini message değişkeninde arar varsa pozitif bir sayı çıktı verir
#print(index)

#isFound = message.startswith('H')   #cümle H ile başlıyorsa true output verir
#isFound = message.endswith('l')    #cümlenin bittiği harfi check eder
#print(isFound)

#message = message.replace('o','S') #message değişkeni içindeki o harflerini S ile değiştirir

#message = message.center(100)  #message çıktısını 100 karaktelik bir alana hizalar


print(message)

'''

########################################################################################################