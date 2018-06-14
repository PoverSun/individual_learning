#coding：utf-8
import os    #处理文件和目录
import re    #

 #定义学生类
class Student:
    def __init__(self):
        self.name = ''
        self.ID = ''
        self.Score = ''

#增加学生信息
def Add(stulist,stu):
    if searchByID(stulist,stu.ID) ==  True:
        print "此ID存在！"
        return False
    stulist.append(stu)
    print "你想保存这个结果吗？"
    nChoose = raw_input("请输入你的选择：Y/N:")
    if nChoose == 'Y' or nChoose == 'y':
        #将所改变的结果写入文件中
        file_object = open("students.txt","a") #追加模式
        file_object.write(stu.ID)
        file_object.write(" ")

        file_object.write(stu.name)
        file_object.write(" ")

        file_object.write(str(stu.Score))
        file_object.write(" ")
        file_object.write("\n")
        return True
    else:
        stulist.remove(stu) # 否则移除

#根据学号查找学号
def searchByID(stulist,ID):
    for i in range(len(stulist)):
        if stulist[i].ID == ID:
            print "姓名：",
            print stulist[i].name,
            print "学号：",
            print stulist[i].ID,
            print "分数：",
            print stulist[i].Score
            return True
        return False
#如何根据姓名查找
def searchByName(stulist,name):
    for i in range(len(stulist)):
        if stulist[i].name == name:
            print "姓名：",
            print stulist[i].name,
            print "学号：",
            print stulist[i].ID,
            print "分数：",
            print stulist[i].Score
            return True
        return False


#如何初始化,读取文件，目的更新学生信息
def Init(stulist):
    print "初始化........"
    file_object = open("students.txt","r")#r用来读取的
    for line in file_object:
        stu = Student()
        line = line.strip("\n")#去掉换行
        s = line.split(" ")  #用空格分隔成列表
        stu.ID = s[0]
        stu.name = s[1]
        stu.Score = s[2]
        stulist.append(stu)

    print "初始化成功!"


#查找的菜单
def QueryMenu(stulist):
    while True:
        print "**********************************"
        print "根据学生的学号进行查找------1"
        print "根据学生的姓名进行查找------2"
        print "离开查找模块---------------3"
        print "**********************************"
        nChoose = raw_input("请输入你的选择：")
        if nChoose == "1":
            ID = raw_input("请输入要查找的ID：")
            searchByID(stulist,ID)
        elif nChoose == "2":
            name = raw_input("请输入要查找的姓名：")
            searchByName(stulist,name)
        elif nChoose == "3":
            break
        else:
            print "选择输入错误，请重新输入！"



#主菜单
def main(stulist):
    while(True):
        print "**********************************"
        print "-------------菜单-----------------"
        print "--------增加一个学生信息---------1"
        print "--------查找一个学生信息---------2"
        print "--------删除一个学生信息---------3"
        print "--------输出所有学生信息---------4"
        print "--------根据分数排序------------5"
        print "--------退出系统----------------6"
        print "**********************************"

        nChoose = raw_input("请输入你的选择：")
        if nChoose == "1":
            stu = Student()#学生
            stu.name = raw_input("请输入学生的姓名：")
            while True:
                stu.ID = raw_input("请输入学生的学号：")
                p = re.compile('^[0-9]{11}$')
                if p.match(stu.ID):
                    break
                else:
                    print "学生的ID是错误的，请输入正确的ID"

            while True:
                stu.Score = eval(raw_input("请输入学生的分数："))
                if re.match("^[0-9]",str(stu.Score)) and stu.Score <=100 and stu.Score > 0:
                    break
                else:
                    print "分数不满足实际情况，应该为0-100之间的数字"
            if Add(stulist,stu) == True:
                print "学生的信息添加成功！"
            else:
                print "学生的信息添加失败！"

        elif nChoose == "2":
            QueryMenu(stulist) #查找
            print "你想保存这个结果吗？"
            choose = raw_input("请输入你的选择：Y/N！  ")
            if choose == "Y" or choose == "y":
                file_object = open("students.txt","w+")  #读写模式
                for stu2 in stulist:
                    file_object.write(stu2.ID)
                    file_object.write(" ")
                    file_object.write(stu2.name)
                    file_object.write(" ")
                    file_object.write(str(stu2.Score))
                    file_object.write(" ")
                    file_object.write("\n")

        else:
            print "错误 "



if __name__  ==  '__main__':
    stulist = []  #存储所以学生的信息
    Init(stulist)
    main(stulist)
