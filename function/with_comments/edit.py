# ====== FILE INI UNTUK FUNCTION EDIT MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action
import csv # mengambil package csv (comma separated values)

# membuat var fileData untuk menyimpan path file data mahasiswa csv
fileData = 'assets/data.csv'

# membuat function untuk mengedit data mahasiswa
def editMahasiswa():
    # action clear screen untuk membersihkan layar terminal
    action.clearScreen() 

    mahasiswa = [] # membuat var mahasiswa untuk menyimpan data mahasiswa dari file data.csv
    tbody = [] # membuat var tbody untuk menyimpan data mahasiswa yang akan ditampilkan di table
    dataFound = [] # membuat var dataFound untuk menyimpan data mahasiswa jika mahasiswa nya ada sesuai keyword pencarian(NIM)
     
    # "with open" untuk membuka file data.csv dan memberi alias file
    # mode 'r'(read) untuk membaca file data.csv
    with open(fileData, mode='r') as file:
        # csv dictreader untuk membaca file csv dengan key value
        csvReader = csv.DictReader(file)
        # looping, untuk membaca setiap baris data dan menampungnya ke var mahasiswa
        for row in csvReader:
            mahasiswa.append(row) 

    # jika data mahasiswanya ada.
    if len(mahasiswa) > 0:
        # cetak judul function
        print('---------------------------------------')
        print("Mengedit Data Mahasiswa")
        print('---------------------------------------')

        # looping data dari var mahasiswa yang sudah di isi data dari file data.csv
        for data in mahasiswa: 
            # membuat var column untuk menyimpan data mahasiswa yang akan ditampilkan di table
            column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
            # var column di tambahkan ke var tbody
            tbody.append(column) 

        # cetak table data mahasiswa
        print(
            tabulate( # function tabulate untuk membuat table
                tbody, # isi table
                headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], # header table
                tablefmt='grid', # gaya table
                showindex=range(1, len(mahasiswa) + 1)  # menampilkan index table dari 1 sampai jumlah data mahasiswa
            )
        )

        print('---------------------------------------')
        # mencari data mahasiswa berdasarkan NIM(key) untuk di edit data nya
        nim = input('NOTE: Ketik 0 untuk Keluar dari Form.\n\nPilih NIM Mahasiswa: ')
        print('---------------------------------------')

        # action clear screen untuk membersihkan layar terminal
        action.clearScreen() 

        # jika nim ditemukan 
        print('-- INFO -------------------------------')
        print(f'Kamu sedang mengedit Data dari NIM: {nim}')
        print('---------------------------------------')

        i = 0  # membuat var i untuk mencari index data mahasiswa
        for data in mahasiswa:  # looping data dari var mahasiswa
            if data['NIM'] == nim:  # jika nim mahasiswa sama dengan nim yang di input
                # var dataFound di isi data mahasiswa yang sama dengan nim yang di input
                dataFound = mahasiswa[i]
            i = i + 1  # var i di tambah 1 agar index nya bertambah sampait data mahasiswa ketemu yang sama dengan nim yang di input

        # validasi, jika nim inputan bukan angka.
        if not nim.isdigit():
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" +
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # balik lagi ke function editMahasiswa (diulang)
            editMahasiswa()
        
        # jika nim inputan 0, maka keluar dari form
        if nim == '0':
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan
            print('\n-- INFO -------------------------------')
            print("Kamu Telah Keluar Dari Form Edit!")
            print('---------------------------------------')

            # balik kemenu utama
            action.backToMenu()
        
        # validasi jika nim inputan tidak ada di data mahasiswa
        if not len(dataFound) > 0:
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"NIM Tidak ditemukan\n" +
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            editMahasiswa() # balik lagi ke function editMahasiswa (diulang)

        # form edit data mahasiswa
        print('-- FORM -------------------------------')
        print("NOTE: Abaikan.. jika salah satu data tidak mau diperbarui!\n")
        nama = input("Masukkan Nama baru Mahasiswa: ")
        jurusan = input("Masukkan Jurusan baru Mahasiswa: ")
        prodi = input("Masukkan Program Studi baru Mahasiswa: ")
        kelas = input("Masukkan Kelas baru Mahasiswa: ").upper()
        print('---------------------------------------')

        i = 0 # membuat var i untuk mencari index data mahasiswa
        for data in mahasiswa: # looping data dari var mahasiswa
            if data['NIM'] == nim: # jika nim mahasiswa sama dengan nim yang di input
                
                if len(nama) == 0: # jika input nama tidak di isi
                    mahasiswa[i]['Nama'] # maka nama tetap sama dengan nama sebelumnya
                else:  # jika nama di isi
                    mahasiswa[i]['Nama'] = nama # maka nama di ganti dengan nama yang baru di input
                
                if len(jurusan) == 0: # jika input jurusan tidak di isi
                    mahasiswa[i]['Jurusan'] # maka jurusan tetap sama dengan jurusan sebelumnya
                else: # jika jurusan di isi
                    mahasiswa[i]['Jurusan'] = jurusan # maka jurusan di ganti dengan jurusan yang baru di input
                
                if len(prodi) == 0:  # jika input prodi tidak di isi
                    mahasiswa[i]['Prodi'] # maka prodi tetap sama dengan prodi sebelumnya
                else: # jika prodi di isi
                    mahasiswa[i]['Prodi'] = prodi # maka prodi di ganti dengan prodi yang baru di input
                
                if len(kelas) == 0: # jika input kelas tidak di isi
                    mahasiswa[i]['Kelas'] # maka kelas tetap sama dengan kelas sebelumnya
                else: # jika kelas di isi
                    mahasiswa[i]['Kelas'] = kelas # maka kelas di ganti dengan kelas yang baru di input
                
            i = i + 1  # var i di tambah 1 agar index nya bertambah, sampai data mahasiswa ketemu yang sama dengan nim yang di input

        # with open untuk membuka file csv dengan mode write (w) lalu dimasukkan ke var csvFile
        # dan dikasih newline='' agar tidak ada baris kosong di file csv nya
        # ====== NOTE: ini seperti refresh file csv nya. ======== #
        with open(fileData, mode='w', newline='') as csvFile:
            # membuat var fieldnames untuk menampung nama field(key) atau header dari data mahasiswa
            fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'] 
            # membuat var writer untuk menulis data ke file csv
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            # menulis header ke file csv
            writer.writeheader()
            # looping data mahasiswa untuk menulis data baru ke file csv
            for newData in mahasiswa:
                # menulis data ke file csv
                writer.writerow({
                    'Nama': newData['Nama'],
                    'NIM': newData['NIM'],
                    'Jurusan': newData['Jurusan'],
                    'Prodi': newData['Prodi'],
                    'Kelas': newData['Kelas']
                })

        # action clear screen untuk membersihkan layar terminal
        action.clearScreen() 

        # cetak pesan berhasil
        print('-- INFO -------------------------------')
        print("Data baru dari NIM", nim, "Berhasil diperbarui!")
        print('---------------------------------------')

        # balik ke menu utama
        action.backToMenu() 
    else: # jika data mahasiswa belum ada

        # cetak pesan
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        # lempar ke data is empty untuk membuat data mahasiswa baru.
        action.dataIsEmpty() 