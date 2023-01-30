import argparse
import model
import setlist_fm_parser
from ytmusicapi import YTMusic
from youtubemusiccache import youtube_music_cache

arg_parser = argparse.ArgumentParser(description = 'Converts a setlist.fm playlist to YouTube Music playlist')
arg_parser.add_argument('playlist_name', help='The name of YouTube Music playlist to create')
arg_parser.add_argument('setlist_playlist', help='Either the URL or path to the HTML output of a setlist.fm playlist')
args = arg_parser.parse_args()

parser = setlist_fm_parser.SetListFmParser()
if args.setlist_playlist.lower().startswith('http'):
	songs = parser.parse_url(args.setlist_playlist)
else:
	songs = parser.parse_file(args.setlist_playlist) # must be a file instead

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

playlist_id = yt.create_playlist(args.playlist_name, args.playlist_name, video_ids)
print(f"Created playlist '{args.playlist_name}' with id: {playlist_id}")
