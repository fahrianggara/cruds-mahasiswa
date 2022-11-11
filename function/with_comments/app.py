# ====== FILE INI UNTUK MENJALANKAN FUNCTION ====== #

# import function main dari file function.py
from function.main import main

# __name__ adalah variabel yang berisi nama dari file yang sedang dijalankan
# __main__ adalah nama dari file yang sedang dijalankan
# jadi jika __name__ sama dengan __main__ maka jalankan function main
if __name__ == '__main__':
    # Me-looping terus sampe ketemu angka 0
    while True:
    # Memanggil function main dari file function.py
        main()