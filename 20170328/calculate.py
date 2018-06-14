from tkinter import *
import sys
def update(event=None):
        results = eval(ent.get())
        output = ent.get()+'='+str(results)+'\n'
        text.insert(END,output)


root = Tk()
root.geometry('600x400+400+100')
Label(root,text='计算器',font=('Time',15,'bold'),fg='blue').pack()
win1 = Frame()
text = Text(win1,width=50,height=15,font=('Time',15,'bold'))
sbar = Scrollbar(win1)
sbar.config(command=text.yview)
sbar.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=sbar.set)
win = Frame()
ent = Entry(win,width=40,font=('Time',15,'bold'))
button = Button(win,text='提交',command=update)
b1 = Button(win,text='退出',command=sys.exit)
ent.bind('<Return>',update)
win1.pack()
text.pack()
win.pack()
ent.pack(side=LEFT)
button.pack(side=LEFT)
b1.pack()

root.mainloop()

