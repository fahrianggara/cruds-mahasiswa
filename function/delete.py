from tabulate import tabulate
import function.action as action
import csv

fileData = 'assets/data.csv'

def deleteMahasiswa():
    action.clearScreen()

    mahasiswa = []
    tbody = []
    dataFound = []

    with open(fileData, mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            mahasiswa.append(row)

    if len(mahasiswa) > 0:
        print('---------------------------------------')
        print("Menghapus Data Mahasiswa")
        print('---------------------------------------')

        for data in mahasiswa:
            column = data['Nama'], data['NIM'], data['Fakultas'], data['Prodi'], data['Kelas']
            tbody.append(column)

        print(
            tabulate(
                tbody,
                headers=['Nama', 'NIM', 'Fakultas','Prodi', 'Kelas'],
                tablefmt='grid',
                showindex=range(1, len(mahasiswa) + 1)
            )
        )

        print('---------------------------------------')
        print("NOTE: Ketik 0 untuk keluar dari Form!\n")
        nim = input("Pilih NIM untuk Menghapus Data: ")
        print('---------------------------------------')

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

            deleteMahasiswa()

        if nim == '0':
            action.clearScreen()

            print('\n-- INFO -------------------------------')
            print("Kamu Telah Keluar Dari Form Delete!")
            print('---------------------------------------')

            action.backToMenu()

        if not len(dataFound) > 0:
            action.clearScreen()

            print('-- WARNING ----------------------------')
            input(
                f"NIM Tidak ditemukan\n" +
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            deleteMahasiswa()

        action.clearScreen()

        action.deleteData(mahasiswa, nim, fileData)
    else:
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        action.dataIsEmpty()

    action.backToMenu()
