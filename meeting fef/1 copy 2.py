import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

class Customer:
    """
    def __init__(self, id, nama, no_hp, no_rekening, alamat):
        self.id
        self.nama
        self.no_hp
        self.no_rekening
        self.alamat
        self.new_customer
    """
        
    def addCustomer(self, data_customer):
        self.id = data_customer['id']
        self.nama = data_customer['nama']
        self.no_hp = data_customer['no_hp']
        self.no_rekening = data_customer['no_rekening']
        self.alamat = data_customer['alamat']

        # simpan data customer di dalam dictionary
        self.new_customer = {
            'id': self.id,
            'nama': self.nama,
            'no_hp': self.no_hp,
            'no_rekening': self.no_rekening,
            'alamat': self.alamat
        }
        return "data customer berhasil disimpan"

    def updateCustomer(self, data_customer):
        self.new_customer["nama"] = data_customer["nama"]
        self.new_customer["no_hp"] = data_customer["no_hp"]
        self.new_customer["no_rekening"] = data_customer["no_rekening"]
        self.new_customer["alamat"] = data_customer["alamat"]
        """
        self.new_customer = {
            'nama': data_customer['nama'],
            'no_hp': data_customer['no_hp'],
            'no_rekening': data_customer['no_rekening'],
            'alamat': data_customer['alamat']
        }
        """
        return "data customer berhasil diupdate"

    def getDetailCustomer(self):
        return self.new_customer
    
class Product:
    """
    def __init__(self, id, nama, harga, stok):
        self.id
        self.nama
        self.harga
        self.stok
        self.new_product
    """
    
    def addProduct(self, data_product):
        self.id = data_product['id']
        self.nama = data_product['nama']
        self.harga = data_product['harga']
        self.stok = data_product['stok']
        self.deskripsi = data_product['deskripsi']

        # simpan data produk di dalam dictionary
        self.new_product = {
            'id': self.id,
            'nama': self.nama,
            'harga': self.harga,
            'stok': self.stok,
            'deskripsi': self.deskripsi
        }
        return "data produk berhasil disimpan"
    
    def updateProduct(self, data_product):
        self.new_product["nama"] = data_product["nama"]
        self.new_product["harga"] = data_product["harga"]
        self.new_product["stok"] = data_product["stok"]
        self.new_product["deskripsi"] = data_product["deskripsi"]

        return "data produk berhasil diupdate"

    def getDetailProduct(self):
        return self.new_product
    
print("=== REGISTRASI CUSTOMER ===")
input_nama = input("Masukkan nama customer: ")
input_no_hp = input("Masukkan no hp customer: ")
input_no_rekening = input("Masukkan no rekening customer: ")
input_alamat = input("Masukkan alamat customer: ")

data_customer = {
    'id': 1,
    'nama': input_nama,
    'no_hp': input_no_hp,
    'no_rekening': input_no_rekening,
    'alamat': input_alamat
}
customer = Customer()
customer.addCustomer(data_customer)
print(customer.getDetailCustomer())

print("=== TAMBAH PRODUCT ===")
products = []
for i in range(3):
    input_nama = input("Masukkan nama produk: ")
    input_harga = int(input("Masukkan harga produk: "))
    input_stok = int(input("Masukkan stok produk: "))
    input_deskripsi = input("Masukkan deskripsi produk: ")

    data_product = {
        'id': i + 1,
        'nama': input_nama,
        'harga': input_harga,
        'stok': input_stok,
        'deskripsi': input_deskripsi
    }
    product = Product()
    product.addProduct(data_product)
    products.append(product.getDetailProduct())

