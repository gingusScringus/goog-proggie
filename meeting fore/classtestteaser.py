class Mobil():
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def get_brand(self):
        return self.brand

mobil1 = Mobil("Toyota", 2020, "Red")
print(mobil1.get_brand())

mobil2 = Mobil("Honda", 2018, "Blue")
print(mobil2.get_brand())

