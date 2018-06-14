#p15_1.py



import tkinter as tk

#创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()
#设置主窗口对象的标题栏
root.title("FishC Demo")
#添加一个label标签
#Label表签中可以显示文本、图标、或者图片
#在这里我们让它显示制定的文本
theLabel = tk.Label(root,text = "我的第二个窗口程序！")
#然后调用Label组件的pack()方法，用于自动调节组件自身的尺寸
theLabel.pack()
#显示窗口
root.mainloop()
