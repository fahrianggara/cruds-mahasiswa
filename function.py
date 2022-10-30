# ====== FILE INI UNTUK MEMBUAT FUNCTION ====== #

# Mengambil package tabulate untuk membuat table
from tabulate import tabulate 

# Membuat variable
namaProjek = "CRUD Mahasiswa"
data_mahasiswa = [] # Type List

# Function back to menu ini berfungsi untuk konfirmasi
def backToMenu():
    input("\nTekan Enter untuk kembali ke Menu")
    main()

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
    menu = int(input("Silahkan pilih Kode Menunya: "))
    print('---------------------------------------\n')

    if menu == 0:
        pilihan = input("Apakah kamu yakin akan keluar dari menu? [Y/T]: ").upper()

        if pilihan == 'Y':
            exit()
        else:
            print("Kamu tidak jadi keluar dari menu!")
            backToMenu()
            
    elif menu == 1:
        print("Kamu Memilih Menu:", menu)
    elif menu == 2:
        print("Kamu Memilih Menu:", menu)
    elif menu == 3:
        print("Kamu Memilih Menu:", menu)
    elif menu == 4:
        print("Kamu Memilih Menu:", menu)
    elif menu == 5:
        print("Kamu Memilih Menu:", menu)
    else:
        print("Oops! Menu tersebut tidak terdaftar!")