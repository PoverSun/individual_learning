def charcount(x):
    dic = {'whitespace':0,'other':0}
    for i in range(97,123):
        i = chr(i)
        dic[i] = 0
    text = list(x)
    for i in x.lower():
        if i in dic.keys():
            dic[i] += 1
        elif i == ' ':
            dic['whitespace'] += 1
        else:
            dic['other'] += 1
    return dic

print(charcount('adflksdf sdjfs 166'))

