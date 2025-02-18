# Latihan Day 6

def validasi_email(email):
    if '@' not in email or '.' not in email:
        return "Email Tidak Valid, Alasan: Format Email Salah"
    
    username, hosting = email.split('@')
    ekstensi = hosting.split('.')
    
    if len(ekstensi) < 2 or len(ekstensi[-2]) > 5:
        return "Email Tidak Valid, Alasan: Format Email Salah"
    
    for char in username:
        if not (char.isalnum() or char in ['_', '.']):
            return "Email Tidak Valid, Alasan: Format Nama Pengguna yang anda masukkan salah"
    
    for part in ekstensi[:-1]:
        if not part.isalnum():
            return "Email Tidak Valid, Alasan: Format Nama Hosting yang anda masukkan Salah"
    
    if len(ekstensi) == 3 and ekstensi[1] == "co" and ekstensi[2] in ["id", "my", "sg"]:
        return "Alamat Email yang anda Masukkan Valid"
    
    elif len(ekstensi[-1]) > 5 or ekstensi[1] == "":
        return "Email Tidak Valid, Alasan: Format Ekstensi yang anda masukkan Salah"
    
    else:
        return "Alamat Email yang anda Masukkan Valid"


email = input("Masukkan Email: ")
hasil = validasi_email(email)
print(hasil)


