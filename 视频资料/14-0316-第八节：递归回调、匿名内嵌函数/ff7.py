#内置函数
'''
len 求长度
min 求最小值
max 求最大值
sorted  排序
reversed 反向
sum  求和

进制转换函数
bin()  转换为二进制
oct()  转换为八进制
hex() 转换为十六进制
ord() 将字符转换成对应的ASCII码值
chr() 将ASCII码值转换成对应的字符
'''

#lambda  匿名函数
'''
关键字lambda用来创建简单的匿名函数。
它既不能包含控制结构也没有return语句，
返回的值就仅仅是表达式计算后得到的值。
使用lambda可以省下函数定义的过程，
可以使得代码更加精简。对于有些只需要使用一两次的函数，
使用lambda也就不需要考虑函数命名的问题。
'''
#作用域
'''
变量的在哪里被赋值的就决定了这个变量作用的区域。
定义在函数外的拥有全局作用域的变量称为全局变量，可以在整个程序
范围内访问，全局变量可以在函数内被访问但不可以在函数内被修改。
定义在函数内部的拥有一个局部作用域的变量称为局部变量，
只能在其被声明的函数内部访问。
'''
#global   用来声明全局变量。
x = 12
def fun():
    a = 24
    global x
    x += a
    return a*a,x
#nonlocal  用来声明使用外层(非全局)变量。
def fun1():
    x = 10
    def fun2():
        nonlocal x
        x +=1
        return x
    return fun2()     
#print(fun1())
#内嵌函数和闭包

def function1(x):
    def function2(y):
        return x+y
    return function2

#递归函数
# 阶乘
'''
1! = 1
2! =1*2
3! = 1*2*3 =2!*3
n! =1*2*....*n = (n-1)!*n
'''
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)*n

#回调函数
from tkinter import *
root = Tk()
root.geometry('400x400+300+100')
def click():
    print('HAHA')
Button(root,text='点我',command=click,bg='red').pack(fill=X,expand=1)
root.mainloop()

