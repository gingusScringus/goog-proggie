import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

class Mobil:
    def __init__ (self, merk, jenismesin):
        self.merk = merk
        self.jenismesin = jenismesin

    def jalan(self):
        return "gaskan"
    
    def rem(self):
        return "rem woi"
class SUV(Mobil):
    def __init__(self, merk, jenismesin, jumlahpintu):
        Mobil.__init__(self, merk, jenismesin)
        self.merk = merk
        self.jenismesin = jenismesin
        self.jumlahpintu = jumlahpintu

    def jalan(self):
        return "rem dulu baru jalan"

mobil_biasa = Mobil("Toyota", "Bensin")
print(mobil_biasa.jalan())

mobil_suv = SUV("Daihatsu", "Diesel", 5)
print(mobil_suv.jalan())
print(mobil_suv.rem())