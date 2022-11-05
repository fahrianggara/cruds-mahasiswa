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

namaProjek = "CRUDS Mahasiswa"

def main():
    action.clearScreen() 

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
    menu = input("Pilih Kode Menunya: ")
    print('---------------------------------------')

    if menu == '0': 
        action.clearScreen() 
        action.exitMenu() 
    elif menu == '1': 
        showMahasiswa()
    elif menu == '2': 
        searchMahasiswa()
    elif menu == '3': 
        createMahasiswa()
    elif menu == '4': 
        editMahasiswa()
    elif menu == '5': 
        deleteMahasiswa()
    else: 
        action.clearScreen()

        print('-- ALERT ------------------------------')
        print("Menu Tersebut Tidak Ada!")
        print('---------------------------------------')

        action.backToMenu() 