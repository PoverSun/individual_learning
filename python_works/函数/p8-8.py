def make_album(singer_name,song_name,number):
    """制作描述音乐专辑的字典"""
    albums = {'歌手名':singer_name,'歌曲名':song_name}
    if number:
        albums['number'] = number
    
    return albums

while True:
    print("请按下列提示输入相应的信息：")
    print("(enter 'q' at any time to quit)")
    singer_name = input("\n请输入歌手姓名：")
    if singer_name == 'q':
        break
    song_name = input("\n请输入歌曲名称：")
    if song_name == 'q':
        break
    number = int(input("\n请输入歌曲数量："))
    if number == 'q':
        break
    musician = make_album(singer_name,song_name,number)
    print(musician)
 
