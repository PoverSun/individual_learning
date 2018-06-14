# 文件输入输出
'''
open函数可以对文本文件进行读写的操作
基本形式：
    open(filename,mode)
 filename是文件名，可以写为绝对路径也可以是相对路径
 mode是打开模式。
 open函数里面有个enconding参数，
 如果打开的文件编码不是gbk,可以通过这个参数来设置编码。
'''

# 文件的打开模式：
'''
r 只读模式，文件不存在时会报错。
w 写入模式，文件存在会清空之前的内容，文件不存在则会新建文件。
x 写入模式，文件存在会报错，文件不存在则会新建文件。
a 追加写入模式，不清空之前的文件，直接将写入的内容添加到后面。
b 以二进制模式读写文件，wb,rb,ab。
+ 可读写模式，r+,w+,x+,a+,这几种模式还遵循了r,w,x,a的基本原则。
'''
# 文件对象方法
#读取文件内容：read()，readline()，readlines()：
'''
f.read(size) 读取文件的内容，将文件的内容以字符串形式返回。
size是可选的数值，指定字符串长度，如果没有指定size或者指定为负数，
就会读取并返回整个文件。当文件大小为当前机器内存两倍时就会产生问题，
反之就尽可能大的size读取和返回数据，如果到了文件末尾，会返回空字符串。

f.readline() 从文件中读取单独一行，字符串结尾会自动加上一个换行符\n，
只有当文件最后遗憾没有以换行符结尾时，这一操作才会被忽略，
这样返回值就不会有混淆。如果返回空字符串，表示到达率文件末尾，
如果是空行，就会描述为\n,一个只有换行符的字符串。

f.readlines() 返回一个列表，列表的元素为文件行的内容。
可以通过列表索引的方式将文件的每一行的内容输出。
可以通过for循环迭代输出每一行的信息。
'''
#文件的写入：write() , writelines()：
'''
f.write() 将要写入的内容以字符串的形式通过write方法写入文件中。
f.writelines() 括号里必须是由字符串元素组成的序列。
'''
#内容的保存和关闭：flush() , close()：
'''
f.flush()在读写模式下，当写完的数据想要读取出来时，
要先缓存区的内容保存到文件当中。
f.close() 关闭文件。对一个已经关闭的文件进行操作会报错。
'''
#光标位置：tell() , seek()：
'''
f.tell() 返回光标在文件中的位置。
f.seek(offset,from)在文件中移动文件指针，
从from(0代表起始位置，1代表当前位置，2代表文件末尾)偏移offset个字节。
'''
#查看文件信息：closed , mode , name ：
'''
closed 查看文件是否已经关闭，返回布尔值。
mode 返回文件打开模式。
name 返回文件名。
'''
# with 形式打开文件，里面的语句执行完后会自动关闭文件。
'''
with open('文件名') as f:
    f.read() 
'''
try:
    print(111)
    f1 = open('super.py')
    raise FileNotFoundError
    print(1+'12')
    print(a)

except (NameError,TypeError) as e:
    print('xxxxxx',e)

except FileNotFoundError:
    print('文件不存在')
else:
    print('nnnnn')
finally:
    f1.close()
print(444)


# 异常
# 异常处理程序常规语法
'''
try:
    suite1        #测试语句块
except exception1:
    suite2        #如果测试语句suite1中发生exception1异常时执行
except (exception2,exception3):
    suite3       #如果测试语句suite1中发生元组中任意异常时执行
except exception4 as reason:    #as把异常的原因赋值给reason
    suite4       #如果测试语句suite1发生exception4的异常时执行
except:
    suite5      #如果测试语句suite1发生异常在所列出的异常之外时执行
else:
    suite5      #如果测试语句块suite1中没有发生异常时执行
finally:
    suit6       #不管测试语句suite1中又没有发生异常都会执行

注意：中间的except，else，finally都是可选的
              但至少有一个，不然try就没有意义了，根据实际中的需求来选择。
'''


# raise 触发异常
# 使用raise语句自己触发异常

# assert断言：用来声明某个条件是真的
# 如果条件是假的则会抛出AssertionError异常

#作业：
'''
1.打开文件，修改内容，写入另一个文件。
  把文件reform.txt中的名人名言改成“某某说：......”的形式保存到另一个文件中。
2.分数等级测试程序中加入异常处理来解决用户输入不合理的情况。
3.
'''



