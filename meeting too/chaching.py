import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

money = float(input("enter money: $"))

savings = float(money * (1+6/100) **100)

print("savings: $", format(savings, ',.2f'))
#print(savings)