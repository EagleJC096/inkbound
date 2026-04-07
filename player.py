from item import Item

class Player:
    def __init__(self, position):
        self._position = position
        self._inventory = []

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, room):
        self._position = room.index
            
    
    def add_to_inventory(self, item):
        if isinstance(item, Item):
            self._inventory.append(item)

    def has_item(self, item_name):
        return any(item.name == item_name for item in self._inventory)