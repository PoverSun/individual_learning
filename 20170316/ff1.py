def ff1(x):
    def ff2(y):
        return x(y)+1
    return ff2

def ffn(m):
    return m*m

h = ff1(ffn)
print(h(6))