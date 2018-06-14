#!/usr/bin/env python
#tkhello1.py
import tkinter

top=tkinter.Tk()  #创建顶层窗口
label=tkinter.Label(top,text='Hello World!')  #创建标签组件
label.pack()   #指定用包管理器放置组件
tkinter.mainloop()  #进入主循环，启动执行
