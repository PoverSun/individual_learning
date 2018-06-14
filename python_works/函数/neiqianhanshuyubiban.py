Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> count = 5
>>> def MyFun():
	count = 10
	print(10)

	
>>> MyFun()
10
>>> print(count)
5
>>> def MyFun():
	count = 10
	print(count)

	
>>> MyFun()
10
>>> def MyFun():
	global count
	count = 10
	print(count)

	
>>> MyFun()
10
>>> print(count)
10
>>> def fun1():
	print('fun1()正在被调用。。。')
	def fun2():
		print('fun2()正在被调用...')

		
>>> fun1()
fun1()正在被调用。。。
>>> fun1()
fun1()正在被调用。。。
>>> fun2()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fun2()
NameError: name 'fun2' is not defined
>>> fun2()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    fun2()
NameError: name 'fun2' is not defined
>>> fun1()
fun1()正在被调用。。。
>>> def fun1():
	print('fun1()正在被调用。。。')
	def fun2():
		print('fun2()正在被调用...')
	fun2()

	
>>> fun1()
fun1()正在被调用。。。
fun2()正在被调用...
>>> def Fun(x):
	def FunY(y):
		return x * y
	return FunY

>>> Fun(x)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Fun(x)
NameError: name 'x' is not defined
>>> Fun()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    Fun()
TypeError: Fun() missing 1 required positional argument: 'x'
>>> i = Fun(8)
>>> i
<function Fun.<locals>.FunY at 0x032C4198>
>>> type(i)
<class 'function'>
>>> i(5)
40
>>> Fun(8)(5)
40
>>> def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2

>>> Fun1()
<function Fun1.<locals>.Fun2 at 0x032C4228>
>>> type(Fun2())
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    type(Fun2())
NameError: name 'Fun2' is not defined
>>> Fun1(6)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    Fun1(6)
TypeError: Fun1() takes 0 positional arguments but 1 was given
>>> Fun1(5)(6)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Fun1(5)(6)
TypeError: Fun1() takes 0 positional arguments but 1 was given
>>> def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()

>>> Fun1()
25
>>> def Fun1():
	x = 5
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()

>>> Fun1()
25
>>> 
