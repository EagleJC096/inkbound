from game import Game
from player import Player

def main():
    print("Welcome to the Text Adventure Game 2!")

    newgame = Game()
    player = Player(5)  # Starting position (room index)

    newgame.load_rooms()
    newgame.game_loop(player)
    # Here you would set up your game world, puzzles, and items
    # For example:
    # key = Item("Key", "A small rusty key.")
    # puzzle = Puzzle("Locked Door", "A door that requires a key to open.", key)
    # Then you would have a game loop to interact with the player

if __name__ == "__main__":
    main()