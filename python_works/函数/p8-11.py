def show_magicians(magic_list,after_change):
    """传递列表给函数"""
    make_great(magic_list,after_change)
    print("修改之前的列表：")
    for magic in magic_list:
        print(magic)
    print("修改之后的列表：")
    for i in after_change:
        print(i)

def make_great(magic_list,after_change):
    """对魔术师列表进行修改"""
    new_list = magic_list[:]
    while new_list:
        current_design = new_list.pop()
        after_change.append('the Great'+ current_design)
#创建一个包含魔术师的列表
magic_list = ['刘谦','晓冬','小甲鱼','晓晓','倩倩']

after_change = []

if __name__=='__main__':
    show_magicians(magic_list,after_change)