#p15_2.py
import tkinter as tk

class App:
    def __init__(self,root):
        #创建一个框架，然后在里面添加一个Button按钮组建
        #创建一般是用于在复杂的布局中起到将组建分组的目的
        frame = tk.Frame(root)
        frame.pack()
        #创建一个按钮组件
        self.hi_there = tk.Button(frame,text = "打招呼",fg="blue",command = self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("互联网的广大朋友们大家好，我是小甲鱼！")


#创建一个topLevel的根窗口，并把它作为参数实例化APP对象

root =tk.Tk()
app = App(root)
#开始主循环
root.mainloop()
