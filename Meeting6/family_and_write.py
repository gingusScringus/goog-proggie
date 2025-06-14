import os
import time
os.system("cls" if os.name == "nt" else "clear")  # clears the console by running a system command

parentCount = int(input("How many parents? "))
if parentCount < 1:
    print("there's no way bruh... :skull:")
    print("aight imma jet")
    exit()
siblingCount = int(input("How many siblings? "))
totalCount = parentCount + siblingCount + 1  # +1 for the user themselves
theOneUses = os.environ.get("USER")  # gets the username of the user
file = open('keluarga.txt', "w")

parentNames = []
siblingNames = []

for i in range (parentCount):
    if (i + 1) % 2 == 1:
        name = input(f"Enter mother {((i + 1) + 1)//2} name: ")
    else:
        name = input(f"Enter father {(i + 1)//2} name: ")
    parentNames.append(name)
    print(f"Parent {i + 1} name: {name}")
for i in range (siblingCount): 
    name = input(f"Enter sibling {i + 1} name: ")
    siblingNames.append(name)
    print(f"Sibling {i + 1} name: {name}")
print(f"Total family members: {totalCount}")
file.write("You: " + theOneUses + "\n")
file.write("Parents: " + ", ".join(parentNames) + " (" + str(parentCount) + ")" + "\n")
file.write("Siblings: " + ", ".join(siblingNames) + " (" + str(siblingCount) + ")" + "\n")
file.write("Family members: " + ", ".join([theOneUses] + parentNames + siblingNames) + " (" + str(totalCount) + ")" + "\n")
file.write(time.strftime("Generated on %Y-%m-%d at %H:%M:%S\n"))
file.close()
file = open('keluarga.txt', "r")
print(file.read())
print("Finished.")
print("Wrote to file", file.name, ", size", os.path.getsize(file.name), "bytes")
file.close()
exit()




