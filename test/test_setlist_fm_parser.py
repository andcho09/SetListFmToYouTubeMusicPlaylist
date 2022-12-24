import model
import setlist_fm_parser

def test_parser():
	parser = setlist_fm_parser.SetListFmParser()
	songs = parser.parse_file('test/khruangbin_20220317.html')
	assert 16 == len(songs)
	assert_song(songs[0], 'Khruangbin', 'First Class')
	assert_song(songs[5], 'Khruangbin', 'Evan Finds the Third Room')
	assert_song(songs[8], 'Khruangbin', 'Let\'s Dance / Coffin Nails / Gazzilion Ear / Deep Fried Frenz / Dazz / Bennie and the Jets / It Was a Good Day / Regulate / Nuthin\' but a "G" Thang / Got Your Money / Electric Relaxation / Get Money / True / Wicked Game')
	assert_song(songs[15], 'Khruangbin', 'People Everywhere (Still Alive)')

def assert_song(actual: model.Song, expected_artist, expected_song):
	assert expected_artist == actual.artist
	assert expected_song == actual.song