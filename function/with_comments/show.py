# ====== FILE INI UNTUK FUNCTION SHOW MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action
import csv # mengambil package csv (comma separated values)

# membuat var fileData untuk menyimpan path file data mahasiswa csv
fileData = 'assets/data.csv'

# membuat function show mahasiswa untuk menampilkan semua data mahasiswa
def showMahasiswa():
    # action clear screen untuk membersihkan layar terminal
    action.clearScreen() 

    # 2 variable ini untuk menampung data2 mahasiswa nanti yang akan dilooping dari file csv
    mahasiswa = []
    tbody = [] 

    # with open untuk membuka file data.csv dan memberi alias csvFile
    with open(fileData, mode='r') as csvFile:
        # csv dictreader untuk membaca file csv dengan key value dimasukkan ke variable csvReader
        csvReader = csv.DictReader(csvFile)
        # loop untuk membaca setiap baris data dan dimasukkan ke variable row lalu di append ke variable mahasiswa
        for row in csvReader:
            mahasiswa.append(row)

    # jika data mahasiswa ada
    if len(mahasiswa) > 0:
        # cetak judul
        print('---------------------------------------')
        print("List Data Mahasiswa")
        print('---------------------------------------')

        # loop untuk membaca setiap data mahasiswa yang sudah di append ke variable mahasiswa dan dimasukkan ke variable data
        for data in mahasiswa:
            # var column untuk menampung data mahasiswa dengan key value lalu di append ke variable tbody
            column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
            # var column di append( ditambahkan ) ke variable tbody untuk menampung data mahasiswa
            tbody.append(column)

        # cetak table dengan function tabulate dari package tabulate
        print(
            tabulate(
                tbody, # data mahasiswa yang sudah di append ke variable tbody 
                headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], # header table
                tablefmt='grid', # gaya table
                showindex=range(1, len(tbody) + 1) # menampilkan index table dari 1 sampai jumlah data mahasiswa
            )
        )
    else: # jika data mahasiswa tidak ada
        # cetak pesan tidak ada data mahasiswa
        print('-- ALERT ------------------------------')
        print("Data Mahasiswa Belum Ada!")
        print('---------------------------------------')
        
        # lempar ke function dataIsEmpty untuk menambahkan data mahasiswa
        action.dataIsEmpty() 

    # lempar ke function backToMenu untuk kembali ke menu utama
    action.backToMenu() 