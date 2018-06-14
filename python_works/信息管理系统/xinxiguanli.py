#coding��utf-8
import os    #�����ļ���Ŀ¼
import re    #

 #����ѧ����
class Student:
    def __init__(self):
        self.name = ''
        self.ID = ''
        self.Score = ''

#����ѧ����Ϣ
def Add(stulist,stu):
    if searchByID(stulist,stu.ID) ==  True:
        print "��ID���ڣ�"
        return False
    stulist.append(stu)
    print "���뱣����������"
    nChoose = raw_input("���������ѡ��Y/N:")
    if nChoose == 'Y' or nChoose == 'y':
        #�����ı�Ľ��д���ļ���
        file_object = open("students.txt","a") #׷��ģʽ
        file_object.write(stu.ID)
        file_object.write(" ")

        file_object.write(stu.name)
        file_object.write(" ")

        file_object.write(str(stu.Score))
        file_object.write(" ")
        file_object.write("\n")
        return True
    else:
        stulist.remove(stu) # �����Ƴ�

#����ѧ�Ų���ѧ��
def searchByID(stulist,ID):
    for i in range(len(stulist)):
        if stulist[i].ID == ID:
            print "������",
            print stulist[i].name,
            print "ѧ�ţ�",
            print stulist[i].ID,
            print "������",
            print stulist[i].Score
            return True
        return False
#��θ�����������
def searchByName(stulist,name):
    for i in range(len(stulist)):
        if stulist[i].name == name:
            print "������",
            print stulist[i].name,
            print "ѧ�ţ�",
            print stulist[i].ID,
            print "������",
            print stulist[i].Score
            return True
        return False


#��γ�ʼ��,��ȡ�ļ���Ŀ�ĸ���ѧ����Ϣ
def Init(stulist):
    print "��ʼ��........"
    file_object = open("students.txt","r")#r������ȡ��
    for line in file_object:
        stu = Student()
        line = line.strip("\n")#ȥ������
        s = line.split(" ")  #�ÿո�ָ����б�
        stu.ID = s[0]
        stu.name = s[1]
        stu.Score = s[2]
        stulist.append(stu)

    print "��ʼ���ɹ�!"


#���ҵĲ˵�
def QueryMenu(stulist):
    while True:
        print "**********************************"
        print "����ѧ����ѧ�Ž��в���------1"
        print "����ѧ�����������в���------2"
        print "�뿪����ģ��---------------3"
        print "**********************************"
        nChoose = raw_input("���������ѡ��")
        if nChoose == "1":
            ID = raw_input("������Ҫ���ҵ�ID��")
            searchByID(stulist,ID)
        elif nChoose == "2":
            name = raw_input("������Ҫ���ҵ�������")
            searchByName(stulist,name)
        elif nChoose == "3":
            break
        else:
            print "ѡ������������������룡"



#���˵�
def main(stulist):
    while(True):
        print "**********************************"
        print "-------------�˵�-----------------"
        print "--------����һ��ѧ����Ϣ---------1"
        print "--------����һ��ѧ����Ϣ---------2"
        print "--------ɾ��һ��ѧ����Ϣ---------3"
        print "--------�������ѧ����Ϣ---------4"
        print "--------���ݷ�������------------5"
        print "--------�˳�ϵͳ----------------6"
        print "**********************************"

        nChoose = raw_input("���������ѡ��")
        if nChoose == "1":
            stu = Student()#ѧ��
            stu.name = raw_input("������ѧ����������")
            while True:
                stu.ID = raw_input("������ѧ����ѧ�ţ�")
                p = re.compile('^[0-9]{11}$')
                if p.match(stu.ID):
                    break
                else:
                    print "ѧ����ID�Ǵ���ģ���������ȷ��ID"

            while True:
                stu.Score = eval(raw_input("������ѧ���ķ�����"))
                if re.match("^[0-9]",str(stu.Score)) and stu.Score <=100 and stu.Score > 0:
                    break
                else:
                    print "����������ʵ�������Ӧ��Ϊ0-100֮�������"
            if Add(stulist,stu) == True:
                print "ѧ������Ϣ��ӳɹ���"
            else:
                print "ѧ������Ϣ���ʧ�ܣ�"

        elif nChoose == "2":
            QueryMenu(stulist) #����
            print "���뱣����������"
            choose = raw_input("���������ѡ��Y/N��  ")
            if choose == "Y" or choose == "y":
                file_object = open("students.txt","w+")  #��дģʽ
                for stu2 in stulist:
                    file_object.write(stu2.ID)
                    file_object.write(" ")
                    file_object.write(stu2.name)
                    file_object.write(" ")
                    file_object.write(str(stu2.Score))
                    file_object.write(" ")
                    file_object.write("\n")

        else:
            print "���� "



if __name__  ==  '__main__':
    stulist = []  #�洢����ѧ������Ϣ
    Init(stulist)
    main(stulist)
