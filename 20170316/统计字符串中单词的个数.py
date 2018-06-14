#题目4：
#输入一个字符串，统计出字符串中的元素的个数。
def charcount(x):
    if type(x)==str:
        input_strs = list(x.lower())#先将输入的字符转换成小写,并转换成列表
        str_all = 'abcdefghigklmnopqrstuvwxyz'#方便写入字典
        dict_list=list(str_all)
        new_dict = {'whitespase': 0, 'other': 0}
        for i in dict_list:
            new_dict[i]=0
        for j in range(0,len(input_strs)):
            new_alp = str(input_strs[j])
            if new_alp in new_dict:
                count = int(new_dict[new_alp])
                count += 1
                new_dict[new_alp]=count
            elif new_alp == ' ':
                count = int(new_dict['whitespase'])
                count += 1
                new_dict['whitespase']=count
            else:
                count = int(new_dict['other'])
                count += 1
                new_dict['other']=count
    else:
        print('对不起，您输入的信息不是字符串，无法统计其个数，请重新输入！！！')
    return print(new_dict)

#改进后的代码
def charcount(x):
    dic = {'whitespace':0,'others':0,'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in x.lower():
        if i in dic.keys():
            dic[i] += 1
        elif i == ' ':
            dic['whitespace'] += 1
        else:
            dic['other'] += 1


