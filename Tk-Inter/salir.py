from tkinter import *

root = Tk()

root.title("Input")
root.geometry("800x600")

frame = LabelFrame(root, text="Login")

btn = Button(frame, text="Salir", command=root.quit)
label = Label(frame, text="Estoy dentro de un frame")

frame.pack(padx=50, pady=50)
btn.pack()
label.pack()

root.mainloop()

