print('---Python基础课-第一章 基本认知---')
print('---1.名字和对象---')
a = 25
A = 56
b = 'Hello Python!'
c = 5.6
d = ['a','b','c']
e = (12,13,14,['c语言','java','Python'])
dict1 = {"李宁":"一切皆有可能",
         "耐克":"Just do it",
         "我用Python":"人生苦短"}

print(type(a))
print(type(A))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(dict1))
print('李宁的口号是：',dict1['李宁'])

print('---2.关键字---')
import keyword #导入keyword模块
print(keyword.kwlist)#使用此方法列出所有的关键字
print('判断continue是否是关键字，是则返回True,否则返回False')
print(keyword.iskeyword('continue'))
print(keyword.iskeyword('finally'))
print(keyword.iskeyword('start'))

print('---3.流程---')
print('例子')
if keyword.iskeyword('global'):
    print('global是关键字')
else:
    print('这个单词不是关键字')
print('---4.作用域---')
def fun1(x,y):
    return x+y

jiafa = fun1(a,A)
print(a)
print(A)
print(jiafa)
print('---5.异常---')
print('测试一个异常')
try:
    print(h)
except Exception as e:
    print('这个异常发生的原因：'+str(e))
print('测试一个异常')    
try:
    print(keyword.kwlist('global'))
except Exception as e:
    print('这个异常发生的原因：'+str(e))

print('---6.模块和包---')
import re
print(re.findall(r'y','python'))

