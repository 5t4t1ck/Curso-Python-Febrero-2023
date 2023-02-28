from tkinter import *

root = Tk()

root.title("Input")
root.geometry("800x600")

input = Entry(root, width=60)
input.pack()
input.insert(0, "Ingresa un texto")

def click():
    texto = input.get()
    label.configure(text=texto)

btn = Button(root, text="Click", command=click)
btn.pack()

label = Label(root, text="Texto de la etiqueta")
label.pack()

root.mainloop()

