# ====== FILE INI UNTUK ACTION FUNCTION ====== #

# Import section
import os # mengambil package os (operating system)
from function.create import createMahasiswa # memanggil function createMahasiswa dari file create.py di folder function
import function.main as func # memanggil function main dari file main.py di folder function

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def backToMenu():
    input("\n>> Tekan ENTER untuk Kembali ke Menu <<")
    func.main() 

def confCreateAgain():
    print('-- ALERT ------------------------------')
    pilihan = input("Apakah kamu mau tambah data lagi? [Y/T]: ").upper()
    print('---------------------------------------')

    if pilihan == 'Y': 
        createMahasiswa()
    elif pilihan == 'T': 
        clearScreen() 
        
        print('-- INFO -------------------------------')
        print("OK, Kamu batal membuat data lagi!")
        print('---------------------------------------')

        backToMenu() 
    else: 
        clearScreen() 
        
        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        confCreateAgain() 

def exitMenu():
    print('-- ALERT ------------------------------')
    pilihan = input("Apakah kamu yakin akan keluar dari menu? [Y/T]: ").upper()
    print('---------------------------------------')

    if pilihan == 'Y': 
        clearScreen() 

        exit( 
            '-- INFO -------------------------------\n' +
            'Kamu telah keluar dari Menu!\n' +
            '---------------------------------------'
        )
    elif pilihan == 'T': 
        clearScreen() 

        print('-- INFO -------------------------------')
        print("Kamu batal Keluar dari Menu!")
        print('---------------------------------------')

        backToMenu() 
    else: 
        clearScreen() 
        
        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        exitMenu()

def dataIsEmpty():
    
    pilihan = input("\nHmm.. Data mahasiswa masih kosong nih. Buat? [Y/T]: ").upper()

    if pilihan == 'Y': 
        createMahasiswa()
    elif pilihan == 'T': 
        clearScreen() 
        
        print('-- INFO -------------------------------')
        print("OK, Kamu batal membuat data baru!")
        print('---------------------------------------')

        backToMenu()
    else: 
        clearScreen() 
        
        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        dataIsEmpty()