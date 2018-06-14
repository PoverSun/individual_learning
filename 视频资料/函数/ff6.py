#控制流程
#while循环
'''
注意：普通应用里，while一定要给一个结束条件，否则就是传说中的死循环
1.while 后面设置退出循环的条件，
         条件不满时退出循环
2.while 后面接值一直为真的条件
        循环体里面通过break来打破这个死循环
'''
'''
循环控制语句总结：
break 
用来终止循环，当循环条件还为真或者序列还没被迭代完，遇到break也会停止循环
continue
用来跳过当次循环的剩余语句，继续执行下一轮的循环
pass 
用来占位，是空语句，没有任何操作，可以保持程序结构的完整。
'''
#关于循环嵌套
#range()
#  m x n =p

for m in range(1,10):
    for n in range(1,m+1):
        print('%s x %s = %s'%(n,m,m*n),end='    ')
    print('')
    
#作业：
    
#打印出九九乘法表
#生成一个100以内能被7整除的列表
#把之前程序封装到函数里，这题不用截图
'''
按下面的要求写出两个求和函数。sum
1.参数为一个列表或元组类型，求里面所有元素的和。
2.参数的个数不限，求所有参数的和。
'''














