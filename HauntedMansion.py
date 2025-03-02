import random

# Create a class for the player to add themselves. 
class Player:
    def __init__(self, name):
        self.name = name
        self.hitpoints = 100
        self.intel = 0
        self.strength = 0
        self.perc = 0
        self.inventory = []
        self.turn = 0
        
    def __repr__(self):
        print("{name} has {hitpoints} HP, {intel} INT, {strength} STR, and {perc} PER.").format(name = self.name, hitpoints = self.hitpoints, intel = self.intel, strength = self.strength, perc = self.perc)
    
    # Used to determine how the player would like to start.
    def play_approach(self, play_type):
        while True:
            play_type = input("Enter a choice between 1-3. 1 is balanced play. 2 is RPG-style, and 3 is survival.")
            
            match play_type:
                case 1:
                    self.intel = 5      # Average intelligence; can pass some riddles, but tough ones require boosts.
                    self.strength = 5   # Can push light objects but struggles with heavy obstacles
                    self.perc = 5       # Notices obvious clues but may miss well-hidden ones.
                    break
                case 2:
                    self.intel = 10     # Average human intelligence
                    self.strength = 10  # Moderate strength
                    self.perc = 10      # Baseline awareness, but not hyper-perceptive
                    break
                case 3:
                    self.intel = 3      # Most riddles are difficult unless hints are found.
                    self.strength = 4   # Struggles to move heavy objects; requires creative solutions
                    self.perc = 6       # More sensitive to eerie details, but still misses hidden dangers.
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

class Rooms:
    rooms = ["Entrance Hall", "Library", "Dining Room", "Cellar", "Master Bedroom", "Attic", "Secret Tunnel"]
    
    def __init__(self, room_name):
        self.room_name = room_name
        
    # Triggered when the player enters the game.
    def entrance_hall(self):
        # Information on the room and options. 
        if self.turn == 0:
            print("You enter a dark mansion that creaks and groans as the wind howls. The entrance hall is cold and empty and you see the front door, a set of old stairs, an old painting, and a candle sitting on a table.")
        else:
            print("You're back in the entrance hall.")
        
        self.turn = self.turn + 1
        input("Do you want to 1. Try to open the door., 2. Examine the old painting., 3. Take the candle from the table., or 4. Climb up the stairs. Enter a choice between 1 and 4.")
        
        while True:
            option = input("Enter a choice. 1-4.")
            
            match option:
                case 1: # "Try to open the door."
                    print("It's locked.")
                    break
                case 2: # "Examine the old painting."
                    print("It whispers a clue.")
                    break
                case 3: # "Take the candle from the table."
                    print("This might be useful later.")
                    self.inventory.append("candle")
                    break
                case 4: # "Climb up the stairs."
                    entry_choice = random.choice(rooms)
                    match entry_choice:
                        case "Entrance Hall":
                            entrance_hall()
                        case "Library":
                            library()
                        case "Dining Room":
                            dining()
                        case "Cellar":
                            cellar()
                        case "Master Bedroom":
                            master()
                        case "Attic":
                            attic()
                        case "Secret Tunnel":
                            tunnel()
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")

    # Triggered when "library" is selected.
    def library(self):
        # Information on the room and options. 
        print("You enter a room with rows and rows of book shelves. There's a door behind you, a door to the east, a strange book in the bookcase across from you, a ladder leaning against one of the stacks, and a lit candle sitting on the table in the middle of the library.")
        
        self.turn = self.turn + 1
        input("Do you want to 1. Try to open the door behind you., 2. Read the strange book., 3. Blow out the candle on the table., 4. Move the ladder., or 5. Enter the East door. Enter a choice between 1 and 5.")
        
        while True:
            option = input("Enter a choice. 1-5.")
            
            match option:
                case 1: # "Try to open the door behind you."
                    print("The door is locked.")
                    break
                case 2: # "Read a strange book."
                    print("A secret door is exposed.")
                    door = input("Do you want to walk through the door? y or n")
                    if door == "y" or "Y":
                        entry_choice = random.choice(rooms)
                        match entry_choice:
                            case "Entrance Hall":
                                entrance_hall()
                            case "Library":
                                library()
                            case "Dining Room":
                                dining()
                            case "Cellar":
                                cellar()
                            case "Master Bedroom":
                                master()
                            case "Attic":
                                attic()
                            case "Secret Tunnel":
                                tunnel()
                    else:
                        print("You walk away from the door.")
                    break
                case 3: # "Move the ladder."
                    print("A ghost appears and wants to speak with you.")
                    print(ghost("library"))                    
                    break
                case 4: # "Move the ladder."
                    print("A note reads 'I thought you would save me.'.")
                    break
                case 5: # "Enter the East door."
                    entry_choice = random.choice(rooms)
                    match entry_choice:
                        case "Entrance Hall":
                            entrance_hall()
                        case "Library":
                            library()
                        case "Dining Room":
                            dining()
                        case "Cellar":
                            cellar()
                        case "Master Bedroom":
                            master()
                        case "Attic":
                            attic()
                        case "Secret Tunnel":
                            tunnel()
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    # Triggered when "dining room" is selected.
    def dining(self):
        # Information on the room and options. 
        print("You enter a room with a long table with a tablecloth and 12 seats, 4 on each side and 1 on each end. There's a door behind you, a door to the north, mysterious food on the plate in front of the chair closest to you, and portraits lining both walls to your left and right.")
        
        self.turn = self.turn + 1
        input("Do you want to 1. Try to open the door behind you., 2. Eat the mysterious food., 3. Look under the tablecloth., 4. Inspect the portraits., or 5. Enter the North door. Enter a choice between 1 and 5.")
        
        while True:
            option = input("Enter a choice. 1-5.")
            
            match option:
                case 1: # "Try to open the door behind you."
                    print("The door is locked.")
                    break
                case 2: # "Eat the mysterious food."
                    choices: ["poison", "hint"]
                    meal = random.choice(choices)
                    if meal == "poison":
                        if self.hitpoints <= 50:
                            print("You've become the new ghost of this mansion.")
                        else:
                            self.hitpoints == self.hitpoints - 50
                            print("You've been poisoned. You've lost HP. Your HP is now at {hitpoints},").format(hitpoints = self.hitpoints)
                    else:
                        print("A note reads 'Go through the south door'.")
                    break
                case 3: # "Look under the tablecloth."
                    print("You find a key.")
                    self.inventory.append("key")                 
                    break
                case 4: # "Inspect the portraits on the wall."
                    print("One is missing an eye.")
                    break
                case 5: # "Enter the North door."
                    entry_choice = random.choice(rooms)
                    match entry_choice:
                        case "Entrance Hall":
                            entrance_hall()
                        case "Library":
                            library()
                        case "Dining Room":
                            dining()
                        case "Cellar":
                            cellar()
                        case "Master Bedroom":
                            master()
                        case "Attic":
                            attic()
                        case "Secret Tunnel":
                            tunnel()
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    def cellar(self):
            # Information on the room and options. 
            print("You're in a dimly lit, cold, damp room that smells a bit like decay. You see racks of old wine bottles, some matches on a table next to you, and...something else?")
            
            self.turn = self.turn + 1
            input("Do you want to 1. Listen carefully., 2. Examine the old wine bottles., or 3. Light a match. Enter a choice between 1 and 3.")
            
            while True:
                option = input("Enter a choice. 1-3.")
                
                match option:
                    case 1: # "Listen carefully."
                        if self.perc > 5:
                            self.perc = self.perc + 1
                            print("You hear some whispers.")
                            whisper = input("Do you want to follow or run? Enter 'f' or 'r'")
                            if whisper == "f":
                                print("A ghost tries to possess you!")
                                if self.strength > 5:
                                    print("The ghost is unsuccessful.")
                                    self.strength = self.strength + 1
                                else:
                                    print("The ghost is now possessing your body. Your soul has moved onto the Underworld.")
                                    self.hitpoints = 0
                            else:
                                entry_choice = random.choice(rooms)
                                match entry_choice:
                                    case "Entrance Hall":
                                        entrance_hall()
                                    case "Library":
                                        library()
                                    case "Dining Room":
                                        dining()
                                    case "Cellar":
                                        cellar()
                                    case "Master Bedroom":
                                        master()
                                    case "Attic":
                                        attic()
                                    case "Secret Tunnel":
                                        tunnel()
                        else:
                            print("A ghost is now possessing your body. Your soul has moved onto the Underworld.")
                            self.hitpoints = 0
                        break
                    case 2: # "Examine the old wine bottles."
                        print("A secret door is opened.")
                        secret_door = input("Would you like to go through it? y or n")
                        if secret_door == "y":
                            entry_choice = random.choice(rooms)
                            match entry_choice:
                                case "Entrance Hall":
                                    entrance_hall()
                                case "Library":
                                    library()
                                case "Dining Room":
                                    dining()
                                case "Cellar":
                                    cellar()
                                case "Master Bedroom":
                                    master()
                                case "Attic":
                                    attic()
                                case "Secret Tunnel":
                                    tunnel()
                        else:
                            break
                    case 3: # "Light a match."
                        print("A hidden passage is shown.")
                        hidden_passage = input("Would you like to follow it? y or no")
                        if hidden_passage == "y":
                            secret_door = input("Would you like to go through it? y or n")
                            match secret_door:
                                case "y":
                                    entry_choice = random.choice(rooms)
                                    match entry_choice:
                                        case "Entrance Hall":
                                            entrance_hall()
                                        case "Library":
                                            library()
                                        case "Dining Room":
                                            dining()
                                        case "Cellar":
                                            cellar()
                                        case "Master Bedroom":
                                            master()
                                        case "Attic":
                                            attic()
                                        case "Secret Tunnel":
                                            tunnel()
                        else:
                            break
                    case _:
                        print("Invalid choice. Please enter a number between 1 and 3.")