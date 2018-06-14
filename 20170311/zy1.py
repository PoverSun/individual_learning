#分数等级测试
while True:
    score = input("请输入你要测试的成绩：\n")
    if score.isdigit():
        score = int(score)
        if score >= 90 and score <= 100:
            print('分数等级----A')
        elif score >= 80 and score < 90:
            print('分数等级----B')
        elif score >= 60 and score < 80:
            print('分数等级----C')
        elif score >=0 and score < 60:
            print('分数等级----D')
        else:
            print('输入的成绩有误，请重新输入！！！')
    else:
        print('你输入的不是数字，请重新输入！！！')
