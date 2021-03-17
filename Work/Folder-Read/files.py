# #folder oluşturma(w yazma modu)
# #file = open("C:\Users\serha\OneDrive\Masaüstü\newfile.txt", "w")    #masaüstüne yeni dosya oluşturma

# #dosya oluşturma ve içine türkçe karakterde olsa yazdırma(dosya varsa içeriğini sile bunları ekler)
# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Serhat Bali")
# file.close()

########################################################################################################33
# #append ile ekleme (yeni değer ekleme ve değeri istenirse alt satıra)
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("Serhat Bali \n")
# file.close()