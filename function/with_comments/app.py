# ====== FILE INI UNTUK MENJALANKAN FUNCTION (UTAMA) ====== #

# import function main dari file main.py di folder function
from function.main import main

# __name__ adalah variabel khusus yang akan bernilai __main__ jika file ini dijalankan
# fungsinya adalah untuk memastikan bahwa file ini dijalankan sebagai file utama dan bukan sebagai file yang diimport
if __name__ == '__main__':
    # Me-looping terus menerus sampai user memilih keluar dari menu
    while True:
    # Memanggil function main dari file function.py
        main()