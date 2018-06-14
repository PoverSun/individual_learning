try:
    f = open('data.txt','w')
    for each_line in f:
        print(each_line)


except OSError as reason:
    print('出错了：' + str(reason))

finally:
    f.close()
