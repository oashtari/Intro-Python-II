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

    def drop_item(self, item):
        for i in self.items:
            if item == i.name:
                # print("what is i", i.name)
                self.items.remove(i)

    #         if i == item.name:


    # def take(self, item):
    #         for i in self.current_room.items:
    #             if i.name == item:
    #                 self.items.append(i)
    #                 self.current_room.items.remove(i)
    #                 i.on_take()
    #                 self.current_room.print_items(self.has_light())
    #                 break