#Excercise 3.6

import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

while True:
    sellingPrice = int(input("Enter selling price: Rp "))
    commisionPrice = int(input("Enter commision price: Rp "))
    totalPrice = sellingPrice + commisionPrice
    print("Total price: Rp ", format(totalPrice, ',.2f'))
    prompt = input("Do you want to continue? (y/n): ")
    if prompt.lower() != 'y':
        break
    