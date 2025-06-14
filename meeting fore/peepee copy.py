import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

jjLingkaran = int(input("Masukkan jari-jari lingkaran: "))
pi = 3.14

def Lingkaran(jariJari):
    luas = pi * jariJari * jariJari
    keliling = 2 * pi * jariJari
    hasil = {
        'luas': luas,
        'keliling': keliling
    }
    return hasil

hasilLingkaran = Lingkaran(jjLingkaran)
print("Luas Lingkaran: ", format(hasilLingkaran["luas"], ',.2f'))
print("Keliling Lingkaran: ", format(hasilLingkaran["keliling"], ',.2f'))
