import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

# show rate
print("")
print("work rate per hour is Rp 50.000, ")
print("")

# set constants
#rate = 50000.0
rate = float(input("enter work rate: Rp "))

# ask user input
work_hour = float(input("enter work hour: "))

#procwss
total_wage = rate * work_hour

print("wages per hour: Rp ", format(total_wage, ',.2f'))
