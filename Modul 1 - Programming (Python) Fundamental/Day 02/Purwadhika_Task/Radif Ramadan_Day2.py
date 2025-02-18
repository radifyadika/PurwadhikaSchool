#LATIHAN 5

sisa_hari1 = 365-255
sisa_hari2 = 255 % 365
print(sisa_hari1, sisa_hari2)
# jumlah_hari = int(input("Masukkan jumlah hari: "))

# tahun = jumlah_hari // 365
# sisa_hari = jumlah_hari % 365
# bulan = sisa_hari // 30
# sisa_hari %= 30
# minggu = sisa_hari // 7
# hari = sisa_hari % 7

# print(f"{tahun} tahun {bulan} bulan {minggu} minggu {hari} hari")

#LATIHAN 6

# import math

# tinggi = float(input("Masukkan Tinggi Badan (dalam cm): "))
# berat = float(input("Masukkan Berat Badan (dalam Kg): "))

# if tinggi <= 0 or berat <= 0:
#     print("Tidak Menerima Nilai Negatif")
# elif tinggi >= 250 or berat >= 300:
#     print("Nilai yang Anda Masukkan Diluar Jangkauan")
# else:
#     bmi = berat / math.pow((tinggi/100), 2)

#     if bmi < 18.5:
#         kategori = "Berat Badan Kurang"
#     elif 18.5 <= bmi <= 24.9:
#         kategori = "Berat Badan Ideal"
#     elif 25 <= bmi <= 29.9:
#         kategori = "Berat Badan Berlebih"
#     elif 30 <= bmi <= 39.9:
#         kategori = "Berat Badan Sangat Berlebih"
#     else:
#         kategori = "Obesitas"

#     print(f'Tinggi {tinggi/100} meter, Berat {berat} Kg, BMI {bmi} dan anda termasuk {kategori} ') 

# #LATIHAN 7

# nilai = float(input("Masukkan Nilai: "))

# if nilai < 0:
#     print("Tidak menerima Nilai Negatif")
# elif nilai > 100:
#     print("Nilai yang Anda Masukkan Diluar Jangkauan")
# else:

#     if nilai >= 90:
#         grade = "Grade A"
#     elif nilai >= 85:
#         grade = "Grade A-"
#     elif nilai >= 80:
#         grade = "Grade B"
#     elif nilai >= 75:
#         grade = "Grade B-"
#     elif nilai >= 70:
#         grade = "Grade C"
#     elif nilai >= 65:
#         grade = "Grade D"
#     elif 40 < nilai < 65:
#         grade = "Perlu Remedial"
#     else:
#         grade = "Tidak Lulus"

#     print(f"Nilai Anda: {nilai} dan Anda {grade}")
