import tkinter
from tkinter import *


root = tkinter.Tk()
root.geometry("300x550+450+100")
root.resizable(0,0)
root.title("Calculator")


lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana",20)
)
lbl.pack(expand = True, fill = "both")

btnrow0 = Frame(root,bg="#1c1c1b")
btnrow0.pack(expand = True, fill = "both")


btnrow1 = Frame(root, bg = "#000000")
btnrow1.pack(expand = True, fill = "both")


btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")


btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")


btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")



btnclear = Button(
    btnrow0,
    text = "C",
    font = ("Verdana",20),
    bg = "#ffdbdb",
    fg = "#f24141",
    relief = GROOVE,
    border = 0
)
btnclear.pack(side = LEFT, expand = True, fill = "both", )


btnbracketopen = Button(
    btnrow0,
    text = "(",
    font = ("Verdana",20),
    bg = "#e3dede",
    relief=GROOVE,
    border=0
)
btnbracketopen.pack(side = LEFT, expand = True, fill = "both")


btnbracketclose = Button(
    btnrow0,
    text = ")",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btnbracketclose.pack(side = LEFT, expand = True, fill = "both")


btndiv = Button(
    btnrow0,
    text = " /",
    font = ("Verdana",16),
    bg="#ff9500",
    padx = 5,
    relief=GROOVE,
    border=0
)
btndiv.pack(side = LEFT, expand = True, fill = "both")




btn7 = Button(
    btnrow1,
    text = "7",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn7.pack(side = LEFT, expand = True, fill = "both")


btn8 = Button(
    btnrow1,
    text = "8",
    font = ("Verdana",20),
    bg="#e3dede",
    relief = GROOVE,
    border = 0
)
btn8.pack(side = LEFT, expand = True, fill = "both")


btn9 = Button(
    btnrow1,
    text = "9",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn9.pack(side = LEFT, expand = True, fill = "both")


btnmul = Button(
    btnrow1,
    text = "x",
    font = ("Verdana",20),
    bg="#ff9500",
    padx = 4,
    relief=GROOVE,
    border=0
)
btnmul.pack(side = LEFT, expand = True, fill = "both")




btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn4.pack(side = LEFT, expand = True, fill = "both")


btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn5.pack(side = LEFT, expand = True, fill = "both")


btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn6.pack(side = LEFT, expand = True, fill = "both")


btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana",20),
    bg = "#ff9500",
    padx = 6,
    relief=GROOVE,
    border=0
)
btnminus.pack(side = LEFT, expand = True, fill = "both")




btn1 = Button(
    btnrow3,
    text = "1",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn1.pack(side = LEFT, expand = True, fill = "both")


btn2 = Button(
    btnrow3,
    text = "2",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn2.pack(side = LEFT, expand = True, fill = "both")


btn3 = Button(
    btnrow3,
    text = "3",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn3.pack(side = LEFT, expand = True, fill = "both")


btnplus = Button(
    btnrow3,
    text = "+",
    font = ("Verdana",20),
    bg ="#ff9500",
    padx =1,
    relief=GROOVE,
    border=0
)
btnplus.pack(side = LEFT, expand = True, fill = "both")



btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btn0.pack(side = LEFT, expand = True, fill = "both")


btndot = Button(
    btnrow4,
    text = ".",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btndot.pack(side = LEFT, expand = True, fill = "both")


btndel = Button(
    btnrow4,
    text = "del",
    font = ("Verdana",20),
    bg="#e3dede",
    relief=GROOVE,
    border=0
)
btndel.pack(side = LEFT, expand = True, fill = "both")

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana",18),
    bg="#51d663",
    padx = 6,
    relief=GROOVE,
    border=0
)
btnequal.pack(side = LEFT, expand = True, fill = "both")

root.mainloop()