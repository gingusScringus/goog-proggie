import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

sisiPersegi = int(input("Masukkan sisi persegi: "))

def luasPersegi(sisi):
    """
    Fungsi untuk menghitung luas persegi
    :param sisi: panjang sisi persegi
    :return: luas persegi
    """
    return sisi * sisi

def kelilingPersegi(sisi):
    """
    Fungsi untuk menghitung keliling persegi
    :param sisi: panjang sisi persegi
    :return: keliling persegi
    """
    return 4 * sisi

def main():
    """
    Fungsi utama untuk menjalankan program
    """
    print("Luas Persegi: ", luasPersegi(sisiPersegi))
    print("Keliling Persegi: ", kelilingPersegi(sisiPersegi))

main()