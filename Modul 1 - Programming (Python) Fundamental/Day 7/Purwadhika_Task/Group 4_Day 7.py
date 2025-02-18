# Kelompok = ['Radif Ramadan','Aprian Handayani', 'Dzaki','Adikurnia']


# Nomor 1
print('='*50, 'Soal 1','='*50)

def koversi_waktu(detik):
    try:
        detik = int(detik)
        if detik > 359999 or detik < 0:
            return "Invalid Input!"
    except:
        return "Invalid Input!"
    
    jam = detik // 3600
    menit = (detik % 3600) // 60
    detik = detik % 60
    konversi = f"{jam:02},{menit:02},{detik:02}"
    return konversi
    
while True:
    detik = input("Masukkan detik : ")
    hasil = koversi_waktu(detik)
   
    if hasil == "Invalid Input!":
        print("Invalid Input!")
    else:
        print("Konversi : ", hasil)
        break

# Nomor 2
# NPWP (Nomor Pokok Wajib Pajak) memiliki kode seri dengan 15 angka, yang menggunakan format sebagai 
# berikut: 99.999.999.9-999.999.

# 1. Dua digit pertama, (99).xxx.xxx.x-xxx.xxx menunjukkan Identitas Wajib Pajak, yaitu:
# 01 sampai 03 adalah Wajib Pajak Badan
# 04 dan 06 adalah Wajib Pajak Pengusaha
# 05 adalah Wajib Pajak Karyawan
# 07 sampai 09 adalah Wajib Pajak Orang Pribadi
# Enam digit berikutnya, xx.(999.999).x-xxx.xxx menunjukkan Nomor Registrasi / Urut yang diberikan 
# Kantor Pusat Direktorat Jenderal Pajak kepada Kantor Pelayanan Pajak (KPP).

# 2. Satu digit berikutnya, xx.xxx.xxx.(9)-xxx.xxx berfungsi sebagai Alat Pengaman untuk menghindari 
# terjadinya pemalsuan atau kesalahan pada NPWP.

# 3. Tiga digit berikutnya, xx.xx.xxx.x-(999).xxx adalah Kode KPP. Jika misalkan kodenya adalah 015, 
# berarti NPWP tersebut dikeluarkan di KPP berkode 015, yaitu KPP Pratama Jakarta Tebet.

# 4. Tiga digit terakhir, xx.xxx.xxx.x-xxx.(999) menunjukkan Status Wajib Pajak:
# 000 berarti berstatus Tunggal / Pusat (biasa disebut NPWP Pusat)
# 00x (001,002 dst) berarti Cabang, dimana angka akhir menunjukkan urutan cabang (cabang ke-1 
# maka 001; cabang ke-2 maka 002; dst.).

# Berdasarkan uraian di atas, buatlah sebuah program yg menerima inputan dari user dan memiliki sebuah 
# return function dengan 1 Argumen untuk melakukan verifikasi kode seri NPWP & menguraikan artinya. 
# Adapun eksekusi program tersebut beserta output yang diharapkan adalah sebagai berikut
print('='*50, 'Soal 2','='*50)

def verify_npwp(npwp):
    # Checking format NPWP
    if npwp[2] != '.' or npwp[6] != '.' or npwp[10] != '.' or npwp[12] != '-' or npwp[16] != '.':
        return "Kode seri NPWP tidak valid!\nKode seri NPWP ini tidak valid dikarenakan tidak mengikuti format baku: 99.999.999.9-999.999."
    
    # Checikng format NPWP lebih dari 15 angka
    if len(npwp) != 20:
        return "Kode seri NPWP tidak valid!\nKode seri NPWP ini tidak valid dikarenakan lebih dari 15 digit angka."
    
    # Checking hanya terdapat angka dan tanda titik pada NPWP
    if not npwp[:20].replace('.', '').replace('-', '').isdigit():
        return "Kode seri NPWP tidak valid!\nKode seri NPWP ini tidak valid dikarenakan terdapat karakter bukan angka di dalamnya."

    # checking identitas wajib pajak
    identitas = int(npwp[:2])
    if identitas not in range(1, 10):
        return "Kode seri NPWP tidak valid!\nKode seri NPWP ini tidak valid dikarenakan 2 digit pertama hanya bisa diisi 01 sampai 09."

    # Checking panjang NPWP
    if len(npwp) != 20:
        return "Kode seri NPWP tidak valid!\nKode seri NPWP ini tidak valid dikarenakan lebih dari 15 digit angka."

    nomor_registrasi = npwp[3:10]
    alat_pengaman = int(npwp[11])
    kode_kpp = int(npwp[13:16])
    status = npwp[17:]
    
    #Checking Identitas
    if identitas in [1, 2, 3]:
        jenis_wp = "Wajib Pajak Badan"
    elif identitas in [4, 6]:
        jenis_wp = "Wajib Pajak Pengusaha"
    elif identitas == 5:
        jenis_wp = "Wajib Pajak Karyawan"
    elif identitas in [7, 8, 9]:
        jenis_wp = "Wajib Pajak Orang Pribadi"

    #Checking Status Wajib Pajak
    if status == '000':
        status_wp = "Tunggal / Pusat (NPWP Pusat)"
    elif status.isdigit() and status.startswith('0'):
        cabang_ke = int(status[1:])
        status_wp = f"Cabang ke-{cabang_ke} (NPWP Cabang)"
    else:
        status_wp = "Status tidak diketahui"

    result = f"Kode seri NPWP valid!\nIdentitas Wajib Pajak: {identitas:02} {jenis_wp}\nNomor Registrasi: {nomor_registrasi}\nAlat Pengaman: {alat_pengaman}\nKode KPP: {kode_kpp:03}\nStatus Wajib Pajak: {status_wp}"
    return result

npwp_input = input("Masukkan NPWP : ")

print(verify_npwp(npwp_input))

# Nomor 3
print('='*50, 'Soal 3','='*50)


def urai(word):
    result = ''
    for i in range(len(word)):
        result += word[:i+1]
    return result

def rajut(word):
    n = 1
    original_word = ''
    while n * (n + 1) // 2 <= len(word):
        n += 1
    n -= 1
    for i in range(n):
        original_word = word[(len(word)-n):]
    return original_word

# Use the function
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

# Expected Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# Expected Output:
# Code
# Python
# Purwadhika