# ====== FILE INI UNTUK FUNCTION EDIT MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
# mengambil semua function dari file action di folder function
import function.action
import csv # mengambil package csv (comma separated values)

fileData = 'assets/data.csv'

def editMahasiswa():
    function.action.clearScreen() 

    mahasiswa = []
    tbody = []
    dataFound = []
     
    with open(fileData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row) 

    if len(mahasiswa) > 0:
        
        print('---------------------------------------')
        print("Mengedit Data Mahasiswa")
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
        nim = input("Pilih NIM Mahasiswa: ")
        print('---------------------------------------')

        function.action.clearScreen() 

        print('-- INFO -------------------------------')
        print(f'Kamu sedang mengedit Data dari NIM: {nim}')
        print('---------------------------------------')

        i = 0
        for data in mahasiswa: 
            if data['NIM'] == nim: 
                dataFound = mahasiswa[i]
            i = i + 1 

        if not nim.isdigit(): 
            function.action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            editMahasiswa() 
        
        if not len(dataFound) > 0:
            function.action.clearScreen() 

            print('-- WARNING ----------------------------')
            input(
                f"NIM Tidak ditemukan\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            editMahasiswa() 

        print('-- FORM -------------------------------')
        print("NOTE: Abaikan.. jika salah satu data tidak mau diperbarui!\n")
        nama = input("Masukkan Nama baru Mahasiswa: ")
        jurusan = input("Masukkan Jurusan baru Mahasiswa: ")
        prodi = input("Masukkan Program Studi baru Mahasiswa: ")
        kelas = input("Masukkan Kelas baru Mahasiswa: ").upper()
        print('---------------------------------------')
            
        i = 0
        for data in mahasiswa: 
            if data['NIM'] == nim: 
                
                if len(nama) == 0: 
                    mahasiswa[i]['Nama']
                else: 
                    mahasiswa[i]['Nama'] = nama
                
                if len(jurusan) == 0: 
                    mahasiswa[i]['Jurusan']
                else: 
                    mahasiswa[i]['Jurusan'] = jurusan
                
                if len(prodi) == 0: 
                    mahasiswa[i]['Prodi']
                else: 
                    mahasiswa[i]['Prodi'] = prodi
                
                if len(kelas) == 0: 
                    mahasiswa[i]['Kelas']
                else: 
                    mahasiswa[i]['Kelas'] = kelas
                
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

        function.action.clearScreen() 

        print('-- INFO -------------------------------')
        print("Data baru dari NIM", nim, "Berhasil diperbarui!")
        print('---------------------------------------')

        function.action.backToMenu() 
    else: 
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        function.action.dataIsEmpty() 