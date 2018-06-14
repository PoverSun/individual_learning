
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
from tkinter import filedialog
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import fileinput
from tkinter import *
from os import *
import os
import time
 
t1 = []
root = None
 
def die():
    root.destroy()
 
def about():
    messagebox.showinfo(title = "当前版本为1.0,欢迎使用",message = "**作者:韩东\n**状态:继续努力ing")
class editor:
    def __init__(self,rt):
        if rt == None:
            self.t = tk.Tk()
        else:
            self.t = tk.Toplevel(rt)
        self.t.title("文本编辑器%d" % (len(t1)+1))
        self.bar = tk.Menu(rt)
 
        self.filem = tk.Menu(self.bar)
        self.filem.add_separator()
        self.filem.add_command(label = "新建",command = self.neweditor)
        self.filem.add_separator()
        self.filem.add_command(label = "打开",command = self.openfile)
        self.filem.add_separator()
        self.filem.add_command(label = "保存",command = self.savefile)
        self.filem.add_separator()
        self.filem.add_command(label = "关闭",command = self.close)
        self.filem.add_separator()
        self.filem.add_command(label = "退出",command = die)
 
        self.editm = tk.Menu(self.bar)
        self.editm.add_separator()
        self.editm.add_command(label = "复制",command = self.copy)
        self.editm.add_separator()
        self.editm.add_command(label = "黏贴",command = self.paste)
        self.editm.add_separator()
        self.editm.add_command(label = "剪切",command = self.cut)
        self.editm.add_separator()
        self.editm.add_command(label = "删除",command = self.delete_text)
        self.editm.add_separator()
        self.editm.add_command(label = "查找",command = self.find_char)
        self.editm.add_separator()
        self.editm.add_command(label = "全选",command = self.select_char_all)
 
 
        self.helpm = tk.Menu(self.bar)
        self.helpm.add_command(label = "关于",command = about)
        self.bar.add_cascade(label = "文件",menu = self.filem)
        self.bar.add_cascade(label = "编辑",menu = self.editm)
        self.bar.add_cascade(label = "帮助",menu = self.helpm)
         
        self.t.config(menu = self.bar)
 
        self.f = tk.Frame(self.t,width = 512)
        self.f.pack(expand =1)
 
        self.st = tkst.ScrolledText(self.t)
        self.st.pack(expand = 1)
 
    def close(self):
        self.t.destroy()
    def openfile(self):
        oname = filedialog.askopenfilename(filetypes = [("打开文件","*.txt")])
        if oname:
            for line in fileinput.input(oname):
                self.st.insert("1.0",line)
            self.t.title(oname)
 
    def savefile(self):
        sname = filedialog.asksaveasfilename(title = "保存好你的宝宝哟",filetypes = [("保存文件","*.txt")])
        if sname:
            ofp = open(sname,"a")
            ofp.write(self.st.get(1.0,tk.END))
            ofp.flush()
            ofp.close()
            self.t.title(sname)
 
    def neweditor(self):
        global root
        t1.append(editor(root))
    def copy(self):
        text = self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
        self.st.clipboard_clear()
        self.st.clipboard_append(text)
    def paste(self):
        try:
            text = self.st.selection_get(selection = "CLIPBOARD")
            self.st.insert(tk.INSERT,text)
        except tk.TclError:
            pass
         
    def cut(self):
        text = self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
        self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
        self.st.clipboard_clear()
        self.st.clipboard_append(text)
         
    def delete_text(self):
        self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
 
    def find_char(self):
        target = simpledialog.askstring("简易文本编辑器","寻找字符串")
        if target:
            end = self.st.index(tk.END)
            endindex = end.split(".")
            end_line = int(endindex[0])
            end_column = int(endindex[1])
            pos_line =1
            pos_column=0
            length =len(target)
            while pos_line <= end_line :
                if pos_line == end_line and pos_column +length > end_column:
                    break
                elif pos_line < end_line and pos_column + length >100:
                   pos_line = pos_line + 1
                   pos_column = 100 - (pos_column + length)
                   if pos_column > end_column:
                        break
                else:
                    pos = str(pos_line)+"."+str(pos_column)
                    where = self.st.search(target,pos,tk.END)
                    if  where:
                        print(where)
                        where1 =where.split(".")
                        sele_end_col = str(int(where1[1])+length)
                        sele = where1[0] + "."+ sele_end_col
                        self.st.tag_add(tk.SEL,where,sele)
                        self.st.mark_set(tk.INSERT,sele)
                        self.st.see(tk.INSERT)
                        #self.st.focus()
                 
                        again = messagebox.askokcancel(title = "继续查询么")
                        if again:
                            pos_line = int(where1[0])
                            pos_column = int(sele_end_col)
                        else:
                            aa=messagebox.showinfo(title = "你终于还是放弃了我",message = "你放弃了我--!")
                            if aa:
                                sys.exit()
                                 
 
    def select_char_all(self):
        self.st.tag_add(tk.SEL,1.0,tk.END)
        self.st.see(tk.INSERT)
        self.st.focus()
if __name__ == "__main__":
    root = None
    t1.append(editor(root))
    root = t1[0].t
    root.mainloop()
