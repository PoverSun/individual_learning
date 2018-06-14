#捕获异常操作
try:
    file_name = input('请用户输入文件名称：')
    f = open(file_name)
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了T_T\n错误原因是：'+ str(reason))
