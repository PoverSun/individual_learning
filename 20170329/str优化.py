'''
将字符串的四个方法写到一个类中，要求这个类继承str的方法
'''
class Best_str(str):
    def __init__(self,x):
        self.x = x

    #大小写转换
    def converted_case(self,x):
        self.s = ''
        self.x = x
        for i in self.x:
            if i.isupper():
                self.s += i.lower()
            elif i.islower():
                self.s += i.upper()
            else:
                self.s += i
        return type(self.x)(self.s)
    #逆序输出字符串
    def reversed_sequence(self,x):
        self.x = x
        self.list1 = list(x)# list1 = reversed(x)
        self.list1.reverse()
        if type(self.x) == str:
            return ''.join(self.list1)
        return type(self.x)(self.list1)
    #升降序判断
    def which_order(self,x):
        self.x = x
        if sorted(self.x) == list(self.x):
            return 'UP'
        elif list(reversed(sorted(self.x))) == list(self.x):
            return 'DOWN'
        else:
            return
    #统计字符串中单词的个数
    def charcount(self,x):
        self.x = x
        dic = {'whitespace':0,'other':0}
        for i in range(97,123):
            i = chr(i)
            dic[i] = 0
        text = list(self.x)
        for i in self.x.lower():
            if i in dic.keys():
                dic[i] += 1
            elif i == ' ':
                dic['whitespace'] += 1
            else:
                dic['other'] += 1
        return dic
