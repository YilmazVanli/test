import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

def kitap_ekle():
    kitap_adi = kitap_adi_entry.get()
    kitap_fiyati = kitap_fiyati_entry.get()

    if kitap_adi and kitap_fiyati:
        try:
            kitap_fiyati = float(kitap_fiyati)
            kitap_id = len(kitap_listesi.kitaplar) + 1
            yeni_kitap = Kitap(kitap_id, kitap_adi, kitap_fiyati)
            kitap_listesi.kitap_ekle(yeni_kitap)
            liste_guncelle()
            messagebox.showinfo("Kitap Ekle", "Kitap başarıyla eklendi.")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz fiyat. Lütfen tekrar deneyin.")
    else:
        messagebox.showwarning("Uyarı", "Lütfen kitap adı ve fiyatını girin.")

def liste_guncelle():
    kitaplar = kitap_listesi.kitaplari_goster()
    for i in range(len(kitaplar)):
        for j in range(len(kitaplar[i])):
            liste_tablosu.set(kitaplar[i][j], i, j)

root = tk.Tk()
root.title("Kitap Listesi")

kitap_adi_label = ttk.Label(root, text="Kitap Adı:")
kitap_adi_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

kitap_adi_entry = ttk.Entry(root)
kitap_adi_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

kitap_fiyati_label = ttk.Label(root, text="Kitap Fiyatı:")
kitap_fiyati_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

kitap_fiyati_entry = ttk.Entry(root)
kitap_fiyati_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

kitap_ekle_button = ttk.Button(root, text="Kitap Ekle", command=kitap_ekle)
kitap_ekle_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

liste_tablosu = ttk.Treeview(root, columns=("ID", "Kitap Adı", "Kitap Fiyatı"))
liste_tablosu.heading("#0", text="")
liste_tablosu.heading("ID", text="ID")
liste_tablosu.heading("Kitap Adı", text="Kitap Adı")
liste_tablosu.heading("Kitap Fiyatı", text="Kitap Fiyatı (TL)")
liste_tablosu.column("#0", width=0, stretch=tk.NO)
liste_tablosu.column("ID", width=30, anchor=tk.W)
liste_tablosu.column("Kitap Adı", width=150, anchor=tk.W)
liste_tablosu.column("Kitap Fiyatı", width=100, anchor=tk.W)
liste_tablosu.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=liste_tablosu.yview)
scrollbar.grid(row=3, column=2, sticky=tk.N+tk.S)
liste_tablosu.configure(yscrollcommand=scrollbar.set)

def kitap_ekle():
    kitap_adi = kitap_adi_entry.get()
    kitap_fiyati = kitap_fiyati_entry.get()

    if kitap_adi and kitap_fiyati:
        try:
            kitap_fiyati = float(kitap_fiyati)
            kitap_id = len(kitap_listesi.kitaplar) + 1
            yeni_kitap = Kitap(kitap_id, kitap_adi, kitap_fiyati)
            kitap_listesi.kitap_ekle(yeni_kitap)
            liste_guncelle()
            messagebox.showinfo("Kitap Ekle", "Kitap başarıyla eklendi.")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz fiyat. Lütfen tekrar deneyin.")
    else:
        messagebox.showwarning("Uyarı", "Lütfen kitap adı ve fiyatını girin.")

def liste_guncelle():
    liste_tablosu.delete(*liste_tablosu.get_children())
    kitaplar = kitap_listesi.kitaplari_goster()
    for kitap in kitaplar:
        liste_tablosu.insert("", tk.END, values=kitap)

root.mainloop()

