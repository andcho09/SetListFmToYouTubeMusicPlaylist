# Convert Setlist.fm to YouTube Music Playlist

## Usage

### First-time setup

1. Set up Python

		$ python -m venv .venv
		$ source .venv/bin/activate
		$ pip install -r requirements.txt

1. Install development modules

		$ pip install -e <path to youtubemusiccache>

1. Create a ``headers_auth.json`` file with YouTube Music authorisation details by following these [instructions](https://ytmusicapi.readthedocs.io/en/latest/setup.html)

### Run

1. In virtual environment...

1. Run

		$ python main.py <name of YouTube Music playlist to create> <setlist.fm URL>

	For example:

		$ python main.py Khruangbin https://www.setlist.fm/setlist/khruangbin/2022/roadrunner-boston-ma-438927e3.html

### Tests

```
python -m pytest
```