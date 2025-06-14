import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

try:
    length = input("Enter a length rectangle: ")
    height = input("Enter a height rectangle: ")
    width = input("Enter a width rectangle: ")

    length = int(length)
    height = int(height)
    width = int(width)

    area = height * width
    perimeter = 2 * (height + width)
    volume = length * area * width
    #print("The area of the rectangle is: ", area)
    #print("The perimeter of the rectangle is: ", perimeter)
    print("The volume of the rectangle is: ", volume)
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()