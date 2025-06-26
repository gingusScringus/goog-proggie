import os
import math
import argparse

# i used argparse as an option if the user wants the decimal number however digits they like it
# so the usage goes something like `python3 ./answer_1.py -f 2` for UNIX or PowerShell
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=int, default=2, help="digits count for decimals")

args = parser.parse_args()

flo = args.f

# function for clearing the terminal, self explanatory
def clearTerminal():
    # it also checks if it's running on Windows (hence "nt"), or else assume UNIX.
    os.system("cls" if os.name == "nt" else "clear")

# superclass and it's ELEVEN subclasses
class BangunDatar():
    def __init__(self, parameter):
        self.parameter = parameter
    def luas(self):
        raise NotImplementedError("luas() unimplemented")
    def keliling(self):
        raise NotImplementedError("keliling() unimplemented")
# 1
class SegitigaSamaSisi(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"]
        }
    def luas(self):
        return self.parameter["sisi"] * self.parameter["sisi"] * math.sqrt(3) / 4
    def keliling(self):
        return 3 * self.parameter["sisi"]
# 2
class SegitigaSikuSiku(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "alas": parameter["alas"],
            "tinggi": parameter["tinggi"]
        }
    def luas(self):
        return 0.5 * self.parameter["alas"] * self.parameter["tinggi"]
    def keliling(self):
        return self.parameter["alas"] + self.parameter["tinggi"] + math.sqrt(self.parameter["alas"]**2 + self.parameter["tinggi"]**2)
# 3
class SegitigaSembarang(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi_a": parameter["sisi_a"],
            "sisi_b": parameter["sisi_b"],
            "sisi_c": parameter["sisi_c"]
        }
    def luas(self):
        s = (self.parameter["sisi_a"] + self.parameter["sisi_b"] + self.parameter["sisi_c"]) / 2
        return math.sqrt(s * (s - self.parameter["sisi_a"]) * (s - self.parameter["sisi_b"]) * (s - self.parameter["sisi_c"]))
    def keliling(self):
        return self.parameter["sisi_a"] + self.parameter["sisi_b"] + self.parameter["sisi_c"]
# 4
class SegitigaSamaKaki(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "alas": parameter["alas"]
        }
    def luas(self):
        return 0.5 * self.parameter["alas"] * math.sqrt(self.parameter["sisi"]**2 - (self.parameter["alas"] / 2)**2)
    def keliling(self):
        return 2 * self.parameter["sisi"] + self.parameter["alas"]
# 5
class Persegi(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
            "sisi": parameter["sisi"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return self.parameter["sisi"] * self.parameter["sisi"]
    
    def keliling(self):
        return 4 * self.parameter["sisi"]
# 6
class PersegiPanjang(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
            "panjang": parameter["panjang"],
            "lebar": parameter["lebar"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return self.parameter["panjang"] * self.parameter["lebar"]
    
    def keliling(self):
        return 2 * (self.parameter["panjang"] + self.parameter["lebar"])
# 7
class Lingkaran(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
            "jari_jari": parameter["jari_jari"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return 3.14 * self.parameter["jari_jari"] * self.parameter["jari_jari"]
    
    def keliling(self):
        return 2 * 3.14 * self.parameter["jari_jari"]
# 8
class Trapesium(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
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
# 9
class BelahKetupat(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
            "sisi": parameter["sisi"],
            "diagonal_1": parameter["diagonal_1"],
            "diagonal_2": parameter["diagonal_2"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return (self.parameter["diagonal_1"] * self.parameter["diagonal_2"]) / 2
    
    def keliling(self):
        return 4 * self.parameter["sisi"]
# 10
class JajarGenjang(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
            "sisi_a": parameter["sisi_a"],
            "sisi_b": parameter["sisi_b"],
            "tinggi": parameter["tinggi"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return self.parameter["sisi_a"] * self.parameter["tinggi"]
    
    def keliling(self):
        return 2 * (self.parameter["sisi_a"] + self.parameter["sisi_b"])
# 11
class LayangLayang(BangunDatar):
    def __init__(self, parameter):
        self.parameter = {
            "sisi_a": parameter["sisi_a"],
            "sisi_b": parameter["sisi_b"],
            "diagonal_1": parameter["diagonal_1"],
            "diagonal_2": parameter["diagonal_2"],
        }
        super().__init__(parameter)
        self.parameter = parameter
    
    def luas(self):
        return (self.parameter["diagonal_1"] * self.parameter["diagonal_2"]) / 2
    
    def keliling(self):
        return 2 * (self.parameter["sisi_a"] + self.parameter["sisi_b"])

# input function replacements
# purpose of these are for substuting the original input functions for a custom one that checks if a value is the correct datatype or not
def inputFloat(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Input bukan angka.")

def inputInt(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Masukkan angka antara {min_value} dan {max_value}.")
                continue
            return value
        except ValueError:
            print("Input bukan bilangan bulat.")
# ex: inputInt("sample text", 0, 10)

def inputString(prompt):
    while True:
        try:
            value = input(prompt).strip().lower()
            if value in ["y", "n"]:
                clearTerminal()
                return value
            else:
                print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        except ValueError:
            print("Pilihan tidak valid.")

# calculation repetition function
def repeatCalculation(calcFunc):
    while True:
        calcFunc()
        repeat = inputString("Hitung ulang bangun datar? (y/n): ")
        if repeat != "y":
            clearTerminal()
            start()
            return

# print the selection
def start():
    clearTerminal()
    print("================= G E O M C A L C (2D) =================")
    print("1. Segitiga (4 jenis)")
    print("2. Persegi")
    print("3. Persegi Panjang")
    print("4. Lingkaran")
    print("5. Trapesium")
    print("6. Belah Ketupat")
    print("7. Jajar Genjang")
    print("8. Layang-Layang")
    print("9. Keluar")

# start the program
start()

while True:
    choice = inputInt("Pilih bangun datar (1-9): ", 1, 9)
    clearTerminal()
    if choice == 9:
        print("Mengeluarkan...")
        break
    elif choice == 1:
        def segitigaSamaSisiCalc():
            print("=== Segitiga Sama Sisi ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            segitiga = SegitigaSamaSisi({"sisi": sisi})
            print(f"Luas: {segitiga.luas():.{flo}f}")
            print(f"Keliling: {segitiga.keliling():.{flo}f}")

        def segitigaSikuSikuCalc():
            print("=== Segitiga Siku-Siku ===")
            alas = inputFloat("Masukkan panjang alas: ")
            tinggi = inputFloat("Masukkan tinggi: ")
            segitiga = SegitigaSikuSiku({"alas": alas, "tinggi": tinggi})
            print(f"Luas: {segitiga.luas():.{flo}f}")
            print(f"Keliling: {segitiga.keliling():.{flo}f}")

        def segitigaSembarangCalc():
            print("=== Segitiga Sembarang ===")
            sisiA = inputFloat("Masukkan panjang sisi a: ")
            sisiB = inputFloat("Masukkan panjang sisi b: ")
            sisiC = inputFloat("Masukkan panjang sisi c: ")
            segitiga = SegitigaSembarang({"sisi_a": sisiA, "sisi_b": sisiB, "sisi_c": sisiC})
            print(f"Luas: {segitiga.luas():.{flo}f}")
            print(f"Keliling: {segitiga.keliling():.{flo}f}")

        def segitigaSamaKakiCalc():
            print("=== Segitiga Sama Kaki ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            alas = inputFloat("Masukkan panjang alas: ")
            segitiga = SegitigaSamaKaki({"sisi": sisi, "alas": alas})
            print(f"Luas: {segitiga.luas():.{flo}f}")
            print(f"Keliling: {segitiga.keliling():.{flo}f}")

        print("============== Segitiga ==============")
        print("1. Segitiga Sama Sisi")
        print("2. Segitiga Siku-Siku")
        print("3. Segitiga Sembarang")
        print("4. Segitiga Sama Kaki")
        print("5. Kembali ke menu utama")
        segitiga_choice = inputInt("Pilih jenis segitiga (1-5): ", 1, 5)
        if segitiga_choice == 1:
            repeatCalculation(segitigaSamaSisiCalc)
        elif segitiga_choice == 2:
            repeatCalculation(segitigaSikuSikuCalc)
        elif segitiga_choice == 3:
            repeatCalculation(segitigaSembarangCalc)
        elif segitiga_choice == 4:
            repeatCalculation(segitigaSamaKakiCalc)
        elif segitiga_choice == 5:
            start()
    elif choice == 2:
        def persegiCalc():
            print("=== Persegi ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            persegi = Persegi({"sisi": sisi})
            print(f"Luas: {persegi.luas():.{flo}f}")
            print(f"Keliling: {persegi.keliling():.{flo}f}")
        repeatCalculation(persegiCalc)
    elif choice == 3:
        def persegiPanjangCalc():
            print("=== Persegi Panjang ===")
            panjang = inputFloat("Masukkan panjang: ")
            lebar = inputFloat("Masukkan lebar: ")
            persegi_panjang = PersegiPanjang({"panjang": panjang, "lebar": lebar})
            print(f"Luas: {persegi_panjang.luas():.{flo}f}")
            print(f"Keliling: {persegi_panjang.keliling():.{flo}f}")
        repeatCalculation(persegiPanjangCalc)
    elif choice == 4:
        def lingkaranCalc():
            print("=== Lingkaran ===")
            jariJari = inputFloat("Masukkan jari-jari: ")
            lingkaran = Lingkaran({"jari_jari": jariJari})
            print(f"Luas: {lingkaran.luas():.{flo}f}")
            print(f"Keliling: {lingkaran.keliling():.{flo}f}")
        repeatCalculation(lingkaranCalc)
    elif choice == 5:
        def trapesiumCalc():
            print("=== Trapesium ===")
            sisiA = inputFloat("Masukkan panjang sisi a: ")
            sisiB = inputFloat("Masukkan panjang sisi b: ")
            tinggi = inputFloat("Masukkan tinggi: ")
            trapesium = Trapesium({"sisi_a": sisiA, "sisi_b": sisiB, "tinggi": tinggi})
            print(f"Luas: {trapesium.luas():.{flo}f}")
            print(f"Keliling: {trapesium.keliling():.{flo}f}")
        repeatCalculation(trapesiumCalc)
    elif choice == 6:
        def belahKetupatCalc():
            print("=== Belah Ketupat ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            diagonal1 = inputFloat("Masukkan panjang diagonal 1: ")
            diagonal2 = inputFloat("Masukkan panjang diagonal 2: ")
            belah_ketupat = BelahKetupat({"sisi": sisi, "diagonal_1": diagonal1, "diagonal_2": diagonal2})
            print(f"Luas: {belah_ketupat.luas():.{flo}f}")
            print(f"Keliling: {belah_ketupat.keliling():.{flo}f}")
        repeatCalculation(belahKetupatCalc)
    elif choice == 7:
        def jajarGenjangCalc():
            print("=== Jajar Genjang ===")
            sisiA = inputFloat("Masukkan panjang sisi a: ")
            sisiB = inputFloat("Masukkan panjang sisi b: ")
            tinggi = inputFloat("Masukkan tinggi: ")
            jajar_genjang = JajarGenjang({"sisi_a": sisiA, "sisi_b": sisiB, "tinggi": tinggi})
            print(f"Luas: {jajar_genjang.luas():.{flo}f}")
            print(f"Keliling: {jajar_genjang.keliling():.{flo}f}")
        repeatCalculation(jajarGenjangCalc)
    elif choice == 8:
        def layangLayangCalc():
            print("=== Layang-Layang ===")
            sisiA = inputFloat("Masukkan panjang sisi a: ")
            sisiB = inputFloat("Masukkan panjang sisi b: ")
            diagonal1 = inputFloat("Masukkan panjang diagonal 1: ")
            diagonal2 = inputFloat("Masukkan panjang diagonal 2: ")
            layang_layang = LayangLayang({"sisi_a": sisiA, "sisi_b": sisiB, "diagonal_1": diagonal1, "diagonal_2": diagonal2})
            print(f"Luas: {layang_layang.luas():.{flo}f}")
            print(f"Keliling: {layang_layang.keliling():.{flo}f}")
        repeatCalculation(layangLayangCalc)
    else:
        # just in case
        raise Exception("Pilihan tidak valid.")
