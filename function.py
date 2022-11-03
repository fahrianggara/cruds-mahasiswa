# ====== FILE INI UNTUK MEMBUAT FUNCTION ====== #

from tabulate import tabulate
import csv 
import os 

fileData = 'data.csv'
namaProjek = "CRUDS Mahasiswa"

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def backToMenu():
    input("\nSilahkan Tekan ENTER untuk kembali ke Menu")
    main() 


def confCreateAgain():
    print('-- ALERT ------------------------------')
    pilihan = input("Apakah kamu mau tambah data lagi? [Y/T]: ").upper()
    print('---------------------------------------')

    if pilihan == 'Y': 
        createMahasiswa()
    elif pilihan == 'T': 
        clearScreen() 
        
        print('---------------------------------------')
        print(">> OK, Kamu batal membuat data lagi! <<")
        print('---------------------------------------')

        backToMenu() 
    else: 
        clearScreen() 
        
        print('-- ALERT ------------------------------')
        print(">> Silahkan pilih Tidak [T] atau Ya [Y] <<")
        print('---------------------------------------')

        confCreateAgain() 


def exitMenu():
    print('-- ALERT ------------------------------')
    pilihan = input("Apakah kamu yakin akan keluar dari menu? [Y/T]: ").upper()
    print('---------------------------------------')

    if pilihan == 'Y': 
        clearScreen() 

        exit( 
            '---------------------------------------\n' +
            '>> Kamu telah keluar dari Menu! <<\n' +
            '---------------------------------------'
        )
    elif pilihan == 'T': 
        clearScreen() 

        print('---------------------------------------')
        print(">> Kamu batal Keluar dari Menu! <<")
        print('---------------------------------------')

        backToMenu() 
    else: 
        clearScreen() 
        
        print('-- ALERT ------------------------------')
        print(">> Silahkan pilih Tidak [T] atau Ya [Y] <<")
        print('---------------------------------------')

        exitMenu()


def dataIsEmpty():
    
    pilihan = input("\nDuuh.. Data mahasiswanya masih kosong nih.. Kamu mau buat? [Y/T]: ").upper()

    if pilihan == 'Y': 
        createMahasiswa()
    elif pilihan == 'T': 
        clearScreen() 
        
        print('---------------------------------------')
        print(">> OK, Kamu batal membuat data baru! <<")
        print('---------------------------------------')

        backToMenu()
    else: 
        clearScreen() 
        
        print('-- ALERT ------------------------------')
        print(">> Silahkan pilih Tidak [T] atau Ya [Y] <<")
        print('---------------------------------------')

        dataIsEmpty()


def main():
    clearScreen() 

    print('---------------------------------------')
    print(f"List Menu | {namaProjek}")
    print('---------------------------------------')

    print(
        tabulate( 
            [
                ["Kode", "Nama Menu"], 
                ["0", "Keluar dari Menu"], 
                ["1", "Menampilkan data Mahasiswa"], 
                ["2", "Mencari data Mahasiswa"], 
                ["3", "Membuat data Mahasiswa"], 
                ["4", "Memperbarui data Mahasiswa"], 
                ["5", "Menghapus data Mahasiswa"], 
            ],
            headers='firstrow', 
            tablefmt='grid' 
        )
    )

    print('---------------------------------------')
    menu = int(input("Pilih Kode Menunya: ")) 
    print('---------------------------------------')

    if menu == 0: 
        clearScreen() 
        exitMenu() 
    elif menu == 1: 
        showMahasiswa()
    elif menu == 2: 
        searchMahasiswa()
    elif menu == 3: 
        createMahasiswa()
    elif menu == 4: 
        editMahasiswa()
    elif menu == 5: 
        deleteMahasiswa()
    else: 
        clearScreen()

        print('-- ALERT ------------------------------')
        print("Oops.. Menu Tersebut Tidak Ada!")
        print('---------------------------------------')

        backToMenu() 


def showMahasiswa():
    clearScreen() 

    mahasiswa = [] 
    tbody = [] 

    with open(fileData) as file:
        fileReader = csv.reader(file, delimiter=",")
        
        for row in fileReader:
            mahasiswa.append(row) 

        if len(mahasiswa) > 0: 
            
            print('---------------------------------------')
            print("Data Mahasiswa")
            print('---------------------------------------')

            thead = mahasiswa.pop(0)

            for data in mahasiswa: 
                tbody.append(data) 

            print(
                tabulate(
                    tbody, 
                    headers=thead, 
                    tablefmt='grid', 
                    showindex=range(1, len(tbody) + 1) 
                )
            )
        else: 
            print('---------------------------------------')
            print(">> Data mahasiswa belum ada! <<")
            print('---------------------------------------')
            
            dataIsEmpty() 

    backToMenu() 


def searchMahasiswa():
    clearScreen() 

    mahasiswa = [] 

    with open(fileData, mode='r') as file:
        fileReader = csv.DictReader(file)
        for row in fileReader:
            mahasiswa.append(row) 

    if len(mahasiswa) > 0:
        print('---------------------------------------')
        print("Mencari data mahasiswa")
        print('---------------------------------------')

        print('---------------------------------------')
        nim = input("Cari mahasiswa berdasarkan NIM: ") 
        print('---------------------------------------')

        dataFound = [] 

        i = 0 
        for data in mahasiswa: 
            if nim.isdigit(): 
                if data['NIM'] == nim: 
                    dataFound = mahasiswa[i] 
            else: 
                clearScreen() 

                print('-- WARNING ----------------------------')
                input(
                    f"Inputan NIM harus menggunakan Angka!\n" + 
                    "---------------------------------------\n" +
                    "\n>> Tekan ENTER untuk Mengulangi <<"
                )
                print('---------------------------------------')

                searchMahasiswa() 

            i = i + 1 

        if len(dataFound) > 0: 
            clearScreen() 

            print('---------------------------------------')
            print(f"Data Mahasiswa dengan NIM {nim} Ditemukan!")
            print('---------------------------------------')
            print(
                tabulate( 
                    [
                        ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], 
                        [   
                            dataFound['Nama'],
                            dataFound['NIM'],
                            dataFound['Jurusan'],
                            dataFound['Prodi'],
                            dataFound['Kelas']
                        ]
                    ],
                    headers='firstrow', 
                    tablefmt='grid', 
                )
            )
        else: 
            clearScreen()

            print('-- ALERT ------------------------------')
            print("Data yang kamu cari Tidak Ditemukan!")
            print('---------------------------------------')

        backToMenu() 

    else: 
        print('---------------------------------------')
        print(">> Data mahasiswa belum ada! <<")
        print('---------------------------------------')

        dataIsEmpty() 


def createMahasiswa():
    clearScreen() 

    mahasiswa = [] 

    with open(fileData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row) 

    with open(fileData, mode='a', newline='') as file:
        fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')
        
        print('-- FORM -------------------------------')
        nim = input('NOTE: ketik "0" untuk keluar dari form.\n\nMasukkan NIM Mahasiswa: ')

        clearScreen() 

        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')

        print('-- FORM -------------------------------')
        print("Masukkan NIM Mahasiswa:", nim)

        for data in mahasiswa:
            if nim.isdigit():
                if data['NIM'] == nim:
                    clearScreen() 

                    print('-- WARNING ----------------------------')
                    input(
                        f"NIM Mahasiswa tersebut sudah ada!\n" + 
                        "---------------------------------------\n" +
                        "\n>> Tekan ENTER untuk Mengulangi <<"
                    )
                    print('---------------------------------------')

                    createMahasiswa() 
            else: 
                clearScreen() 

                print('-- WARNING ----------------------------')
                input(
                    f"Inputan NIM harus menggunakan Angka!\n" + 
                    "---------------------------------------\n" +
                    "\n>> Tekan ENTER untuk Mengulangi <<"
                )
                print('---------------------------------------')

                createMahasiswa() 

        if not nim.isdigit():
            clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            createMahasiswa() 
        
        if nim == '0':
            clearScreen()

            print('\n-- ALERT ------------------------------')
            print("Kamu Batal Mengisi Form!")
            print('---------------------------------------')

            backToMenu() 
        
        nama = input("Masukkan Nama Mahasiswa: ")
        jurusan = input("Masukkan Jurusan Mahasiswa: ")
        prodi = input("Masukkan Program Studi Mahasiswa: ")
        kelas = input("Masukkan Kelas Mahasiswa: ").upper() 
        print('---------------------------------------')

        if len(nama) == 0 and len(jurusan) == 0 and len(prodi) == 0 and len(kelas) == 0:
            clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Data tidak boleh ada yang kosong!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            createMahasiswa() 
        else:
            if mahasiswa == []: 
                writer.writeheader() 

            writer.writerow({ 
                'Nama': nama,
                'NIM': nim,
                'Jurusan': jurusan,
                'Prodi': prodi,
                'Kelas': kelas
            })

        clearScreen() 

        print('---------------------------------------')
        print(">> Data Mahasiswa berhasil disimpan! <<")
        print('---------------------------------------')

    confCreateAgain() 


def editMahasiswa():
    clearScreen() 

    mahasiswa = []
    tbody = []
    dataFound = []
     
    with open(fileData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row) 

    if len(mahasiswa) > 0:
        
        print('---------------------------------------')
        print("Mengedit data mahasiswa")
        print('---------------------------------------')

        for data in mahasiswa: 
            
            column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
            tbody.append(column) 

        print(
            
            tabulate(
                tbody, 
                headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], 
                tablefmt='grid', 
                showindex=range(1, len(mahasiswa) + 1) 
            )
        )

        print('---------------------------------------')
        nim = input("Pilih NIM Mahasiswa: ")
        print('---------------------------------------')

        clearScreen() 

        print('---------------------------------------')
        print(f'Kamu sedang mengedit data dengan NIM "{nim}"')
        print('---------------------------------------')

        i = 0
        for data in mahasiswa: 
            if nim.isdigit(): 
                if data['NIM'] == nim: 
                    dataFound = mahasiswa[i]
            else: 
                clearScreen() 

                print('-- WARNING ----------------------------')
                input(
                    f"Inputan NIM harus menggunakan Angka!\n" + 
                    "---------------------------------------\n" +
                    "\n>> Tekan ENTER untuk Mengulangi <<"
                )
                print('---------------------------------------')

                editMahasiswa() 
            i = i + 1 

        
        if not len(dataFound) > 0:
            clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"NIM Tidak ditemukan\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            editMahasiswa() 

        print('-- FORM -------------------------------')
        
        nama = input("Masukkan Nama baru Mahasiswa: ")
        jurusan = input("Masukkan Jurusan baru Mahasiswa: ")
        prodi = input("Masukkan Program Studi baru Mahasiswa: ")
        kelas = input("Masukkan Kelas baru Mahasiswa: ").upper()
        print('---------------------------------------')
            
        i = 0
        for data in mahasiswa: 
            if data['NIM'] == nim: 
                
                if len(nama) == 0: 
                    mahasiswa[i]['Nama']
                else: 
                    mahasiswa[i]['Nama'] = nama
                
                if len(jurusan) == 0: 
                    mahasiswa[i]['Jurusan']
                else: 
                    mahasiswa[i]['Jurusan'] = jurusan
                
                if len(prodi) == 0: 
                    mahasiswa[i]['Prodi']
                else: 
                    mahasiswa[i]['Prodi'] = prodi
                
                if len(kelas) == 0: 
                    mahasiswa[i]['Kelas']
                else: 
                    mahasiswa[i]['Kelas'] = kelas
                
            i = i + 1 

        with open(fileData, mode='w', newline='') as csvFile:
            fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'] 
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames) 
            writer.writeheader() 
            for newData in mahasiswa: 
                writer.writerow({
                    'Nama': newData['Nama'],
                    'NIM': newData['NIM'],
                    'Jurusan': newData['Jurusan'],
                    'Prodi': newData['Prodi'],
                    'Kelas': newData['Kelas']
                })

        clearScreen() 

        print('---------------------------------------')
        print(">> Data baru dari NIM", nim, "Berhasil diperbarui! <<")
        print('---------------------------------------')

        backToMenu() 
    else: 
        print('---------------------------------------')
        print(">> Data mahasiswa belum ada! <<")
        print('---------------------------------------')

        dataIsEmpty() 


def deleteMahasiswa():
    clearScreen() 

    mahasiswa = []
    tbody = []

    with open(fileData, mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            mahasiswa.append(row)

    if len(mahasiswa) > 0:
        print('---------------------------------------')
        print("Menghapus data mahasiswa")
        print('---------------------------------------')

        for data in mahasiswa:
            column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
            tbody.append(column)

        print(
            tabulate(
                tbody,
                headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'],
                tablefmt='grid',
                showindex=range(1, len(mahasiswa) + 1)
            )
        )

        print('---------------------------------------')
        nim = input("Pilih NIM untuk menghapus Data: ")
        print('---------------------------------------')

        i = 0
        for data in mahasiswa:
            if data['NIM'] == nim:
                mahasiswa.remove(mahasiswa[i])
            i = i + 1

        with open(fileData, mode='w', newline='') as csvFile:
            fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()
            for newData in mahasiswa:
                writer.writerow({
                    'Nama': newData['Nama'],
                    'NIM': newData['NIM'],
                    'Jurusan': newData['Jurusan'],
                    'Prodi': newData['Prodi'],
                    'Kelas': newData['Kelas']
                })

        print('-- ALERT ------------------------------')
        print(">> DATA BERHASIL DIHAPUS <<")
        print('---------------------------------------')
    else:
        print('---------------------------------------')
        print(">> Data mahasiswa belum ada! <<")
        print('---------------------------------------')

        dataIsEmpty()

    backToMenu() 