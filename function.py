# ====== FILE INI UNTUK MEMBUAT FUNCTION ====== #

# Mengambil package tabulate untuk membuat table
from tabulate import tabulate 
import csv

file_data = 'data.csv'

# Membuat variable
namaProjek = "CRUD Mahasiswa"
data_mahasiswa = [] # Type List

# Function back to menu ini berfungsi untuk konfirmasi dan kembali ke menu
def backToMenu():
    input("\nSilahkan Tekan ENTER untuk kembali ke Menu")
    main()

def createMahasiswa():
    print('---------------------------------------')
    print("Membuat data mahasiswa")
    print('---------------------------------------')
    with open(file_data, mode='a', newline='') as file:
        fieldnames = ['Nama','NIM','Jurusan','Prodi','Kelas']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        nama = input("Masukkan nama mahasiswa: ")
        nim = int(input("Masukkan nim mahasiswa: "))
        jurusan = input("Masukkan jurusan mahasiswa: ")
        prodi = input("Masukkan program studi mahasiswa: ")
        kelas = input("Masukkan kelas mahasiswa: ").upper()

        writer.writerow({
            'Nama': nama,
            'NIM' : nim,
            'Jurusan' : jurusan,
            'Prodi' : prodi,
            'Kelas' : kelas
        })

        print('---------------------------------------')
        print(">> Data mahasiswa berhasil disimpan! <<")
        print('---------------------------------------')

    backToMenu()
    

def showMahasiswa():
    mahasiswaData = []
    tbody = []
    thead = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas']

    print('---------------------------------------')
    print("Data Mahasiswa")
    print('---------------------------------------')

    with open(file_data) as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            mahasiswaData.append(row)

        if (len(mahasiswaData) > 0):
            for data in mahasiswaData:
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
    print('\n---------------------------------------')
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
        print("Kamu Memilih Menu:", menu)
    elif menu == 3:
        createMahasiswa()
    elif menu == 4:
        print("Kamu Memilih Menu:", menu)
    elif menu == 5:
        print("Kamu Memilih Menu:", menu)
    else:
        print('---------------------------------------')
        print(">> Oops, Menu tersebut tidak terdafar! <<")
        print('---------------------------------------')

        backToMenu()  