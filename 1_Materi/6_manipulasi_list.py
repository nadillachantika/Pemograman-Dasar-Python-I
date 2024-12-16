'''Macam teknik manipulasi list'''

# Mengakses Elemen didalam list
buah = ["apel", "jeruk", "mangga", "pisang"]

print(buah[0])  # Output: apel
print(buah[2])  # Output: mangga
print(buah[-1]) # Output: pisang # Index terakhir





''' Menambahkan elemen ke dalam list'''
# Append
buah.append("jambu")
print(buah)  # Output: ['apel', 'jeruk', 'mangga', 'pisang', 'jambu']

# Insert
buah.insert(1, "kiwi")  # Menambahkan elemen "kiwi" pada index ke-1

# Extend
buah_lain = ["melon", "anggur"]
buah.extend(buah_lain)  # Menggabungkan list buah_lain ke dalam list buah





''' Menghapus elemen didalam list '''
# Remove
buah.remove("jeruk")  # Menghapus elemen "jeruk" dari list buah

# Pop
buah.pop()  # Menghapus elemen terakhir dari list buah

# Clear
buah.clear()  # Menghapus semua elemen dari list buah




'''Mengetahui Panjang List'''
# Len
panjang_list = len(buah)



'''Menggabungkan List'''
# Menggabungkan
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
combined_list = list_1 + list_2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]


# Membagi list
print(combined_list[2:5])  # Output: [3, 4, 5]




'''Mencari Elemen dalam List'''
# Menggunakan in
buah = ["apel", "jeruk", "mangga", "pisang"]
print("jeruk" in buah)  # Output: True

#  Menemukan indeks dari elemen
buah = ["apel", "jeruk", "mangga", "pisang"]
print(buah.index("mangga"))  # Output: 2



'''Looping melalui List'''
buah = ["apel", "jeruk", "mangga", "pisang"]
for buah in buah:
    print(buah)