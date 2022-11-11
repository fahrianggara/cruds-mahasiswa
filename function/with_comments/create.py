# ====== FILE INI UNTUK FUNCTION CREATE MAHASISWA ====== #

import csv # mengambil package csv (comma separated values)
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action

# membuat var fileData untuk menyimpan path file data mahasiswa csv
fileData = 'assets/data.csv'

# membuat function create mahasiswa untuk menambahkan data mahasiswa
def createMahasiswa():
    # action clear screen untuk membersihkan layar terminal
    action.clearScreen() 

    # var mahasiswa ini untuk menampung data yang TIDAK memakai key value
    mahasiswa = []
    # var data mahasiswa ini untuk menampung data yang memakai key value
    dataMahasiswa = []

    # mengambil data TIDAK memakai key-nya
    with open(fileData) as csvFile:
        # csv reader untuk membaca file csv dan dimasukkan ke variable csvReader
        csvReader = csv.reader(csvFile, delimiter=",")
        # loop untuk membaca setiap baris data dan dimasukkan ke variable row lalu di append ke variable mahasiswa
        for row in csvReader:
            mahasiswa.append(row)

    # mengambil data dengan memakai key-nya
    # with open untuk membuka file data.csv dan memberi alias csvFile dengan mode read(r)
    with open(fileData, mode='r') as csvFile:
        # csv dictreader untuk membaca file csv dengan key value dimasukkan ke variable csvReader
        csvReader = csv.DictReader(csvFile)
        # loop untuk membaca setiap baris data dan dimasukkan ke variable row lalu di append ke variable dataMahasiswa
        for row in csvReader:
            dataMahasiswa.append(row)

    """
    membuka file data.csv dan memberi alias csvFile dengan mode append(a)
    untuk menambahkan data dan tidak menimpa data yang sudah ada.
    newline='' untuk menghilangkan baris kosong di akhir file csv
    lalu dimasukkan ke variable csvFile
    """
    with open(fileData, mode='a', newline='') as csvFile:
        # fieldnames untuk menentukan key value dari data yang akan ditambahkan. Sebagai header
        fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas']
        # csv dictwriter untuk menulis data dengan key value(fieldnames) lalu dimasukkan ke variable csvWriter
        csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)

        # ========= SECTION INI UNTUK PENGECEKAN DAN VALIDASI INPUTAN NIM ========= #
        # cetak judul
        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')
        
        print('-- FORM -------------------------------')
        # input nim mahasiswa
        nim = input('NOTE: Ketik "0" untuk keluar dari form.\n\nMasukkan NIM Mahasiswa: ')
        
        # action clear screen untuk membersihkan layar terminal
        action.clearScreen() 

        # ========== SECTION INI UNTUK NIM YANG SUDAH DI CHECK DAN OK HASILNYA ========== #
        # cetak judul
        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')

        # form untuk input data mahasiswa
        print('-- FORM -------------------------------')
        # cetak nim yang sudah di check
        print("Masukkan NIM Mahasiswa:", nim)

        # looping ini untuk mengecek apakah nim yang diinput sudah ada atau belum
        for data in dataMahasiswa:
            if data['NIM'] == nim:
                # action clear screen untuk membersihkan layar terminal
                action.clearScreen() 

                # cetak pesan error
                print('-- WARNING ----------------------------')
                input(
                    f"NIM Mahasiswa tersebut sudah ada!\n" + 
                    "---------------------------------------\n" +
                    "\n>> Tekan ENTER untuk Mengulangi <<"
                )
                print('---------------------------------------')

                # ulang lagi
                createMahasiswa() 
        
        # jika nim bukan angka
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

            # ulang lagi
            createMahasiswa() 

        # jika inputan nim 0 maka keluar dari form pembuatan
        if nim == '0':
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan
            print('\n-- ALERT ------------------------------')
            print("Kamu Batal Mengisi Form!")
            print('---------------------------------------')


            # action untuk kembali ke menu utama
            action.backToMenu() 

        # validasi nim harus 8 digit, gaboleh lebih dan kurang
        if len(nim) > 8:
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen() 

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus 8 Digit!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # ulang lagi
            createMahasiswa() 

        elif len(nim) < 8:
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen() 

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus 8 Digit!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # ulang lagi
            createMahasiswa() 
        
        nama = input("Masukkan Nama Mahasiswa: ") # input nama mahasiswa
        jurusan = input("Masukkan Jurusan Mahasiswa: ") # input jurusan mahasiswa
        prodi = input("Masukkan Program Studi Mahasiswa: ") # input prodi mahasiswa
        kelas = input("Masukkan Kelas Mahasiswa: ").upper()  # input kelas mahasiswa dan di uppercase(untuk mengubah huruf kecil menjadi huruf besar)
        print('---------------------------------------')

        # validasi jika inputan salah satu form kosong
        if len(nama) == 0 and len(jurusan) == 0 and len(prodi) == 0 and len(kelas) == 0:
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen() 

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"Data tidak boleh ada yang kosong!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # ulang lagi
            createMahasiswa() 
        else: # jika semua form sudah terisi
            # Jika, datanya cuma header saja, maka buat datanya saja. headernya tidak usah.
            if len(mahasiswa) == 1:
                csvWriter.writerow({ 
                    'Nama': nama,
                    'NIM': nim,
                    'Jurusan': jurusan,
                    'Prodi': prodi,
                    'Kelas': kelas
                })
            else: # jika data full kosong semua(baru)
                if mahasiswa == []: # jika var mahasiswa koosong maka..
                    csvWriter.writeheader() # buat header

                # buat data
                csvWriter.writerow({ 
                    'Nama': nama,
                    'NIM': nim,
                    'Jurusan': jurusan,
                    'Prodi': prodi,
                    'Kelas': kelas
                })

        # action clear screen untuk membersihkan layar terminal
        action.clearScreen() 

        # cetak pesan berhasil
        print('-- INFO -------------------------------')
        print("Data Mahasiswa berhasil disimpan!")
        print('---------------------------------------')

    # lempar ke fungsi conf create again untuk konfirmasi apakah mau membuat lagi atau tidak
    action.confCreateAgain() 