# Excersice 3.5
import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command


"""
for i in range(5):
    print("Enter number ", i + 1, ": ", end="")
    if i == 0:
        firstNum = int(input())
    elif i == 1:
        secondNum = int(input())
    elif i == 2:
        thirdNum = int(input())
    elif i == 3:
        fourthNum = int(input())
    elif i == 4:
        fifthNum = int(input())
"""
n = int(input(" Enter the count of numbers you want to enter: "))

for i in range(n):
    print("Enter number ", i + 1, ": ", end="")
    if i == 0:
        firstNum = int(input())
    elif i == 1:
        secondNum = int(input())
    elif i == 2:
        thirdNum = int(input())
    elif i == 3:
        fourthNum = int(input())
    elif i == 4:
        fifthNum = int(input())

allTheTotals = firstNum + secondNum + thirdNum + fourthNum + fifthNum
print("The total of all the numbers is: ", allTheTotals)