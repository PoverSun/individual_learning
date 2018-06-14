def make_sandwich(*toppings):
    """概述要制作的三明治"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- "+topping)


make_sandwich('奶油')
make_sandwich('面粉','糖','香油')
make_sandwich('鱼','肉','虾','蛋糕')
make_sandwich('面粉','糖','香油','小甲鱼','xiaodong','xiaoxiao')