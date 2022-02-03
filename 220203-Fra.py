from tkinter import *
from tkinter.messagebox import *
from fractions import Fraction
from tkinter import font
def b1Act():
    asmd = Toplevel()
    asmd.geometry('400x550')
    asmd.title('分数四则运算')
top = Tk()
top.title('分数运算器')
top.geometry('255x70')
top.resizable(False,False)
f1 = font.Font(size=20)
lab1 = Label(top,text='主菜单',font=f1)
lab1.place(relx=0.5,rely=0.25,anchor=CENTER)
butt1 = Button(top,text='四则运算',command=b1Act)
butt1.place(relx=0.2,rely=0.7,anchor=CENTER,relwidth=0.25)
butt2 = Button(top,text='约分')
butt2.place(relx=0.5,rely=0.7,anchor=CENTER,relwidth=0.25)
butt3 = Button(top,text='小数化分数')
butt3.place(relx=0.8,rely=0.7,anchor=CENTER,relwidth=0.25)
top.mainloop()