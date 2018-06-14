Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def myFirstFunction(name):
	print(name)

	
>>> myFirstFuntion('晓冬')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myFirstFuntion('晓冬')
NameError: name 'myFirstFuntion' is not defined
>>> myFirstFunction('晓冬')
晓冬
>>> def exchangeRate(dollar):
	"""美元—>人民币
        汇率暂时定为6.5
        """
	return dollar * 6.5

>>> exchangeRate(100)
650.0
>>> exchangeRate.__doc__
'美元—>人民币\n        汇率暂时定为6.5\n        '
>>> help(exchangeRate)
Help on function exchangeRate in module __main__:

exchangeRate(dollar)
    美元—>人民币
    汇率暂时定为6.5

>>> def saySomething(name,words)
SyntaxError: invalid syntax
>>> def saySomething(name,words):
	print(name + '->' + words)

	
>>> saySomething("小甲鱼","让编程改变世界！")
小甲鱼->让编程改变世界！
>>> saySomething("让编程改变世界！","小甲鱼")
让编程改变世界！->小甲鱼
>>> saySomething(words="让编程改变世界！",name="小甲鱼")
小甲鱼->让编程改变世界！
>>> def greet_user():
	"""显示简单的问候语！！"""
	print("Hello,王集平！！！")

	
>>> greet_user()
Hello,王集平！！！
>>> def greet_user(username):
	"""显示简单的问候语"""
	print("Hello, " + username.title() + "!")

	
>>> greet_user('jesse')
Hello, Jesse!
>>> 
>>> greet_user('sarah')
Hello, Sarah!
>>> 
