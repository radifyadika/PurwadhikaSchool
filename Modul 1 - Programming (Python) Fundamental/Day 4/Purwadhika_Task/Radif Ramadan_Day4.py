
# LATIHAN NOMOR 1

try:
    angka = int(input("Masukkan Angka: "))
    if angka <= 0:
        print("Angka harus di atas 0")
    else:
        factorial = 1
        i = 1
        while i <= angka:
            factorial *= i
            i += 1
        print("Nilai Faktorial dari", angka, "adalah", factorial)
except:
    print("Input tidak bisa menerima string")
    
# LATIHAN NOMOR 2

try:
    angka = input("Masukkan Angka: ")
    # Inisialisasi variabel untuk jumlah total
    total = 0

    for digit in angka:
        total += int(digit)

    print("Total angka dari inputan:", total)
except:
    print('Nilai yang anda masukan tidak sesuai')

# LATIHAN NOMOR 3

# Inisialisasi variabel untuk jumlah total
total = 0

for angka in range(1, 101):
    if angka % 3 == 0 and angka % 5 == 0:
        total += angka

print("Total semua angka antara 1 dan 100 yang habis dibagi 3 dan 5 adalah:", total)

#LATIHAN NOMOR 4

range_awal = int(input("Masukkan Range awal: "))
range_akhir = int(input("Masukkan Range akhir: "))

# Inisialisasi variabel untuk jumlah angka genap dan ganjil
jumlah_genap = 0
jumlah_ganjil = 0

for angka in range(range_awal, range_akhir):
    if angka % 2 == 0:
        jumlah_genap += angka
    else:
        jumlah_ganjil += angka

print("Jumlah Angka genap dari", range_awal, "hingga", range_akhir, "adalah", jumlah_genap, "dan jumlah nilai ganjil adalah", jumlah_ganjil)
