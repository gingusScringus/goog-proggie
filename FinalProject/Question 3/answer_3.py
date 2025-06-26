import os
import platform
import datetime
import random
import re
import argparse
# doesn't look good but whatever

parser = argparse.ArgumentParser()
parser.add_argument("-t", type=str, default="transaksi.txt", help="custom filename for text file (default: transaksi.txt)")

args = parser.parse_args()
tf = args.t
# tf = text file

def clearTerminal():
    os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

def createFile(filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename)
    abs_path = os.path.abspath(file_path)
    print(f"Checking if file {filename} exists...")
    if not os.path.exists(file_path):
        print(f"File {filename} does not exist. Creating a new file...")
        with open(file_path, "w") as file:
            file.write("")
            print(f"File {filename} created successfully at {abs_path}.")
    elif os.path.isfile(file_path):
        print(f"File {filename} already exists at {abs_path}")
    else:
        raise Exception(f"man idk")
    return abs_path

class Transaksi:
    all_transaksi = []

    def __init__(self, id, customer, product, jumlah, invoice, tanggal, harga):
        self.id = id
        self.customer = customer
        self.product = product
        self.jumlah = jumlah
        self.invoice = invoice
        self.tanggal = tanggal
        self.harga = harga

    def addTransaksi(self):
        transaksi_dict = {
            "id": self.id,
            "customer": self.customer,
            "product": self.product,
            "jumlah": self.jumlah,
            "invoice": self.invoice,
            "tanggal": self.tanggal,
            "harga": self.harga
        }
        Transaksi.all_transaksi.append(transaksi_dict)
        return "Data transaksi berhasil disimpan."

    @classmethod
    def listTransaksi(cls):
        return cls.all_transaksi
    
    def generateTransaksiToFile(self, file_path):
        script_dir = os.path.dirname(__file__)
        abs_path = os.path.join(script_dir, file_path)
        with open(abs_path, "a") as file:
            line = (
                "--------------------\n"
                f"ID        : {self.id}\n"
                f"Customer  : {self.customer}\n"
                f"Product   : {self.product}\n"
                f"Jumlah    : {self.jumlah}\n"
                f"Invoice   : {self.invoice}\n"
                f"Tanggal   : {self.tanggal}\n"
                f"Harga     : Rp{self.harga}\n"
                "--------------------\n\n"
            )
            file.write(line)

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

def inputInvoice(prompt):
    pattern = r"^INV-\d{3}-\d{4}$"
    while True:
        invoice = input(prompt)
        if re.match(pattern, invoice):
            return invoice
        else:
            print("Invoice harus dalam format INV-XXX-XXXX.")

def inputTanggal(prompt):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    while True:
        tanggal = input(prompt)
        if re.match(pattern, tanggal):
            return tanggal
        else:
            print("Tanggal harus dalam format YYYY-MM-DD.")

# transagsi repetition function
def repeatTransaksi(transaksiFunc):
    while True:
        transaksiFunc()
        repeat = inputString("Hitung ulang transaksi? (y/n): ")
        if repeat != "y":
            clearTerminal()
            start()
            return

def start():
    clearTerminal()
    print("====================== SISTEM TRANSAGSI ======================")
    print(f"Halo, {customer_name}")
    print(f"Berjalan di sistem {platform.system()} pada waktu {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    print("1. Tambah Transaksi")
    print("2. List Transaksi")
    print("3. Keluar")



clearTerminal()
createFile(tf)
customer_name = input("Input nama: ")
start()

while True:
    choice = inputInt("Pilih menu: ", 1, 3)
    clearTerminal()
    if choice == 1:
        def inputTransaksi():
            print("=== Input Transaksi ===")
            id = random.randint(1000, 999999)
            customer = customer_name
            invoice = inputInvoice("Input Invoice (INV-XXX-XXXX): ")
            tanggal = inputTanggal("Input Tanggal (YYYY-MM-DD): ")
            product = input("Input Product Code: ")
            jumlah = inputInt("Input Jumlah: ")
            harga = inputFloat("Input Harga (Rp): ")

            transaksi_data = {
                'id': id,
                'customer': customer,
                'product': product,
                'jumlah': jumlah,
                'invoice': invoice,
                'tanggal': tanggal,
                'harga': harga
            }
            transaksi = Transaksi(**transaksi_data)
            transaksi.addTransaksi()
            transaksi.generateTransaksiToFile(tf)
            print("Transaksi berhasil ditambahkan.")
        repeatTransaksi(inputTransaksi)
    elif choice == 2:
        print("============================== List Transaksi ===============================")
        print("ID      Customer      Product      Jumlah   Invoice        Tanggal      Harga")
        transaksi_list = Transaksi.listTransaksi()
        if not transaksi_list:
            print("Belum ada transaksi di memory.")
            input("Tekan tombol apapun untuk kembali...")
            clearTerminal()
            start()
        else:
            for transaksi in transaksi_list:
                print(
                    f"{str(transaksi['id']).ljust(8)} "
                    f"{str(transaksi['customer']).ljust(12)} "
                    f"{str(transaksi['product']).ljust(10)} "
                    f"{str(transaksi['jumlah']).ljust(7)} "
                    f"{str(transaksi['invoice']).ljust(13)} "
                    f"{str(transaksi['tanggal']).ljust(11)} "
                    f"{str(transaksi['harga']).ljust(8)}"
                )
            input("Tekan tombol apapun untuk kembali...")
            clearTerminal()
            start()
    elif choice == 3:
        print("Mengeluarkan...")
        break
    else:
        raise Exception("Pilihan tidak valid.")

