#针对不同异常设置多个except
try:
    sum = 1 + '1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()

except OSError as reason:
    print('文件出错啦T_T\n错误原因是：' + str(reason))

except TypeError as reason:
    print('类型出错啦T_T\n错误原因是：' + str(reason))
