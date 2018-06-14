# def fibonacci():
#     a, b = 1, 1  # 一开始，让a b 分别为 第一项 和 第二项
#     yield a
#     yield b
#     while True:
#         a, b = b, a+b   # 让 a变成下一项（第三项）， 让 b 变成第四项（a和b的和）
#         yield b

# fi = fibonacci()
# for i in range(20):
#     print(next(fi))

def fibonacci(n):
    the_list = [1, 1]
    while True:
        new_item = the_list[-2] + the_list[-1]
        the_list.append(new_item)
        if len(the_list) == n:
            break
    return the_list

print(fibonacci(20))
