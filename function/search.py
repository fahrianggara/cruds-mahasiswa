# ====== FILE INI UNTUK FUNCTION SEARCH MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
import function.action as action # mengambil semua function dari file action.py di folder function dan kasih aliasn action
import csv # mengambil package csv (comma separated values)

# ini file data.csv
fileData = 'assets/data.csv'

# function untuk mencari data mahasiswa
def searchMahasiswa():
    # action untuk menampilkan membersihkan layar
    action.clearScreen() 

    # variable untuk menampung data mahasiswa
    mahasiswa = [] 

    # with open untuk membuka file data.csv dan memberi alias file
    with open(fileData, mode='r') as file:
        # csv dictreader untuk membaca file csv dengan key value
        fileReader = csv.DictReader(file)
        # loop untuk membaca setiap baris data
        for row in fileReader:
            # menambahkan data mahasiswa ke variable mahasiswa
            mahasiswa.append(row) 

    #  jika data mahasiswa tidak ada
    if len(mahasiswa) > 0:
        print('---------------------------------------')
        print("Mencari Data Mahasiswa")
        print('---------------------------------------')

        print('---------------------------------------')
        print('NOTE: Ketik 0 untuk keluar dari pencarian!\n')
        # input nim untuk menampung keyword pencarian
        nim = input("Cari mahasiswa berdasarkan NIM: ") 
        print('---------------------------------------')

        # data found untuk menampung data mahasiswa yang ditemukan
        dataFound = [] 

        # i untuk menampung index data mahasiswa
        i = 0 
        #  loop untuk membaca setiap data mahasiswa
        for data in mahasiswa:
            # jika nim yang dicari sama dengan nim mahasiswa
            if data['NIM'] == nim: 
                # menambahkan data mahasiswa index ke variable dataFound
                dataFound = mahasiswa[i] 
            # i bertambah 1 untuk index selanjutnya sampai data ditemukan dan loop berhenti
            i = i + 1 
        
        # jika nim bukan angka
        if not nim.isdigit(): 
            # action untuk menampilkan membersihkan layar
            action.clearScreen() 

            # action untuk menampilkan pesan error
            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # kembali ke function searchMahasiswa
            searchMahasiswa() 
        
        # jika nim 0 maka kembali ke menu utama
        if nim == '0':
            # action untuk menampilkan membersihkan layar
            action.clearScreen()

            # action untuk menampilkan pesan keluar
            print('\n-- ALERT ------------------------------')
            print("Kamu keluar dari pencarian!")
            print('---------------------------------------')

            # action untuk kembali menu utama
            action.backToMenu() 

        # jika data mahasiswa ditemukan
        if len(dataFound) > 0:
            # action untuk menampilkan membersihkan layar
            action.clearScreen() 

            # action untuk menampilkan data mahasiswa yang ditemukan
            print('-- INFO -------------------------------')
            print(f"Data Mahasiswa dengan NIM {nim} Ditemukan!")
            print('---------------------------------------')
            print(
                tabulate( # function tabulate untuk membuat table
                    [
                        ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], # header table(first row)
                        [   # data table
                            dataFound['Nama'],
                            dataFound['NIM'],
                            dataFound['Jurusan'],
                            dataFound['Prodi'],
                            dataFound['Kelas']
                        ]
                    ],
                    headers='firstrow', # menampilkan header di baris pertama
                    tablefmt='grid', # gaya table
                )
            )
        else: # jika data mahasiswa tidak ditemukan
            action.clearScreen() # action untuk menampilkan membersihkan layar

            # action untuk menampilkan pesan error jika data mahasiswa tidak ditemukan
            print('-- ALERT ------------------------------')
            input(
                f"Data yang kamu cari tidak ditemukan!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # kembali ke function searchMahasiswa dan mencari data mahasiswa lagi sampai ditemukan
            searchMahasiswa()

        # action untuk kembali ke menu utama
        action.backToMenu() 

    # jika data mahasiswa tidak ada
    else: 
        # kasih pesan error jika data mahasiswa tidak ada
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        # lempar ke function dataIsEmpty untuk menambahkan data mahasiswa
        action.dataIsEmpty() 