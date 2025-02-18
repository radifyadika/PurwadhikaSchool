# Kelompok 04 = ['Radif Ramadan','Aprian Handayani', 'Dzaki','Adikurnia']
# Capstone x MySQL (Task Team Assignment 3)
import mysql.connector

data_stok = {}
database = {}

nama_kolom = ["ID", "Nama Produk", "Kategori", "Unit", "Harga Satuan"]

db =  mysql.connector.connect(
    host = 'localhost', username = 'kelompok4', password = 'kelompok4',
    database = 'warehouse'
)

cursor = db.cursor()


# FITUR FITUR YANG TERSEDIA

def register():
    print('═'*50)
    print("---------- 🧑🏻‍💻 Register 🧑🏻‍💻 ----------\n")
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
        hobi = ', '.join(hobi)
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
            for user_id, user_data in database.items():
                sql_user = """
                    INSERT INTO users (
                        userID, Password, Email, Nama, Gender, Usia, Pekerjaan, Hobi, Kota, RT, RW, Zipcode, Latitude, Longitude, Nomor_Hp
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                user_values = (
                    user_id, user_data["password"], user_data["email"], user_data["nama"], user_data["gender"],
                    user_data["usia"], user_data["pekerjaan"], user_data["hobi"], user_data["alamat"]["kota"],
                    user_data["alamat"]["rt"], user_data["alamat"]["rw"], user_data["alamat"]["zip_code"],
                    user_data["alamat"]["geo"]["lat"], user_data["alamat"]["geo"]["long"], user_data["no_hp"]
                )
                cursor.execute(sql_user, user_values)
            db.commit()
            print("Data tersimpan Di Database")
        else:
            print("Data tidak tersimpan")
        main()
    
def login():
    print('═'*50)
    print("---------- 🔐 Login 🔐 ----------\n")
    attempt = 0
    max_attempts = 5
    cursor.execute("""SELECT userid, password FROM users""")
    login_user = cursor.fetchall()
    while attempt < max_attempts:
        user_id = input("Masukkan ID : ")
        password = input("Masukkan Password : ")
        for user in login_user:
            if user[0] == user_id:
                if user[1] == password:
                    print("\nAnda Berhasil Login")
                    menu_utama()
                else:
                    print("!! Password Salah (ID sudah ada, tetapi password berbeda) !!")
        else:
            print("!! ID & Password Salah !!")

        attempt += 1
        if attempt == max_attempts:
            print("!! Anda telah gagal melakukan login sebanyak 5 kali. Silahkan coba lagi. !!")
            return None

def main():
    while True:
        print("════════════════════════════════════════════\n📱 SELAMAT DI APLIKASI WAREHOUSE BY JCDSOL 📱\n════════════════════════════════════════════ ")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("\nPilih Menu: ")

        if choice == "2":
            register()
        elif choice == "1":
            login()
        elif choice == "3":
            print("░  Terima kasih telah menggunakan Warehouse by JCDSOL Apps  ░")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
           
def menu_utama():
    menu = input('''
═════════════════════════════════════════\n👋 SELAMAT DATANG DI JCDSOL ELECSTORAGE 👋\n═════════════════════════════════════════ 
    1. Report Stock Gudang 
    2. Tambah Stock Baru ke Gudang
    3. Update Stock Gudang
    4. Delete Stock Gudang
    5. Exit Program
\nMasukkan Menu yang Anda Inginkan (1-5) : ''')

    if menu == '1':
        print("══"*50)
        menu_report()
    elif menu == '2':
        print("══"*50)
        menu_create()
    elif menu == '3':
        print("══"*50)
        menu_update()    
    elif menu == '4':
        print("══"*50)
        menu_delete()
    elif menu == '5':
        print("😊 😊 😊 Terimakasih Telah Berkunjung 😊 😊 😊")
        exit() 
    else:
        menu_utama()
        
def menu_report():
    print('''
---------- 📄 📄 📄 Menu Report Stock Gudang 📄 📄 📄 ----------

    Pilihan Menu Report Stock Gudang:
    1. Tampilkan Data Stock Gudang
    2. Tampilkan Data Stock Spesifik (Kategori)
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Tampilan Stok Yang Ingin Dipilih (1-3) : ")

    if user_input == '1':
        print("══"*50)
        tampilan_data()
        yes_no(menu_report,menu_utama)
    elif user_input == '2':
        print("══"*50)
        def report_sub2():
            kategori_yang_dicari = input("\n▣ Masukkan kategori produk yang ingin ditampilkan: ").title()
            cursor.execute("SELECT * FROM stock WHERE Kategori = %s", (kategori_yang_dicari.lower(),))
            result = cursor.fetchall()
            if result:
                cursor.execute("SELECT * FROM stock WHERE Kategori = %s", (kategori_yang_dicari.lower(),))
                data_stok = cursor.fetchall()
                print("\n▓▓▓ Laporan Stok JCDSOL Elecstorage ▓▓▓\n")
                print(f"{nama_kolom[0]: <10}|{nama_kolom[1]: <35}|{nama_kolom[2]: <15}|{nama_kolom[3]: <5}|{nama_kolom[4]: <20}")
                print("══════════+═══════════════════════════════════+═══════════════+═════+════════════")
                for row in data_stok:
                    kode_produk, nama_produk, kategori, unit, harga_satuan = row
                    harga_satuan_formatted = f"Rp {harga_satuan:,.0f}"
                    print(f"{kode_produk: <10}|{nama_produk: <35}|{kategori: <15}|{str(unit): <5}|{harga_satuan_formatted: <20}")
            else:
                print(f"Kategori '{kategori_yang_dicari}' tidak ditemukan dalam Data Stock Gudang.")
        report_sub2()
        yes_no(menu_report,menu_utama)
    elif user_input == '3':
        menu_utama()
    else:
        menu_report() 

def menu_create():
    def menu_create_sub1():
        print("\n«------ Silahkan Input Stock Baru ke Gudang ------»")
        while True:
            nama_produk = input("▣ Masukkan nama produk: ").title()
            if any(detail['Nama Produk'].lower() == nama_produk.lower() for detail in data_stok.values()):
                print("Nama produk sudah ada dalam data. Silakan masukkan nama produk yang berbeda.")
            else:
                break
        kategori = input("▣ Masukkan kategori: ").title()
        while True:
            unit = (input("▣ Masukkan Jumlah Unit: "))
            if not unit.isdigit():
                print("\n⚠ Warning Error: Masukkan Nilai Berupa Angka!!!")
                continue
            harga_satuan = (input("▣ Masukkan Harga Satuan: "))
            if not harga_satuan.isdigit():
                print("\n⚠ Warning Error: Masukkan Nilai Berupa Angka!!!")
                continue
            break
        # Generate Kode Produk baru Jika Produk baru
        prefix = kategori[:3].upper()
        nomor = 1
        for kode in data_stok.keys():
            if kode.startswith(prefix):
                nomor += 1
        kode_produk = f"{prefix}-{str(nomor).zfill(3)}"
        
        def tambah_data():
            data_stok[kode_produk] = {
                "Nama Produk": nama_produk,
                "Kategori": kategori,
                "Unit": unit,
                "Harga Satuan": harga_satuan
            }
        yes_no(tambah_data, menu_create)
        print(f"Produk berhasil ditambahkan dengan Kode Produk: {kode_produk}")
        for kode_produk, data in data_stok.items():
            sql_user = """
                INSERT INTO stock (
                    ID, Nama_Produk, Kategori, Unit, Harga_Satuan
                ) VALUES (%s, %s, %s, %s, %s)
            """
            user_values = (
                kode_produk, data["Nama Produk"], data["Kategori"], data["Unit"], data["Harga Satuan"]
            )
            cursor.execute(sql_user, user_values)
        db.commit()
    print("══"*50)
    print('''
---------- ✏️ ✏️ ✏️  Menu Tambah Stock Baru ke Gudang ✏️ ✏️ ✏️ ----------

    Pilihan Menu Tambah Stock Baru ke Gudang:
    1. Menambah Stock Baru ke Gudang
    2. Menampilkan Semua Data pada Gudang
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Pilih Perintah yang Anda Inginkan (1-3) : ")

    if user_input == '1':
        print("══"*50)
        menu_create_sub1()
        yes_no(menu_create,menu_utama)
    elif user_input == '2':
        print("══"*50)
        tampilan_data()
        yes_no(menu_create,menu_utama)
    elif user_input == '3':
        print("══"*50)
        menu_utama()
    else:
        menu_create()
    
def menu_update():
    def update_sub1():
        while True:
            tampilan_data()
            item_updatestok = input("\n▣ Masukkan Nama Produk yang Ingin Anda update: ").title()
            cursor.execute("SELECT id FROM stock WHERE LOWER(Nama_Produk) = %s", (item_updatestok.lower(),))
            result = cursor.fetchone()
            if result:
                item_update_key = result[0]
            else:
                print("Nama Produk tidak ditemukan.")
                break
            
            if item_update_key:
                while True:
                    print("══"*50)
                    jenis_update = int(input(f'''\n---------- Update Field (Kolom) Data Stok "{item_updatestok}"  ----------\n
        1. Nama Barang 
        2. Kategori 
        3. Unit 
        4. Harga Satuan 
        5. Kembali ke Menu Update
                                                
    Field yang ingin Anda Update (1-5): '''))
                    
                    if jenis_update == 1:
                        item_baru = input("\n▣ Masukkan Nama Produk Baru: ").title()
                        cursor.execute("SELECT COUNT(*) FROM stock WHERE LOWER(Nama_Produk) = %s", (item_baru.lower(),))
                        result = cursor.fetchone()
                        if result[0] > 0:
                            print("Nama Produk Sudah Ada, Masukkan Nama Baru")
                            yes_no(update_sub1, menu_utama)
                        else:
                            def update_nama():
                                cursor.execute("UPDATE stock SET Nama_Produk = %s WHERE id = %s", (item_baru, item_update_key))
                                db.commit()
                                tampilan_data()
                                print("\nNama Produk Berhasil Diupdate.")
                            yes_no(update_nama, update_sub1)

                    elif jenis_update == 2:
                        kategori_baru = input("\n▣ Masukkan Detail Kategori Baru: ").title()
                        def update_kategori():
                            cursor.execute("UPDATE stock SET Kategori = %s WHERE id = %s", (kategori_baru, item_update_key))
                            db.commit()
                            tampilan_data()
                            print("\nKategori Berhasil Diupdate.")
                        yes_no(update_kategori, update_sub1)
                        break
                            
                    elif jenis_update == 3:
                        unit_baru = int(input("\n▣ Masukkan Jumlah Stok Baru: "))
                        def update_unit():
                            cursor.execute("UPDATE stock SET Unit = %s WHERE id = %s", (unit_baru, item_update_key))
                            db.commit()
                            tampilan_data()
                            print("\nJumlah Stok Berhasil Diupdate.")
                        yes_no(update_unit, update_sub1)
                        break

                    elif jenis_update == 4:
                        harga_baru = int(input("\n▣ Masukkan Harga Satuan Produk Baru: "))
                        def update_harga():
                            cursor.execute("UPDATE stock SET Harga_Satuan = %s WHERE id = %s", (harga_baru, item_update_key))
                            db.commit()
                            tampilan_data()
                            print("\nHarga Satuan Produk Berhasil Diupdate.")
                        yes_no(update_harga, update_sub1)
                        break
                    elif jenis_update == 5:
                        menu_update()
                    else:
                        menu_update()
            break           
        print("══"*50)
        yes_no(menu_update, menu_utama)
    print("══"*50)
    print('''
---------- ⚙️⚙️⚙️   Menu Update Stock dari Gudang ⚙️⚙️⚙️ ----------

    Pilihan Menu Update Stock dari Gudang:
    1. Update Stock dari Gudang
    2. Menampilkan Semua Data pada Gudang
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Pilih Perintah yang Anda Inginkan (1-3) : ")

    if user_input == '1':
        print("══"*50)
        update_sub1()
        yes_no(menu_update,menu_utama)
    elif user_input == '2':
        print("══"*50)
        tampilan_data()
        yes_no(menu_update,menu_utama)
    elif user_input == '3':
        print("══"*50)
        menu_utama()
    else:
        menu_update()
    
def menu_delete():
    def menu_delete_sub1():
        print("══"*50)
        print('''\n---------- Hapus Data Stock dari Gudang ----------\n
        1. Hapus Data Stock di Gudang (Per Baris)
        2. Hapus Data sesuai Filtering Anda (Kategori)
        3. Hapus Semua Data di Gudang
        4. Kembali ke Menu Delete
        ''')
        user_input_delete = int(input('Delete yang Ingin Dipilih (1-4): '))    
        if user_input_delete == 1:
            tampilan_data()
            item_deletestok = input("Masukkan nama item yang mau dihapus: ").title()
            
            # Mencari Kode Produk berdasarkan Nama Produk
            cursor.execute("SELECT id FROM stock WHERE LOWER(Nama_Produk) = %s", (item_deletestok.lower(),))
            result = cursor.fetchone()
            if result:
                item_delete_key = result[0]
                def hapus_produk():
                    cursor.execute("DELETE FROM stock WHERE id = %s", (item_delete_key,))
                    db.commit()
                    tampilan_data()
                    print("Produk berhasil dihapus.")
                yes_no(hapus_produk, menu_delete)
            else:
                menu_delete_sub1()  
                
        if user_input_delete == 2:
            tampilan_data()
            kategori_hapus = input("▣ Masukkan kategori yang mau dihapus: ").title()

            def hapus():
                cursor.execute("DELETE FROM stock WHERE LOWER(Kategori) = %s", (kategori_hapus.lower(),))
                db.commit()
                tampilan_data()
                print(f"Semua produk dengan kategori '{kategori_hapus}' berhasil dihapus.")
                yes_no(menu_delete, menu_utama)
                        
            yes_no(hapus, menu_delete)
            
        if user_input_delete == 3:
            def hapus():
                cursor.execute("DELETE FROM stock")
                db.commit()
                tampilan_data()
                print("Semua produk di gudang berhasil dihapus.")
                yes_no(menu_delete, menu_utama)

            yes_no(hapus, menu_delete)
        
        if user_input_delete == 4:
            menu_delete()
        else:
            menu_delete_sub1()
    print("══"*50)
    print('''
---------- 🗑️ 🗑️ 🗑️  Menu Delete Stock Gudang 🗑️ 🗑️ 🗑️ ----------

    Pilihan Menu Delete Stock Gudang:
    1. Hapus Data Stock di Gudang
    2. Menampilkan Semua Data pada Gudang
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Tampilan Stok Yang Ingin Dipilih (1-3) : ")

    if user_input == '1':
        print("══"*50)
        menu_delete_sub1()
        yes_no(menu_delete,menu_utama)
    elif user_input == '2':
        print("══"*50)
        tampilan_data()
        yes_no(menu_delete,menu_utama)
    elif user_input == '3':
        print("══"*50)
        menu_utama()
    else:
        menu_delete()
                
# Function Pendukung Untuk (menampilkan data) dan (Yes or No Question)    
    
def tampilan_data():
    cursor.execute("SELECT ID, nama_produk, kategori, unit, harga_satuan FROM stock")
    data_stok = cursor.fetchall()
    print("\n▓▓▓ Laporan Stok JCDSOL Elecstorage ▓▓▓\n")
    print(f"{nama_kolom[0]: <10}|{nama_kolom[1]: <35}|{nama_kolom[2]: <15}|{nama_kolom[3]: <5}|{nama_kolom[4]: <20}")
    print("══════════+═══════════════════════════════════+═══════════════+═════+════════════")
    for row in data_stok:
        kode_produk, nama_produk, kategori, unit, harga_satuan = row
        harga_satuan_formatted = f"Rp {harga_satuan:,.0f}"
        print(f"{kode_produk: <10}|{nama_produk: <35}|{kategori: <15}|{str(unit): <5}|{harga_satuan_formatted: <20}")
    if len(data_stok) == 0:
        print("\t\tTidak ada Record yang tersedia.") 
    
def yes_no(yes, no):
    yes_no_input = input("\nApakah anda ingin melanjutkan (Y/N)? ").lower()
    if yes_no_input == 'y':
        yes()
    elif yes_no_input == 'n':
        no()
    else:
        print("\nINFO!! : Input yang anda masukkan salah")
        yes_no(yes, no)

   
main()

