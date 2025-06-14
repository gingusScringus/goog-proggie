import os
os.system("cls" if os.name == "nt" else "clear")  # clears the console by running a system command

howmanyinput = int(input("How many times to repeat? "))
texter = str(input("Input text: "))
total = 0 
file = open('kucinf.txt', "w")
for i in range(1, total + 1):
    print(f"{texter} ke-{i}")
    total += 1
print("Finished.")