'''
# Fungsi

def nama_fungsi(parameter):
    # Blok kode fungsi
    
'''


#  Fungsi dengan Argument
def salam(nama):
    print("Halo", nama)
    

def hitung_keliling_persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    print("Keliling persegi panjang:", keliling)
   
    
# Fungsi dengan Kembalian(Return)
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def tambah(a, b):
    return a + b


# Fungsi dengan Default Argument

def salam(nama, salam="Halo"):
    print(salam, nama)  
    
def hitung_harga_setelah_diskon(harga, diskon=0):
    harga_diskon = harga - (harga * diskon / 100)
    return harga_diskon
