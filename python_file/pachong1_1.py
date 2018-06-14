import urllib

import urllib.request

for i in range(1,100,2):
      req = urllib.request.Request('http://img1.mm131.com/pic/'+str(10+i)+'/4.jpg')
      response = urllib.request.urlopen(req)
      with open('mm'+str(i)+'.jpg','wb')as f:
            f.write(response.read())
