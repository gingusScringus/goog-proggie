import os
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command

var1 = int(99) # is a integer
var2 = float(45.9) # is a float
var3 = float(7.0) # is a float
var4 = int(7) # is a integer
var5 = str('abc') # is a string

print("var1 is ", var1, "and its type is ", type(var1))
print("var2 is ", var2, "and its type is ", type(var2))
print("var3 is ", var3, "and its type is ", type(var3))
print("var4 is ", var4, "and its type is ", type(var4))
print("var5 is ", var5, "and its type is ", type(var5))

my_value = 99
my_value = 0
print("my_value is ", my_value, "and its type is ", type(my_value))