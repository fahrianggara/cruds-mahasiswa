from tabulate import tabulate 
from function.show import showMahasiswa 
from function.search import searchMahasiswa 
from function.create import createMahasiswa 
from function.edit import editMahasiswa 
from function.delete import deleteMahasiswa 
import function.action as action

namaProjek = "CRUDS Mahasiswa UBSI"

def main():
    action.clearScreen() 
    
    print('---------------------------------------')
    print(f"Daftar Menu | {namaProjek}")
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
    
    if not menu.isdigit(): 
        action.clearScreen() 
        
        print('-- WARNING ----------------------------')
        input(
            f"Harus Menggunakan Angka!\n" + 
            "---------------------------------------\n" +
            "\n>> Tekan ENTER untuk Mengulangi <<"
        )
        print('---------------------------------------')

        main()

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