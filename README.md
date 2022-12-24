# Convert Setlist.fm to YouTube Music Playlist

## Usage

### First-time setup

1. Set up Python

		$ python -m venv .venv
		$ source .venv/bin/activate
		$ pip install -r requirements.txt

1. Create a ``headers_auth.json`` file with YouTube Music authorisation details by following these [instructions](https://ytmusicapi.readthedocs.io/en/latest/setup.html)

		# In Python shell
		from ytmusicapi import YTMusic
		yt = YTMusic('headers_auth.json')

