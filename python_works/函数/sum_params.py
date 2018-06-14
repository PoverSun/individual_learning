Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
\
>>> def test(*params):
	print('参数的长度是：',len(params));
	print('第二个参数是：',params[1]);

	
>>> test(1,'小甲鱼',3.14,5,6,7,8)
参数的长度是： 7
第二个参数是： 小甲鱼
>>> def test(*params,exp):
	print('参数的长度是：',len(params));
	print('第二个参数是：',params[1]);

	
>>> test(1,'小甲鱼',3.14,5,6,7,8)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    test(1,'小甲鱼',3.14,5,6,7,8)
TypeError: test() missing 1 required keyword-only argument: 'exp'
>>> test(1,'小甲鱼',3.14,5,6,7,exp=8)
参数的长度是： 6
第二个参数是： 小甲鱼
>>> def test(*params,exp=8):
	print('参数的长度是：',len(params));
	print('第二个参数是：',params[1]);

	
>>> test(1,'小甲鱼',3.14,5,6,7,8)
参数的长度是： 7
第二个参数是： 小甲鱼
>>> 
