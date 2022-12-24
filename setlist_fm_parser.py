from typing import List
import model
import json
import urllib.request

class SetListFmParser:

	def parse_url(self, url: str, output_file='output.html') -> List[model.Song]:
		_info = urllib.request.urlretrieve(url, output_file)
		return self.parse_file(output_file)

	def parse_file(self, input_file: str) -> List[model.Song]:
		"""Parses songs from the given setlist.fm HTML file.

		Args:
			input_file (str): path to the input file to parse

		Returns:
			List[model.Song]: a list of model.Song objects or an empty list if no songs could be found
		"""
		result = []
		with open(input_file, 'r', encoding='utf-8') as f:
			# Dodgy HTML parsing to find the 'YouTubeSearch.setPlaylist' inside the JavaScript
			html = f.read()
		index = html.find('YouTubeSearch.setPlaylist')
		if index > 0:
			html = html[index + 26: html.find('}]', index) + 2] # JSON list
			j = json.loads(html)

			for hit in j:
				result.append(model.Song(hit['artist'], hit['song']))

		# Oops
		return result
