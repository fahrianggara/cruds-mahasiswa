# ====== FILE INI UNTUK FUNCTION DELETE MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
# mengambil semua function dari file action di folder function
import function.action
import csv # mengambil package csv (comma separated values)

fileData = 'assets/data.csv'

def deleteMahasiswa():
    function.action.clearScreen() 

    mahasiswa = []
    tbody = []

    with open(fileData, mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            mahasiswa.append(row)

    if len(mahasiswa) > 0:
        print('---------------------------------------')
        print("Menghapus Data Mahasiswa")
        print('---------------------------------------')

        for data in mahasiswa:
            column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
            tbody.append(column)

        print(
            tabulate(
                tbody,
                headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'],
                tablefmt='grid',
                showindex=range(1, len(mahasiswa) + 1)
            )
        )

        print('---------------------------------------')
        nim = input("Pilih NIM untuk menghapus Data: ")
        print('---------------------------------------')

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
    else:
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        function.action.dataIsEmpty()

    function.action.backToMenu() 