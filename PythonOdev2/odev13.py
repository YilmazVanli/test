class Kitap:
    def __init__(self, kitapId, kitapAdi, kitapFiyati):
        self.kitapId=kitapId
        self.kitapAdi=kitapAdi
        self.kitapFiyati=kitapFiyati

    def display(self):
        return f"KitapId: {self.kitapId}\nKitapAdi: {self.kitapAdi}\nKitapFiyati: {self.kitapFiyati}TL\n"
    print("\t\t\t\t\t\t\t!!Kütüphanemize Hoş Geldiniz!!")
    
while True:
    kitapId=input("Lütfen Kitap Id giriniz: ")
    kitapAdi=input("Lütfen Kitap Adi giriniz: ")
    kitapFiyati=input("Lütfen Kitap Fiyati giriniz: ")
    kitap=Kitap(kitapId,kitapAdi,kitapFiyati)
    print(kitap.display())
    
    print("Devam etmek ister misiniz? (E/H)")
    secim=input()

    if secim == 'h' or secim == 'H':
        print("Teşekkür eder iyi günler dileriz...")
        break

    elif secim == 'e' or 'E':
        continue
    
    else:
        print("Yanliş Seçim Yaptiniz Tekrar Deneyiniz !")
        continue
