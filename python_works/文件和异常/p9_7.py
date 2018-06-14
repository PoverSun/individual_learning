#就算出现异常，也会执行收尾工作


try:
    f = open('record.txt')
    print(f.read())
    sum = 1 + '1'


except:
    print('出错了')

finally:
    f.close()

   
#测试是否关闭文件
print(f.read())
"""Traceback (most recent call last):
  File "F:/python_works/文件和异常/p9_7.py", line 18, in <module>
    print(f.read())
ValueError: I/O operation on closed file."""
