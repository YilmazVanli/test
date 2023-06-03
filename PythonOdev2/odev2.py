class Kitap:
    def __init__(self, kitap_id, kitap_adi, kitap_fiyati):
        self.kitap_id = kitap_id
        self.kitap_adi = kitap_adi
        self.kitap_fiyati = kitap_fiyati

    def __str__(self):
        return f"Kitap ID: {self.kitap_id}\nKitap Adı: {self.kitap_adi}\nKitap Fiyatı: {self.kitap_fiyati} TL"


class KitapListesi:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitaplari_goster(self):
        if not self.kitaplar:
            print("Kitap bulunmamaktadır.")
        else:
            for kitap in self.kitaplar:
                print(kitap)


kitap_listesi = KitapListesi()

while True:
    kitap_adi = input("Kitap Adı (Çıkmak için 'q' tuşuna basın): ")
    if kitap_adi.lower() == 'q':
        break

    try:
        kitap_fiyati = float(input("Kitap Fiyatı: "))
        kitap_id = len(kitap_listesi.kitaplar) + 1

        yeni_kitap = Kitap(kitap_id, kitap_adi, kitap_fiyati)
        kitap_listesi.kitap_ekle(yeni_kitap)
        print("Kitap başarıyla eklendi.\n")
    except ValueError:
        print("Geçersiz fiyat. Lütfen tekrar deneyin.\n")

print("Kitap Listesi:")
kitap_listesi.kitaplari_goster()
