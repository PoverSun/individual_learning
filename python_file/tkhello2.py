#!/usr/bin/env python
#tkhello2.py
import tkinter

top=tkinter.Tk()  #创建顶层窗口
quit=tkinter.Button(top,text='Hello World!',command=top.quit)  #创建按钮组件
quit.pack()   #指定用包管理器放置组件
tkinter.mainloop()  #进入主循环，启动执行
