# LATIHAN NOMOR 1

hari = {
    "senin": "monday",
    "selasa": "tuesday",
    "rabu": "wednesday",
    "kamis": "thursday",
    "jumat": "friday",
    "sabtu": "saturday",
    "minggu": "sunday"
}

nama_hari = input("Masukkan nama Hari: ").lower()

if nama_hari in hari:
    print(f"{nama_hari.capitalize()} - in English is - {hari[nama_hari].capitalize()}")

elif nama_hari in hari.values():
    # Mencari nama hari dalam bahasa Indonesia berdasarkan nama hari dalam bahasa Inggris
    for key, value in hari.items():
        if value == nama_hari:
            hari_indo = key
            break
    print(f"{nama_hari.capitalize()} - in Bahasa is - {hari_indo.capitalize()}")

else:
    print("Nama hari tidak valid.")


# LATIHAN NOMOR 2

hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]


hari_ini= input("Masukkan nama hari: ").lower()
jumlah_hari = int(input("Masukkan jumlah hari: "))


indeks_hari = hari.index(hari_ini)

indeks_hari_selanjutnya = (indeks_hari + jumlah_hari) % 7

print(f"Hari ini hari {hari_ini.capitalize()}, {jumlah_hari} hari lagi adalah hari {hari[indeks_hari_selanjutnya].capitalize()}")

# LATIHAN NOMOR 3

# Input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ").lower()

kata = kalimat.split()

kata_terbalik = []

for huruf in kata:
    kata_terbalik.append(huruf[::-1])

kalimat_terbalik = ' '.join(kata_terbalik)

print(kalimat_terbalik.capitalize())

# LATIHAN NOMOR 4

print("Masukan list dengan koma!!")
list_awal = input("Masukkan list: ").split(',')


list_unik = []

for elemen in list_awal:
    if elemen not in list_unik:
        list_unik.append(elemen)


print("List dengan elemen unik tanpa duplikat:", list_unik)

# LATIHAN NOMOR 5

lirik_lagu = input("Masukkan lirik lagu: ")

kata = lirik_lagu.lower().split()

frekuensi_kata = {}
for kata in kata:
    if kata in frekuensi_kata:
        frekuensi_kata[kata] += 1
    else:
        frekuensi_kata[kata] = 1

print("Output:")
for kata, frekuensi in frekuensi_kata.items():
    print(f"{kata.capitalize()} : {frekuensi}")

# LATIHAN NOMOR 6

kata1 = input("Masukkan kata 1: ").replace(" ", "").lower()
kata2 = input("Masukkan kata 2: ").replace(" ", "").lower()

list1 = list(kata1)
list2 = list(kata2)

list1.sort()
list2.sort()

if list1 == list2:
    print(f"{kata1} merupakan anagram dari {kata2}")
else:
    print(f"{kata1} bukan anagram dari {kata2}")


