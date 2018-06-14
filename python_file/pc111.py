import urllib2

response = urllib.urlopen('http://www.baidu.com')
print(response.getcode())


cont = response.read()
