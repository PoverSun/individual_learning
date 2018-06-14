def ss():
    while True:
        score = input('请输入您的分数（q退出）：')
        if score == 'q':
            break
        elif score == '':
            continue
        _score = score.replace('.','',1)
        if _score.isdigit():
            #if _score==score:
                #score = int(score)
            #else:
            score = float(score)
            if 90<=score<=100:
                print('A')
            elif 80<=score<90:
                print('B')
            elif 60<=score<80:
                print('C')
            elif 0<=score<60:
                print('D')
            else:
                print('输入有误')
        else:
            print('输入有误')
