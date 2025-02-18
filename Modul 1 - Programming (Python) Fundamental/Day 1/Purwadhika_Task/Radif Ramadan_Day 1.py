#LATIHAN 1

#Persamaa linear dua variabel

# x + y = 13
# 2x + 4y = 32

# x = 13 - y
# 2 (13 - y) + 4y = 32
# y = (32 - (2 * 13)) / (4 - 2)

jumlah_peliharaan = 13
jumlah_kaki = 32

kaki_ayam = 2
kaki_kambing = 4

jumlah_kambing = (jumlah_kaki - (kaki_ayam * jumlah_peliharaan)) / (kaki_kambing - kaki_ayam)
jumlah_ayam = jumlah_peliharaan - jumlah_kambing

print(f"Andre memiliki ayam {jumlah_ayam} ekor dan kambing {jumlah_kambing} ekor, maka Andre memiliki hewan peliharaan sebanyak {jumlah_ayam + jumlah_kambing}")

#LATIHAN 2



# Persamaan dua variabel
# ayah -> x
# budi -> y

# 4 tahun yang lalu
## x - 4 = y - 4 
## x - 4 = (y -4) * 6
## x = (6 * y) - 24 + 4
## x = 6y - 20

JumlahAyahdanBudi = 50

# Sekarang
## x + y = 50
## y + (6y - 20) = 50
## 7y - 20 = 50
## 7y = 70
## y = 70 / 7
## y = 10 ---> Budi = 10

budi = 10
ayah = (6 * budi) - 20

budi = JumlahAyahdanBudi - ayah
ayah = JumlahAyahdanBudi - budi

print(f'Usia ayah saat ini adalah {ayah} tahun dan usia budi saat ini adalah {budi} tahun')

#LATIHAN 3

kalimat = input("Masukkan kalimat: ")
karakter = input("Masukkan karakter (Huruf atau angka): ")

jumlah_karakter = kalimat.count()

print(f"Jumlah karakter '{karakter}' di dalam kalimat '{kalimat}' adalah {jumlah_karakter}.")

#LATIHAN 4

kalimat = input("Masukkan Kalimat: ")
huruf_vokal = input("Masukkan huruf vokal: ")

vokal = 'aeiouAEIOU'
kalimat_berubah = ''

for huruf in kalimat:
    if huruf in vokal:
        if huruf:
            huruf = huruf_vokal
    kalimat_berubah += huruf
    
print("Kalimat dengan vokal yang telah diganti sesuai huruf vokal yang di input:")
print(kalimat_berubah)
