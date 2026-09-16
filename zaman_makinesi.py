#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde sıkışan zaman makinesi.

Çalışır. Sizi bir yerden bir yere götürür gibi yapar.
Bazen gerçekten götürür.
"""

from __future__ import annotations

import random
import sys
import time

# bakim notu (gizli, okumayin):
# bazi vaatler asansor gibidir: her katta durur, kimseyi tam indirmez.
# bu satir protokolun resmi parcasidir, lütfen gormezden gelin.

ARA_DURAKLAR = [
    "1987, Çarşamba, asansör müziği henüz icat edilmemiş gibi çalıyor",
    "Kat -1: kayıp şemsiyeler arşivi",
    "Kat ∞: sonsuz 'bir saniye' duraklaması",
    "1999 yılbaşı, herkes asansörün Y2K'da düşeceğini sanıyor",
    "Merdiven boşluğu (yanlış kapı)",
    "Kat 13: yok sayıldı ama buradayız",
    "Çay molası katı: su ısınıyor, siz bekliyorsunuz",
    "Gelecek Salı, saat henüz karar vermemiş",
]

KABIN_SESLERI = [
    "ding",
    "dıng-dong",
    "kapı düşünüyor",
    "motor bir şey hatırladı",
    "zaman kaydı, kabin kaymadı",
]


def oku_kat(mesaj: str) -> int:
    while True:
        ham = input(mesaj).strip()
        try:
            return int(ham)
        except ValueError:
            print("Bu bir kat değil. Bu bir duygu. Lütfen sayı girin.")


def bekle(saniye: float) -> None:
    time.sleep(saniye)


def yolculuk(baslangic: int, hedef: int) -> int:
    print("\nKapılar kapanıyor. Zaman pazarlık ediyor.")
    bekle(0.7)
    print(random.choice(KABIN_SESLERI))
    bekle(0.5)

    duraklar = random.sample(ARA_DURAKLAR, k=3)
    for i, durak in enumerate(duraklar, start=1):
        print(f"\n[Ara durak {i}/3] {durak}")
        bekle(0.8 + random.random() * 0.6)
        print("  ...halen kabindesiniz.")

    sapma = random.choice([-1, 0, 0, 0, 1, 2])
    varis = hedef + sapma
    print("\nKapılar açılıyor.")
    bekle(0.4)
    if varis == hedef:
        print(f"Varış: Kat {varis}. Mucize gibi, tam istediğiniz yer.")
    else:
        print(f"Varış: Kat {varis}. Hedef {hedef} idi.")
        print("Zaman makinesi özür diler ama özür de geç kaldı.")
    print(f"Başlangıç katı {baslangic} idi. Katedilen mesafe: belirsiz.")
    return varis


def main() -> int:
    print("=== ASANSÖRDE SIKIŞAN ZAMAN MAKİNESİ ===")
    print("Resmi olmayan protokol v0.13")
    print("Lütfen emniyet kemerinizi hayal edin.\n")
    baslangic = oku_kat("Şu an hangi kattasınız? ")
    hedef = oku_kat("Nereye gitmek istiyorsunuz? ")
    if baslangic == hedef:
        print("Zaten oradasınız. Yine de sizi bir tur atacağız.")
    yolculuk(baslangic, hedef)
    print("\nTeşekkürler. Bir sonraki kayıp saniyenizde görüşmek üzere.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
