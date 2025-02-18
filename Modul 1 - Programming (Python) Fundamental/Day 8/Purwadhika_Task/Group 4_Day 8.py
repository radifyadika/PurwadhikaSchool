# Kelompok 04 = ['Radif Ramadan','Aprian Handayani', 'Dzaki','Adikurnia']

# Account Register (Task Team Assignment 2_2)
database = {}

def main():
    while True:
        print("\n####### Selamat datang di XXYY Apps #######")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nPilih Menu: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                user_profile(user_id)
        elif choice == "3":
            print("░  Terima kasih telah menggunakan XXYY Apps  ░")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            
def register():
    print("----------- Register ------------")
    while True:
        #User Id
        while True:
            user_id = input("▣ UserId : ")
            if len(user_id) < 6 or len(user_id) > 20:
                print("Username minimal memiliki 6 karakter dan maksimal 20 karakter")
            if any(c in "/.,@#$%" for c in user_id):
                print("Username tidak boleh mengandung karakter spesial seperti '/.,@#$%'")
                continue

            valid = True
            for char in user_id:
                if not char.isalnum():
                    print("Username mengandung karakter tidak valid")
                    valid = False
                    break
            if not valid:
                continue

            Huruf = False
            Angka = False
            for char in user_id:
                if char.isalpha():
                    Huruf = True
                elif char.isdigit():
                    Angka = True

            if not Huruf or not Angka:
                print("Username harus kombinasi huruf dan angka")
                continue

            break
        
        # Password
        while True:
            password = input("▣ Password : ")
            if not any(c.isupper() for c in password) \
                or not any(c.islower() for c in password) \
                or not any(c.isdigit() for c in password) \
                or not any(c in "/.,@#$%" for c in password) \
                or len(password) < 8:
                print("!! Password harus kombinasi huruf kapital, huruf kecil, angka, dan karakter khusus (/.,@#$%) minimal 8 karakter !!\n")
                continue
            break
        
        # Email
        while True:
            email = input("▣ Email: ")

            if '@' not in email or '.' not in email:
                print("!! Email Tidak Valid, Alasan: Format Email Salah !!\n")
            else:
                username, hosting = email.split('@')
                ekstensi = hosting.split('.')
                
                if len(ekstensi) < 2 or len(ekstensi[-2]) > 5:
                    print("!! Email Tidak Valid, Alasan: Format Email Salah !!\n")
                else:
                    valid_username = all(char.isalnum() or char in ['_', '.'] for char in username)
                    if not valid_username:
                        print("!! Email Tidak Valid, Alasan: Format Nama Pengguna yang Anda masukkan salah !!\n")
                    else:
                        valid_hosting = all(part.isalnum() for part in ekstensi[:-1])
                        if not valid_hosting:
                            print("!! Email Tidak Valid, Alasan: Format Nama Hosting yang Anda masukkan Salah !!\n")
                        else:
                            if len(ekstensi) == 3 and ekstensi[1] == "co" and ekstensi[2] in ["id", "my", "sg"]:
                                break
                            elif len(ekstensi[-1]) > 5 or ekstensi[1] == "":
                                print("!! Email Tidak Valid, Alasan: Format Ekstensi yang Anda masukkan Salah !!\n")
                            break
        
        # Nama
        while True:
            nama = input("▣ Nama : ")
            if all(kata.isalpha() for kata in nama.split()):
                break
            else:
                print("!! Nama hanya boleh berisi alfabet !!\n")
        
        # Gender
        while True:
            gender = input("▣ Gender (Female/Male): ")
            if gender.lower() not in ["female", "male"]:
                print("!! Gender hanya bisa Female atau Male !!\n")
                continue
            break
        
        # Usia
        while True:
            usia = input("▣ Usia : ")
            if not usia.isdigit() or int(usia) < 17 or int(usia) > 80:
                print("!! Usia harus berupa angka, minimal 17 tahun, maksimal 80 tahun !!\n")
                continue
            break
        
        # Pekerjaan
        while True:
            pekerjaan = input("▣ Pekerjaan : ")
            if not pekerjaan.isalpha():
                print("!! Pekerjaan hanya boleh berisi alfabet !!\n")
                continue
            break
        
        # Hobi
        while True:
            hobi = input("▣ Hobi (pisahkan dengan koma jika lebih dari satu): ").split(",")
            hobi = [h.strip() for h in hobi if h.strip().isalpha()]
            if len(hobi) < 2:
                print("!! Minimal 2 hobi harus dimasukkan. Silakan coba lagi !!\n")
                continue
            break
        
        # Alamat
        while True:
            print("▣ Alamat: ")
            kota = input("\t▣ Nama Kota : ")
            if not kota.isalpha():
                print("    !! Nama Kota hanya boleh berisi alfabet!!\n")
                continue
            break
        while True:
            rt = input("\t▣ RT : ")
            if not rt.isdigit() :
                print("\t!! RT harus berupa angka integer !!\n")
                continue
            break
        while True:
            rw = input("\t▣ RW : ")
            if not rw.isdigit() :
                print("\t!! RW harus berupa angka integer !!\n")
                continue
            break
        while True:
            zip_code = input("\t▣ Zip Code : ")
            if not (len(zip_code) == 5 and zip_code.isdigit()):
                print("\t!! Zip Code harus 5 digit angka !!\n")
                continue
            break
        
        # latitude dan longitude
        while True:
            try:
                geo_lat = float(input("\t▣ Geo : \n\t\t▣ Latitude : "))
                geo_long = float(input("\t\t▣ Longitude : "))
                break  
            except ValueError:
                print("!! Latitude dan Longitude harus berisi Float !!\n")
                
        # Nomor HP
        while True:
            no_hp = input("▣ No Hp : ")
            if not (no_hp.isdigit() and len(no_hp) >= 11 and len(no_hp) <= 13):
                print("!! No Hp harus berupa angka, dan memiliki 11 - 13 karakter !!\n")
                continue
            break
        
        # SIMPAN
        simpan = input("▣ Simpan Data (Y/N): ").upper()
        if simpan == "Y":
            database[user_id] = {
                "password": password,
                "email": email,
                "nama": nama,
                "gender": gender,
                "usia": usia,
                "pekerjaan": pekerjaan,
                "hobi": hobi,
                "alamat": {
                    "kota": kota,
                    "rt": rt,
                    "rw": rw,
                    "zip_code": zip_code,
                    "geo": {
                        "lat": geo_lat,
                        "long": geo_long
                    }
                },
                "no_hp": no_hp
            }
            print("Data tersimpan")
        else:
            print("Data tidak tersimpan")
        main()
    
def login():
    print("----------- Login ------------")
    attempt = 0
    max_attempts = 5
    while attempt < max_attempts:
        user_id = input("Masukkan ID : ")
        password = input("Masukkan Password : ")

        if user_id in database:
            if database[user_id]["password"] == password:
                print("\nAnda Berhasil Login")
                return user_id
            else:
                print("!! Password Salah (ID sudah ada, tetapi password berbeda) !!")
        else:
            print("!! ID & Password Salah !!")

        attempt += 1
        if attempt == max_attempts:
            print("!! Anda telah gagal melakukan login sebanyak 5 kali. Silahkan coba lagi. !!")
            return None

def user_profile(user_id):
    user_data = database[user_id]
    print("||| Data Anda |||\n")
    print("▣ Nama:", user_data["nama"])
    print("▣ Email:", user_data["email"])
    print("▣ Gender:", user_data["gender"])
    print("▣ Usia:", user_data["usia"])
    print("▣ Pekerjaan:", user_data["pekerjaan"])
    print("▣ Hobi:", ", ".join(user_data["hobi"]))
    print("▣ Alamat:")
    print("  ▣ Nama Kota:", user_data["alamat"]["kota"])
    print("  ▣ RT:", user_data["alamat"]["rt"])
    print("  ▣ RW:", user_data["alamat"]["rw"])
    print("  ▣ Zip Code:", user_data["alamat"]["zip_code"])
    print("  ▣ Geo:\n   ▣ Latitude:", user_data["alamat"]["geo"]["lat"])
    print("   ▣ Longitude:", user_data["alamat"]["geo"]["long"])
    print("▣ No Hp:", user_data["no_hp"])

main()

