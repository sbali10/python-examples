#girilen ürün sayısı kadar isim ve fiyat bilgisini listele

urunler = []
adet = int(input("Ürün Sayısı : "))
i = 0

while (i < adet):
    name = input("Ürün ismi: ")    
    price = input("Ürün fiyatı: ")
    urunler.append({
        "name" : name,
        "price" : price

    })
    i += 1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")
