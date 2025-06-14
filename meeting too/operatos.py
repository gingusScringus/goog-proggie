import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

input1 = float(input("enter first input: "))
input2 = float(input("enter second input: "))
input3 = float(input("enter third input: "))
input4 = float(input("enter fourth input: "))

result1 = input1 + input2 + input3
result2 = input1 / input2 - input3
result3 = input1 + input2 * input3 - input4
result4 = (input1 + input2) * input3
result5 = input1 / (input2 - input3)
result6 = input1 + input2 * (input3 - input4)
result7 = input1 // input2
result8 = input1 % input2

print("result1: ", result1)
print("result2: ", result2)
print("result3: ", result3)
print("result4: ", result4)
print("result5: ", result5)
print("result6: ", result6)
print("result7: ", result7)
print("result8: ", result8)
