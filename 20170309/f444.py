dict1 = {'name':'lily','age':20,'gender':'female','Class':9}
dict2 = {'name':'jack','age':25,'gender':'male','Class':9}
dict3 = {'name':'jane','age':19,'gender':'female','Class':9}

list1 = [dict1,dict2,dict3]
name_list=[]
for i in range(0,3):
    new_name = list1[i].pop('name')
    name_list.append(new_name)
dict_name = ['info1','info2','info3']
for j in range(0,3):
    dict_name[j] ={name_list[j]:list1[j]}
    print(dict_name[j])

