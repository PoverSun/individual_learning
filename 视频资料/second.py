while True:
    score = input('输入你的分数：')
    try:
        # 先尝试把客户当成好人
        floated_score = float(score)
        if floated_score >= 90:
            print('A')
        elif floated_score >= 80:
            print('B')
        elif floated_score >= 65:
            print('C')
        else:
            print('不及格')
    except ValueError as err:
        # 不能把字符串，转换成浮点
        print(err, '智能忽略')
        # 这一次循环已经结束了


print('程序没问题，继续运行了')


while True:
    score = input('输入你的分数：')
    if not score.replace('.', '').isdigit():
        if score == 'q': break
        continue
    floated_score = float(score)
    if floated_score >= 90:
        print('A')
    elif floated_score >= 80:
        print('B')
    elif floated_score >= 65:
        print('C')
    else:
        print('不及格')
