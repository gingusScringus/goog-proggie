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
    
# customer
data_customer_1 = {
    'id': 1,
    'nama': 'John Doe',
    'no_hp': '08123456789',
    'no_rekening': '1234567890',
    'alamat': 'Jakarta'
}
customer_1 = Customer()
customer_1.addCustomer(data_customer_1)
print(customer_1.getDetailCustomer())

data_customer_1_update = {
    'nama': 'John Smith',
    'no_hp': '08123456789',
    'no_rekening': '1234567890',
    'alamat': 'Batavia'
}
customer_1.updateCustomer(data_customer_1_update)
print(customer_1.getDetailCustomer())

data_customer_2 = {
    'id': 2,
    'nama': 'Jane Doe',
    'no_hp': '08123456789',
    'no_rekening': '1234567890',
    'alamat': 'Jakarta'
}
customer_2 = Customer()
customer_2.addCustomer(data_customer_2)
print(customer_2.getDetailCustomer())

# product

data_product_1 = {
    'id': 1,
    'nama': 'Produk A',
    'harga': 100000,
    'stok': 50,
    'deskripsi': 'Deskripsi Produk A'
}

product_1 = Product()
product_1.addProduct(data_product_1)
print(product_1.getDetailProduct())

data_product_1_update = {
    'nama': 'Produk A Sigma',
    'harga': 120000,
    'stok': 40,
    'deskripsi': 'Deskripsi Produk A Sigma'
}
product_1.updateProduct(data_product_1_update)
print(product_1.getDetailProduct())

data_product_2 = { 
    'id': 2,
    'nama': 'Produk B',
    'harga': 200000,
    'stok': 30,
    'deskripsi': 'Deskripsi Produk B'
}
product_2 = Product()
product_2.addProduct(data_product_2)
print(product_2.getDetailProduct())

data_product_3 = { 
    'id': 3,
    'nama': 'Produk C',
    'harga': 400000,
    'stok': 60,
    'deskripsi': 'Deskripsi Produk C'
}
product_3 = Product()
product_3.addProduct(data_product_3)
print(product_3.getDetailProduct())