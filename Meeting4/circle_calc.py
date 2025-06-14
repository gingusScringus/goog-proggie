import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

jjLingkaran = int(input("Masukkan jari-jari lingkaran: "))
pi = 3.14

def hitungLuasLingkaran(jariJari):
    luas = pi * jariJari * jariJari
    return luas
def hitungKelilingLingkaran(jariJari): 
    keliling = 2 * pi * jariJari
    return keliling
def main():
    print("Luas Lingkaran: ", format(hitungLuasLingkaran(jjLingkaran), ',.2f'))
    print("Keliling Lingkaran: ", format(hitungKelilingLingkaran(jjLingkaran), ',.2f'))

main()