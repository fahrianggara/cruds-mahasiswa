from tabulate import tabulate 
from function.show import showMahasiswa 
from function.search import searchMahasiswa 
from function.create import createMahasiswa 
from function.edit import editMahasiswa 
from function.delete import deleteMahasiswa 
import function.action as action

namaProjek = "CRUDS Mahasiswa UBSI"

def menu():
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
    pilihan = input("Pilih Kode Menunya: ")
    print('---------------------------------------')
    
    if not pilihan.isdigit(): 
        action.clearScreen() 
        
        print('-- WARNING ----------------------------')
        input(
            f"Harus Menggunakan Angka!\n" + 
            "---------------------------------------\n" +
            "\n>> Tekan ENTER untuk Mengulangi <<"
        )
        print('---------------------------------------')

        menu()

    if pilihan == '0': 
        action.clearScreen() 
        action.exitMenu() 
    elif pilihan == '1': 
        showMahasiswa()
    elif pilihan == '2': 
        searchMahasiswa()
    elif pilihan == '3': 
        createMahasiswa()
    elif pilihan == '4': 
        editMahasiswa()
    elif pilihan == '5': 
        deleteMahasiswa()
    else: 
        action.clearScreen()
        
        print('-- ALERT ------------------------------')
        print("Menu Tersebut Tidak Ada!")
        print('---------------------------------------')
        
        action.backToMenu() 