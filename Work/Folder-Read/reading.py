
# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()


file = open("newfile.txt","r", encoding="utf-8")

#################################################
# for i in file:
#     print(i, end="")
################################################
# content = file.read()
# #content = file.read(5)   #ilk 5 karakteri alır
# print(content)

# file.close
##################################################
#print(file.readline())   #satır olarak okur
#file.close()

###################################################
#print(file.readlines(0))
#file.close()

######################################################################################################
with open("newfile.txt","r",encoding="utf-8") as file:          #file.close kullnamamak için with kullandık
    content = file.read()
    print(content)
    file.seek(5)                #cursorü 5.karakter konumuna gönderdik
    print(file.tell())           #cursorün nerede olduğunu gösterir
    content2 = file.read()
    print(content2)               #5.satırda bıraktığımız cursörden geri kalanları yazdırdık