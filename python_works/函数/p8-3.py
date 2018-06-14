def make_shirt(shirt_size,shirt_fontstyle):
    print("T恤的尺码：%s,T恤的字样：%s" %(shirt_size,shirt_fontstyle))
print('使用位置实参来调用这个函数完成习题：\n')   
make_shirt('\tXXL','Fover-love-to-my-love\n')
print('使用关键字实参来调用这个函数完成习题：\n')   
make_shirt(shirt_size = '\tXL',shirt_fontstyle = 'I beleve Myself,and I can success!')
