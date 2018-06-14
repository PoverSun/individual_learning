#猜数字游戏
import random
print("-------------欢迎来玩猜字游戏---------------")
print("--------提示：输入一个数字，猜猜看^_^-------")
print("------如果想要退出游戏，请输入字母:Q或q-----")
def fun(user_num,rand_num):
     if user_num == rand_num:
        print("^_^恭喜你，猜对了！^_^")
        print("哇哦，厉害了，Word哥！你真棒")
        flag = 1
     elif user_num > rand_num:
        print("***你猜的数字大了，继续努力吧***")
     else:
        print("---很遗憾，猜小了，继续努力吧---")


def start():
    rand_num = random.randint(0,10) #生成一个随机数
    user_num = input("请输入你猜的数字：\n")
    if user_num.isdigit():
        user_num = int(user_num)
        fun(user_num,rand_num)
    elif user_num == 'Q' or user_num == 'q':
        print("你确定退出游戏吗？确定---y/Y,继续游戏---n/N")
        op1 = input("请输入你的选择：\n")
        if op1 == 'y' or op1 == 'Y':
            print("退出游戏，，，，")
            exit(0)
    else:
        print('你输入的不是数字，请重新输入！！！')

cishu = 1
while cishu<=3:
    start()
    cishu += 1
    flag = str(flag)
    if flag:
        pass
    else:
        print('很遗憾，最多只能猜3次，你3次都没有猜中，欢迎下次再来！！！')

