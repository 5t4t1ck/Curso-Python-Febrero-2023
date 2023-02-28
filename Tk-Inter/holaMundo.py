from tkinter import *

root = Tk()

root.title("Hola Mundo desde TkInter!!!")
root.geometry("800x600")
# label = Label(root, text="Hola Mundo!").pack()
label = Label(root, text="Hola Mundo!")
label2 = Label(root, text="Hola Mundo! 02")
label3 = Label(root, text="Hola Mundo! 03")

label.pack()
label2.pack()
label3.pack()

root.mainloop()