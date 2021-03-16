# try:
#     x=int(input("x: "))
#     y=int(input("y: "))

#     print(x/y)

# except (ZeroDivisionError,ValueError):
#     print("Yanlış değer girdiniz")

######################################################################################################


#liste = ["1","3","5a","10b","20","k7"]


# #listeden sadece nümerik değerleri çeker
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue



# #kullanıcı "q" ya basmadıkça her inputun sayı olduğunu kontrol et yoksa error ver

# while True:
#     sayi = input("sayi: ")
#     if sayi == "q":
#         break

#     try:
#         result = float(sayi)
#     except ValueError:
#         print("geçersiz sayı")
#         continue



#türkçe karakter hatası

def checkPassword(parola):
    turkce_karakter = "şçğöüıİÜÖĞÇŞ"
    
    for i in parola:
        if i in turkce_karakter:
            raise TypeError("parola türkçe karakter içeremez")
    
        else:
            pass
    
    print("Geçerli parola")

parola = input("şifre giriniz: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)

