def recursion(n):
    """阶乘函数的算法"""
    final = n
    for i in range(1,n):
        final *= i

    return final



number = int(input("请输入一个整数："))
final = recursion(number)
print('%d的阶乘是：%d'% (number,final))
