def yunsuan(userA,userB,operate):
   '���㺯��'
   try:
       A = int(userA)
       B = int(userB)
       operate_list = { '+':(A+B),'-':(A-B),'*':(A * B),'/':(A / B)}
       return operate_list[operate]
   except KeyError:
        
       return '%s û���������' % operate
       
   except ValueError:
          
       return '����Ҹ����֣�'
   except ZeroDivisionError:
              
          return '%s ����Ϊ������' % userB
       
def user_input():
    '��ȡ�û�����'
    userA = raw_input('����������A: ')
    userB = raw_input('����������B: ')
    operate = raw_input('��ѡ���������(+��-��*��/)��')
            
    return  yunsuan(userA,userB,operate)
print user_input()
