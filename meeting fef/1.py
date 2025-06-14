
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

    def updateCustomer(self, data_customer):
        self.new_customer["nama"] = data_customer["nama"]
        self.new_customer[""]
        self.new_customer = {
            'nama': data_customer['nama'],
            'no_hp': data_customer['no_hp'],
            'no_rekening': data_customer['no_rekening'],
            'alamat': data_customer['alamat']
        }
        return True

    def getDetailCustomer(self):
        return self.new_customer
    
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