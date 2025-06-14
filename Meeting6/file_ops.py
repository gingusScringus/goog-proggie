import os
import playsound
os.system("cls" if os.name == "nt" else "clear")  # clears the console by running a system command

texter = str(input("input: "))
max = int(input("enter max: "))
# alarm = playsound("~/Music/alarm.wav")  # plays an alarm sound

fiel = open('kucinf.txt', "w")
for i in range(1, max):
    fiel.write((texter+" ke-"),str(i),"\n")

fiel.close()
fiel = open('kucinf.txt', "r")
print(fiel.read())
print("finished.")
print("wrote to file ", fiel.name, ", size ", os.path.getsize(fiel.name), " bytes")
fiel.close()
exit()