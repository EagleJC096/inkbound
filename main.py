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


                                          by Mr. Spare
====================================================================================================
"""
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
    newgame.cursor_blink(0.5, 0.5)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    player = Player(5)  # Starting position (room index)
    newgame.load_rooms()
    newgame.slow_print(newgame.rooms[4].discover(player))  # Start in the initial room
    newgame.game_loop(player)

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    
    newgame.slow_print("The portal glows even brighter, and you find yourself unable to see anything else!", blink=True)
    newgame.cursor_blink(3, 0.3)
    newgame.slow_print("You feel dizzy as you realize the portal is transporting you. . . somewhere.", delay=0.5)
    newgame.cursor_blink(5, 0.3)
    newgame.slow_print("As you brace for whatever comes next, you are sure that, whatever it is, you are more than ready to face the challenge. \n", delay=0.2)
    newgame.slow_print("Press Enter to see what lies beyond!", delay=0.1)
    input()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    ending = """Thank you so much for playing "Inkbound." I hope that you have enjoyed your experience!
This game was made as a demonstration of the final project for the Introduction to Computer Science
course at Bob Jones Academy. I had a lot of fun creating this game, and I hope you had fun playing it!

Until next time, adventurer. . ."""

    newgame.title_print(title_screen)
    newgame.slow_print(ending, delay=0.05)
    newgame.cursor_blink(5, 0.5)

    newgame.slow_print("\n\nPress Enter to exit the game.", delay=0.05)
    input()  # Wait for the player to press Enter

if __name__ == "__main__":
    main()