class Turtle:
    """
    Pyhton 中的类名约定以大写字母开头
    特征的描述称为属性，在代码层来看其实都是变量
    """
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'


    #方法实际就是函数，通过调用这些函数来完成某些工作
    def climb(self):
        print("我正在努力地向前爬")
    def run(self):
        print("我正在飞快地向前跑")
    def bite(self):
        print("咬死你咬死你")
    def eat(self):
        print("有的吃，真满足T_T")
    def sleep(self):
        print("困了，睡了，晚安，Zzzz")
