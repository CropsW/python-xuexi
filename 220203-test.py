from tkinter import *
from tkinter.messagebox import *
def b1Act():
    showinfo('新年大吉！','祝您在2022年发财！')
top = Tk()
top.title('Hello 2022!')
top.geometry('300x140')
top.resizable(False,False)
butt1 = Button(top,text='Touch me!',command=b1Act)
butt1.place(relx=0.5,rely=0.5,anchor=CENTER)
top.mainloop()