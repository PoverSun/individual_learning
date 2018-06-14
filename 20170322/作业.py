class People:
    def __init__(self,name,sex,age):
        self.name = name #名字
        self.sex = sex  #性别
        self.age = age  #年龄

    def run(self):
        """模拟人的跑步"""
        print(self.name.title() + ' is now running.')

    def eat(self):
        print(self.name.title() + ' is eatting now.')
# p = People('xiaodong','男',22)
# p.run()
# p.eat()
class Student(People):
    "学生类与人的不同"
    def __init__(self,name,sex,age,score):
        super().__init__(name,sex,age)
        self.score = score
    def pingce(self):
        if 60 >=self.score >= 0:
            print('分数----等级D')
        elif 80 >= self.score >= 60:
            print('分数----等级C')
        elif 90 > self.score >=80:
            print('分数----等级B')
        elif 100 >= self.score >=90:
            print('分数----等级A')
        else:
            print('您输入的数据不合法！')

s = Student('xiaodong','男','22',98)
s.pingce()