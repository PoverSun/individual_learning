def hanoi(n,x,y,z):
    """汉诺塔"""
    if n == 1:
        print(x,'-->',z) #如果只有一层，直接从x移动到z

    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        print(x,'-->',z)#将最底下的第64个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将Y上的63个盘子移动到z上

num = int(input('请输入要操作的数字：0/1'))

while(num == 1):
    n = int(input('请输入汉诺塔的层数：'))
    hanoi(n,'X','Y','Z')
if num == 0:
    print('退出程序！！！') 
