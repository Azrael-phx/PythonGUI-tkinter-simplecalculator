from tkinter import *
from tkinter import messagebox
screen = Tk()
screen.title("My Calculator")
screen.geometry("360x480")


screen.maxsize(width=360,height=420)
screen.minsize(width=360,height=420)

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ""
    tex.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo("Notification", "Try again, Something is wrong here", parent=screen)

#Adding binding functions to each button

def on_entryenter(e):
    entry1.configure(bg="red", fg="white")
def on_entryleave(e):
    entry1.configure(bg="orange", fg="black")

def on_enter7(e):
    btn7.configure(bg="red")
def on_leave7(e):
    btn7.configure(bg="powder blue")

def on_enter8(e):
    btn8.configure(bg="red")
def on_leave8(e):
    btn8.configure(bg="powder blue")

def on_enter9(e):
    btn9.configure(bg="red")
def on_leave9(e):
    btn9.configure(bg="powder blue")

def on_enteradd(e):
    btnadd.configure(bg="red")
def on_leaveadd(e):
    btnadd.configure(bg="powder blue")

def on_enter4(e):
    btn4.configure(bg="red")
def on_leave4(e):
    btn4.configure(bg="powder blue")

def on_enter5(e):
    btn5.configure(bg="red")
def on_leave5(e):
    btn5.configure(bg="powder blue")

def on_enter6(e):
    btn6.configure(bg="red")
def on_leave6(e):
    btn6.configure(bg="powder blue")

def on_entersub(e):
    btnsub.configure(bg="red")
def on_leavesub(e):
    btnsub.configure(bg="powder blue")

def on_enter1(e):
    btn1.configure(bg="red")
def on_leave1(e):
    btn1.configure(bg="powder blue")

def on_enter2(e):
    btn2.configure(bg="red")
def on_leave2(e):
    btn2.configure(bg="powder blue")

def on_enter3(e):
    btn3.configure(bg="red")
def on_leave3(e):
    btn3.configure(bg="powder blue")

def on_entermul(e):
    btnmul.configure(bg="red")
def on_leavemul(e):
    btnmul.configure(bg="powder blue")

def on_enter0(e):
    btn0.configure(bg="red")
def on_leave0(e):
    btn0.configure(bg="powder blue")

def on_enterclear(e):
    btnclear.configure(bg="red")
def on_leaveclear(e):
    btnclear.configure(bg="powder blue")

def on_enterequal(e):
    btnequal.configure(bg="red")
def on_leaveequal(e):
    btnequal.configure(bg="powder blue")

def on_enterdiv(e):
    btndiv.configure(bg="red")
def on_leavediv(e):
    btndiv.configure(bg="powder blue")

tex = StringVar()
operator = ""

#Adding an entry box
entry1 = Entry(screen, bg="Orange",font=('arial',23,'italic bold'), bd="10", justify="right",textvariable=tex)
entry1.grid(row=0,columnspan=5)

#Adding buttons in the screen row=1

btn7 = Button(screen,text="7",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(7),
              activebackground="green", activeforeground="white")
btn7.grid(row=1,column=1)

btn8 = Button(screen,text="8",font=("arial",22,"italic bold"), bd=8, padx="34", pady="11",command=lambda:click(8),
              activebackground="green", activeforeground="white")
btn8.grid(row=1,column=2)

btn9 = Button(screen,text="9",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(9),
              activebackground="green", activeforeground="white")
btn9.grid(row=1,column=3)

btnadd = Button(screen,text="+",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click("+"),
                activebackground="green", activeforeground="white")
btnadd.grid(row=1,column=4)

#Adding buttons in the screen, row=2

btn4 = Button(screen,text="4",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(4),
              activebackground="green", activeforeground="white")
btn4.grid(row=2,column=1)

btn5 = Button(screen,text="5",font=("arial",22,"italic bold"), bd=8, padx="34", pady="11",command=lambda:click(5),
              activebackground="green", activeforeground="white")
btn5.grid(row=2,column=2)

btn6 = Button(screen,text="6",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(6),
              activebackground="green", activeforeground="white")
btn6.grid(row=2,column=3)

btnsub = Button(screen,text="-",font=("arial",20,"italic bold"), bd=8, padx="15", pady="11",command=lambda:click("-"),
                activebackground="green", activeforeground="white")
btnsub.grid(row=2,column=4)

#Adding buttons in the screen, row=3

btn1 = Button(screen,text="1",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(1),
              activebackground="green", activeforeground="white")
btn1.grid(row=3,column=1)

btn2 = Button(screen,text="2",font=("arial",22,"italic bold"), bd=8, padx="34", pady="11",command=lambda:click(2),
              activebackground="green", activeforeground="white")
btn2.grid(row=3,column=2)

btn3 = Button(screen,text="3",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(3),
              activebackground="green", activeforeground="white")
btn3.grid(row=3,column=3)

btnmul = Button(screen,text="*",font=("arial",20,"italic bold"), bd=8, padx="15", pady="11",command=lambda:click("*"),
                activebackground="green", activeforeground="white")
btnmul.grid(row=3,column=4)

#Adding buttons in the screen, row=4

btn0= Button(screen,text="0",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=lambda:click(0),
             activebackground="green", activeforeground="white")
btn0.grid(row=4,column=1)

btnclear = Button(screen,text="Clear",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=clear,
                  activebackground="green", activeforeground="white")
btnclear.grid(row=4,column=2)

btnequal = Button(screen,text="=",font=("arial",20,"italic bold"), bd=8, padx="11", pady="11",command=equal,
                  activebackground="green", activeforeground="white")
btnequal.grid(row=4,column=3)

btndiv = Button(screen,text="/",font=("arial",20,"italic bold"), bd=8, padx="15", pady="11",command=lambda:click("/"),
                activebackground="green", activeforeground="white")
btndiv.grid(row=4,column=4)

#Adding hovering effect to each button

entry1.bind("<Enter>, on_entryenter")
entry1.bind("<Leave>, on_entryleave")

btn7.bind("<Enter>", on_enter7)
btn7.bind("<Leave>", on_leave7)

btn8.bind("<Enter>", on_enter8)
btn8.bind("<Leave>", on_leave8)

btn9.bind("<Enter>", on_enter9)
btn9.bind("<Leave>", on_leave9)

btnadd.bind("<Enter>", on_enteradd)
btnadd.bind("<Leave>", on_leaveadd)

btn6.bind("<Enter>", on_enter6)
btn6.bind("<Leave>", on_leave6)

btn5.bind("<Enter>", on_enter5)
btn5.bind("<Leave>", on_leave5)

btn4.bind("<Enter>", on_enter4)
btn4.bind("<Leave>", on_leave4)

btnsub.bind("<Enter>", on_entersub)
btnsub.bind("<Leave>", on_leavesub)

btn3.bind("<Enter>", on_enter3)
btn3.bind("<Leave>", on_leave3)

btn2.bind("<Enter>", on_enter2)
btn2.bind("<Leave>", on_leave2)

btn1.bind("<Enter>", on_enter1)
btn1.bind("<Leave>", on_leave1)

btnmul.bind("<Enter>", on_entermul)
btnmul.bind("<Leave>", on_leavemul)

btn0.bind("<Enter>", on_enter0)
btn0.bind("<Leave>", on_leave0)

btnclear.bind("<Enter>", on_enterclear)
btnclear.bind("<Leave>", on_leaveclear)

btnequal.bind("<Enter>", on_enterequal)
btnequal.bind("<Leave>", on_leaveequal)

btndiv.bind("<Enter>", on_enterdiv)
btndiv.bind("<Leave>", on_leavediv)

screen.mainloop()

