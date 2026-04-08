import os
import sys
import time
from door import Door
from puzzle import *
from item import Item
import puzzle
from room import Room
import random


class Game:
    def __init__(self):
        self.rooms = []

    def print_Room(self, player_index):
        columns = 3
        total_rooms = len(self.rooms)
        rows = total_rooms // columns

        complete_map = []
        for r in range(rows):

            # ---------- TOP WALLS ----------
            top_line = ""
            for c in range(columns):
                room_number = r * columns + c + 1
                room = self.rooms[room_number - 1]

                if room.isDiscovered:
                    top_line += "+-----+"
                else:
                    top_line += "       "
            top_line += "\n"
            complete_map.append(top_line)

            # ---------- CONTENT LINE ----------
            content_line = ""
            for c in range(columns):
                room_number = r * columns + c + 1
                room = self.rooms[room_number - 1]

                if room.isDiscovered:
                    symbol = ""
                    if room_number == player_index:
                        symbol = "P"
                    elif room_number == 9:
                        symbol = "֎"

                    content_line += f"| {symbol:^3} |"
                else:
                    content_line += "       "
            content_line += "\n"
            complete_map.append(content_line)

            # ---------- BOTTOM WALLS ----------
            bottom_line = ""
            for c in range(columns):
                room_number = r * columns + c + 1
                room = self.rooms[room_number - 1]

                if room.isDiscovered:
                    bottom_line += "+-----+"
                else:
                    bottom_line += "       "
            bottom_line += "\n"
            complete_map.append(bottom_line)

        for line in complete_map:
            for c in line:
                print(c, end="")
                time.sleep(0.01)
                

        time.sleep(1)

    
    def title_print(self, ascii_art):
        delay = 0.01
        lines = ascii_art.splitlines()

        # Normalize width
        max_width = max(len(line) for line in lines)
        padded_lines = [line.ljust(max_width) for line in lines]

        # Animate column by column
        for col in range(1, max_width + 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            for line in padded_lines:
                print(line[:col])
            time.sleep(delay)

    def slow_print(self, text, delay=0.03, blink=False):
        for c in text:
            nat_delay = random.uniform(0.01, delay)  # Randomize delay for a more natural effect
            if c == "\n" and blink:
                self.cursor_blink(2, 0.4)
            else:
                time.sleep(nat_delay)
            print(c, end="")
        print("")  # Move to the next line after printing the text

    def cursor_blink(self, duration=5, interval=0.5):
        end_time = time.time() + duration
        while time.time() < end_time:
            print("█", end="")
            time.sleep(interval)
            sys.stdout.write('\b \b')
            time.sleep(interval)

    def game_loop(self, player):
        while not self.win_condition(player):
            choice_is_valid = False
            
            for room in self.rooms:
                if choice_is_valid:
                    break
                if player.position == room.index:
                    current_room_desc = ""
                    if not room.isDiscovered:
                        current_room_desc = room.discover(player)
                    else:
                        current_room_desc = room.other_description
                    time.sleep(1)
                    self.print_Room(player.position)
                    time.sleep(1)
                    self.slow_print(current_room_desc)
                    print("")
                    time.sleep(1)
                    room_choices = self.load_choices(room)
                    i = 0
                    for choice in room_choices:
                        self.slow_print(f"{i + 1}: {choice[1]}")
                        i += 1
                    print("")
                    
                    while True:
                        try:
                            door_choice = int(input("What would you like to do? ")) - 1
                            if 0 <= door_choice < len(room_choices):
                                choice_is_valid = self.move_player(player, room.doors[door_choice])
                                break
                            else:
                                self.slow_print("Invalid choice. Please try again.")
                        except ValueError:
                            self.slow_print("Invalid input. Please enter a number.")
                            continue

    def load_choices(self, room):
        choices = []
        for door in room.doors:
            if door.isWall:
                choice = [None, f"Look at the {door.name}"]
            else:
                choice = [door.leads_to.index, f"The {door.name}: {door.description}"]
            choices.append(choice)
        return choices

    def move_player(self, player, door):
        if not door.isLocked():
            player.position = door.leads_to
            os.system('cls' if os.name == 'nt' else 'clear')
            self.slow_print(f"You move through the {door.name} to {door.leads_to.name}.")
            return True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if door.isWall:
                self.slow_print(f"{door.description}")
                return False
            self.slow_print(f"The {door.name} is locked. You need to solve the puzzle to unlock it. Type 'exit' to go back.\n")
            self.solve_attempt(door.puzzle, player, door)
            return False
        
    def solve_attempt(self, puzzle, player, door):
        self.slow_print(puzzle.description)
        user_input = input("Enter your solution: ")
        while not user_input.lower() == "exit":
            if puzzle.validate_attempt(user_input, player):
                self.slow_print("Puzzle solved! The door is now unlocked.")
                door.unlock()
                self.move_player(player, door)
                return True
            else:
                self.slow_print("Incorrect solution. Try again.")
                user_input = input("Enter your solution: ")
        self.slow_print("Exiting puzzle attempt.")
        return False
        

    def win_condition(self, player):
        # Define the win condition for the game, such as reaching a specific room or collecting certain items
        for item in player._inventory:
            if item.name == "Portal":
                return True
        return False
            
    def end_game(self):
        self.slow_print("Game Over. Thanks for playing!")

    def load_rooms(self):
        r0_initial_desc = """When you wake up, you have no idea where you are, and no memory of how you got here. 
You are lying on the cold, hard ground, with one clear thought: "I need to get out of here!" 
You look at your wrist, and you can immediately see some kind of marking that looks like a tattoo, 
and it reminds you of the room you are in. As you look around you, you see two doors and a marking on the wall of your room. 
You must get out of this place by any means necessary.

But how?"""
        r2_initial_desc = """This room is more like a hall. 
You see two doors, one on the west wall and one on the east wall, as well as the south door that you came from.
Both side doors seem to be locked. You cannot go anywhere else without attempting to unlock a door. 
As you look down, movement catches your eye. The tatoo on your wrist seems to grow and shift--
ink spreads across your skin and forms into two rooms now. It's a living map under your skin!
You can see that your location is marked with a 'P', and the room you started from is marked as well.
Maybe there are more rooms to uncover, and maybe you can find a way out of here if you explore them all.

What now?"""

        # Initialize Rooms
        r1 = Room(1, "Room 1", "When you enter the room, you see storage shelves lining the walls, but they are mostly empty. However, you do find an odd looking key. You take the key and put in in the pocket of your clothes for later use.", "You are back in the empty storage room.")
        r2 = Room(2, "Room 2", r2_initial_desc, "You are back in Room 2.")
        r3 = Room(3, "Room 3", "The light you saw from the start room looks even brighter as it shines from under a doorway to the south.", "You go back through the airlock. It's a cool room, but you need to find the ID badge for the safe.")
        r4 = Room(4, "Room 4", "You are in Room 4, which almost looks like barracks. There are bunkbeds (still made), and someone appears to have written on the wall.", "You are back in the barracks.")
        r0 = Room(5, "Start Room", r0_initial_desc, "You are in the start room.", True)
        r6 = Room(6, "Room 6", "You are in Room 6. The light you saw from the start room looks even brighter as it shines from under a safe door to the south.", "You are back in Room 6.")
        r7 = Room(7, "Room 7", "You are in Room 7. This appears to be someone's study. A math equation is on the whiteboard behind an impressive desk. It looks complicated.", "You are back in the study in Room 7.")
        r8 = Room(8, "Room 8", "You are in Room 8, and you can finally see what that blue glow is! You stand in a room that appears to be a control room, with a bulletproof glass window separating you from a glowing blue circle on the floor of Room 9. 'This is where I need to go!' you realize. There's an ID badge on the table that just might help.", "You are back in Room 8.")
        r9 = Room(9, "Room 9", "Finally! You have found the room with the mysterious blue glow. Inside lies a ring of blue light on the floor that apears to be a portal. As you walk towards the portal, you realize that it is time to step beyond these mysterious walls to see what lies beyond.", "You are back in Room 9. That blue glow through the window is really something!")

        # Initialize Items
        key1 = Item("Key", "An unusual metal key.", r1.index)
        r1.set_item(key1)
        key2 = Item("ID Badge", "An ID badge with the name Jim Chuck Robson.", r8.index)
        r8.set_item(key2)
        portal = Item("Portal", "A swirling blue portal.", r9.index)
        r9.set_item(portal)

        # Initialize Puzzles
        # ex_puzzle = WordPuzzle("Example Puzzle", "Solve this puzzle to unlock the door.", "Example Solution")
        unlockable_puzzle = WordPuzzle("Unlockable", "This door is locked.", None)
        
        r2_r1_puzzle = WordPuzzle("You see a door with a keypad lock.", "Above the keypad, you see a crude compass scratched into the door. Which way are you facing again?", "west")
        r2_r3_puzzle = KeyPuzzle("You see a door with a keyhole.", "This is a most unusual keyhole! It seems to be made for a very specific key. Do you have the key that fits?","", key1)

        r0_r4_puzzle = WordPuzzle("This door has a keypad.", "What word would be used for this door?", "StarForce")

        r3_r6_puzzle = NumberPuzzle("You see a door with a number pad.", "Who would have had access to this room?", 5294)

        r6_r9_puzzle = KeyPuzzle("You see a door with an ID badge scanner.", "This door seems to be locked, but there is a scanner that looks like it is meant for an ID badge. Do you have the correct ID badge to unlock this door?", "", key2)

        r4_r7_puzzle = WordPuzzle("You see a door with a keypad.", "Since the door is ornate, maybe it's for someone special?", "Daniels")

        r7_r8_puzzle = NumberPuzzle("You see a door with a number pad.", "What is the code to unlock this door?", 6975349)

        # Initialize Doors
        r0.add_door(Door("North Door", "A doorway that seems to have its door completely removed. You can still see the marks where the hinges were.", r2))
        r0.add_door(Door("East Wall", "There is a small hole in the wall, and a faint blue light bleeds through. Sunlight?", None, isWall=True))
        r0.add_door(Door("West Door", "Solid and metal. Is something important behind it?", r4, r0_r4_puzzle))
        r0.add_door(Door("South Wall", "This wall is covered in frames where photographs of various people were probably displayed. All of the photos are gone, though. Only one nameplate remains: 'Commander Daniels.' What is this place? And why did it need a commander?", None, isWall=True))

        r1.add_door(Door("East Door", "Back to Room 2.", r2))

        r2.add_door(Door("North Wall", "The wall is bare, except for a poster with a soldier at attention and the word 'StarForce' emblazoned on it.", None, isWall=True))
        r2.add_door(Door("West Door", "A door marked 'Storage.'", r1, r2_r1_puzzle))
        r2.add_door(Door("East Door", "Looks like it needs a key.", r3, r2_r3_puzzle))
        r2.add_door(Door("South Door", "Back to the starting room.", r0))

        r3.add_door(Door("West Door", "Back to Room 2.", r2))
        r3.add_door(Door("South Door", "Looks like an airlock designed to keep the atmosphere in. You can see a door that looks like a safe at the far end of the room.", r6, r3_r6_puzzle))

        r4.add_door(Door("East Door", "Back to the start room.", r0))
        r4.add_door(Door("North Wall", "On the wall near someone's bunk, you see four faint numbers scratched into the wall: 5294. Could this be a clue for something?", None, isWall=True))
        r4.add_door(Door("South Door", "Ornate and made of ironwood. Something tells you this door may be the most important of all!", r7, r4_r7_puzzle))

        r6.add_door(Door("North Door", "Back to Room 3.", r3))
        r6.add_door(Door("South Door", "Almost like a safe door. There's no keyhole or pad for this one...just an ID badge scanner.", r9, r6_r9_puzzle))
        r6.add_door(Door("West Wall", "You can see through the hole back to the start room. It's amazing how far you've come!", None, isWall=True))

        r7.add_door(Door("North Door", "Back to the barracks.", r4))
        r7.add_door(Door("South Wall", "This wall is covered in mathematical equations and diagrams. It looks like someone was trying to solve a very difficult problem, but it looks like the answer was erased. Thankfully, you can see the faint outline of the answer: 6975349.", None, isWall=True))
        r7.add_door(Door("East Door", "Heavy and iron, but it looks like it could be opened with the right code.", r8, r7_r8_puzzle))

        r8.add_door(Door("West Door", "Back to the study.", r7))

        r9.add_door(Door("North Door", "Back through the airlock.", r6))
        r9.add_door(Door("Portal", "The portal to freedom! Step through to escape and see what lies beyond!", None, None, isWall=True))

        # Add Rooms to the Game
        self.rooms.append(r1)
        self.rooms.append(r2)
        self.rooms.append(r3)
        self.rooms.append(r4)
        self.rooms.append(r0)
        self.rooms.append(r6)
        self.rooms.append(r7)
        self.rooms.append(r8)
        self.rooms.append(r9)