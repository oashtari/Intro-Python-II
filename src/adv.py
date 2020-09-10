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
Item('crystal ball', 'thy fortune')]),

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


newPlayer = Player(input("Hi, what is is your name?\n"), room["outside"], ["bag"])
# currentRoom = newPlayer.location

print(f" Hi {newPlayer.name}, \n ")

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
    print(f"You are currently in: \n  {newPlayer.location} \n")
    currentRoom = f"{newPlayer.location}"
    # print(f"CURRENT ROOM {currentRoom}")

    path, grab = input("Which direction would you like to go?\n Would you like to pick up any items?").split()
    path = path.strip().lower().split()[0]
    path = path[0]
    # print("path is: ", path)
    # print("item is: ", grab)
    whatis = type(newPlayer.location)
    print(f"TYPE: {whatis}")

    for i,c in enumerate(newPlayer.location.items):
        if grab in c.name:
            newPlayer.add_item(grab)
            print(f"PLAYER ITEMS: {newPlayer.items}")
            print(f"LOCATION: {newPlayer.location}")
            # newPlayer.location.drop_item(grab)
            print(f"ROOM ITEMS POST DROP: {c.name}: {c.description}")
        else:
            print(f"There is no {grab.upper()} in this room")

    

    if path == 'q':
        break
    
    if path in options:
        newPlayer.try_path(path)
    
    # if grab in newPlayer.location.items:
    #     print("TEST MOFO")
    # else: 
    #     "that item is not available"



# * Add a new type of sentence the parser can understand: two words.

#   * Until now, the parser could just understand one sentence form:

#      `verb`

#     such as "n" or "q".

#   * But now we want to add the form:

#     `verb` `object`

#     such as "take coins" or "drop sword".

#   * Split the entered command and see if it has 1 or 2 words in it to determine
#     if it's the first or second form.




# * Implement support for the verb `get` followed by an `Item` name. This will be
#   used to pick up `Item`s.

#   * If the user enters `get` or `take` followed by an `Item` name, look at the
#     contents of the current `Room` to see if the item is there.

#      * If it is there, remove it from the `Room` contents, and add it to the
#        `Player` contents.

#      * If it's not there, print an error message telling the user so.

#      * Add an `on_take` method to `Item`.

#         * Call this method when the `Item` is picked up by the player.

#         * `on_take` should print out "You have picked up [NAME]" when you pick up an item.

#         * The `Item` can use this to run additional code when it is picked up.

#      * Add an `on_drop` method to `Item`. Implement it similar to `on_take`.

# * Implement support for the verb `drop` followed by an `Item` name. This is the
#   opposite of `get`/`take`.

# * Add the `i` and `inventory` commands that both show a list of items currently
#   carried by the player.