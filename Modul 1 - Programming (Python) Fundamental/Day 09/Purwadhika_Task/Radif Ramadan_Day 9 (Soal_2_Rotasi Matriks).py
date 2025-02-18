# LATIHAN DAY 9 (Matriks)

def putar_deret(angka, opsi):
    if opsi == 1:
        return [list(reversed(col)) for col in zip(*angka)]
    elif opsi == 2:
        return [list(reversed(row)) for row in reversed(angka)]
    elif opsi == 3:
        return [[angka[row][col] for row in range(len(angka))] for col in range(len(angka[0])-1, -1, -1)]

angka = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

opsi = int(input("Masukkan angka 1-3: "))

if opsi not in [1, 2, 3]:
    print("Opsi tidak valid.")
else:
    print('[')
    hasil = putar_deret(angka, opsi)
    for row in hasil:
        print(row)
    print(']')