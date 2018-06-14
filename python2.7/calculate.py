def yunsuan(userA,userB,operate):
   '运算函数'
   try:
       A = int(userA)
       B = int(userB)
       operate_list = { '+':(A+B),'-':(A-B),'*':(A * B),'/':(A / B)}
       return operate_list[operate]
   except KeyError:
        
       return '%s 没有这个运算' % operate
       
   except ValueError:
          
       return '请给我个数字！'
   except ZeroDivisionError:
              
          return '%s 不能为除数！' % userB
       
def user_input():
    '获取用户输入'
    userA = raw_input('请输入数字A: ')
    userB = raw_input('请输入数字B: ')
    operate = raw_input('请选择运算符号(+、-、*、/)：')
            
    return  yunsuan(userA,userB,operate)
print user_input()
