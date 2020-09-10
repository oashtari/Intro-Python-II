# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        stuff = f"{self.name}, {self.description}, and all the available items:\n"
        # stuff += f"{self.items}"
        for i,c in enumerate(self.items):
            stuff += str(i+1) + ":\t" + c.name + ":\t" + c.description + "\n"
        return stuff


    def add_item(self, item):
        self.items.append(item)