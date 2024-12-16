
def input_user():
    '''meminta input user'''
    celcius = float(input("Masukkan suhu dalam celcius: "))
    return celcius

def konversi(celcius):
    '''menghitung konversi suhu'''
    fahrenheit = (9/5 * celcius) + 32
    return fahrenheit


while True: 
    CELCIUS = input_user()
    FAHRENHEIT = konversi(CELCIUS)
    print(f"Suhu dalam fahrenheit: {FAHRENHEIT}F")

    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == "n":
        break