# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        stuff = f"{self.name} \n these items are availble to pick up:\n"
        # stuff += f"{self.items}"
        for i,c in enumerate(self.items):
            stuff += str(i+1) + ":\t" + c.name + ":\t" + c.description + "\n"
        return stuff


    def add_item(self, item):
        self.items.append(item)

    def get_item(self, item):
        for item in self.items:
            return item.name

    def remove_item(self, item_name):
        for i,item in enumerate(self.items):
            if item_name == item.name:
                return self.items.pop(i)