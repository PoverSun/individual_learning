#题目1
#给定一个任意的序列，对这个序列进行逆序输出
def reversed_sequence(x):
    if type(x) == str:
        list1 = list(x)
        list1.reverse()
        result = ''.join(list1)
    else:
        list1 = list(x)
        list1.reverse()
        result = tuple(list1)
        
    return result
#优化后的代码

def reversed_sequence(x):
    list1 = list(x)# list1 = reversed(x)
    list1.reverse()
    if type(x) == str:
        return ''.join(list1)
    return type(x)(list1)
