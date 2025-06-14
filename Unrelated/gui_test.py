from tkinter import*
window = Tk()

window.title("umm this is a windowssshhhh")
window.geometry("320x240")

label = Label(window, text="this is a label")
label.pack(pady=10)

def on_button_click():
    window.configure(bg="lightblue")
    label.configure(text="yayy!!!!!")

#butten = Button(window, text="cilk meee!!!", command=lambda: print("Button Clicked!")) # lambda function for one-off operation, meaning no need for another line lmao
butten = Button(window, text="Click Me", command=on_button_click)
butten.pack(pady=20)


window.mainloop()

