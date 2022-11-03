# ====== FILE INI UNTUK MEMBUAT FUNCTION ====== #

# Mengambil function tabulate dari package tabulate untuk membuat table
from tabulate import tabulate
import csv # mengambil package csv (comma separated values)
import os # mengambil package os (operating system)

# Membuat variable
fileData = 'data.csv'
namaProjek = "CRUDS Mahasiswa"

# function clearscreen ini berfungsi untuk membersihkan layar di terminal, jadi agar tidak spam
def clearScreen():
    # menjalankan perintah cls (jika di Windows) dan clear (jika di Linux dan Unix).
    os.system('cls' if os.name == 'nt' else 'clear')

# Function back to menu ini berfungsi untuk konfirmasi dan kembali ke menu
def backToMenu():
    input("\nSilahkan Tekan ENTER untuk kembali ke Menu")
    main() # balik ke function menu

'''
function confCreateAgain berfungsi untuk mengkonfirmasi apakah ditambah atau tidak, 
nanti ada pilihannya jika y berarti tambah, jika t berarti engga, kembali ke menu
'''
def confCreateAgain():
    print('-- ALERT ------------------------------')
    confirm = input("Apakah kamu mau tambah data lagi? [Y/T]: ").upper()
    print('---------------------------------------')

    if confirm == 'Y': # jika user meng iyakan
        createMahasiswa() # lempar ke function create mahasiswa
    else: # jika tidak atau lainnya
        backToMenu() # panggil function back to menu

# Function exit menu, function ini digunakan untuk keluar dari menu
def exitMenu():
    clearScreen() # panggil function clearscreen

    # membuat input lalu dimasukkan ke dalam var pilihan, dan value inputnya nanti di uppercase(kapital)
    pilihan = input("Apakah kamu yakin akan keluar dari menu? [Y/T]: ").upper()

    if pilihan == 'Y': # ketika user pilih Y maka keluar dari menunya dan loopingnya diberentikan
        exit( # function adalah berguna untuk keluar dari looping, sama halnya break
            '\n---------------------------------------\n' +
            '>> Kamu telah keluar dari Menu! <<\n' +
            '---------------------------------------'
        )
    else: # jika user pilihan selain dari y maka lanjut melooping lagi
        print('\n---------------------------------------')
        print(">> Kamu batal Keluar dari Menu! <<")
        print('---------------------------------------')

        backToMenu() # panggil function back to menu

# Function Main atau Menu
def main():
    clearScreen() # panggil function clearscreen

    # Cetak judul functionnya
    print('---------------------------------------')
    print(f"List Menu | {namaProjek}")
    print('---------------------------------------')

    print(
        # memanggil function tabulate dari file tabulate untuk membuat table
        tabulate( 
            [
                ["Kode", "Nama Menu"], # <-- firstrow
                ["0", "Keluar dari Menu"], # isi tablenya
                ["1", "Menampilkan data Mahasiswa"], # isi tablenya
                ["2", "Mencari data Mahasiswa"], # isi tablenya
                ["3", "Membuat data Mahasiswa"], # isi tablenya
                ["4", "Memperbarui data Mahasiswa"], # isi tablenya
                ["5", "Menghapus data Mahasiswa"], # isi tablenya
            ],
            headers='firstrow', # judul table diambil dari firstrow
            tablefmt='grid' # style tablenya
        )
    )

    print('---------------------------------------')
    menu = int(input("Pilih Kode Menunya: ")) # membuat var menu type input
    print('---------------------------------------')

    """
    Ini adalah logic nya, jadi ketika user memilih 0 maka 
    panggil functionnya sesuai dengan dilist diatas
    """
    if menu == 0: # jika menu 0 maka panggil function exitMenu
        exitMenu() 
    elif menu == 1: # jika menu 1 maka panggil function showMahasiswa
        showMahasiswa()
    elif menu == 2: # jika menu 2 maka panggil function searchMahasiswa
        searchMahasiswa()
    elif menu == 3: # jika menu 3 maka panggil function createMahasiswa
        createMahasiswa()
    elif menu == 4: # jika menu 4 maka panggil function editMahasiswa
        editMahasiswa()
    elif menu == 5: # jika menu 5 maka panggil function deleteMahasiswa
        deleteMahasiswa()
    else: # jika si user pilih selain dari 0 sampai 5, maka kena validasi

        print('\n-- ALERT ------------------------------')
        print("Oops.. Menu Tersebut Tidak Ada!")
        print('---------------------------------------')

        backToMenu() # panggil function back to menu

# function show mahasiswa, function ini digunakan untuk melihat data mahasiswa
def showMahasiswa():
    clearScreen() # panggil function clearscreen

    mahasiswa = [] # membuat var type list
    tbody = [] # membuat var type list

    # Cetak judul functionnya
    print('---------------------------------------')
    print("Data Mahasiswa")
    print('---------------------------------------')

    with open(fileData) as file:
        """
        with ini adalah pernyataan untuk membuka file, jadi with ini seperti try/finally untuk pernyataan
        kesalahan yang digunakan.

        open() adalah function yang dibuat untuk membuka file yg digunakan untuk membaca atau memodifikasi
        file yg dipilih. didalam function ada paramater(suatu nilai untuk dikirimkan ke dalam fungsi), 
        yaitu var file data yg isinya file csvnya

        dan as ini adalah alias, jadi function open tadi dimasukkan var alias file
        """

        fileReader = csv.reader(file, delimiter=",")
        '''
        function reader dalam csv ini adalah untuk membaca file dari file csvnya
        dan param pertama itu adalah file csvnya, kedua delimiter yaitu pembatas untuk memisahkan string teks
        '''
        # loop dari var file reader
        for row in fileReader:
            mahasiswa.append(row) # var row yg isinya adalah file csv dimasukkan ke dalam var mahasiswa

        # Pengecekan
        if len(mahasiswa) > 0: # Jika ada datanya
            '''
            pop ini berfungsi mengapus list dari urutan yg kamu pilih, pop ini dimulai dari urutan 0
            berarti kita akan menghapus judul tablenya
            '''
            thead = mahasiswa.pop(0)

            for data in mahasiswa: # looping dari var mahasiswa type list masukkan ke dalam var data
                tbody.append(data) # var data dimasukkan ke var tbody

            print(
                # memanggil function tabulate dari file tabulate untuk membuat table
                tabulate(
                    tbody, # isi table nya
                    headers=thead, # header tablenya
                    tablefmt='grid', # gaya tablenya
                    showindex=range(1, len(tbody) + 1) # nomer indeksnya 1 sampai seterusnya
                )
            )
        else: # Jika tidak ada datanya
            print(">> Data mahasiswa belum ada! <<")
            print('---------------------------------------')

    backToMenu() # panggil function back to menu

# Function search mahasiswa, function digunakan mencari data mahasiswa dengan kunci nim mahasiswa.
def searchMahasiswa():
    clearScreen() # panggil function clearscreen

    mahasiswa = [] # var type list

    """
    - with ini adalah pernyataan untuk membuka file, jadi with ini seperti try/finally untuk pernyataan
    kesalahan yang digunakan.

    - open() adalah function yang dibuat untuk membuka file yg digunakan untuk membaca atau memodifikasi
    file yg dipilih. didalam function ada paramater(suatu nilai untuk dikirimkan ke dalam fungsi), 
    param pertama file data yaitu file csvnya, dan yang kedua ada mode='r' yaitu (read) cuma membaca aja tidak bisa di edit,

    dan as ini adalah alias, jadi function open tadi dimasukkan var alias file
    """
    with open(fileData, mode='r') as file:
        """
        csv (Comma Separated Values) adalah format impor dan ekspor yang paling umum untuk database.
        yaa ini seperti non database, tidak seperti sql dan lain2.

        DictReader ini adalah function untuk membaca data dari function csv yg diambil dari file csv.
        nah didalam function, ada paramnya, yaitu file yg berisi dari file csv nya
        """
        fileReader = csv.DictReader(file)

        for row in fileReader:
            mahasiswa.append(row) # var row yg isinya adalah file csv dimasukkan ke dalam var mahasiswa

    nim = input("Cari mahasiswa berdasarkan NIM: ") # inputan data NIM
    dataFound = [] # ini berfungsi jika data ada maka akan dimasukkan ke var data found

    i = 0 # index adalah 0
    for data in mahasiswa: # loop
        if data['NIM'] == nim: # jika ada data nim yg sama seperti inputan nim
            dataFound = mahasiswa[i] # i ini adalah index. data mahasiswa yg berindex dimasukkan ke var data found yg typenya list
        i = i + 1 # berfungsi untuk meloop sampai dia ketemu data nim nya yg sama seperti inputan nim

    if len(dataFound) > 0: # Jika data ditemukan
        # cetak hasil
        print('---------------------------------------')
        print(f"Data Mahasiswa dengan NIM {nim} Ditemukan!")
        print('---------------------------------------')
        print(
            tabulate( # memanggil function tabulate dari file tabulate untuk membuat table
                [
                    ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], # firstrow(header table)
                    [   # data yang dicari
                        dataFound['Nama'],
                        dataFound['NIM'],
                        dataFound['Jurusan'],
                        dataFound['Prodi'],
                        dataFound['Kelas']
                    ]
                ],
                headers='firstrow', # header diambil firstrow
                tablefmt='grid', # style tablenya
            )
        )
    else: # jika tidak ada datanya
        print(">> Data tidak ditemukan! <<")
        print('---------------------------------------')

    backToMenu() # panggil function back to menu

# function create mahasiswa, function ini untuk membuat data mahasiswa baru
def createMahasiswa():
    clearScreen() # panggil function clearscreen

    mahasiswa = [] # membuat var type list agar nanti dimasukkan data dari file csvnya

    """
    - with ini adalah pernyataan untuk membuka file, jadi with ini seperti try/finally untuk pernyataan
    kesalahan yang digunakan.

    - open() adalah function yang dibuat untuk membuka file yg digunakan untuk membaca atau memodifikasi
    file yg dipilih. didalam function ada paramater(suatu nilai untuk dikirimkan ke dalam fungsi), 
    param pertama file data yaitu file csvnya, dan yang kedua ada mode='r' yaitu (read) cuma membaca aja tidak bisa di edit,

    dan as ini adalah alias, jadi function open tadi dimasukkan var alias file
    """
    with open(fileData, mode='r') as file:
        """
        csv (Comma Separated Values) adalah format impor dan ekspor yang paling umum untuk database.
        yaa ini seperti non database, tidak seperti sql dan lain2.

        DictReader ini adalah function untuk membaca data dari function csv yg diambil dari file csv.
        nah didalam function, ada paramnya, yaitu file yg berisi dari file csv nya
        """
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row) # var row yg isinya adalah file csv dimasukkan ke dalam var mahasiswa

    """
    - with ini adalah pernyataan untuk membuka file, jadi with ini seperti try/finally untuk pernyataan
    kesalahan yang digunakan.

    - open() adalah function yang dibuat untuk membuka file yg digunakan untuk membaca atau memodifikasi
    file yg dipilih. didalam function ada paramater(suatu nilai untuk dikirimkan ke dalam fungsi), 
    param pertama file data yaitu file csvnya, dan yang kedua ada mode='a' yaitu (append) Membuat file baru jika tidak ada, 
    seperti function append() mengisi data urutan terakhir
    dan ketiga newline, jadi ketika kita sudah membuat data baru maka data tersebut langsung ke bawah (newline "\n")

    dan as ini adalah alias, jadi function open tadi dimasukkan var alias file
    """
    with open(fileData, mode='a', newline='') as file:
        fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'] # judul header yg dimasukkan ke var fieldnames

        """
        csv (Comma Separated Values) adalah format impor dan ekspor yang paling umum untuk database.
        yaa ini seperti non database, tidak seperti sql dan lain2.

        DictWriter ini adalah function untuk membuat/menulis(writer) data dari function csv yg diambil dari file csv.
        nah didalam function ada paramnya, yg pertama: file yaitu file csv nya dan yg
        kedua fieldnames yaitu judul dari fieldnya/isinya
        """
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Cetak judul functionnya
        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')

        # SEGMENT FORM 1, ADA ALERTNYA UNTUK KELUAR DARI FORM
        print('-- FORM -------------------------------')
        # inputan untuk nim
        nim = input('NOTE: ketik "0" untuk keluar dari form.\n\nMasukkan NIM Mahasiswa: ')

        clearScreen() # clear screnn

        # SEGMENT FORM 2, MENGHAPUS ALERT KELUAR DARI FORM, JIKA SUDAH SELESAI DARI INPUTAN NIM
        print('---------------------------------------')
        print("Membuat Data Mahasiswa")
        print('---------------------------------------')

        print('-- FORM -------------------------------')
        print("Masukkan NIM Mahasiswa:", nim)

        # looping data mahasiswa
        for data in mahasiswa:
            # validasi, jika nimnya adalah angka
            if nim.isdigit():
                # validasi, jika nimnya sudah ada(unique)
                if data['NIM'] == nim:
                    print('\n-- WARNING ----------------------------')
                    input(
                        f"NIM Mahasiswa tersebut sudah ada!\n" + 
                        "---------------------------------------\n" +
                        "\n>> Tekan ENTER untuk Mengulangi <<"
                    )
                    print('---------------------------------------')

                    createMahasiswa() # lempar ke function create mahasiswa
            else: # jika nimnya bukanlah angka
                print('\n-- WARNING ----------------------------')
                input(
                    f"Inputan NIM harus menggunakan Angka!\n" + 
                    "---------------------------------------\n" +
                    "\n>> Tekan ENTER untuk Mengulangi <<"
                )
                print('---------------------------------------')

                createMahasiswa() # lempar ke function create mahasiswa
        
        # jika user ketik batal maka batal isi form
        if nim == '0':
            print('\n-- ALERT ------------------------------')
            print("Kamu Batal Mengisi Form!")
            print('---------------------------------------')

            backToMenu() # lempat ke function back to menu

        # membuat file inputan
        nama = input("Masukkan Nama Mahasiswa: ")
        jurusan = input("Masukkan Jurusan Mahasiswa: ")
        prodi = input("Masukkan Program Studi Mahasiswa: ")
        kelas = input("Masukkan Kelas Mahasiswa: ").upper() # mengasih upper string
        print('---------------------------------------')

        if mahasiswa == []: # Jika data mahasiswa kosong maka buat header data
            writer.writeheader() # buat header data

        # membuat data dari var inputan tadi dan disimpan ke file data.csv
        writer.writerow({ 
            'Nama': nama,
            'NIM': nim,
            'Jurusan': jurusan,
            'Prodi': prodi,
            'Kelas': kelas
        })

        # cetak message kalo udah disimpan
        print('-- ALERT ------------------------------')
        print(">> Data Mahasiswa berhasil disimpan! <<")
        print('---------------------------------------')

    confCreateAgain() # lempar ke function createagain

# function edit mahasiswa, function ini digunakan untuk mengedit data mahasiswa.
def editMahasiswa():
    clearScreen() # membersihkan terminal, jadi fokus ke edit mahasiswa

    # Cetak title untuk function edit mahasiswa
    print('---------------------------------------')
    print("Mengedit data mahasiswa")
    print('---------------------------------------')

    # membuat variable type list
    mahasiswa = []
    tbody = []
    dataFound = []

     # membuka file csv dengan mode read
    with open(fileData, mode='r') as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            mahasiswa.append(row) # data yg di csv dimasukkan ke var mahasiswa

    for data in mahasiswa: # melooping lagi data dari var mahasiswa
        # datanya mahasiswa dengan setiap key, dimasukkan ke var column
        column = data['Nama'], data['NIM'], data['Jurusan'], data['Prodi'], data['Kelas']
        tbody.append(column) # var column dimasukkan ke dalam var tbody

    print(
        # cetak list data mahasiswa dengan membuat table dari tabulate
        tabulate(
            tbody, # isi table
            headers=['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'], # headers
            tablefmt='grid', # style tablenya
            showindex=range(1, len(mahasiswa) + 1) # kasih nomernya
        )
    )

    print('---------------------------------------')
    nim = input("Pilih NIM Mahasiswa: ")
    print('---------------------------------------')

    i = 0
    for data in mahasiswa: # looping
        if nim.isdigit(): # kondisi, jika inputan adalah digit.
            if data['NIM'] == nim: # jika data sesuai dengan input nim
                dataFound = mahasiswa[i]
        else: # jika inputan bukan digit, maka kasih pesan.
            print('\n-- WARNING ----------------------------')
            input(
                f"Inputan NIM harus menggunakan Angka!\n" + 
                "---------------------------------------\n" +
                "\n>> Tekan ENTER untuk Mengulangi <<"
            )
            print('---------------------------------------')

            editMahasiswa() # lempar ke function edit mahasiswa
        i = i + 1 # mengulang terus sampe ketemu sesuai nim yg dicari

    # kondisi, Jika data tidak ada, maka harus ngulang lagi
    if not len(dataFound) > 0:
        print('\n-- WARNING ----------------------------')
        input(
            f"NIM Tidak ditemukan\n" + 
            "---------------------------------------\n" +
            "\n>> Tekan ENTER untuk Mengulangi <<"
        )
        print('---------------------------------------')

        editMahasiswa() # lempar ke function edit mahasiswa
    
    print('-- FORM -------------------------------')
    # Membuat var type input, untuk mengganti data baru
    nama = input("Masukkan Nama baru Mahasiswa: ")
    jurusan = input("Masukkan Jurusan baru Mahasiswa: ")
    prodi = input("Masukkan Program Studi baru Mahasiswa: ")
    kelas = input("Masukkan Kelas baru Mahasiswa: ").upper()
    print('---------------------------------------')
        
    i = 0
    for data in mahasiswa: # looping
        if data['NIM'] == nim: # jika data nim sama seperti input var nim
            # Proses mengedit data lama jadi data yg baru
            # [i] adalah index, si doi ini akan terus mencari datanya sampe ketemu sama nim yg diinputkan
            # setelah [i] adalah keynya atau header tablenya
            # --------------------------------------
            if len(nama) == 0: # jika inputan kosong, maka biarkan saja
                mahasiswa[i]['Nama']
            else: # jika ada, maka replace data lama jadi baru
                mahasiswa[i]['Nama'] = nama
            # --------------------------------------
            if len(jurusan) == 0: # jika inputan kosong, maka biarkan saja
                mahasiswa[i]['Jurusan']
            else: # jika ada, maka replace data lama jadi baru
                mahasiswa[i]['Jurusan'] = jurusan
            # --------------------------------------
            if len(prodi) == 0: # jika inputan kosong, maka biarkan saja
                mahasiswa[i]['Prodi']
            else: # jika ada, maka replace data lama jadi baru
                mahasiswa[i]['Prodi'] = prodi
            # --------------------------------------
            if len(kelas) == 0: # jika inputan kosong, maka biarkan saja
                mahasiswa[i]['Kelas']
            else: # jika ada, maka replace data lama jadi baru
                mahasiswa[i]['Kelas'] = kelas
            # --------------------------------------
        i = i + 1 # mengulang terus sampe ketemu sesuai nim yg dicari

    """Proses masukkan data ke file csv
    Pertama membuka filenya csv dulu dengan function open() yg paramnya berisi:
    1. file csv-nya
    2. modenya, mode w berarti writing, jadi ketika data ada maka hapus data lama, sebaliknya jika tidak ada data maka buat baru.
    3. newline(baris baru), berarti ketika file sudah di update maka otomatis ke baris yg baru(kebawah), 
    """
    with open(fileData, mode='w', newline='') as csvFile:
        fieldnames = ['Nama', 'NIM', 'Jurusan', 'Prodi', 'Kelas'] # key atau judul
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames) # membuat var writer dengan berfungsi untuk membuat/menulis(writer) data file csv.
        writer.writeheader() # membuat/menulis header
        for newData in mahasiswa: # loop data mahasiswa lalu dimasukkan ke var newdata
            writer.writerow({
                # disinilah insert data ke file csvnya, yg pertama ada key-nya, lalu diisi dengan data isinya
                'Nama': newData['Nama'],
                'NIM': newData['NIM'],
                'Jurusan': newData['Jurusan'],
                'Prodi': newData['Prodi'],
                'Kelas': newData['Kelas']
            })
    # cetak pesan jika data sudah disimpan
    print('---------------------------------------')
    print(">> Data baru dari NIM", nim, "Berhasil diperbarui! <<")
    print('---------------------------------------')

    backToMenu() # lempar ke back to menu

def deleteMahasiswa():
    clearScreen() # panggil function clearscreen

    mahasiswa = []
    tbody = []

    with open(fileData, mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            mahasiswa.append(row)

    print('---------------------------------------')
    print("Menghapus data mahasiswa")
    print('---------------------------------------')

    if len(mahasiswa) > 0:
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
                # REMOVE DATA DISINI
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

        print('-- ALERT ------------------------------')
        print(">> DATA BERHASIL DIHAPUS <<")
        print('---------------------------------------')
    else:
        print(">> Data tidak ditemukan! <<")
        print('---------------------------------------')

    backToMenu() # panggil function back to menu
