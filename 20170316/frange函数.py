#题目5：
#写一个属于你自己的 frange函数，frange与range类似，一样的参数规则，但是每一项必须要是float类型
def frange(*x):
    new_list=[]#用来存放自定义函数生成的一个列表
    first = float(list(x)[0])
    end = 0.0
    step = 1.0
    if len(x)==1:
        first = end
        end = float(list(x)[0])
        while first<end:
            new_list.append(first)
            first += step
    elif len(x)==2:
        while first<float(list(x)[1]):
            new_list.append(first)#更新列表
            first += step
    else:
        step = float(list(x)[2])
        while first < float(list(x)[1]):
            new_list.append(first)#更新列表
            first += step
    return print(new_list)
frange(10)
#改进后的代码
#必备参数放在默认参数之前
'''
def frange(start,stop=0.0,step=1):
    if stop == 0.0:
        stop = start
        start = 0.0
    result = []
    while start < stop:
        result.append(float(start))
        start += step
    return result
'''

