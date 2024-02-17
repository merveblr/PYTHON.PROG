# -*- coding: utf-8 -*-


class Kütüphane:
    def __init__(self, dosya_yolu="books.txt"):
        self.dosya_yolu = dosya_yolu
        self.dosya = open(dosya_yolu, "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplistesi(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()
        for kitap in kitaplar:
            kitapb = kitap.split(',')
            kitapadi, yazar, yayintarihi, sayfasayisi = kitapb
            print(f"Kitap: {kitapadi}, Yazar: {yazar}")

    def kitap_ekle(self):
        kitapadi = input("Kitap Adını Giriniz: ")
        yazar = input("Kitabın Yazarı Kimdir: ")
        yayintarihi = input("Kitabın Yayınlanma Tarihi Nedir: ")
        sayfasayisi = input("Kitabın Sayfa Sayısı Kaçtır: ")
        kitapb = f"{kitapadi},{yazar},{yayintarihi},{sayfasayisi}\n"
        self.dosya.write(kitapb)
        print("KİTAP KÜTÜPHANEYE EKLENMİŞTİR!")

    def kitap_sil(self):
        silinecek_kitapadi = input("Silmek İstediğiniz Kitap Adını Giriniz: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()
        guncelkitaplar = []

        for kitap in kitaplar:
            if silinecek_kitapadi not in kitap:
                guncelkitaplar.append(kitap)

        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines("\n".join(guncelkitaplar))
        print("KİTAP BAŞARIYLA SİLİNDİ!")


kutuphane = Kütüphane()
print("Önceden eklenmiş 5 kitap:")
kutuphane.kitaplistesi()
print()

while True:
    print("       MENÜ       ")
    print("1- Kitap Listesi")
    print("2- Kitap Ekle")
    print("3- Kitap Sil")
    print("4- Çıkış")

    kullanici = input("1-4 Arası Bir Sayı Giriniz: ")

    if kullanici == "1":
        kutuphane.kitapları_listele()
    elif kullanici == "2":
        kutuphane.kitap_ekle()
    elif kullanici== "3":
        kutuphane.kitap_sil()
    elif kullanici == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz Seçim. 1 ve 4 Arasındaki Sayılardan Seçin!")