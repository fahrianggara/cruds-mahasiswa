import csv
import os
from function.create import createMahasiswa
import function.main as func


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def backToMenu():
    input("\n>> Tekan ENTER untuk Kembali ke Menu <<")
    func.main()


def confCreateAgain():
    print()

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
    print()
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


def deleteData(mahasiswa, nim, fileData):
    hapus = input(f"\nApakah kamu yakin akan Menghapus Data dengan NIM: {nim} ? [Y/T]: ").upper()

    if hapus == 'Y':
        clearScreen()

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

        print('-- INFO -------------------------------')
        print(f"Data dengan NIM {nim} berhasil dihapus!")
        print('---------------------------------------')
    elif hapus == 'T':
        clearScreen()

        print('-- INFO -------------------------------')
        print("Kamu Batal Menghapus Data!")
        print('---------------------------------------')

        backToMenu()
    else:
        clearScreen()

        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        deleteData(mahasiswa, nim, fileData)
