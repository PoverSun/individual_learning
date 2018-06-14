list_guest = ['佳佳','逆天超超','大师兄','韩飞','白皓','乔震']
print('+++***...................请客开始了.....................***+++')
#打印消息
for i in list_guest:
      print('\t'+i+':'+'我想和你一起共进晚餐，特意来邀请你的,希望你能赏光'+'\n')
print('\t我邀请了'+str(len(list_guest)-1)+'个人共进晚餐')
#有一位嘉宾无法赴约
not_come = list_guest.pop(0)
print('提示：'+"佳佳由于工作原因，无法赴约，他表示很抱歉"+'\n')
list_guest.insert(0,'胡子')
A_new_friends=list_guest[0]

#打印邀请消息
print('\t'+A_new_friends+':'+'我想和你一起共进晚餐，特意来邀请你的,希望你能赏光'+'\n')

print('我找到了一个更大的餐桌，这真是个好消息!!!\n')
#添加三位新成员
list_guest.insert(0,'陆恒')
list_guest.insert(3,'田瑞')
list_guest.append('金宝玉')
new_friends=['陆恒','田瑞','金宝玉']
for i in new_friends:
      print('\t'+i+':'+'我想和你一起共进晚餐，特意来邀请你的,希望你能赏光'+'\n')

#介绍新加入的成员
print('给大家介绍今天来的几个朋友：\n')
for i in new_friends:
      print(i)
print("\n奥！这真是个不幸的消息，新购买的餐桌无法到达,我可能没办法请你们这么多人吃饭了，真的很抱歉")
print('\t最终决定：我只能邀请两位嘉宾和我共进晚餐')

list_number = len(list_guest)
#删除没办法邀请的嘉宾
while list_number>2:
      list_number = list_number - 1
      pop_list=list_guest.pop()
      print('\n\t'+pop_list+':'+'很抱歉，不能请你吃饭了')
      print(list_guest)

#打印还能邀请的嘉宾
print('显示还能邀请的嘉宾：')
print(list_guest)
#告诉剩下的两位嘉宾他们任然在受邀名单里


print(list_guest[0] + ':'+'你依然在我的邀请范围内')
print(list_guest[1] + ':'+'你依然在我的邀请范围内')
print('\t我邀请了'+str(len(list_guest))+'个人和我一起共进晚餐')
#删除列表中的剩余成员
del list_guest[0]
print(list_guest)
del list_guest[0]
print("程序结束时，名单为：")
print(list_guest)

print('+++***...................请客结束.....................***+++')
   
      

