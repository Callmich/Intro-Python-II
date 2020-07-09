from room import Room, Items
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("shadow of the Cave Entrance", "North of you, the cave mount beckons.", "canteen", "sword"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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



character = Player(room['outside'])
print()
print()
print(character.currentRoom)
# Gameplay Loop
while character.isPlaying == True:
    adventure = input("\nPlease Press: \n[N] to go North\n[S] to go South\n[E] to go East\n[W] to go West\n or [Q] Quit\n\n ").upper()
    if adventure == "Q":
        print()
        print("See you next Time!")
        character.isPlaying = False
    elif adventure in ["N", "S", "E", "W"]:
        print()
        character.move(adventure)
    else:
        print()
        print("You must be using a new fangled compass - I don't understand that direction.")
    
    