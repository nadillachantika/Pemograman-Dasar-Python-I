
# while True:
#     pilihan = input("Ingin konversi suhu lagi? (y/n): ")
#     if pilihan == "y":
#        elif pilihan == "n":
#         break
#     else:
#         print("Pilihan tidak valid")

def celcius_to_kelvin(celcius:float) -> float:
   '''FUNGSI MENGHITUNG CELCIUS KE KELVIN'''
   kelvin = celcius + 273 
   return kelvin

def message(hasil):
   print('Hasil konversi suhu adalah', hasil)
   


suhu = input("Ingin konversi suhu ke suhu apa (fahrenheit/kelvin/reamur)? ")
if suhu == "fahrenheit":
   celcius = float(input("Masukkan suhu dalam celcius: "))
   fahrenheit = celcius * 1.8 + 32
   message(fahrenheit)
elif suhu == "kelvin":
   celcius = float(input("Masukkan suhu dalam celcius: "))
   kelvin = celcius_to_kelvin(celcius)
   message(kelvin)
elif suhu == "reamur":
   celcius = float(input("Masukkan suhu dalam celcius: "))
   reamur = celcius * 0.8
   message(reamur)
else:
   print("Pilihan tidak valid")
    

print(f"suhu 24 derjat celcius ke kelvin adalah {celcius_to_kelvin(24)}")

