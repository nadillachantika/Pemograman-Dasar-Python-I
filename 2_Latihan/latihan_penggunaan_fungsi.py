'''Latihan Fungsi'''

import os

# Library os di Python adalah pustaka standar yang menyediakan berbagai fungsi untuk berinteraksi dengan sistem operasi.
# os.mkdir('folder_baru') 

def header():
    '''fungsi Header'''
    os.system("clear") # untuk membersikan terminal (commend line)
    print(f"{'PROGRAM MENGHITUNG LUAS':^100}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^100}")
    print(f"{'-'*100:^100}")

    
def input_user():
    '''fungsi input user'''
    # Mengambil input user
    lebar = int(input("Masukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")


# Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user() 
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)

    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")
display("coba", '100')