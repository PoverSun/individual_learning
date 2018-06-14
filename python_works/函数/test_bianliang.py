def discounts(price,rate):
    final_price = price * rate
    old_price = 88 #在这里试图修改全局变量
    print('这里试图修改全局变量old_price的值：',old_price)
    old_price = 88 #在这里试图修改全局变量
    print('修改前old_price的值是：',old_price)
    return final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('修改后old_price的值是：',old_price)
print('打折后价格是：',new_price)
print('这里试图打印局部变量final_price的值：',final_price)
