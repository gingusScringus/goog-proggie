import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

def luasBD(bangun, pmBangun):
    luas = 0
    pi = 3.14
    if bangun == "persegi":
        if "sisi" in pmBangun:
            luas = pmBangun["sisi"] * pmBangun["sisi"]
        else:
            return "sisi tidak ada"
    elif bangun == "lingkaran":
        if "jariJari" in pmBangun:
            luas = pi * pmBangun["jariJari"] * pmBangun["jariJari"]
        else:
            return "jari-jari tidak ada"
    else:
        return "tidak ada bangun yang dipilih"
    return luas
def kelilingBD(bangun, pmBangun):
    keliling = 0
    pi = 3.14
    if bangun == "persegi":
        if "sisi" in pmBangun:
            keliling = 4 * pmBangun["sisi"]
        else:
            return "sisi tidak ada"
    elif bangun == "lingkaran":
        if "jariJari" in pmBangun:
            keliling = 2 * pi * pmBangun["jariJari"]
        else:
            return "jari-jari tidak ada"
    else:
        return "tidak ada bangun yang dipilih"
    return keliling

bangunPilihan = input("mau hitung bangun apa? (persegi/lingkaran/persegi panjang): ")


