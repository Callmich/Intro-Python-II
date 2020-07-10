# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, isPlaying = True):
        self.name = name
        self.currentRoom = currentRoom
        self.isPlaying = isPlaying
        self.items = []
    def move(self, compass):
        travelTo = getattr(self.currentRoom, F'{compass}_to')
        if travelTo == None:
            print(F"You Can't Go {compass}. There is a goat in the way.")
        else:
            self.currentRoom = travelTo
            # print(self.currentRoom)
    def open_inventory(self):
        for i in self.items:
            print(i)


