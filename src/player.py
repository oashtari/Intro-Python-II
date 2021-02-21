# Write a class to hold player information, e.g. what room they are in
# currently.
from typing import List
from item import Item

class Player:
    def __init__(self, location, items=None):
        # self.name = name
        self.location = location
        if items == None:
            self.items = []
        else:
            self.items = items

    def try_path(self, path):
        attribute = path + '_to'

        if hasattr(self.location, attribute):
            self.location = getattr(self.location, attribute)

        else:
            print("YOU SHALL NOT PASS\n")

    def add_item(self, item):
        self.items.append(item)
        item.on_take()

    def remove_item(self, item_name):
        for i,item in enumerate(self.items):
            if item_name == item.name:
                item.on_drop()
                return self.items.pop(i)

    def get_inventory(self):
        print(f"Here's everything in my bag:\n")
        for i in self.items:
            print(f"{i.name}: {i.description}")
            
