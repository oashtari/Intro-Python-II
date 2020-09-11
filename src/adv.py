from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('flashlight', 'to test item')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('sword', 'very long'), Item('fire', 'quite bright')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Item('sack', 'to hold stuff'), 
Item('crystal', 'thy fortune')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('cup', 'for thirst'), 
Item('phone', 'to call your mom')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[Item('book', 'for boredom'), 
Item('baby', 'feed it')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(room["outside"])
# currentRoom = player.location

# print(f" Hi {player.name}, \n ")

options = ['n', 's', 'e', 'w']

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



while True:
    print(f"You are currently in: \n  {player.location} \n")
    currentRoom = f"{player.location}"

    action = input("Hi player, welcome to your adventure,\n you can either enter a new room by choosing to go [n]orth, [s]outh, [e]ast, or [w]est,\n OR you can choose to take [item_name] or drop [item_name] in a room,\n finally you can see your items by typing [i]nventory\n").split()
    # print("INITIAL ACTION", len(action))
    # print('ACTION', action)
    if len(action) == 1:
        path = action[0].strip().lower().split()[0]
        print('PATH', path)
        path = path[0]

        if path == 'q':
            break
        
        if path in options:
            player.try_path(path)

        if path == 'i':
            player.get_inventory()
        
    elif len(action) == 2:
        if action[0] == 'take' or action[0] == 'get':
            removed_item = player.location.remove_item(action[1])
            player.add_item(removed_item)
            on_take(removed_item)
        elif action[0] == 'drop':
            removed_item = player.remove_item(action[1])
            player.location.add_item(removed_item)
            print(f"DROPPED: {player.location.items}")
        else:
            print(f"There is no {action[1].upper()} in this room")

    else:
        print("I do not understand your preferred action, please try again.")
