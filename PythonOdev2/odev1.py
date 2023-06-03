import pysimplegui as sg

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
            return [["Kitap bulunmamaktadır."]]
        else:
            tablo = [["ID", "Kitap Adı", "Kitap Fiyatı (TL)"]]
            for kitap in self.kitaplar:
                tablo.append([kitap.kitap_id, kitap.kitap_adi, kitap.kitap_fiyati])
            return tablo


kitap_listesi = KitapListesi()

layout = [
    [sg.Text("Kitap Adı:"), sg.Input(key="-KITAP_ADI-")],
    [sg.Text("Kitap Fiyatı:"), sg.Input(key="-KITAP_FIYATI-")],
    [sg.Button("Kitap Ekle"), sg.Button("Çıkış")],
    [sg.Table(values=[], headings=["ID", "Kitap Adı", "Kitap Fiyatı (TL)"], key="-LISTE-")]
]

window = sg.Window("Kitap Listesi", layout)

while True:
    event, values = window.read()
    if event == "Çıkış" or event == sg.WINDOW_CLOSED:
        break

    kitap_adi = values["-KITAP_ADI-"]
    kitap_fiyati = values["-KITAP_FIYATI-"]

    if kitap_adi and kitap_fiyati:
        try:
            kitap_fiyati = float(kitap_fiyati)
            kitap_id = len(kitap_listesi.kitaplar) + 1

            yeni_kitap = Kitap(kitap_id, kitap_adi, kitap_fiyati)
            kitap_listesi.kitap_ekle(yeni_kitap)
            window["-LISTE-"].update(values=kitap_listesi.kitaplari_goster())
            sg.popup("Kitap başarıyla eklendi.")
        except ValueError:
            sg.popup("Geçersiz fiyat. Lütfen tekrar deneyin.")

    window["-KITAP_ADI-"].update("")
    window["-KITAP_FIYATI-"].update("")

window.close()
