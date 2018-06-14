with open('reform.txt','r') as f:
    for line in f:
        line = line.strip()
        reversed_line = list(reversed(line.split('—')))
        reversed_line = '说：'.join(reversed_line)
        print(reversed_line)

f.close()
