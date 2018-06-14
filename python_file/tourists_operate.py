tourists=['Shanxi','Beijing','chongqi','Shanghai','Xinjiang','Changji']
print("1.原始序列为："+'\n'+str(tourists))
print("2.使用sorted按字母顺序打印列表为："+'\n'+str(sorted(tourists)))
print("3.核实该列表是否被改变："+'\n'+str(tourists))
print("4.使用sorted按字母顺序相反的顺序打印列表为："+'\n'+str(sorted(tourists,reverse=True)))
print("5.再次核实该列表是否被改变："+'\n'+str(tourists))

tourists.reverse()
print('\n'+str(tourists))

tourists.reverse()
print(tourists)

tourists.sort()
print('排序后的列表为：')
print(tourists)

tourists.sort(reverse=True)
print('第二次修改后的列表为：')
print(tourists)

