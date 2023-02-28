from tkinter import *

root = Tk()

root.title("Hola desde TkInter...")
root.geometry("800x600")

label = Label(root, text="Primera Línea")
label1 = Label(root, text="                                                 ")
label2 = Label(root, text="Segunda Línea")

label.grid(row=0, column=0)
label1.grid(row=0, column=2)
label2.grid(row=0, column=10)

root.mainloop()

