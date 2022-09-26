import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Dare", "Stan Bush", "The Transformers (1986)")

    def test_song_has_title(self):
        self.assertEqual("Dare", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Stan Bush", self.song.artist)

    def test_song_has_movie(self):
        self.assertEqual("The Transformers (1986)", self.song.movie)

