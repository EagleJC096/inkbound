class Door:
    def __init__(self, name, description, leads_to, puzzle=None):
        self.name = name
        self.description = description
        self.leads_to = leads_to
        self.puzzle = puzzle
        if puzzle:
            self._isLocked = True
        else:
            self._isLocked = False

    def isLocked(self):
        return self._isLocked
    
    def unlock(self):
        if self.puzzle and self.puzzle._isSolved:
            self._isLocked = False

