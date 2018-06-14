number_list = []
for value in range(1,11):
      number_list.append(value**3)
print(number_list)
#使用列表解析生成列表
number_list = [value**3 for value in range(1,11)]
print('\n'+str(number_list))
for value in number_list[:3]:
      print(value)
      #打印前三个元素
print("\nThe first three items in the list are:"+str(number_list[:3]))

#打印中间三个元素
print("\nthree items from the middoe of the list are:"+str(number_list[3:6]))
#打印最后三个元素
print("\nThe first three items in the list are:"+str(number_list[7:]))
