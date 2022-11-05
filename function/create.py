# ====== FILE INI UNTUK FUNCTION CREATE MAHASISWA ====== #

import csv # mengambil package csv (comma separated values)
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action

fileData = 'assets/data.csv'

def createMahasiswa():
    action.clearScreen() 

    mahasiswa = []
    dataMahasiswa = []

    # mengambil data tidak memakai key-nya
    with open(fileData) as csv_file:
        csvReader = csv.reader(csv_file, delimiter=",")
        for row in csvReader:
            mahasiswa.append(row)

    # mengambil data memakai key-nya
    with open(fileData, mode='r') as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            dataMahasiswa.append(row)

    with open(fileData, mode='a', newline='') as file:
        fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')
        
        print('-- FORM -------------------------------')
        nim = input('NOTE: ketik "0" untuk keluar dari form.\n\nMasukkan NIM Mahasiswa: ')

        action.clearScreen() 

        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')

        print('-- FORM -------------------------------')
        print("Masukkan NIM Mahasiswa:", nim)

        for data in dataMahasiswa:
            if data['NIM'] == nim:
                action.clearScreen() 

                print('-- WARNING ----------------------------')
                input(
                    f"NIM Mahasiswa tersebut sudah ada!\n" + 
                    "---------------------------------------\n" +
                    "\n>> Tekan ENTER untuk Mengulangi <<"
                )
                print('---------------------------------------')

                createMahasiswa() 
        
        if not nim.isdigit():
            action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            createMahasiswa() 

        if nim == '0':
            action.clearScreen()

            print('\n-- ALERT ------------------------------')
            print("Kamu Batal Mengisi Form!")
            print('---------------------------------------')

            action.backToMenu() 

        if len(nim) > 8:
            action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus 8 Digit!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            createMahasiswa() 

        elif len(nim) < 8:
            action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus 8 Digit!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            createMahasiswa() 
        
        nama = input("Masukkan Nama Mahasiswa: ")
        jurusan = input("Masukkan Jurusan Mahasiswa: ")
        prodi = input("Masukkan Program Studi Mahasiswa: ")
        kelas = input("Masukkan Kelas Mahasiswa: ").upper() 
        print('---------------------------------------')

        if len(nama) == 0 and len(jurusan) == 0 and len(prodi) == 0 and len(kelas) == 0:
            action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Data tidak boleh ada yang kosong!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            createMahasiswa() 
        else:
            # Jika, datanya cuma header saja, maka buat datanya saja.
            if len(mahasiswa) == 1:
                writer.writerow({ 
                    'Nama': nama,
                    'NIM': nim,
                    'Jurusan': jurusan,
                    'Prodi': prodi,
                    'Kelas': kelas
                })
            else: # jika data full kosong semua(baru)
                if mahasiswa == []: # jika data full kosong buat header
                    writer.writeheader()

                writer.writerow({ 
                    'Nama': nama,
                    'NIM': nim,
                    'Jurusan': jurusan,
                    'Prodi': prodi,
                    'Kelas': kelas
                })

        action.clearScreen() 

        print('-- INFO -------------------------------')
        print("Data Mahasiswa berhasil disimpan!")
        print('---------------------------------------')

    action.confCreateAgain() 