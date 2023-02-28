from tkinter import *

root = Tk()

root.title("Marcos")
root.geometry("800x600")

frame = LabelFrame(root, padx=50, pady=50, borderwidth=5)

btn = Button(frame, text="Salir", command=root.quit)
label = Label(frame, text="Estoy dentro de un frame")

frame.pack(padx=50, pady=50)
btn.pack()
label.pack()

root.mainloop()

