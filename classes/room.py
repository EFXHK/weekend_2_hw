# class Room:
#     def __init__(self, room, name, song):
#         self.name = name
#         self.room = room
#        self.song = song
#        self.guest = guest

class Room:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.guest = []

    def add_song(self, song):
        self.songs.append(song)

    def add_guest(self, guest):
        self.guest.append(guest)

        
        
