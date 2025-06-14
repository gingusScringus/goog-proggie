import os 
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command
try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    sum_of_numbers = int(num1) + int(num2)
    average = sum_of_numbers / 2

    print("The sum of {01} and {1} is {2}".format(num1, num2, sum_of_numbers))
    print("The average of {0} and {1} is {2}".format(num1, num2, average))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()