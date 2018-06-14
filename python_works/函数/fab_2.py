def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    elif n== 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
number = int(input('请输入需要经过多少个月份:'))
result = fab(number)
print(result)
