# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def try_path(self, path):
        attribute = path + '_to'

        if hasattr(self.location, attribute):
            self.location = getattr(self.location, attribute)

        else:
            print("YOU SHALL NOT PASS\n")

    # def __str__(self):
    #     place = f"{self.location}"

    #     return or print place  

