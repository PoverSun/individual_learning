#!/usr/bin/env python
#tkhello4.py
from tkinter import *



def resize(ev=None):
    label.config(font='Arial -%d bold' % scale.get())


top=Tk()  #创建顶层窗口
top.geometry('250x150')

label=Label(top,text='Hello World!',font='Arial -12 bold')
label.pack(fill=Y,expand=1)

scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)


quit=Button(top,text="Quit",command=top.quit,activeforeground='white',activebackground='red')
quit.pack()

mainloop()
