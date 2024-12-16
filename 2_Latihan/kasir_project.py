

def input_user():
    '''Meminta input user'''
    hargaBarang = float(input("Masukkan Harga Barang: "))
    nilaiDiskon = float(input("Masukkan Nilai Diskon (%): "))
    return hargaBarang, nilaiDiskon

def total_harga(hargaBarang, nilaiDiskon):
    '''menghitung total setelah diskon''' 
    return hargaBarang - (hargaBarang * (nilaiDiskon/100))



def main() : 
    while True: #untuk mengulang program
            HARGA,DISKON = input_user()
            RESULT = total_harga(HARGA,DISKON)

            print(f"Total Setelah Diskon: {RESULT}")

            isContinue = input("apakah lanjut?")
            if isContinue == "n":
                break #aplikasi berhenti jika user menginputka "n"
            
      
main()