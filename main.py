import model
import setlist_fm_parser
from ytmusicapi import YTMusic
from youtubemusiccache import youtube_music_cache

# Parse setlist.fm
url = 'https://www.setlist.fm/setlist/khruangbin/2022/roadrunner-boston-ma-438927e3.html'
playlist_title = 'Khruangbin'

parser = setlist_fm_parser.SetListFmParser()
#songs = parser.parse_url(url)
songs = parser.parse_file('output.html')

# Search for songs on YouTube music
playlist_songs = []
yt = youtube_music_cache.YTMCache(YTMusic('headers_auth.json'))
for song in songs:
	youtube_track = yt.get_track(song.song, song.artist)
	if youtube_track is not None and youtube_track['score'] > 80:
		youtube_song = model.Song(youtube_track['artists'][0]['name'], youtube_track['track'], youtube_track['album']['name'], youtube_track['id'])
		playlist_songs.append(youtube_song)
		print(f"Found {str(youtube_song)}")
	else:
		print()
		print(f"WARN: Couldn't find {str(song)} so skipping. Best hit was {str(youtube_track)}")
		print()
yt.close()

# Add them to a playlist
video_ids = [playlist_song.videoId for playlist_song in playlist_songs]

playlist_id = yt.create_playlist(playlist_title, playlist_title, video_ids)
print(f"Created playlist '{playlist_title}' with id: {playlist_id}")
