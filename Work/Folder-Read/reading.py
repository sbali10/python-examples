
# try:
#     file = open("Work\Folder-Read\newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()


file = open("Work\Folder-Read\newfile.txt","r", encoding="utf-8")

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

###sayfa başında güncelleme###

# with open("Work\Folder-Read\newfile.txt","r+",encoding="utf-8") as file:          #file.close kullnamamak için with kullandık
#     content = file.read()
#     content = "ÖBBali\n" + content
#     file.write(content)
#     #file.seek(0)                #cursorü 0.karakter konumuna gönderdik
#     #print(file.tell())           #cursorün nerede olduğunu gösterir
#     #content2 = file.read()
#     #print(content2)               #5.satırda bıraktığımız cursörden geri kalanları yazdırdık


# with open("Work\Folder-Read\newfile.txt","r",encoding="utf-8") as file:              #dosya başına ekleme 
#     print(file.read())

################################################################################################################

###sayfa sonunda güncelleme###

# with open("Work\Folder-Read\newfile.txt","a", encoding="utf-8") as file:             #dosya sonun ekleme yapar
#     file.write("\nCBali")

# with open("Work\Folder-Read\newfile.txt", "r", encoding="utf-8") as file:            #içine yazdığımız dosyayı ekrana yazdırır
#     print(file.read())


################################################################################################################

###Sayfa ortasına ekleme yapma###

# with open("Work\Folder-Read\newfile.txt", "r+", encoding="utf-8") as file:
#     list = file.readlines()
#     list.insert(1,"OrtayaEkle2")
#     file.seek(0)
#     file.writelines(list)
#     # print(list)
#     # for i in list:
#     #     file.write(i)

# with open("Work\Folder-Read\newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

################################################################################################################

