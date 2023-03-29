from Luas.persegi import *
from Luas.persegi_panjang import *
from Luas.segitiga import *
from Luas.lingkaran import *
from Luas.trapesium import *
from Luas.jajar_genjang import *
from Volume.kubus import *
from Volume.balok import *
from Volume.tabung import *
from Volume.kerucut import *
from Volume.limas import *
from Volume.prisma import *

while True:
    print(" ")
    print("----- PROGRAM PERHITUNGAN LUAS DAN VOLUME -----")
    print(" ")
    print("Pilih Bangun Dibawah Ini : ")
    print("1. Menghitung Luas Bangun 2 Dimensi")
    print("2. Menghitung Volume Bangun 3 Dimensi")
    print("3. Exit")
    print(" ")
    pilih = input("Pilih (1, 2 Dan 3) : ")
    print(" ")

    if pilih == "1":
        print("----- Masukkan Bangun 2 Dimensi -----")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Jajar Genjang")
        print("6. Trapesium")
        print(" ")
        
        dua_dimensi = input("Pilih bangun datar yang akan dicari : ") #input opsi 2 dimensi
        
        if dua_dimensi == "1": #Menu Persegi
            sisi_persegi = float(input("Panjang Sisi : "))
            luas = (persegi(sisi_persegi)) #import rumus persegi dan hitung
            print('Luas Persegi = ', (luas)) #cetak hasil persegi
            
        elif dua_dimensi == "2": #Menu Persegi Panjang
            panjang_pp = float(input("Masukkan Panjang : "))
            lebar_pp = float(input("Masukkan Lebar : "))
            luas = (persegi_panjang(panjang_pp, lebar_pp)) #import rumus persegi panjang dan hitung
            print('Luas Persegi Panjang = ', (luas)) #cetak hasil persegi panjang
    
        elif dua_dimensi == "3": #Menu Segitiga
            alas_segitiga = float(input("Masukkan Alas : "))
            tinggi_segitiga = float(input("Masukkan Tinggi : "))
            luas = (segitiga(alas_segitiga, tinggi_segitiga)) #import rumus segitiga dan hitung
            print('Luas Segitiga = ', (luas)) #cetak hasil segitiga
            
        elif dua_dimensi == "4": #Menu Lingkaran
            jari_lingkaran = float(input("Masukkan Jari-jari : "))
            luas = (lingkaran(jari_lingkaran)) #import rumus lingkaran dan hitung
            print('Luas Lingkaran = ', (luas)) #cetak hasil lingkaran
            
        elif dua_dimensi == "5": #Menu Jajar Genjang
            alas_jajargenjang = float(input("Masukkan Alas : "))
            tinggi_jajargenjang = float(input("Masukkan Tinggi : "))
            luas = (jajar_genjang(alas_jajargenjang, tinggi_jajargenjang)) #import rumus jajar genjang dan hitung
            print('Luas Jajar Genjang = ', (luas)) #cetak hasil jajar genjang
            
        elif dua_dimensi == "6": #Menu Trapesium
            atas_trapesium = float(input("Masukkan Panjang Atas : "))
            bawah_trapesium = float(input("Masukkan Sisi Bawah : "))
            tinggi_trapesium = float(input("Masukkan Tinggi : "))
            luas = (trapesium(atas_trapesium, bawah_trapesium, tinggi_trapesium)) #import rumus trapesium dan hitung
            print('Luas Trapesium = ', (luas)) #cetak hasil trapesium
            


        else: print("=======Pilihan menu tidak tersedia=======")
        
    elif pilih == "2":
        print("----- Masukkan Bangun 3 Dimensi -----")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. Limas")
        print("6. Prisma")
        print(" ")

        tiga_dimensi=input("Pilih bangun ruang yang akan dicari : ") #input opsi 3 dimensi
        
        if tiga_dimensi == "1": #Menu Kubus
            sisi_kubus = float(input("Masukkan Panjang Sisi : "))
            volume = (kubus(sisi_kubus)) #import rumus kubus dan hitung
            print('Volume Kubus = ', (volume)) #cetak hasil kubus
            
        elif tiga_dimensi == "2": #Menu Balok
            panjang_balok = float(input("Masukkan Panjang : "))
            lebar_balok = float(input("Masukkan Lebar : "))
            tinggi_balok = float(input("Tinggi : "))
            volume = (balok(panjang_balok, lebar_balok, tinggi_balok)) #import rumus balok dan hitung
            print('Volume Balok = ', (volume)) #cetak hasil balok
            
        elif tiga_dimensi == "3": #Menu Tabung
            jari_tabung = float(input("Masukkan Jari-jari : "))
            tinggi_tabung = float(input("Masukkan Tinggi : "))
            volume = (tabung(jari_tabung, tinggi_tabung)) #import rumus tabung dan hitung
            print('Volume Tabung = ', (volume)) #cetak hasil tabung
            
        elif tiga_dimensi == "4": #Menu Kerucut
            jari_kerucut = float(input("Masukkan Jari-jari : "))
            tinggi_kerucut = float(input("Masukkan Tinggi : "))
            volume = (kerucut(jari_kerucut, tinggi_kerucut)) #import rumus kerucut dan hitung
            print('Volume Kerucut = ', (volume)) #cetak hasil kerucut
            
        elif tiga_dimensi == "5": #Menu limas
            lalas_limas = float(input("Masukkan Luas Alas : "))
            tinggi_limas = float(input("Masukkan Tinggi : "))
            volume = (limas(lalas_limas, tinggi_limas)) #import rumus limas dan hitung
            print('Volume Limas = ', (volume)) #cetak hasil limas
            
        elif tiga_dimensi == "6": #Menu Prisma
            lalas_prisma = float(input("Masukkan Luas Alas : "))
            tinggi_prisma = float(input("Masukkan Tinggi : "))
            volume = (prisma(lalas_prisma, tinggi_prisma)) #import rumus prisma dan hitung
            print('Volume Prisma = ', (volume)) #cetak hasil prisma
     
    elif pilih == "3":
        kembali = input("Apakah anda ingin melanjutkan? (Yes/No) ")
        if kembali == "No":
            break
        elif kembali == "Yes":
            continue       
        
        else: print("=======Pilihan menu tidak tersedia=======")
            
    else : print("=======Pilihan menu tidak tersedia=======")
       