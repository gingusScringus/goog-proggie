import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

# polymorphism (now wit input)

class BangunDatar():
    def __init__(self, parameter):
        self.parameter = parameter
    def luas(self):
        return "hitung luas"
    def keliling(self):
        return 4 * "hitung keliling"
class PersegiPanjang(BangunDatar):
    def __init__(self, parameter):
        parameter = {
            "panjang": parameter["panjang"],
            "lebar": parameter["lebar"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return self.parameter["panjang"] * self.parameter["lebar"]
    
    def keliling(self):
        return 2 * (self.parameter["panjang"] + self.parameter["lebar"])
    
class Persegi(BangunDatar):
    def __init__(self, parameter):
        parameter = {
            "sisi": parameter["sisi"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return self.parameter["sisi"] * self.parameter["sisi"]
    
    def keliling(self):
        return 4 * self.parameter["sisi"]
class Lingkaran(BangunDatar):
    def __init__(self, parameter):
        parameter = {
            "jari_jari": parameter["jari_jari"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return 3.14 * self.parameter["jari_jari"] * self.parameter["jari_jari"]
    
    def keliling(self):
        return 2 * 3.14 * self.parameter["jari_jari"]
class Trapesium(BangunDatar):
    def __init__(self, parameter):
        parameter = {
            "sisi_a": parameter["sisi_a"],
            "sisi_b": parameter["sisi_b"],
            "tinggi": parameter["tinggi"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return (self.parameter["sisi_a"] + self.parameter["sisi_b"]) / 2  * self.parameter["tinggi"]
    
    def keliling(self):
        return self.parameter["sisi_a"] + self.parameter["sisi_b"] + 2 * self.parameter["tinggi"]

# contoh penggunaan
print("Bangun Datar")

print("=== Persegi Panjang ===")
input_panjang = int(input("Masukkan panjang: "))
input_lebar = int(input("Masukkan lebar: "))
persegi_panjang = PersegiPanjang({"panjang": input_panjang, "lebar": input_lebar})
print("Luas Persegi Panjang:", persegi_panjang.luas())
print("Keliling Persegi Panjang:", persegi_panjang.keliling())

print("=== Persegi ===")
input_sisi = int(input("Masukkan sisi: "))
persegi = Persegi({"sisi": input_sisi})
print("Luas Persegi:", persegi.luas())
print("Keliling Persegi:", persegi.keliling())

print("=== Lingkaran ===")
input_jari_jari = int(input("Masukkan jari-jari: "))
lingkaran = Lingkaran({"jari_jari": input_jari_jari})
print("Luas Lingkaran:", lingkaran.luas())
print("Keliling Lingkaran:", lingkaran.keliling())

print("=== Trapesium ===")
input_sisi_a = int(input("Masukkan sisi a: "))
input_sisi_b = int(input("Masukkan sisi b: "))
input_tinggi = int(input("Masukkan tinggi: "))
trapesium = Trapesium({"sisi_a": input_sisi_a, "sisi_b": input_sisi_b, "tinggi": input_tinggi})
print("Luas Trapesium:", trapesium.luas())
print("Keliling Trapesium:", trapesium.keliling())

