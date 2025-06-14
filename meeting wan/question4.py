import os
import random
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

# i'm not actually sure if this is how wages work irl but here it is i guess

try:
    upah = random.randint(1, 100) * 1000  # courtesy of copilot, this basically randomizes the wage between 1 and 1000000. probably not how it works irl but whatever.
    jamKerja = input("enter work hour: ")
    jamKerja = int(jamKerja)
    totalUpah = upah * jamKerja

    print("wages per hour: ", upah, "Rp")   
    print("work hour: ", jamKerja)
    print("total wage: ", totalUpah, "Rp")
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()