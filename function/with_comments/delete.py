# ====== FILE INI UNTUK FUNCTION DELETE MAHASISWA ====== #

# mengambil function tabulate dari package tabulate untuk membuat table
from tabulate import tabulate
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action
import csv  # mengambil package csv (comma separated values)

# membuat var fileData untuk menyimpan path file data mahasiswa csv
fileData = 'assets/data.csv'

# membuat function untuk menghapus data mahasiswa
def deleteMahasiswa():
    # action clear screen untuk membersihkan layar terminal
    action.clearScreen()

    mahasiswa = []  # membuat var mahasiswa untuk menyimpan data mahasiswa dari file data.csv
    tbody = []  # membuat var tbody untuk menyimpan data mahasiswa yang akan ditampilkan di table
    # membuat var dataFound untuk menyimpan data mahasiswa jika mahasiswa nya ada sesuai keyword pencarian(NIM)
    dataFound = []

    # "with open" untuk membuka file data.csv dan memberi alias file
    # mode 'r'(read) untuk membaca file data.csv
    with open(fileData, mode='r') as csvFile:
        # csv dictreader untuk membaca file csv dengan key value
        csvReader = csv.DictReader(csvFile)
        # looping, untuk membaca setiap baris data dan menampungnya ke var mahasiswa
        for row in csvReader:
            mahasiswa.append(row)

    # jika data mahasiswanya ada.
    if len(mahasiswa) > 0:
        # cetak judul function
        print('---------------------------------------')
        print("Menghapus Data Mahasiswa")
        print('---------------------------------------')

        # looping data dari var mahasiswa yang sudah di isi data dari file data.csv
        for data in mahasiswa:
            # membuat var column untuk menyimpan data mahasiswa yang akan ditampilkan di table
            column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
            # var column di tambahkan ke var tbody
            tbody.append(column)

        # cetak table data mahasiswa
        print(
            tabulate(  # function tabulate untuk membuat table
                tbody,  # isi table
                headers=['Nama', 'NIM', 'Jurusan',
                         'Prodi', 'Kelas'],  # header table
                tablefmt='grid',  # gaya table
                # menampilkan index table (1 - setiap data mahasiswa)
                showindex=range(1, len(mahasiswa) + 1)
            )
        )

        # form
        print('---------------------------------------')
        print("NOTE: Ketik 0 untuk keluar dari Form!\n")
        # input nim mahasiswa yang akan di hapus
        nim = input("Pilih NIM untuk Menghapus Data: ")
        print('---------------------------------------')

        i = 0  # membuat var i untuk mencari index data mahasiswa
        for data in mahasiswa:  # looping data dari var mahasiswa
            if data['NIM'] == nim:  # jika nim mahasiswa sama dengan nim yang di input
                # var dataFound di isi data mahasiswa yang sama dengan nim yang di input
                dataFound = mahasiswa[i]
            i = i + 1  # var i di tambah 1 agar index nya bertambah sampai data mahasiswa ketemu yang sama dengan nim yang di input

        # validasi, jika nim inputan bukan angka.
        if not nim.isdigit():
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" +
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            # balik lagi ke function deleteMahasiswa (diulang)
            deleteMahasiswa()

        # jika nim inputan 0, maka keluar dari form
        if nim == '0':
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan
            print('\n-- INFO -------------------------------')
            print("Kamu Telah Keluar Dari Form Delete!")
            print('---------------------------------------')

            # balik kemenu utama
            action.backToMenu()

        # validasi jika nim inputan tidak ada di data mahasiswa
        if not len(dataFound) > 0:
            # action clear screen untuk membersihkan layar terminal
            action.clearScreen()

            # cetak pesan error
            print('-- WARNING ----------------------------')
            input(
                f"NIM Tidak ditemukan\n" +
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            deleteMahasiswa() # balik lagi ke function deleteMahasiswa (diulang)

        # action clear screen untuk membersihkan layar terminal
        action.clearScreen()

        # lempar ke action delete data di file action.py
        action.deleteData(mahasiswa, nim, fileData)
    else: # jika data mahasiswa belum ada
        # cetak pesan
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')

        # lempar ke data is empty untuk menambahkan data mahasiswa baru
        action.dataIsEmpty()

    # balik ke menu utama
    action.backToMenu()
