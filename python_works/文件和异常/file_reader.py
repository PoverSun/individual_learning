with open('pi_digits.txt') as file_object:
      contents = file_object.read()
      print(contents.rstrip())#删除末尾的空白


#逐行读取
filename = 'pi_digits.txt'
print('\n')
with open(filename) as file_object:
      for line in file_object:
            print(line.rstrip())
