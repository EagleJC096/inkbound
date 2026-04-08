class Room:
    def __init__(self, index, name, initial_description, other_description, isDiscovered=False):
        self.index = index
        self.name = name
        self.initial_description = initial_description
        self.other_description = other_description
        self.doors = []
        self.item = None
        self._isDiscovered = isDiscovered

    def add_door(self, door):
        self.doors.append(door)

    def set_item(self, item):
        self.item = item

    @property
    def isDiscovered(self):
        return self._isDiscovered

    def discover(self, player):
        self._isDiscovered = True
        description = self.initial_description
        player.position = self
        if self.item:
            player._inventory.append(self.item)
            self.item = None
            description += f"\n\nYou found {player._inventory[-1].description}."
        return description


    