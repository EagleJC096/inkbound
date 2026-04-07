from item import Item

class Puzzle:
    def __init__(self, name, description, solution):
        self.name = name
        self.description = description
        self.solution = solution
        self._isSolved = False

    def attempt(self, attempted_solution):
        if attempted_solution == self.solution:
            self._isSolved = True
            return True
        return False
    
    def validate_attempt(self, attempted_input, player=None):
        raise NotImplementedError("This method should be implemented by subclasses.")


class KeyPuzzle(Puzzle):
    def __init__(self, name, description, solution, key):
        super().__init__(name, description, solution)
        self.key = key

    def validate_attempt(self, attempted_input, player=None):
        if attempted_input.lower() == "yes" and player and self.key in player._inventory:
            self._isSolved = True
            return True
        return False


class NumberPuzzle(Puzzle):
    def __init__(self, name, description, solution):
        super().__init__(name, description, solution)

    def validate_attempt(self, attempted_input, player=None):
        try:
            attempted_input = int(attempted_input)
            return self.attempt(attempted_input)

        except ValueError:
            return False


class PatternPuzzle(Puzzle):
    def __init__(self, name, description, solution):
        super().__init__(name, description, solution)

    def validate_attempt(self, attempted_input, player=None):
        if isinstance(attempted_input, str):
            return self.attempt(attempted_input)
            


class WordPuzzle(Puzzle):
    def __init__(self, name, description, solution):
        super().__init__(name, description, solution)

    def validate_attempt(self, attempted_input, player=None):
        if isinstance(attempted_input, str):
            return self.attempt(attempted_input)
        elif attempted_input is None:
            return False
        else:
            return False
