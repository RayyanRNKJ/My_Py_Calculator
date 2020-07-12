import tkinter
from tkinter import *


root = tkinter.Tk()
root.geometry("300x500+450+100")
root.resizable(0,0)
root.title("Calculator")

btnrow1 = Frame(root, bg ="#000000")
btnrow1.pack(expand = True, fill = "both")


btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")


btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")


btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

root.mainloop()