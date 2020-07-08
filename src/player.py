# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom = 'outside'):
        self.currentRoom = currentRoom

testPlayer = Player()

print(testPlayer.currentRoom)