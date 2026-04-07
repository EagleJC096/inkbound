import os
import time
from door import Door
from puzzle import *
from item import Item
import puzzle
from room import Room


class Game:
    def __init__(self):
        self.rooms = []
        self.item_indexes = []

    def show_rooms(self):
        self.print_Room()

    # def print_Room(self, player_index):
    #     columns=3
    #     rows = len(self.rooms) // columns
    #     horizontal_wall = "+-----"
    #     empty_space = "|     "

    #     index = 1

    #     for r in range(rows):
    #         # Top wall
    #         print((horizontal_wall * columns) + "+")

    #         # Room content line
    #         line = ""
    #         for c in range(columns):

    #             # Decide what to display
    #             symbol = ""
    #             if index == player_index:
    #                 symbol = "P "
    #             elif index == 9:
    #                 symbol = "֎ "

    #             line += f"|  {symbol:^3}"
    #             index += 1

    #         line += "|"
    #         print(line)

    #         # Padding line
    #         print((empty_space * columns) + "|")

    #     # Bottom wall
    #     print((horizontal_wall * columns) + "+")
    #     time.sleep(1)

    # def print_Room(self, player_index):
        columns = 3
        total_rooms = len(self.rooms)
        rows = total_rooms // columns

        for r in range(rows):

            # ---------- TOP WALLS ----------
            top_line = ""
            for c in range(columns):
                room_number = r * columns + c + 1      # ✅ 1-based
                room = self.rooms[room_number - 1]    # ✅ convert to 0-based

                if room.isDiscovered:
                    top_line += "+-----"
                else:
                    top_line += "      "
            if room.isDiscovered: top_line += "+"
            print(top_line)

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

                    content_line += f"|  {symbol:^3}"
                else:
                    content_line += "      "

            # Right wall only if the LAST room in the row is discovered
            last_room_number = r * columns + columns
            last_room = self.rooms[last_room_number - 1]
            content_line += "|" if last_room.isDiscovered else ""
            print(content_line)

            # ---------- PADDING LINE ----------
            padding_line = ""
            for c in range(columns):
                room_number = r * columns + c + 1
                room = self.rooms[room_number - 1]

                if room.isDiscovered:
                    padding_line += "|     "
                else:
                    padding_line += "      "

            padding_line += "|" if last_room.isDiscovered else ""
            print(padding_line)

        # ---------- BOTTOM WALLS ----------
        bottom_line = ""
        for c in range(columns):
            room_number = total_rooms - columns + c + 1
            room = self.rooms[room_number - 1]

            if room.isDiscovered:
                bottom_line += "+-----"
            else:
                bottom_line += "      "
        bottom_line += "+"
        print(bottom_line)

        time.sleep(1)

    def print_Room(self, player_index):
        columns = 3
        total_rooms = len(self.rooms)
        rows = total_rooms // columns

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
            print(top_line)

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
            print(content_line)

            # ---------- BOTTOM WALLS ----------
            bottom_line = ""
            for c in range(columns):
                room_number = r * columns + c + 1
                room = self.rooms[room_number - 1]

                if room.isDiscovered:
                    bottom_line += "+-----+"
                else:
                    bottom_line += "       "
            print(bottom_line)

        time.sleep(1)
    
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
                    print(current_room_desc)
                    print("")
                    room_choices = self.load_choices(room)
                    i = 0
                    for choice in room_choices:
                        print(f"{i + 1}: {choice[1]}")
                        i += 1
                    print("")
                    
                    while True:
                        try:
                            door_choice = int(input("Which door would you like to go through? ")) - 1
                            if 0 <= door_choice < len(room_choices):
                                choice_is_valid = self.move_player(player, room.doors[door_choice])
                                break
                            else:
                                print("Invalid choice. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue

    def load_choices(self, room):
        choices = []
        for door in room.doors:
            choice = [door.leads_to.index, f"Move through the {door.name}"]
            choices.append(choice)
        return choices

    def move_player(self, player, door):
        if not door.isLocked():
            player.position = door.leads_to
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You move through the {door.name} to {door.leads_to.name}.")
            return True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if door.puzzle.solution is None:
                print(f"{door.description}")
                return False
            print(f"The {door.name} is locked. You need to solve the puzzle to unlock it. Type 'exit' to go back.\n")
            self.solve_attempt(door.puzzle, player, door)
            return False
        
    def solve_attempt(self, puzzle, player, door):
        print(puzzle.description)
        user_input = input("Enter your solution: ")
        while not user_input.lower() == "exit":
            if puzzle.validate_attempt(user_input, player):
                print("Puzzle solved! The door is now unlocked.")
                door.unlock()
                self.move_player(player, door)
                return True
            else:
                print("Incorrect solution. Try again.")
                user_input = input("Enter your solution: ")
        print("Exiting puzzle attempt.")
        return False
        

    def win_condition(self, player):
        # Define the win condition for the game, such as reaching a specific room or collecting certain items
        for item in player._inventory:
            if item.name == "Portal":
                print("Congratulations! You've found the portal and won the game!")
                return True
        return False
            
    def end_game(self):
        print("Game Over. Thanks for playing!")

    def load_rooms(self):
        r0_initial_desc = """When you wake up, 
you have no idea where you are, and no memory of how you got here. 
You are lying on the cold, hard ground, with one clear thought: 
"I need to get out of here!" You look at your wrist, 
and you can immediately see some kind of marking that looks like a tattoo, 
and it reminds you of the room you are in. As you look around you, 
you see a door in each of the four walls of your room. 
You must get out of this place by any means necessary.
But how?"""

        # Initialize Rooms
        r1 = Room(1, "Room 1", "When you enter the room, you see storage shelves lining the walls, but they are mostly empty. However, you do find an odd looking key. You take the key and put in in the pocket of your clothes for later use.", "You are back in the empty storage room.")
        r2 = Room(2, "Room 2", "This room has a strange feeling. You see two doors, one on the west wall and one on the east wall, as well as the south door that you came from. Both side doors seem to have puzzles attached. You cannot go anywhere else without attempting a puzzle. What now?", "You are back in Room 2.")
        r3 = Room(3, "Room 3", "The light you saw from the start room looks even brighter as it shines from under a doorway to the south.", "You go back through the airlock. It's a cool room, but you need to find the ID badge for the safe.")
        r4 = Room(4, "Room 4", "You are in Room 4, which almost looks like barracks. There are bunkbeds (still made), and someone appears to have written on the wall.", "You are back in the barracks. That pattern on the wall is really out of place...")
        r0 = Room(5, "Start Room", r0_initial_desc, "You are back in the start room.", True)
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

        r4_r7_puzzle = PatternPuzzle("You see a door with a strange pattern.", "What could this pattern mean?", "The pattern resembles a star.")

        r7_r8_puzzle = NumberPuzzle("You see a door with a number pad.", "What is the code to unlock this door?", 6975349)

        # Initialize Doors
        r0.add_door(Door("North Door", "You walk through a doorway that seems to have its door completely removed. You can still see the marks where the hinges were.", r2))
        r0.add_door(Door("East Door", "The door here seems to be sealed, but there is a small crack in the frame, and a faint blue light bleeds through. Sunlight?", r6, unlockable_puzzle))
        r0.add_door(Door("West Door", "The door is firm and made of metal. Is something important behind it?", r4, r0_r4_puzzle))

        r1.add_door(Door("East Door", "This door goes to Room 2.", r2))

        r2.add_door(Door("North Door", "The door here is completely sealed and is bare, except for a poster with a soldier at attention and the word 'StarForce' emblazoned on it.", r9, unlockable_puzzle))
        r2.add_door(Door("West Door", "This door goes back to Room 1.", r1, r2_r1_puzzle))
        r2.add_door(Door("East Door", "This door goes to Room 3.", r3, r2_r3_puzzle))
        r2.add_door(Door("South Door", "This door goes to the starting room.", r0))

        r3.add_door(Door("West Door", "This door goes back to Room 2.", r2))
        r3.add_door(Door("South Door", "This door looks like an airlock designed to keep the atmosphere in. You can see a door that looks like a safe at the far end of the room. A mysterious blue glow emanates from it.", r6, r3_r6_puzzle))

        r4.add_door(Door("East Door", "This door goes back to the start room.", r0))
        r4.add_door(Door("South Door", "The door is ornate and made of ironwood. Something tells you this door may be the most important of all!", r7, r4_r7_puzzle))

        r6.add_door(Door("North Door", "This door goes back to Room 3.", r3))
        r6.add_door(Door("South Door", "This door looks like a safe. There's no keyhole or pad for this one...just an ID badge scanner", r9, r6_r9_puzzle))

        r7.add_door(Door("North Door", "This door goes back to the barracks.", r4))
        r7.add_door(Door("East Door", "This door is heavy and iron, but it looks like it could be opened with the right code.", r8, r7_r8_puzzle))

        r8.add_door(Door("West Door", "This door goes back to the study.", r7))

        r9.add_door(Door("North Door", "This door goes back to the airlock.", r6))

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