import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Movie Music")
    
    def test_room_has_name(self):
        self.assertEqual("Movie Music", self.room.name)

    def test_room_has_songs(self):
        self.assertEqual([], self.room.songs)

    def test_can_add_songs(self):
        #AAAAAAAAAAHHHHH
        # arrange - do ur setup, or else
        song = Song("Dare", "Stan Bush", "The Transformers(1986)")
        # act - what do
        self.room.add_song(song)
        # assert - make sure
        self.assertEqual([song], self.room.songs)


    def test_can_check_in_guests(self):
        self.assertEqual([], self.room.guest)

    def test_can_check_in_guests(self):
        #stop screaming
        # arrange set up
        guest = Guest("Optimus Prime")  # idk why its breaking 
        # act - what should be happening
        self.room.add_guest(guest)
        # assert - what comes out
        self.assertEqual([guest], self.room.guest)


