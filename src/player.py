# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom, isPlaying = True):
        self.currentRoom = currentRoom
        self.isPlaying = isPlaying
    def move(self, compass):
        travelTo = getattr(self.currentRoom, F'{compass}_to')
        if travelTo == None:
            print("You Can't Go That Way")
        else:
            self.currentRoom = travelTo
            print(self.currentRoom)


