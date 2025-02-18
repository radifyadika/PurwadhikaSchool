# RADIF RAMADAN
# LATIHAN NOMOR 1 (Kalkulator)

def kalkulator(angka1, angka2, operator):
    try:
        if '.' in angka1 or '.' in angka2:
            angka1 = float(angka1)
            angka2 = float(angka2)
        else:
            angka1 = int(angka1)
            angka2 = int(angka2)
    except:
        return "Error: Input harus berupa angka (integer atau float)."

    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '/':
        try:
            hasil = angka1 / angka2
        except:
            return "Error: Tidak dapat membagi dengan nol."
    else:
        return "Error: Operator tidak valid. Gunakan +, -, * atau /."

    return f"Hasil dari {angka1} {operator} {angka2} = {hasil}"

angka1 = input("Masukkan Angka 1: ")
angka2 = input("Masukkan Angka 2: ")
operator = input("Masukkan Operator (+, -, *, /): ")

hasil = kalkulator(angka1, angka2, operator)
print(hasil)

# LATIHAN NOMOR 2 (Sandi Morse)
# Dictionary untuk inisiasi kode Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

reverse_morse_dict = {v: k for k, v in morse_dict.items()}

def encode_to_morse(text):
    return ' / '.join(morse_dict.get(char.upper(), '') for char in text)

def decode_from_morse(morse_code):
    words = morse_code.split(' / ')
    return ''.join(reverse_morse_dict.get(word, '') for word in words)

def auto_decoder_encoder(inputan):
    if all(char in '.- /' for char in inputan):
        # Input adalah kode Morse
        decoded_message = decode_from_morse(inputan)
        return f"Kode Morse yg anda masukkan ({inputan}) jika diubah menjadi kata-kata Menjadi ({decoded_message})"
    elif inputan.isalnum() or ' ' in inputan:
        encoded_message = encode_to_morse(inputan)
        return f"Kata yg anda masukkan adalah ({inputan}) Jika diubah menjadi Kode Morse Menjadi ({encoded_message})"
    else:
        return "Hanya menerima Alfabet, Angka dan Spasi (Untuk kalimat)"
    
inputan = input("Masukkan Inputan (Morse atau Kata): ")
hasil = auto_decoder_encoder(inputan)
print(hasil)

