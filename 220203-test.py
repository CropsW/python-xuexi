import sys
from tkinter import *
from tkinter.messagebox import *
import os


def b1Act():
    mBox1 = askyesno('新年大吉！', '祝您在2022年发财！是否看照片？')
    if mBox1 == True:
        os.startfile('A:4(100PHOTO)\SAM_3776.JPG')
    else:
        showwarning('我强迫你！','必须得看！')
        os.startfile('A:4(100PHOTO)\SAM_3776.JPG')
        sys.exit()



top = Tk()
top.title('Hello 2022!')
top.geometry('300x140')
top.resizable(False, False)
butt1 = Button(top, text='Touch me!', command=b1Act)
butt1.place(relx=0.5, rely=0.5, anchor=CENTER)
top.mainloop()
