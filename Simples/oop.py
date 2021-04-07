# #class  -> Person (name, surname, birthday, calculateAge())       Person: classımız içerisinde objeler var ve calculateAge() metodumuz var   (örneğin : ahmet için ahmet.calculateAge() çağrılır)

# #object = instance


# class Person:

#     pass

#     #class attributes
#     address = "no information"
#     #constructor attributes
#     def __init__(self, name, year):
#     #object attributes
#         self.name = name
#         self.year = year
#         print("init metodu çalıştı")
#     #instance methods
#     def intro(self):
#         print("Hello there " +  self.name)
    
#     #instance methods

#     def calculateAge(self):
#         return 2021 - self.year

# # object (instance)

# p1 = Person(name="ali", year=1994)
# p2 = Person(name="veli", year=1998)

# p1.intro()
# p2.intro()

# print(f"adım: {p1.name} ve yaşım: {p1.calculateAge()}")
# print(f"adım: {p2.name} ve yaşım: {p2.calculateAge()}")

# '''
# #updating 

# #p1.name = "Selami"   #burdan farklı object verilebilir

# #accessing object attributes
# print(f'p1 name: {p1.name} year: {p1.year} address: {p1.address}')
# print(f"p2 name: {p2.name} year: {p2.year} address: {p2.address}")

# print(p1)
# print(p2)

# #print(type(p1))
# #print(type(p2))
# '''



# ###################################################################################################################################################
# alan ve çevre hesaplama

# class Circle:
#     #class object attribitu
#     pi = 3.14

#     def __init__(self, yaricap=1):
#         self.yaricap = yaricap

#         #methods

#     def cevre_hesapla(self):
#         return 2 * self.pi * self.yaricap
#     def alan_hesapla(self):
#         return self.pi * (self.yaricap**2)

# c1 = Circle()    #yaricap = 1 
# c2 = Circle(5)

# print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
# print(f"c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")
