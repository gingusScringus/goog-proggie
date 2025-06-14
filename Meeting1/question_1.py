import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    result = float(num1) + float(num2)
    print("the result is: " + str(result))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()