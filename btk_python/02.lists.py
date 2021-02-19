#my_list =  [1,2,'uc',4,5.6]

#list1 = ['bir','iki']
#list2 = ['uc','dort','bes']
#my_list = list1 + list2

#print(len(my_list))
#print(my_list[2])

#print(my_list)

###############################

#arabalar = ['Bmw', 'Mercedes', 'VW', 'Audi']

#print(len(arabalar)) #eleman sayısını yazdırır

#print(arabalar[0], arabalar[3]) #listenin ilk ve son değerini yazdırır

#arabalar[2] = "Porsche"  #VW değerini Porsche ile değiştrir
#print(arabalar)

#result = 'Mercedes' in arabalar  #mercedes değeri arabalar list i içinde var mı?

#result = arabalar[-2]   #liste eksi 2 indexinin yazdırır


#result = arabalar[0:3] #listenin ilk 3 elemanını yazdırır

#arabalar[-2:] = ['toyota', 'renault']  #listenin son 2 değerini değiştirri
#result = arabalar

#result = arabalar + ["nissan", "skoda"] # listeye ekleme yapar ama mevcut listeyi değiştrimez yeni lliste oluşturur

#del arabalar[-1] # sondaki itemı siler listeden


#print(result)

#####################################################################################################

#numbers = [1, 3, 5.6, 0, -2]
#letters = ['a', 'bkc', 'de', 'merhaba']

#val = max(numbers)
#val = min(numbers)
#val = numbers[2:6]

#val = max(letters)
#val = min(letters)

#numbers.append(10)  #liste sonuna değeri ekler
#numbers.insert(3, 21)  #3. değerden sonra 21 i ekler(0 dan başla sayamaya)
#numbers.insert(-1, 555) #sondan bir önceki sıraya 555 i ekler listede

#numbers.pop(2)  #2.indexteki elemanı siler
#numbers.remove(3)   #3 ü listeden siler(elemanı direk listeden silme)

#numbers.sort()  #listedeki indexleri sıralar
#numbers.reverse()  #listeyi terse çevirir
#print(len(numbers)) #eleman sayısını yazdırır
#print(numbers.count(9))   #listede kaç adet 9 elemanı var bakar

#print(numbers)


############################################################################################################

names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

#names.append('Cenk')     #Cenk'i listenin sonuna ekler

#names.insert(0, 'Sena')     #Sena'yı listenin başına ekler

#names.remove('Deniz')       #Deniz'i listeden uçurur

#d = names.index('Deniz')    #Deniz'index(listedeki konum nosu) nosunu verir
#print(d)

#result = 'Ali' in names      #Ali listenin bir elemanı mı diye kontrol eder
#print(result)

#names.reverse()              #liste elemanlarını ters çevirir

#names.sort()                  #elemanları alfabetik sıralar

#str = "Chevrolet,Dacia"  
#result = str.split(',')        #string ifadeyi listeye çevirir
#print(result)

#min = min(years)
#print(min)                       #listenin en küçük elemanını yazdırır
#max = max(years)
#print(max)                       #listenin en büyük elemanını yazdırır

#result = years.count(1998)        #1998 ifadesi listede kaç kere var onu yazdırır
#print(result)

#years.clear()                       #years listesinin temizler



#print(names)