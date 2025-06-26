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

# superclass and it's n subclasses
class BangunDatar():
    def __init__(self, parameter):
        self.parameter = parameter
    def volume(self):
        raise NotImplementedError("volume() unimplemented")

# 1
class LimasSegitiga(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "alas": parameter["alas"],
            "tinggi_alas": parameter["tinggi_alas"],
            "tinggi_limas": parameter["tinggi_limas"]
        }

    def volume(self):
        luas_alas = self.parameter["alas"] * self.parameter["tinggi_alas"] / 2
        return luas_alas * self.parameter["tinggi_limas"] / 3
# 2
class LimasSegiempat(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "tinggi_limas": parameter["tinggi_limas"]
        }

    def volume(self):
        luas_alas = self.parameter["sisi"] ** 2
        return luas_alas * self.parameter["tinggi_limas"] / 3
# 3
class LimasSegilima(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "tinggi_limas": parameter["tinggi_limas"]
        }

    def volume(self):
        luas_alas = (5 * self.parameter["sisi"] ** 2) / (4 * math.tan(math.pi / 5))
        return luas_alas * self.parameter["tinggi_limas"] / 3
# 4
class LimasSegienam(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "tinggi_limas": parameter["tinggi_limas"]
        }

    def volume(self):
        luas_alas = (3 * math.sqrt(3) * self.parameter["sisi"] ** 2) / 2
        return luas_alas * self.parameter["tinggi_limas"] / 3
# 5
class PrismaSegitiga(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "alas": parameter["alas"],
            "tinggi_alas": parameter["tinggi_alas"],
            "tinggi_prisma": parameter["tinggi_prisma"]
        }

    def volume(self):
        luas_alas = self.parameter["alas"] * self.parameter["tinggi_alas"] / 2
        return luas_alas * self.parameter["tinggi_prisma"]
# 6
class PrismaSegiempat(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "tinggi_prisma": parameter["tinggi_prisma"]
        }

    def volume(self):
        luas_alas = self.parameter["sisi"] ** 2
        return luas_alas * self.parameter["tinggi_prisma"]
# 7
class PrismaSegilima(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "tinggi_prisma": parameter["tinggi_prisma"]
        }

    def volume(self):
        luas_alas = (5 * self.parameter["sisi"] ** 2) / (4 * math.tan(math.pi / 5))
        return luas_alas * self.parameter["tinggi_prisma"]
# 8
class PrismaSegienam(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"],
            "tinggi_prisma": parameter["tinggi_prisma"]
        }

    def volume(self):
        luas_alas = (3 * math.sqrt(3) * self.parameter["sisi"] ** 2) / 2
        return luas_alas * self.parameter["tinggi_prisma"]
# 9
class Kubus(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "sisi": parameter["sisi"]
        }

    def volume(self):
        return self.parameter["sisi"] ** 3
# 10
class Balok(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "panjang": parameter["panjang"],
            "lebar": parameter["lebar"],
            "tinggi": parameter["tinggi"]
        }

    def volume(self):
        return self.parameter["panjang"] * self.parameter["lebar"] * self.parameter["tinggi"]
# 11
class Bola(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "jari_jari": parameter["jari_jari"]
        }

    def volume(self):
        return (4/3) * math.pi * self.parameter["jari_jari"] ** 3
# 12
class Kerucut(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "jari_jari": parameter["jari_jari"],
            "tinggi": parameter["tinggi"]
        }

    def volume(self):
        return (1/3) * math.pi * self.parameter["jari_jari"] ** 2 * self.parameter["tinggi"]
# 13
class Tabung(BangunDatar):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.parameter = {
            "jari_jari": parameter["jari_jari"],
            "tinggi": parameter["tinggi"]
        }

    def volume(self):
        return math.pi * self.parameter["jari_jari"] ** 2 * self.parameter["tinggi"]


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
    print("================= G E O M C A L C (3D) =================")
    print("1. Limas (4 jenis)")
    print("2. Prisma (4 jenis)")
    print("3. Kubus")
    print("4. Balok")
    print("5. Bola")
    print("6. Kerucut")
    print("7. Tabung")
    print("8. Keluar")

# start the program
start()

while True:
    choice = inputInt("Pilih bangun datar (1-8): ", 1, 8)
    clearTerminal()
    # this used to be 0 but revised to the last count because idk less confusion ig
    if choice == 8:
        print("Mengeluarkan...")
        break
    elif choice == 1:
        def LimasSegitigaCalc():
            print("=== Limas Segitiga ===")
            alas = inputFloat("Masukkan panjang alas segitiga: ")
            tinggi_alas = inputFloat("Masukkan tinggi segitiga: ")
            tinggi_limas = inputFloat("Masukkan tinggi limas: ")
            limas = LimasSegitiga({"alas": alas, "tinggi_alas": tinggi_alas, "tinggi_limas": tinggi_limas})
            print(f"Volume Limas Segitiga: {limas.volume():.{flo}f}")
        def LimasSegiempatCalc():
            print("=== Limas Segiempat ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            tinggi_limas = inputFloat("Masukkan tinggi limas: ")
            limas = LimasSegiempat({"sisi": sisi, "tinggi_limas": tinggi_limas})
            print(f"Volume Limas Segiempat: {limas.volume():.{flo}f}")
        def LimasSegilimaCalc():
            print("== Limas Segilima ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            tinggi_limas = inputFloat("Masukkan tinggi limas: ")
            limas = LimasSegilima({"sisi": sisi, "tinggi_limas": tinggi_limas})
            print(f"Volume Limas Segilima: {limas.volume():.{flo}f}")
        def LimasSegienamCalc():
            print("=== Limas Segienam ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            tinggi_limas = inputFloat("Masukkan tinggi limas: ")
            limas = LimasSegienam({"sisi": sisi, "tinggi_limas": tinggi_limas})
            print(f"Volume Limas Segienam: {limas.volume():.{flo}f}")
        print("================ Limas =================")
        print("1. Limas Segitiga")
        print("2. Limas Segiempat")
        print("3. Limas Segilima")
        print("4. Limas Segienam")
        print("0. Kembali ke menu utama")
        limas_choice = inputInt("Pilih jenis limas (0-4): ", 0, 4)
        if limas_choice == 0:
            start()
            continue
        elif limas_choice == 1:
            repeatCalculation(LimasSegitigaCalc)
        elif limas_choice == 2:
            repeatCalculation(LimasSegiempatCalc)
        elif limas_choice == 3:
            repeatCalculation(LimasSegilimaCalc)
        elif limas_choice == 4:
            repeatCalculation(LimasSegienamCalc)
    elif choice == 2:
        def PrismaSegitigaCalc():
            print("=== Prisma Segitiga ===")
            alas = inputFloat("Masukkan panjang alas segitiga: ")
            tinggi_alas = inputFloat("Masukkan tinggi segitiga: ")
            tinggi_prisma = inputFloat("Masukkan tinggi prisma: ")
            prisma = PrismaSegitiga({"alas": alas, "tinggi_alas": tinggi_alas, "tinggi_prisma": tinggi_prisma})
            print(f"Volume Prisma Segitiga: {prisma.volume():.{flo}f}")
        def PrismaSegiempatCalc():
            print("=== Prisma Segiempat ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            tinggi_prisma = inputFloat("Masukkan tinggi prisma: ")
            prisma = PrismaSegiempat({"sisi": sisi, "tinggi_prisma": tinggi_prisma})
            print(f"Volume Prisma Segiempat: {prisma.volume():.{flo}f}")
        def PrismaSegilimaCalc():
            print("=== Prisma Segilima ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            tinggi_prisma = inputFloat("Masukkan tinggi prisma: ")
            prisma = PrismaSegilima({"sisi": sisi, "tinggi_prisma": tinggi_prisma})
            print(f"Volume Prisma Segilima: {prisma.volume():.{flo}f}")
        def PrismaSegienamCalc():
            print("=== Prisma Segienam ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            tinggi_prisma = inputFloat("Masukkan tinggi prisma: ")
            prisma = PrismaSegienam({"sisi": sisi, "tinggi_prisma": tinggi_prisma})
            print(f"Volume Prisma Segienam: {prisma.volume():.{flo}f}")
        print("================ Prisma =================")
        print("1. Prisma Segitiga")
        print("2. Prisma Segiempat")
        print("3. Prisma Segilima")
        print("4. Prisma Segienam")
        print("5. Kembali ke menu utama")
        prisma_choice = inputInt("Pilih jenis prisma (1-5): ", 1, 5)
        clearTerminal()
        if prisma_choice == 5:
            clearTerminal()
            start()
            continue
        elif prisma_choice == 1:
            repeatCalculation(PrismaSegitigaCalc)
        elif prisma_choice == 2:
            repeatCalculation(PrismaSegiempatCalc)
        elif prisma_choice == 3:
            repeatCalculation(PrismaSegilimaCalc)
        elif prisma_choice == 4:
            repeatCalculation(PrismaSegienamCalc)
    elif choice == 3:
        def KubusCalc():
            print("=== Kubus ===")
            sisi = inputFloat("Masukkan panjang sisi: ")
            kubus = Kubus({"sisi": sisi})
            print(f"Volume Kubus: {kubus.volume():.{flo}f}")
        repeatCalculation(KubusCalc)
    elif choice == 4:
        def BalokCalc():
            print("=== Balok ===")
            panjang = inputFloat("Masukkan panjang balok: ")
            lebar = inputFloat("Masukkan lebar balok: ")
            tinggi = inputFloat("Masukkan tinggi balok: ")
            balok = Balok({"panjang": panjang, "lebar": lebar, "tinggi": tinggi})
            print(f"Volume Balok: {balok.volume():.{flo}f}")
        repeatCalculation(BalokCalc)
    elif choice == 5:
        def BolaCalc():
            print("=== Bola ===")
            jari_jari = inputFloat("Masukkan jari-jari bola: ")
            bola = Bola({"jari_jari": jari_jari})
            print(f"Volume Bola: {bola.volume():.{flo}f}")
        repeatCalculation(BolaCalc)
    elif choice == 6:
        def KerucutCalc():
            print("=== Kerucut ===")
            jari_jari = inputFloat("Masukkan jari-jari kerucut: ")
            tinggi = inputFloat("Masukkan tinggi kerucut: ")
            kerucut = Kerucut({"jari_jari": jari_jari, "tinggi": tinggi})
            print(f"Volume Kerucut: {kerucut.volume():.{flo}f}")
        repeatCalculation(KerucutCalc)
    elif choice == 7:
        def TabungCalc():
            print("=== Tabung ===")
            jari_jari = inputFloat("Masukkan jari-jari tabung: ")
            tinggi = inputFloat("Masukkan tinggi tabung: ")
            tabung = Tabung({"jari_jari": jari_jari, "tinggi": tinggi})
            print(f"Volume Tabung: {tabung.volume():.{flo}f}")
        repeatCalculation(TabungCalc)
    else:
        raise Exception("Pilihan tidak valid.")


