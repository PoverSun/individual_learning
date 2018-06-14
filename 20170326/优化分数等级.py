def fens():
    while True:
        score = input('请输入您的分数(q退出): ')
        if score == 'q':
            break
        try:
            score = float(score)
            if 90<=score<=100:
                print('A')
            elif 80<=score<90:
                print('B')
            elif 60<=score<80:
                print('C')
            elif 0<=score<60:
                print('D')
        except Exception as e:
            print('输入有误！')
            print('错误原因：'+str(e))
    print('输入有误！')
f = fens()