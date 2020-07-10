from room import Room
from player import Player
from item import Items

collectables = {
    "SWORD": Items("SWORD", "A very good Sword", "outside"),
    "HANDAXE": Items("HANDAXE", "It is Sharp", "outside"),
    "COINS": Items("COINS", "$$$", "foyer"),
    "KEY": Items("KEY", "A key for something", "overlook")
}

# Declare all the rooms

room = {
    'outside':  Room("shadow of the Cave Entrance", "North of you, the cave mount beckons.", 'outside'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", 'treasure'),

    "player": None
}


# Link rooms together

room['outside'].N_to = room['foyer']
room['foyer'].S_to = room['outside']
room['foyer'].N_to = room['overlook']
room['foyer'].E_to = room['narrow']
room['overlook'].S_to = room['foyer']
room['narrow'].W_to = room['foyer']
room['narrow'].N_to = room['treasure']
room['treasure'].S_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playerName = input("Please Enter: Your character's name!")

character = Player(playerName, room['outside'])
print()
print(F'Welcome {character.name}!')
key = [collectables[obj] for obj in collectables]
# for f in key:
#     if room[f.location] == character.currentRoom:
#         print(f)
for f in key:
        if room[f.location] == character.currentRoom and f not in character.currentRoom.items:
            character.currentRoom.items.append(f)

def open_inventory():
    print('inventory: ')
    character.open_inventory()
# print(key[0].location)

# cRoom = Room(character.currentRoom)
print()
print()
# x

# Gameplay Loop
while character.isPlaying == True:
    print(character.currentRoom)
    adventure = input("\nPlease Enter: \n[N] to go North\n[S] to go South\n[E] to go East\n[W] to go West\n or [Q] Quit\n\n ").upper()
    args = len(adventure)
    if args == 1:
        if adventure == "Q":
            print()
            print("See you next Time!")
            character.isPlaying = False
        elif adventure in ["N", "S", "E", "W"]:
            print()
            character.move(adventure)
            print()
            for f in key:
                if room[f.location] == character.currentRoom and f not in character.currentRoom.items:
                    character.currentRoom.items.append(f)
                else:
                    pass
        elif adventure == "I":
            open_inventory()
        else:
            print()
            print("You must be using a new fangled compass - I don't understand that direction.\n")
    else:
        x = str(adventure).split()
        # print(x)
        if x[0] == "GET":
            y = str(x[1])
            # character.currentRoom.checkItems(y)
            # print(y)
            for f in key:
                if str(f).startswith(y):
                    character.items.append(f)
                    f.location = 'player'
                    collectables[y].location = 'player'
                    character.currentRoom.items.remove(f)
                    print(F'You have picked up the {y}')
                    
                    # print(f.location)
        elif x[0] == "DROP":
            y = str(x[1])
            # print(str(character.currentRoom.title))
            for f in key:
                if str(f).startswith(y):
                    character.items.remove(f)
                    f.location = character.currentRoom.title
                    collectables[y].location = character.currentRoom.title
                    character.currentRoom.items.append(f)
                    print(F'You have dropped the {y}')
        else:
            print("I did not understand")
    # for f in key:
    #     if room[f.location] == character.currentRoom and f not in character.currentRoom.items:
    #         character.currentRoom.items.append(f)
    
    