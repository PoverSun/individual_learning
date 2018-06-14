f = open('reform.txt')
new_file_name = 'reform1.txt'
list1 = []
for i in f:
    list1.append(i.split('——'))
for j in list1[0:17:2]:
    j[1] = j[1].replace('\n','说：')
    f1 = open('%s'%new_file_name,'a')
    f1.write(j[1]+j[0]+'\n\n')
f1.close()
f.close()
print("***新文件名为'%s',请点击查看***"%new_file_name)
    
        
        
