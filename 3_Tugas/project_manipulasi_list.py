# Membuat function untuk setiap operasi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak dapat dibagi dengan 0"
    return a / b


# Membuat kalkulator    
def kalkulator():
    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator!")
            break

        # Meminta input angka dari pengguna
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar!")
            continue

        # Melakukan operasi sesuai pilihan
        if pilihan == '1':
            print(f"Hasil penjumlahan: {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil pengurangan: {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil perkalian: {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil pembagian: {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Menjalankan kalkulator
kalkulator()
