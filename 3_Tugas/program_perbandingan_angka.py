while True: 
    pilihan = input("Ingin input angka lagi?: ")
    if pilihan == "y":
        angka_pertama = int(input("Masukkan angka pertama: "))
        angka_kedua = int(input("Masukkan angka kedua: "))

        if angka_pertama > angka_kedua:
            print("Angka pertama lebih besar dari angka kedua")
        elif angka_pertama < angka_kedua:
            print("Angka pertama lebih kecil dari angka kedua")
        else:
            print("Angka pertama sama dengan angka kedua")
    elif pilihan == "n":
        break
    else:
        print("Pilihan tidak valid")