# ====== FILE INI UNTUK FUNCTION SEARCH MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
import function.action as action # mengambil semua function dari file action.py di folder function dan kasih aliasn action
import csv # mengambil package csv (comma separated values)

fileData = 'assets/data.csv'

def searchMahasiswa():
    action.clearScreen() 

    mahasiswa = [] 

    with open(fileData, mode='r') as file:
        fileReader = csv.DictReader(file)
        for row in fileReader:
            mahasiswa.append(row) 

    if len(mahasiswa) > 0:
        print('---------------------------------------')
        print("Mencari Data Mahasiswa")
        print('---------------------------------------')

        print('---------------------------------------')
        print('NOTE: Ketik 0 untuk keluar dari pencarian!\n')
        nim = input("Cari mahasiswa berdasarkan NIM: ") 
        print('---------------------------------------')

        dataFound = [] 

        i = 0 
        for data in mahasiswa:
            if data['NIM'] == nim: 
                dataFound = mahasiswa[i] 
            i = i + 1 
        
        if not nim.isdigit(): 
            action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            searchMahasiswa() 
        
        if nim == '0':
            action.clearScreen()

            print('\n-- ALERT ------------------------------')
            print("Kamu keluar dari pencarian!")
            print('---------------------------------------')

            action.backToMenu() 

        if len(dataFound) > 0: 
            action.clearScreen() 

            print('-- INFO -------------------------------')
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
            action.clearScreen()

            print('-- ALERT ------------------------------')
            input(
                f"Data yang kamu cari tidak ditemukan!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            searchMahasiswa() # ulang lagi

        action.backToMenu() 

    else: 
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        action.dataIsEmpty() 