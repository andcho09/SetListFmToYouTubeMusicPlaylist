from typing import List
from ytmusicapi import YTMusic
import model

class YouTubeMusicProxy():
	"""Proxy for YTMusic API
	"""

	def __init__(self, auth_file='headers_auth.json'):
		self.yt = YTMusic(auth_file)


	def search_song(self, song: model.Song) -> model.Song:
		"""Searches for the given song and returns the top hit

		Args:
			song (model.Song): the song to search for

		Returns:
			The top hit as a model.Song with 'album' and 'videoId' populated or None if no hit can be found
		"""
		return self._search_song_str(song.artist, song.song)

	def _search_song_str(self, artist: str, title: str) -> model.Song:
		hits = self.yt.search(f"{artist} {title}", 'songs', ignore_spelling=True)
		if len(hits) > 0:
			hit = hits[0]
			return model.Song(hit['artists'][0]['name'], hit['title'], hit['album']['name'], hit['videoId']) # This only gets the first artist
		return None

	def create_playlist(self, title: str) -> str:
		"""Creates a new playlist

		Args:
			title (str): the name of the playlist to create

		Returns:
			str: ID of the YouTube playlist
		"""
		return self.yt.create_playlist(title, title)

	def append_playlist_items(self, playlist_id: str, video_ids: List[str]):
		return self.yt.add_playlist_items(playlist_id, video_ids)
