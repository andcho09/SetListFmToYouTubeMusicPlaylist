class Song():

	def __init__(self, artist: str, song: str, album: str = None, videoId: str = None):
		self.artist = artist
		self.song = song
		self.album = None
		self.videoId = videoId # YouTube music video ID
	
	def __str__(self):
		album = "" if self.album is None else f", album: '{self.album}'"
		videoId = "" if self.videoId is None else f", videoId: '{self.videoId}'"
		return f"artist: '{self.artist}', song: '{self.song}{album}{videoId}"

	def __repr__(self):
		return self.__str__()