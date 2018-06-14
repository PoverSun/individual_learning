1 # -*- coding: utf-8 -*-
  2 from __future__ import unicode_literals
  3 from HttpClient import HttpClient
  4 import sys,re,os
  5 from threading import Thread
  6 from Queue import Queue
  7 from time import sleep
  8 
  9 q = Queue()#图片集url队列
 10 imgCount = 0
 11 class getRosiUrl(HttpClient):#一级url爬取类
 12     def __init__(self):
 13         self.__pageIndex = 1
 14         self.__Url = "http://www.5442.com/tag/rosi/"
 15         self.__refer = 'http://www.5442.com/tag/rosi.html'
 16 　　#将爬取的图片集url放入队列
 17     def __getAllPicUrl(self,pageIndex):
 18         realurl = self.__Url + str(pageIndex) + ".html"
 19         print realurl
 20         pageCode = self.Get(realurl,self.__refer)
 21         type = sys.getfilesystemencoding()
 22         #print pageCode[0:1666].decode("gb2312",'ignore').encode(type)
 23         pattern = re.compile('<div.*?title">.*?<span><a href="(.*?)".*?</a>',re.S)
 24         items = re.findall(pattern,pageCode.decode("gb2312",'ignore').encode(type))
 25         for item in items:
 26             #print item
 27             global q
 28             q.put(item)
 29             #print "放入队列"
 30 　　#得到最新页码
 31     def __getNewPage(self):
 32         pageCode = self.Get("http://www.5442.com/tag/rosi.html",self.__refer)
 33         type = sys.getfilesystemencoding()
 34         pattern = re.compile(r'<ul.*?<li .*?pageinfo">(.*?)</li>',re.S)
 35         newPage = re.search(pattern,pageCode.decode("gb2312",'ignore').encode(type))
 36         num  = re.search("[0-9]+",newPage.group(1).decode("gb2312",'ignore').split("/")[0]).group()
 37         if newPage != None:
 38             return int(num)
 39         return 0
 40 
 41     def start(self):
 42         page = self.__getNewPage()
 43         for i in range(1,page):
 44             self.__getAllPicUrl(i)
 45 
 46 #图片下载类
 47 class downloadImg(HttpClient):
 48     def __init__(self):
 49         self.__pageIndex = 1
 50         self.__floder = "rosi"
 51         self.__Url = "http://www.5442.com/meinv/20150904/27058.html"
 52         self.__refer = 'http://www.5442.com/tag/rosi.html'
 53     def __getNewPage(self):
 54         pageCode = self.Get(self.__Url,self.__refer)
 55         type = sys.getfilesystemencoding()
 56         pattern = re.compile(r'<ul.*?<li>.*?<a>(.*?)</a></li>',re.S)
 57         newPage = re.search(pattern,pageCode.decode("gb2312",'ignore').encode(type))
 58         if newPage !=None: 59             num = re.search("[0-9]+",newPage.group(1).decode("gb2312",'ignore').split("/")[0]).group() 60             return int(num)
 61         return 0
 62 　　#得到图片集名称
 63     def __getBookName(self):
 64         pageCode = self.Get(self.__Url,self.__refer)
 65         type = sys.getfilesystemencoding()
 66         pattern = re.compile(r'<h1><a.*?>(.*?)</a>',re.S)
 67         title = re.findall(pattern,pageCode.decode("gb2312",'ignore').encode(type))
 68         if title != None:
 69             return title[0]
 70         return "未命名"
 71 　　#得到每页图片url
 72     def __getAllPicUrl(self,pageIndex):
 73         realurl = self.__Url[:-5] + "_" + str(pageIndex) + ".html"
 74         pageCode = self.Get(realurl)
 75         type = sys.getfilesystemencoding()
 76         pattern = re.compile('<p align="center" id="contents">.*?<a.*?<img src=(.*?) alt=.*?>',re.S)
 77         items = re.findall(pattern,pageCode.decode("gb2312",'ignore').encode(type))
 78         self.__savePics(items,self.__floder)
 79 　　#下载保存图片
 80     def __savePics(self,img_addr,folder):
 81         for item in img_addr:
 82             filename = self.__floder + "\\" +item.split('/')[-1][:-1]
 83             print "正在保存图片：" + filename
 84             print item[1:-1]
 85             with open(filename,'wb') as file:
 86                 img = self.Get(item[1:-1])
 87                 file.write(img)
 88             global imgCount
 89             imgCount = imgCount + 1
 90     def start(self):
 91         while True:
 92             global q
 93             self.__Url = q.get()#从队列中取出一条图片集url
 94             title = self.__getBookName()
 95             self.__floder = os.getcwd() + "\\rosi\\" + title.decode("gb2312",'ignore')
 96             isExists=os.path.exists(self.__floder)
 97             if not isExists:
 98                 type = sys.getfilesystemencoding()
 99                 os.mkdir(self.__floder)
100 
101             page = self.__getNewPage() + 1
102             for i in range(self.__pageIndex,page):
103                 self.__getAllPicUrl(i)
104 
105             q.task_done()#完成一项任务
106 
107 
108         
109 
110 if __name__ == '__main__':
111     isExists=os.path.exists("rosi")#创建保存目录
112     if not isExists:
113         os.mkdir("rosi")
114     for i in range(5):#新建5个线程 等待队列
115         print i
116         downImg = downloadImg()
117         t = Thread(target=downImg.start)
118         t.setDaemon(True)
119         t.start()
120     rosi = getRosiUrl()
121     rosi.start()
122 
123     q.join
