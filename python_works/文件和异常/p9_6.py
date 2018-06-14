try:
    f = open('record.txt')
    print(f.read())
    sum = 1 + '1'
    f.close()

except:
    print('出错啦')
