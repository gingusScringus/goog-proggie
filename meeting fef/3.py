import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

# polymorphism

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
        return (self.parameter["sisi_a"] + self.parameter["sisi_b"]) /2 * self.parameter["tinggi"]
    
    def keliling(self):
        return self.parameter["sisi_a"] + self.parameter["sisi_b"] + 2 * self.parameter["tinggi"]

# contoh penggunaan
print("=== Bangun Datar ===")

print("=== Persegi Panjang ===")
persegiPanjank = PersegiPanjang({"panjang": 10, "lebar": 5})
print("luas: ", persegiPanjank.luas())
print("keliling: ", persegiPanjank.keliling())

print("=== Persegi ===")
persegi = Persegi({"sisi": 5})
print("luas: ", persegi.luas())
print("keliling: ", persegi.keliling())

print("=== Lingkaran ===")
lingkaran = Lingkaran({"jari_jari": 7})
print("luas: ", lingkaran.luas())
print("keliling: ", lingkaran.keliling())

print("=== Trapesium ===")
trapesium = Trapesium({"sisi_a": 5, "sisi_b": 10, "tinggi": 4})
print("luas: ", trapesium.luas())
print("keliling: ", trapesium.keliling())


