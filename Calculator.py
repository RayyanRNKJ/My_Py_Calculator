import tkinter
from tkinter import *



val = ""
vls = 0
operator = ""



def btn1_is_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_is_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_is_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_is_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_is_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_is_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_is_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_is_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_is_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn0_is_clicked():
    global val
    val = val + "0"
    data.set(val)


def btndot_is_clicked():
    global val
    val = val + "."
    data.set(val)


def btnplus_is_clicked():
    global vls
    global operator
    global val
    vls = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btnminus_is_clicked():
    global vls
    global operator
    global val
    vls = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btnmul_is_clicked():
    global vls
    global operator
    global val
    vls = float(val)
    operator = "*"
    val = val + "x"
    data.set(val)


def btndiv_is_clicked():
    global vls
    global operator
    global val
    vls = float(val)
    operator = "/"
    val = val + "÷"
    data.set(val)


def btnclear_is_clicked():
    global vls
    global operator
    global val
    vls = 0
    val = ""
    operator = ""
    data.set(val)


def btndel_is_clicked():
    #global vls
    #global operator
    global val
    #vls = 0
    val = val[:-1]
    #operator = ""
    data.set(val)


def btnequal_is_clicked():
    global vls
    global operator
    global val
    val = val.replace("x","*")
    val = val.replace("÷", "/")
    if operator == "+":
        total = str(eval(val))
        data.set(total)
        val = str(total)
    elif operator == "-":
        total = str(eval(val))
        data.set(total)
        val = str(total)
    elif operator == "*":
        total = str(eval(val))
        data.set(total)
        val = str(total)
    elif operator == "/":
        try:
            total = str(eval(val))
        except: ZeroDivisionError
        val = "Sorry, Division By Zero Is Not Possible!!!"
        data.set(val)
        data.set(total)
        val = str(total)





root = tkinter.Tk()
root.geometry("300x550+450+100")
root.resizable(0, 0)
root.title("Calculator")

data = StringVar()
lbl = Label(
    root,
    text="Label",
    wraplength=300,
    justify=RIGHT,
    anchor=SE,
    font=("Verdana", 20),
    height=3,
    textvariable=data,
    bg="white",
    fg="black",
)
lbl.pack(expand=True, fill="both")

btnrow0 = Frame(root, bg="#1c1c1b")
btnrow0.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btnclear = Button(
    btnrow0,
    text="C",
    font=("Verdana", 21),
    bg="#ffdbdb",
    fg="#f24141",
    padx=67,
    relief=GROOVE,
    border=0,
    command=btnclear_is_clicked
)
btnclear.pack(side=LEFT, expand=True, fill="both", )



btndiv = Button(
    btnrow0,
    text=" /",
    font=("Verdana", 16),
    bg="#ff9500",
    relief=GROOVE,
    border=0,
    command=btndiv_is_clicked
)
btndiv.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    btnrow1,
    text="7",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn7_is_clicked
)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow1,
    text="8",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn8_is_clicked
)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow1,
    text="9",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn9_is_clicked
)
btn9.pack(side=LEFT, expand=True, fill="both")

btnmul = Button(
    btnrow1,
    text="x",
    font=("Verdana", 20),
    bg="#ff9500",
    padx=4,
    relief=GROOVE,
    border=0,
    command=btnmul_is_clicked
)
btnmul.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text="4",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn4_is_clicked
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn5_is_clicked
)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn6_is_clicked
)
btn6.pack(side=LEFT, expand=True, fill="both")

btnminus = Button(
    btnrow2,
    text="-",
    font=("Verdana", 20),
    bg="#ff9500",
    padx=6,
    relief=GROOVE,
    border=0,
    command=btnminus_is_clicked
)
btnminus.pack(side=LEFT, expand=True, fill="both")

btn1 = Button(
    btnrow3,
    text="1",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn1_is_clicked
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow3,
    text="2",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn2_is_clicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow3,
    text="3",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn3_is_clicked
)
btn3.pack(side=LEFT, expand=True, fill="both")

btnplus = Button(
    btnrow3,
    text="+",
    font=("Verdana", 20),
    bg="#ff9500",
    padx=1,
    relief=GROOVE,
    border=0,
    command=btnplus_is_clicked
)
btnplus.pack(side=LEFT, expand=True, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btn0_is_clicked
)
btn0.pack(side=LEFT, expand=True, fill="both")

btndot = Button(
    btnrow4,
    text=".",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btndot_is_clicked
)
btndot.pack(side=LEFT, expand=True, fill="both")

btndel = Button(
    btnrow4,
    text="del",
    font=("Verdana", 20),
    bg="#e3dede",
    relief=GROOVE,
    border=0,
    command=btndel_is_clicked
)
btndel.pack(side=LEFT, expand=True, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("Verdana", 18),
    bg="#51d663",
    padx=6,
    relief=GROOVE,
    border=0,
    command=btnequal_is_clicked
)
btnequal.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
