# ====== FILE INI UNTUK MEMBUAT FUNCTION ====== #

# Mengambil package tabulate untuk membuat table
from tabulate import tabulate
import csv
import os

fileData = 'data.csv'

# Membuat variable
namaProjek = "CRUD Mahasiswa"
mahasiswa = []  # Type List

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function back to menu ini berfungsi untuk konfirmasi dan kembali ke menu
def backToMenu():
    input("\nSilahkan Tekan ENTER untuk kembali ke Menu")
    main()

def confCreateAgain():
    print('-- ALERT ------------------------------')
    confirm = input("Apakah kamu mau tambah data lagi? [Y/T]: ").upper()
    print('---------------------------------------')

    if confirm == 'Y':
        createMahasiswa()
    else:
        backToMenu()

def deleteMahasiswa():
    clearScreen()

    mahasiswa = []
    tbody = []

    with open(fileData, mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            mahasiswa.append(row)

    print('---------------------------------------')
    print("Menghapus data mahasiswa")
    print('---------------------------------------')

    if len(mahasiswa) > 0:
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
        
        print('---------------------------------------')
        print(">> DATA BERHASIL DIHAPUS <<")
        print('---------------------------------------')
    else:
        print(">> Data tidak ditemukan! <<")
        print('---------------------------------------')

    backToMenu()

def editMahasiswa():
    clearScreen()

    mahasiswa = []
    tbody = []

    with open(fileData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row)

    print('---------------------------------------')
    print("Mengedit data mahasiswa")
    print('---------------------------------------')
    
    if len(mahasiswa) > 0:
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
        nama = input("Masukkan Nama baru Mahasiswa: ")
        jurusan = input("Masukkan Jurusan baru Mahasiswa: ")
        prodi = input("Masukkan Program Studi baru Mahasiswa: ")
        kelas = input("Masukkan Kelas baru Mahasiswa: ").upper()

        i = 0
        for data in mahasiswa:
            if data['NIM'] == nim:

                mahasiswa[i]['Nama'] = nama
                mahasiswa[i]['Jurusan'] = jurusan
                mahasiswa[i]['Prodi'] = prodi
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
        
        print('---------------------------------------')
        print("Data baru dari NIM:", nim)
        print('---------------------------------------')
        print(
            tabulate(
                [
                    [nama, nim, jurusan, prodi, kelas],
                ],
                headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'],
                tablefmt='grid',
            )
        )
        
    else:
        print(">> Data tidak ditemukan! <<")
        print('---------------------------------------')

    backToMenu()

def searchMahasiswa():
    clearScreen()

    mahasiswa = []

    with open(fileData, mode='r') as file:
        fileReader = csv.DictReader(file)
        for row in fileReader:
            mahasiswa.append(row)

    nim = input("Cari mahasiswa berdasarkan NIM: ")
    dataFound = []

    i = 0
    for data in mahasiswa:
        if data['NIM'] == nim:
            dataFound = mahasiswa[i]
        i = i + 1

    if len(dataFound) > 0:
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
        print(">> Data tidak ditemukan! <<")
        print('---------------------------------------')

    backToMenu()

def createMahasiswa():
    clearScreen()

    print('---------------------------------------')
    print("Membuat data mahasiswa")
    print('---------------------------------------')

    mahasiswa = []

    with open(fileData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row)

    with open(fileData, mode='a', newline='') as file:
        fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        nim = input("Masukkan nim mahasiswa: ")

        for data in mahasiswa:
            if data['NIM'] == nim:
                print('\n-- ALERT ------------------------------')
                input(">> NIM Mahasiswa sudah ada! <<")
                print('---------------------------------------')

                createMahasiswa()

        nama = input("Masukkan nama mahasiswa: ")
        jurusan = input("Masukkan jurusan mahasiswa: ")
        prodi = input("Masukkan program studi mahasiswa: ")
        kelas = input("Masukkan kelas mahasiswa: ").upper()

        writer.writerow({
            'Nama': nama,
            'NIM': nim,
            'Jurusan': jurusan,
            'Prodi': prodi,
            'Kelas': kelas
        })

        print('---------------------------------------')
        print(">> Data mahasiswa berhasil disimpan! <<")
        print('---------------------------------------')

    confCreateAgain()


def showMahasiswa():
    clearScreen()

    mahasiswa = []
    tbody = []

    print('---------------------------------------')
    print("Data Mahasiswa")
    print('---------------------------------------')

    with open(fileData) as file:
        fileReader = csv.reader(file, delimiter=",")
        for row in fileReader:
            mahasiswa.append(row)

        if (len(mahasiswa) > 0):
            label = mahasiswa.pop(0)
            thead = label

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
            print(">> Data mahasiswa belum ada! <<")
            print('---------------------------------------')

    backToMenu()


def exitMenu():
    clearScreen()
    print('---------------------------------------')
    pilihan = input("Apakah kamu yakin akan keluar dari menu? [Y/T]: ").upper()

    if pilihan == 'Y':
        exit()
    else:
        print()
        print(">> Kamu batal Keluar dari Menu! <<")
        print('---------------------------------------')

        backToMenu()

# Function Main atau Menu
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
        print('---------------------------------------')
        print(">> Oops, Menu tersebut tidak terdafar! <<")
        print('---------------------------------------')

        backToMenu()
