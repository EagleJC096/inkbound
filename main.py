from game import Game
from player import Player
import time
import os

def main():

    title_screen = r"""
====================================================================================================


                           .=======================ooooooo
                   ___   ,'    \_________________________________________
                  /   /-/       /                           ////////////  ''--..._
                  \___\-\       \                           \\\\\\\\\\\\  __..--'
                         `---------------------------------''''''''''''''

             ██▒   ██▄     █   ██ ▄█▀  ▄████▄   ▒▄█████▄   ▄█   █▄  ██▄     █   ▄█████▄
            ▒██▒   ██ ▀█   █  ░██▄█▒ ░░██  ▐█▄▒▒▒██   ██   ██   ██  ██ ▀█   █▒▒▒██▒  ██▒
            ▒██▒   ██  ▀█ ██▒▒░███▄░▒  ██▄▄▄█▀▒▒▒██   ██   ██   ██  ██  ▀█ ██   ██░   ██▒
            ░██░   ██▒  ▐▌██▒░▒██ █▄░▒░██   ██░▒▒██   ██▒▒▒██   ██  ██▒  ▐▌██▒▒ ██   ██▒
            ░██░▒▒▒██░   ▓██░░▒██▒ █▄▒░▀█▄▄▄█▀▒▒▒▀█████▀   ▀█████▀░░██░   ▓██  ▒█████▀▒░


===================================================================================================="""
    game_description = ["""You wake with no memory.
A map is etched into your skin.
Each step will reveal the truth.""", """Find the exit.
Let the ink guide you.""", """Press Enter to wake from your dreams..."""]

    newgame = Game()
    newgame.title_print(title_screen)
    time.sleep(3)  # Pause for 3 seconds before showing the description

    for line in game_description:
        newgame.slow_print(line, blink=True)
        newgame.cursor_blink(3, 0.3)  # Blink the cursor for 2 seconds after each line
        print("")  # Add a newline after each line of the description

    input()  # Wait for the player to press Enter

    newgame.slow_print("System Starting...", delay=0.5)
    newgame.cursor_blink(3, 0.5)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    player = Player(5)  # Starting position (room index)
    newgame.load_rooms()
    newgame.slow_print(newgame.rooms[4].discover(player))  # Start in the initial room
    newgame.game_loop(player)

if __name__ == "__main__":
    main()