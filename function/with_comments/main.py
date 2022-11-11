# ====== FILE INI UNTUK MAIN FUNCTION ====== #

# import package
from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action
# import main
from function.show import showMahasiswa # memanggil function showMahasiswa dari file show.py di folder function
from function.search import searchMahasiswa # memanggil function searchMahasiswa dari file search.py di folder function
from function.create import createMahasiswa # memanggil function createMahasiswa dari file create.py di folder function
from function.edit import editMahasiswa # memanggil function editMahasiswa dari file edit.py di folder function
from function.delete import deleteMahasiswa # memanggil function deleteMahasiswa dari file delete.py di folder function

# namaprojek untuk menampilkan nama projek di menu  
namaProjek = "CRUDS Mahasiswa UBSI"

# function main untuk menampilkan menu menu
def main():
    # action clear screen untuk membersihkan layar terminal
    action.clearScreen() 

    # cetak judul menu
    print('---------------------------------------')
    print(f"List Menu | {namaProjek}")
    print('---------------------------------------')

    # cetak table dengan function tabulate dari package tabulate
    print(
        tabulate( 
            [
                ["Kode", "Nama Menu"], # header table (baris pertama)
                # Data data menu
                ["0", "Keluar dari Menu"], 
                ["1", "Menampilkan data Mahasiswa"], 
                ["2", "Mencari data Mahasiswa"], 
                ["3", "Membuat data Mahasiswa"], 
                ["4", "Memperbarui data Mahasiswa"], 
                ["5", "Menghapus data Mahasiswa"], 
            ],
            headers='firstrow', # header diambil dari baris pertama
            tablefmt='grid' # gaya table
        )
    )

    # cetak input kode menu untuk memilih menu
    print('---------------------------------------')
    menu = input("Pilih Kode Menunya: ")
    print('---------------------------------------')

    # validasi jika input menu bukan angka
    if not menu.isdigit(): 
        # action clear screen untuk membersihkan layar terminal
        action.clearScreen() 

        # cetak pesan error
        print('-- WARNING ----------------------------')
        input(
            f"Harus Menggunakan Angka!\n" + 
            "---------------------------------------\n" +
            "\n>> Tekan ENTER untuk Mengulangi <<"
        )
        print('---------------------------------------')

        # diulang lagi ke function main
        main()

    # jika input menu adalah 0
    if menu == '0': 
        action.clearScreen() 
        action.exitMenu() 
    elif menu == '1': # jika input menu adalah 1 maka akan menampilkan data mahasiswa
        showMahasiswa()
    elif menu == '2': # jika input menu adalah 2 maka akan diarahkan ke pencarian data mahasiswa
        searchMahasiswa()
    elif menu == '3': # jika input menu adalah 3 maka akan diarahkan ke pembuatan data mahasiswa
        createMahasiswa()
    elif menu == '4': # jika input menu adalah 4 maka akan diarahkan ke pembaruan data mahasiswa
        editMahasiswa()
    elif menu == '5': # jika input menu adalah 5 maka akan diarahkan ke penghapusan data mahasiswa
        deleteMahasiswa()
    else: # jika input menu selain 0 sampai 5
        # action clear screen untuk membersihkan layar terminal
        action.clearScreen()

        # cetak pesan error
        print('-- ALERT ------------------------------')
        print("Menu Tersebut Tidak Ada!")
        print('---------------------------------------')

        # diulang lagi ke function main
        action.backToMenu() 