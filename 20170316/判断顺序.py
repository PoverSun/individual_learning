# 题目3：
#输入一个序列，判断这个序列是升序，降序还是无序。
def which_order(x):
    if type(x) == str:
        fun(x)
    elif type(x)==list:
        fun(x)

def fun(x):
    default_list = list(x)#转换成列表
    new_list = [] #用来存放将字符转换成对应的ASCII码的值
    for i in default_list:
        if type(i) == int:
            j = int(i)
            new_list.append(j)
        elif i.islower() or i.isupper():
            j = ord(i)
            new_list.append(j)
        else:
            j = int(i)
            new_list.append(j)
    new_up_list = sorted(new_list)
    new_down_list = list(reversed(new_up_list))
    if new_list ==new_up_list:
        print('UP')
    elif new_list == new_down_list:
        print('DOWN')
    else:
        print(None)
which_order([1,2,3])
        
