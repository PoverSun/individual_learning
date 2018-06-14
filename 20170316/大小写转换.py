# 题目2：
'''给定一个任意的字符序列，
将字符序列中的大写字母转换成小写，
将小写字母转换成大写'''
def fun(x):
    list1 = list(x)
    for i in range(0,len(list1)):
        if list1[i].islower():
            list1[i]=list1[i].upper()
        elif list1[i].isupper():
            list1[i]=list1[i].lower()
    return list1
    
def converted_case(x):
    try:
        if type(x) == str:
            result = ''.join(fun(x))
        else:
            result = fun(x)
        return result
    except Exception as e:
        print('出错的原因是：'+str(e))
#改进后的代码
def converted_case(x):
    s = ''
    for i in x:
        if i.isupper():
            s += i.lower()
        elif i.islower():
            s += i.upper()
        else:
            s += i
    return type(x)(s)