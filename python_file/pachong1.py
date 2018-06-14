import urllib.request

req = urllib.request.Request('http://placekitten.com/g/500/600')
response = urllib.request.urlopen(req)

cat_img = response.read()


with open('cat_400_600.jpg','wb')as f:
    f.write(cat_img)
