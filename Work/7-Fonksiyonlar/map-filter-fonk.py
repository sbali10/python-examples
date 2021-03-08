'''
def square(num): return num ** 2    

numbers = [1,3,5,9]

result = list(map(square, numbers))     #map numbers içindeki tüm değerleri square fonksiyonuna gönderir

print(result)


#########################################################################################

numbers = [1,3,5,9]

result = list(map(lambda num: num ** 2, numbers))         # lambda kullanılarak fonksiyon oluşturmadan eylem tanımlanır

print(result)

#######################################################################################

'''
numbers = [1,3,5,9,4,10] 

def check_even(num): return num % 2 == 0

#result = list(filter(check_even, numbers))               #numbers içindeki değerler check_even fonk girer uygun olanlar return edilir
#result = list(filter(lambda num: num%2==0, numbers))     #lambda ile özelliği kendimiz tanımlarız

#result = check_even(numbers[3])                          #numbers içindeki 3. değerin uyup uymadığını kontrol eder

print(result)