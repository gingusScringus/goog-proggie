import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

panjangPersegi = int(input("Masukkan panjang persegi: "))
lebarPersegi = int(input("Masukkan lebar persegi: "))

def luasPersegi(panjang, lebar):
    """
    Fungsi untuk menghitung luas persegi panjang
    :param panjang: panjang persegi panjang
    :param lebar: lebar persegi panjang
    :return: luas persegi panjang
    """
    return panjang * lebar
def kelilingPersegi(panjang, lebar):
    """
    Fungsi untuk menghitung keliling persegi panjang
    :param panjang: panjang persegi panjang
    :param lebar: lebar persegi panjang
    :return: keliling persegi panjang
    """
    return 2 * (panjang + lebar)
def main():    
    print("Luas persegi panjang adalah: ", luasPersegi(panjangPersegi, lebarPersegi))
    print("Keliling persegi panjang adalah: ", kelilingPersegi(panjangPersegi, lebarPersegi))
    # Fungsi untuk menghitung luas dan keliling persegi panjang

main()