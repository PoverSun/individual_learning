from tkinter import *
import urllib.request,urllib.parse
import json

def translate(event=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    content = text1.get(1.0,END)
    text2.delete(1.0,END)
    if '\n' == content[0]:
        content = '空'
    print(repr(content))
    data={
        'type':'AUTO',
        'i':content,
        'doctype':'json',
        'xmlVersion':1.8,
        'keyfrom':'fanyi.web',
        'ue':'UTF-8',
        'action':'FY_BY_ENTER',
        'typoResult':'true'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']
    text2.insert(END,target)


root = Tk()
root.geometry('600x500+300+100')
Label(root,text='有道翻译',fg='blue',font=('romam',15,'bold')).pack()
text1=Text(root,width=100,height=10,font=('romam',15,'bold'))
text2=Text(root,width=100,height=10,font=('romam',15,'bold'))
button = Button(root,text='开始翻译',command=translate)
text1.bind('<Return>',translate)

text1.pack()
text2.pack()
button.pack()


root.mainloop()