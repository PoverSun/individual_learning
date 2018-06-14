#1.利用递归写斐波那契数列的函数f(n)。
def f(n):
    if n < 1:
        print('对不起，您输入的数值不符合要求，请重新输入！')
    elif n == 1 or n ==2:
        return 1
    else :
        return f(n-1)+f(n-2)
    #循环输出斐波那契数列
    return f(n)

n = input("请输入一个n值:")
if n.isdigit():
    n = int(n)
    new_list = []
    if n < 1:
        print('对不起，您输入的数值不符合要求，请重新输入！')
    else:
        for i in range(1,n):
            new_list.append(f(i))
        print('斐波那契数列：'+str(new_list))

