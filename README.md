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
                              *A Text‑Based Escape Room Puzzle Game*

📖 Overview

**Inkbound** is a text-based escape room game written in Python using object-oriented programming.  
The player wakes up in an unfamiliar place with no memory and a mysterious tattoo on their wrist. As they explore, they discover the tattoo is a living map that updates as new rooms are explored. To escape, the player must solve puzzles, collect items, unlock doors, and trace the correct path through the rooms.

The game emphasizes exploration, logical reasoning, and narrative discovery, all delivered through a command-line interface.


🎮 Gameplay Summary
*   The player starts in the central room.
*   The tattoo map begins incomplete and expands as rooms are visited.
*   Doors between rooms may be locked and require:
    *   Solving puzzles
    *   Using items
*   The goal is to reach the final room and escape.


🧠 Core Features

*   Fully text-based gameplay
*   Dynamic ASCII room map
*   Inventory system
*   Multiple puzzle types using inheritance
*   Locked and unlocked doors
*   A clear win condition
*   Atmospheric story integrated into gameplay


🗂️ Project Structure

    Inkbound/
    ├── main.py          # Initializer and start/end credits
    ├── game.py          # Main game loop
    ├── player.py        # Player and inventory handling
    ├── room.py          # Room definitions and behaviors
    ├── door.py          # Door and locking logic
    ├── items.py         # Item and KeyItem classes
    ├── puzzles.py       # Puzzle base class and subclasses
    ├── README.md        # Project documentation


🧱 Object-Oriented Design

Core Classes

*   **Game** – Controls the main loop and player actions
*   **Player** – Tracks current room, inventory, and visited rooms
*   **Room** – Holds items, puzzles, and doors
*   **Door** – Connects rooms and controls access

Inheritance

*   **Item**
    *   `KeyItem`
*   **Puzzle**
    *   `NumberPuzzle`
    *   `WordPuzzle`
    *   `PatternPuzzle`
    *   `KeyPuzzle`

OOP Concepts Used

*   ✅ Encapsulation
*   ✅ Inheritance
*   ✅ Polymorphism
*   ✅ Composition


🧩 Puzzle Types

The game includes multiple puzzle types, such as:

*   **Word puzzles** (enter correct words)
*   **Number puzzles** (solve number patterns)
*   **Key puzzles** (use the correct item)

Some puzzles block progress and must be solved to continue.


🗺️ ASCII Map System

The tattoo map is represented using ASCII art.
The map updates dynamically as rooms are explored.


▶️ How to Run the Game

1.  Make sure you have **Python 3.8+** installed.
2.  Open a terminal in the project folder.
3.  Run:
    ```bash
    python game.py
    ```
4.  Follow the on-screen prompts to move and interact.


🏁 Win Condition

The game is won when the player:

*   Unlocks the final door
*   Solves the final pattern puzzle
*   Enters the goal room


👨‍💻 Author

**Inkbound** was created as a final project for a Computer Science course, demonstrating object‑oriented design, problem‑solving, and creative storytelling in Python.
*   Puzzles, items, rooms, and story integration

