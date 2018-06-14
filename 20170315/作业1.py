'''#打印九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            print('%s x %s = %s'%(i,j,i*j),end='  ')
    print('')#换行
#生成一个n以内能被m整除的列表,此处的n是整数，n,m让用户自己输入
list1 = []#创建一个空的列表，用来存放被7整除的数
def fun(n,m):
    for i in range(n):
            if i % m == 0:# 从0开始，0也能被7整除
                list1.append(i)
    print('%s以内能被%s整除的数构成的列表： '%(n,m)+str(list1))
    return list1
def run(n,m):
    if n.isdigit():
        n = int(n)
        if m.isdigit():
            m = int(m)
            fun(n,m)
        else:
            print('你输入的m不是整数，请重新输入')
    else:
        print('你输入的n不是整数，请重新输入')

while True:
    print("----1.进入程序----")
    print("----q.退出程序----")
    print("----Q.退出程序----")
    op = input('请选择输入一个操作数： ')
    if op.isdigit():
        op = int(op)
        if op == 1:
            n = input('请输入一个范围的最大数n:')
            m = input('请输入一个除数m:')
            run(n,m)
        else:
            print('输入有误，请重新输入')
    elif op == 'q' or op == 'Q':
        exit(0)
'''






