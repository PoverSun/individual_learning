# -*-coding:utf-8 -*-
from tkinter import *
import sys

class Calculate(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x400+400+100')
        Label(self.root,text='计算器',font=('Time',15,'bold'),fg='blue').pack()
        self.win1 = Frame()
        self.text = Text(self.win1,width=50,height=15,font=('Time',15,'bold'))
        self.sbar = Scrollbar(self.win1)
        self.sbar.config(command=self.text.yview)
        self.sbar.pack(side=RIGHT,fill=Y)
        self.text.config(yscrollcommand=self.sbar.set)
        self.win = Frame()
        self.ent = Entry(self.win,width=40,font=('Time',15,'bold'))
        self.button = Button(self.win,text='提交',command=self.update)
        self.b1 = Button(self.win,text='退出',command=sys.exit)
        self.ent.bind('<Return>',self.update)
        self.win1.pack()
        self.text.pack()
        self.win.pack()
        self.ent.pack(side=LEFT)
        self.button.pack(side=LEFT)
        self.b1.pack()

    def update(self,event=None):
        self.results = eval(self.ent.get())
        self.output = self.ent.get()+'='+str(self.results)+'\n'
        self.text.insert(END,self.output)

calculate = Calculate()
calculate.root.mainloop()
