# ====== FILE INI UNTUK FUNCTION SHOW MAHASISWA ====== #

from tabulate import tabulate # mengambil function tabulate dari package tabulate untuk membuat table
# mengambil semua function dari file action.py di folder function dan kasih aliasn action
import function.action as action
import csv # mengambil package csv (comma separated values)

fileData = 'assets/data.csv'

def showMahasiswa():
    action.clearScreen() 

    mahasiswa = [] 
    tbody = [] 

    with open(fileData) as file:
        fileReader = csv.reader(file, delimiter=",")
        
        for row in fileReader:
            mahasiswa.append(row) 

        if len(mahasiswa) > 0: 
            
            print('---------------------------------------')
            print("List Data Mahasiswa")
            print('---------------------------------------')

            thead = mahasiswa.pop(0)

            for data in mahasiswa: 
                tbody.append(data) 

            print(
                tabulate(
                    tbody, 
                    headers=thead, 
                    tablefmt='grid', 
                    showindex=range(1, len(tbody) + 1) 
                )
            )
        else: 
            print('-- ALERT ------------------------------')
            print("Data Mahasiswa Belum Ada!")
            print('---------------------------------------')
            
            action.dataIsEmpty() 

    action.backToMenu() 