#!/usr/bin/env python
#tkhello3.py
import tkinter

top=tkinter.Tk()  #创建顶层窗口
hello=tkinter.Label(top,text='Hello World!')
hello.pack()

quit=tkinter.Button(top,text='退出',command=top.quit,bg='red',fg='white')  #创建按钮组件
quit.pack(fill=tkinter.X,expand=1)   #指定用包管理器放置组件
tkinter.mainloop()  #进入主循环，启动执行
