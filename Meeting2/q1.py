import os

#user_name = input("Enter your name: ")
user_name = os.getlogin() # Get the username of the current user
pc_name = os.uname().nodename # Get the name of the current machine
os.system("cls" if os.name == "nt" else "clear") # clears the console by running a system command
# Display a greeting message
print("Hello, " + user_name + "! Welcome to the program.")
print("You are using the machine: " + pc_name)