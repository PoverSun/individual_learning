#2.输出100以内的所有素数，素数之间以一个空格区分。
#判断是否为素数
def isSuShu(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
sushu_list = []#用来存放素数
no_sushu_list = [] #用来存放其他数
for x in range(101):
    if isSuShu(x) == True:
        sushu_list.append(x)
    else:
        no_sushu_list.append(x)
print("1-100之间的所有素数为：",end=' ')
for i in sushu_list:
    print(i,end=" ")

#改进后的代码
def susu():
    x = []
    for i in range(2,100):
        for j in range(1,i):
            if i % j == 0:
                break
            else:
                x.append(str(i))

    return ' '.join(x)


