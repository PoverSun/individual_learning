def make_car(maker,model,**car_info):
    """创建一个字典，其中包含我们知道的制造汽车的信息"""
    car={}
    car['maker_name']=maker
    car['model_name']=model
    for key,value in car_info.items():
        car[key]=value
    return car
car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)