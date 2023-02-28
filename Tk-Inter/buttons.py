from tkinter import *

root = Tk()

root.title("Buttons")
root.geometry("800x600")

label = Label(root, text="Hola Mundo!")

def click():
    label.pack()

btn = Button(root, text="Click", command=click, fg="yellow", bg="blue")
btn.pack()


root.mainloop()

