def fun1(x):
    def fun2(y):
        return x+y
    return fun2

a = fun1(1)
print(a(2))
