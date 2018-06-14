import tkinter as tk

class App:
    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame,text = "打招呼"，fg = command = self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("我用Python")

root = tk.Tk()
app = App(root)

root.mainloop()

