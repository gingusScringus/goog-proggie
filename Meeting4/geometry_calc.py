import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

bangunPilihan = input("mau hitung bangun apa? (persegi/lingkaran/persegi panjang): ")

def luasBD(bangun, sisi, jariJari):
    pi = 3.14
    if bangun == "persegi":
        luas = sisi * sisi
    elif bangun == "lingkaran":
        luas = pi * jariJari * jariJari
    else:
        return "RUSAK"
    
    return luas

def kelilingBD(bangun, sisi, jariJari):
    pi = 3.14
    if bangun == "persegi":
        keliling = 4 * sisi
    elif bangun == "lingkaran":
        keliling = 2 * pi * jariJari
    else:
        return "RUSAK"
    
    return keliling

if bangunPilihan == "persegi":
    sisiPersegi = int(input("Masukkan sisi persegi: "))
    print("Luas Persegi: ", luasBD(bangunPilihan, sisiPersegi, 0))
    print("Keliling Persegi: ", kelilingBD(bangunPilihan, sisiPersegi, 0))
elif bangunPilihan == "lingkaran":
    jariJariLingkaran = int(input("Masukkan jari-jari lingkaran: "))
    print("Luas Lingkaran: ", luasBD(bangunPilihan, 0, jariJariLingkaran))
    print("Keliling Lingkaran: ", kelilingBD(bangunPilihan, 0, jariJariLingkaran))
else:
    print("zonk")