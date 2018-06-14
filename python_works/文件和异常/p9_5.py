#对多个异常统一处理
#except后边还可以跟多个异常，然后对这些异常进行统一处理：


try:
    int('abc')
    sum = 1 +'1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()

except(OSError,TypeError,ValueError) as reason:
    print('出错啦T_T\n错误原因是：' + str(reason))


    
