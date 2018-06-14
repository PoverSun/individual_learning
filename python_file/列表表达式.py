Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [x*x for x in range(0,10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> r = []
>>> for x in range(0,10)
SyntaxError: invalid syntax
>>> for x in range(0,10):
	r.append(x*x)

	
>>> r
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> result = []
>>> for x in range(4):
	for y in range(10,14):
		result.append((x,y))

		
>>> result
[(0, 10), (0, 11), (0, 12), (0, 13), (1, 10), (1, 11), (1, 12), (1, 13), (2, 10), (2, 11), (2, 12), (2, 13), (3, 10), (3, 11), (3, 12), (3, 13)]
>>> [(x,y) for x in range(4) for y in range(10,14)]
[(0, 10), (0, 11), (0, 12), (0, 13), (1, 10), (1, 11), (1, 12), (1, 13), (2, 10), (2, 11), (2, 12), (2, 13), (3, 10), (3, 11), (3, 12), (3, 13)]
>>> result=[]
>>> for x in range(10):
	if x%2==0:result.append(x)

	
>>> result
[0, 2, 4, 6, 8]
>>> [x for x in range(10) if x%2==0]
[0, 2, 4, 6, 8]
>>> girls = ['alice','bernice','clarice']
>>> boys = ['chris','arnold','bob']
>>> result= []
>>> for b in boys:
	for g in girls:
		if b[0]==g[0]:result.append(b+'+'+g)

		
>>> result
['chris+clarice', 'arnold+alice', 'bob+bernice']
>>> [b+'+'+g for b in boys for g in girls if b[0]==g[0]]
['chris+clarice', 'arnold+alice', 'bob+bernice']
>>> 
