pizzas= ['Garden pizza','Fruit pizza','Spicy chicken pizza','Italian beef pizza']
for pizza in pizzas:
      print('\t'+"I like pepperoni "+str(pizza))

print('\n\tI relly love pizza')

animals=['cat','dog','deer','rabbit']
for animal in animals:
      print(animal)
      print('A dog would make a great pet')

print('\nAny of these animals would make a great pet!\n')


friends_pizzas = pizzas[:]
print('副本为：'+str(friends_pizzas))
friends_pizzas.append('good pizza')
#副本列表添加元素后:
print(friends_pizzas)
pizzas.append('better pizza')
#原来列表添加元素后:
print(pizzas)
for i in pizzas:
      print(i)
print('My favorite pizzas are:'+'' +str(pizzas)+'\n')
for i in friends_pizzas:
      print(i)
print('My friend\'s favorite pizzas are:'+'' +str(friends_pizzas)+'\n')
