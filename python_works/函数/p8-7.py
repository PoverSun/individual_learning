def make_album(singer_name,song_name,number=''):
    """制作描述音乐专辑的字典"""
    albums = {'歌手名':singer_name,'歌曲名':song_name}
    if number:
        albums['number'] = number
    return albums



musician = make_album('周杰伦','稻香',number=12)
print(musician)
 
