import setlist_fm_parser
import youtube_music

url = 'https://www.setlist.fm/setlist/khruangbin/2022/roadrunner-boston-ma-438927e3.html'

parser = setlist_fm_parser.SetListFmParser()
#result = parser.parse_url(url)
songs = parser.parse_file('output.html')
for song in songs:
	print(song)

yt = youtube_music.YouTubeMusicProxy()
print(yt.search_song(songs[0]))
print(yt.search_song(songs[1]))