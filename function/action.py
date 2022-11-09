# ====== FILE INI UNTUK ACTION FUNCTION ====== #

# Import section
import csv  # mengambil package csv (comma separated values)
import os  # mengambil package os (operating system)
# memanggil function createMahasiswa dari file create.py di folder function
from function.create import createMahasiswa
# memanggil function main dari file main.py di folder function
import function.main as func

# membuat function untuk membersihkan layar
def clearScreen():
    # untuk windows menggunakan cls dan untuk linux menggunakan clear
    os.system('cls' if os.name == 'nt' else 'clear')

# membuat function untuk kembali ke menu
def backToMenu():
    # menampilkan pesan
    input("\n>> Tekan ENTER untuk Kembali ke Menu <<")
    # pergi ke function main(utama)
    func.main()

# membuat function confcreateagain untuk konfirmasi membuat data lagi
def confCreateAgain():
    print('-- ALERT ------------------------------')
    # var pilihan untuk menampung inputan dari user dan diubah menjadi huruf besar dan pilihan harus Y atau T
    pilihan = input("Apakah kamu mau tambah data lagi? [Y/T]: ").upper()
    print('---------------------------------------')

    # jika pilihan sama dengan Y
    if pilihan == 'Y':
        # pergi ke function createMahasiswa
        createMahasiswa()
    elif pilihan == 'T':  # jika pilihan sama dengan T
        # membersihkan layar
        clearScreen()

        # menampilkan pesan
        print('-- INFO -------------------------------')
        print("OK, Kamu batal membuat data lagi!")
        print('---------------------------------------')

        # pergi ke function backToMenu
        backToMenu()
    else:  # jika pilihan tidak sama dengan Y dan T
        # membersihkan layar
        clearScreen()

        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        # pergi ke function confCreateAgain dan mengulang kembali sampai user memasukkan inputan yang benar (Y/T)
        confCreateAgain()

# membuat function exit untuk keluar dari program
def exitMenu():
    print('-- ALERT ------------------------------')
    # var pilihan untuk menampung inputan dari user dan diubah menjadi huruf besar dan pilihan harus Y atau T
    pilihan = input("Apakah kamu yakin akan keluar dari menu? [Y/T]: ").upper()
    print('---------------------------------------')

    # jika pilihan sama dengan Y
    if pilihan == 'Y':
        # membersihkan layar
        clearScreen()

        # function exit untuk keluar dari program dan menampilkan pesan
        exit(
            '-- INFO -------------------------------\n' +
            'Kamu telah keluar dari Menu!\n' +
            '---------------------------------------'
        )
    elif pilihan == 'T':  # jika pilihan sama dengan T
        # membersihkan layar
        clearScreen()

        # menampilkan pesan
        print('-- INFO -------------------------------')
        print("Kamu batal Keluar dari Menu!")
        print('---------------------------------------')

        # pergi ke function backToMenu
        backToMenu()
    else:  # jika pilihan tidak sama dengan Y dan T
        # membersihkan layar
        clearScreen()

        # menampilkan pesan
        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        # pergi ke function exitMenu dan mengulang kembali sampai user memasukkan inputan yang benar (Y/T)
        exitMenu()

# membuat function data is empty jika data kosong
def dataIsEmpty():

    # var pilihan untuk menampung inputan dari user dan diubah menjadi huruf besar dan pilihan harus Y atau T
    pilihan = input(
        "\nHmm.. Data mahasiswa masih kosong nih. Buat? [Y/T]: ").upper()

    if pilihan == 'Y':  # jika pilihan sama dengan Y
        createMahasiswa()  # pergi ke function createMahasiswa
    elif pilihan == 'T':  # jika pilihan sama dengan T
        # membersihkan layar
        clearScreen()

        # menampilkan pesan
        print('-- INFO -------------------------------')
        print("OK, Kamu batal membuat data baru!")
        print('---------------------------------------')

        # pergi ke function backToMenu
        backToMenu()
    else:  # jika pilihan tidak sama dengan Y dan T
        # membersihkan layar
        clearScreen()

        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        # pergi ke function dataIsEmpty dan mengulang kembali sampai user memasukkan inputan yang benar (Y/T)
        dataIsEmpty()

# membuat function delete data dengan parameter mahasiswa, nim, dan file csvnya dari file delete.py
def deleteData(mahasiswa, nim, fileData):
    # var hapus ini untuk menampung inputan dari user dan diubah menjadi huruf besar dan pilihan harus Y atau T
    hapus = input(
        f"\nApakah kamu yakin akan Menghapus Data dengan NIM: {nim} ? [Y/T]: ").upper()

    if hapus == 'Y':  # jika pilihan sama dengan Y
        # membersihkan layar
        clearScreen()

        # i sama dengan 0 untuk menampung index
        i = 0
        # looping untuk mengecek data mahasiswa
        for data in mahasiswa:
            # jika nim sama dengan nim yang diinputkan user
            if data['NIM'] == nim:
                # hapus data mahasiswa berdasarkan index
                mahasiswa.remove(mahasiswa[i])
            # ini berfungsi untuk menambah index jika data mahasiswa tidak sama dengan nim yang diinputkan user,
            # sampai data mahasiswa sama dengan nim yang diinputkan user
            i = i + 1

        # membuka file csv dengan mode write dan menampungnya ke var csvFile.
        # ini berfungsi untuk menulis ulang data yang sudah dihapus seperti refresh data
        with open(fileData, mode='w', newline='') as csvFile:
            # fieldnames untuk menampung nama kolom (header) dari file csv
            fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas']
            # var writer untuk menulis data ke file csv dan dictwriter ini untuk menulis data dengan format dictionary,
            # isinya adalah file csv dan fieldnames
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            # menulis header
            writer.writeheader()
            # looping untuk menulis data mahasiswa
            for newData in mahasiswa:
                # menulis data mahasiswa sama
                writer.writerow({
                    'Nama': newData['Nama'],
                    'NIM': newData['NIM'],
                    'Jurusan': newData['Jurusan'],
                    'Prodi': newData['Prodi'],
                    'Kelas': newData['Kelas']
                })

        # menampilkan pesan jika data berhasil dihapus
        print('-- INFO -------------------------------')
        print(f"Data dengan NIM {nim} berhasil dihapus!")
        print('---------------------------------------')
    elif hapus == 'T':  # jika pilihan sama dengan T
        # membersihkan layar
        clearScreen()

        print('-- INFO -------------------------------')
        print("Kamu Batal Menghapus Data!")
        print('---------------------------------------')

        # pergi ke function backToMenu
        backToMenu()
    else:  # jika pilihan tidak sama dengan Y dan T
        clearScreen()  # membersihkan layar

        print('-- ALERT ------------------------------')
        print("Silahkan pilih Tidak [T] atau Ya [Y]")
        print('---------------------------------------')

        # pergi ke function deleteData dan mengulang kembali sampai user memasukkan inputan yang benar (Y/T)
        # dan menyimpan parameter mahasiswa, nim, dan file csvnya
        deleteData(mahasiswa, nim, fileData)
