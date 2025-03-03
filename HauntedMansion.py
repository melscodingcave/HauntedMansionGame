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
        return "{name} has {hitpoints} HP, {intel} INT, {strength} STR, and {perc} PER.".format(name = self.name, hitpoints = self.hitpoints, intel = self.intel, strength = self.strength, perc = self.perc)
    
    # Used to determine how the player would like to start.
    def play_approach(self, play_type):
        while True:
            play_type = input("Enter a choice between 1-3. 1 is balanced play. 2 is RPG-style, and 3 is survival.")
            
            match play_type:
                case "1":
                    self.intel = 5      # Average intelligence; can pass some riddles, but tough ones require boosts.
                    self.strength = 5   # Can push light objects but struggles with heavy obstacles
                    self.perc = 5       # Notices obvious clues but may miss well-hidden ones.
                    break
                case "2":
                    self.intel = 10     # Average human intelligence
                    self.strength = 10  # Moderate strength
                    self.perc = 10      # Baseline awareness, but not hyper-perceptive
                    break
                case "3":
                    self.intel = 3      # Most riddles are difficult unless hints are found.
                    self.strength = 4   # Struggles to move heavy objects; requires creative solutions
                    self.perc = 6       # More sensitive to eerie details, but still misses hidden dangers.
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

class Rooms:
    def __init__(self, room_name, player):
        self.room_name = room_name
        self.player = player
        self.rooms = ["Entrance Hall", "Library", "Dining Room", "Cellar", "Master Bedroom", "Attic", "Secret Tunnel"]
        self.room_methods = {
            "Entrance Hall": self.entrance_hall,
            "Library": self.library,
            "Dining Room": self.dining,
            "Cellar": self.cellar,
            "Master Bedroom": self.master_bedroom,
            "Attic": self.attic,
            "Secret Tunnel": self.secret_tunnel
        }
        
    # Triggered when the player enters the game.
    def entrance_hall(self):
        # Information on the room and options. 
        if self.player.turn == 0:
            print("You enter a dark mansion that creaks and groans as the wind howls. The entrance hall is cold and empty and you see the front door, a set of old stairs, an old painting, and a candle sitting on a table.")
        else:
            print("You're back in the entrance hall.")
        
        self.player.turn += 1
        input("Do you want to 1. Try to open the door., 2. Examine the old painting., 3. Take the candle from the table., or 4. Climb up the stairs. Enter a choice between 1 and 4.")
        
        while True:
            option = input("Enter a choice. 1-4.")
            
            match option:
                case "1": # "Try to open the door."
                    print("It's locked.")
                    break
                case "2": # "Examine the old painting."
                    print("It whispers a clue.")
                    break
                case "3": # "Take the candle from the table."
                    print("This might be useful later.")
                    self.inventory.append("candle")
                    break
                case "4": # "Climb up the stairs."
                    self.room_methods[random.choice(self.rooms)]()
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")

    # Triggered when "library" is selected.
    def library(self):
        # Information on the room and options. 
        print("You enter a room with rows and rows of book shelves. There's a door behind you, a door to the east, a strange book in the bookcase across from you, a ladder leaning against one of the stacks, and a lit candle sitting on the table in the middle of the library.")
        
        self.player.turn += 1
        input("Do you want to 1. Try to open the door behind you., 2. Read the strange book., 3. Blow out the candle on the table., 4. Move the ladder., or 5. Enter the East door. Enter a choice between 1 and 5.")
        
        while True:
            option = input("Enter a choice. 1-5.")
            
            match option:
                case "1": # "Try to open the door behind you."
                    print("The door is locked.")
                    break
                case "2": # "Read a strange book."
                    print("A secret door is exposed.")
                    door = input("Do you want to walk through the door? y or n")
                    if door.lower() == "y":
                        self.room_methods[random.choice(self.rooms)]()
                    else:
                        print("You walk away from the door.")
                    break
                case "3": # "Move the ladder."
                    print("A ghost appears and wants to speak with you.")
                    print(ghost("library"))                    
                    break
                case "4": # "Move the ladder."
                    print("A note reads 'I thought you would save me.'.")
                    break
                case "5": # "Enter the East door."
                    self.room_methods[random.choice(self.rooms)]()
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    # Triggered when "dining room" is selected.
    def dining(self):
        # Information on the room and options. 
        print("You enter a room with a long table with a tablecloth and 12 seats, 4 on each side and 1 on each end. There's a door behind you, a door to the north, mysterious food on the plate in front of the chair closest to you, and portraits lining both walls to your left and right.")
        
        self.player.turn += 1
        input("Do you want to 1. Try to open the door behind you., 2. Eat the mysterious food., 3. Look under the tablecloth., 4. Inspect the portraits., or 5. Enter the North door. Enter a choice between 1 and 5.")
        
        while True:
            option = input("Enter a choice. 1-5.")
            
            match option:
                case "1": # "Try to open the door behind you."
                    print("The door is locked.")
                    break
                case "2": # "Eat the mysterious food."
                    choices: ["poison", "hint"]
                    meal = random.choice(choices)
                    if meal == "poison":
                        if self.hitpoints <= 50:
                            print("You've become the new ghost of this mansion.")
                        else:
                            self.hitpoints -= 50
                            print("You've been poisoned. You've lost HP. Your HP is now at {hitpoints},").format(hitpoints = self.hitpoints)
                    else:
                        print("A note reads 'Go through the south door'.")
                    break
                case "3": # "Look under the tablecloth."
                    print("You find a key.")
                    self.player.inventory.append("key")                 
                    break
                case "4": # "Inspect the portraits on the wall."
                    print("One is missing an eye.")
                    break
                case "5": # "Enter the North door."
                    self.room_methods[random.choice(self.rooms)]()
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    def cellar(self):
            # Information on the room and options. 
            print("You're in a dimly lit, cold, damp room that smells a bit like decay. You see racks of old wine bottles, some matches on a table next to you, and...something else?")
            
            self.player.turn += 1
            input("Do you want to 1. Listen carefully., 2. Examine the old wine bottles., or 3. Light a match. Enter a choice between 1 and 3.")
            
            while True:
                option = input("Enter a choice. 1-3.")
                
                match option:
                    case "1": # "Listen carefully."
                        if self.player.perc > 5:
                            self.player.perc += 1
                            print("You hear some whispers.")
                            whisper = input("Do you want to follow or run? Enter 'f' or 'r'")
                            if whisper == "f":
                                print("A ghost tries to possess you!")
                                if self.player.strength > 5:
                                    print("The ghost is unsuccessful.")
                                    self.player.strength += 1
                                else:
                                    print("The ghost is now possessing your body. Your soul has moved onto the Underworld.")
                                    self.player.hitpoints = 0
                            else:
                                self.room_methods[random.choice(self.rooms)]()
                        else:
                            print("A ghost is now possessing your body. Your soul has moved onto the Underworld.")
                            self.player.hitpoints = 0
                        break
                    case "2": # "Examine the old wine bottles."
                        print("A secret door is opened.")
                        secret_door = input("Would you like to go through it? y or n")
                        if secret_door.lower() == "y":
                            self.room_methods[random.choice(self.rooms)]()
                        else:
                            break
                    case "3": # "Light a match."
                        print("A hidden passage is shown.")
                        hidden_passage = input("Would you like to follow it? y or no")
                        if hidden_passage.lower() == "y":
                            secret_door = input("Would you like to go through it? y or n")
                            match secret_door.lower():
                                case "y":
                                    self.room_methods[random.choice(self.rooms)]()
                        break
                    case _:
                        print("Invalid choice. Please enter a number between 1 and 3.")
    
    def master_bedroom(self):
        # Information on the room and options. 
        print("You find yourself in a room with a four-poster bed, a dusty mirror and a dilapidated wardrobe. The door you entered in is now behind you.")
        
        self.player.turn += 1
        input("Do you want to 1. Open the wardrobe., 2. Look under the bed., 3. Stare into the mirror., or 4. Try the door behind you. Enter a choice between 1 and 4.")
        
        while True:
            option = input("Enter a choice. 1-4.")
            
            match option:
                case "1": # "Open the wardrobe."
                    print("A ghost appears and wants to speak with you.")
                    print(ghost("master"))    
                    break
                case "2": # "Look under the bed."
                    if self.player.hitpoints <= 50:
                            print("You've become the new ghost of this mansion after being attacked by a ghoul.")
                    else:
                        self.player.hitpoints -= 50
                        print("You've been attacked! You've lost HP. Your HP is now at {hitpoints},").format(hitpoints = self.hitpoints)
                        ghoul_fight = input("Will you run or fight the ghoul? y or n")
                        if ghoul_fight.lower() == "y":
                            if self.strength >= 8:
                                print("You won the fight! The ghoul left behind a key.")
                                self.player.inventory.append("Ghoul Key")
                            elif self.player.strength >= 4:
                                print("The fight is evenly matched.")
                                fight_option = input("Choose a number between 1 & 5.")
                                random_num = random.randint(1, 5)
                                if random_num == fight_option:
                                    print("You won the fight! The ghoul left behind a key.")
                                    self.player.inventory.append("Ghoul Key")
                                else:
                                    print("You've lost! You've become the newest ghost of this mansion.")
                                    self.player.hitpoints = 0
                            else:
                                print("You've lost! You've become the newest ghost of this mansion.")
                                self.player.hitpoints = 0
                    break
                case "3": # "Stare into the mirror."
                    print("Your reflect is....different.")
                    break
                case "4": # "Try the door behind you"
                    self.room_methods[random.choice(self.rooms)]()
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")
                    
    def attic(self):
        # Information on the room and options. 
        print("You find yourself in a dark room with long forgotten objects. There's a window to the outside world, the door behind you, a broken doll, and an old chest.")
        
        self.player.turn += 1
        input("Do you want to 1. Look out the window., 2. Open the old chest., 3. Pick up the broken doll., or 4. Try the door behind you. Enter a choice between 1 and 4.")
        
        while True:
            option = input("Enter a choice. 1-4.")
            
            match option:
                case "1": # "Look out the window."
                    print("A shadow is seen moving through the garden.")
                    break
                case "2": # "Open the old chest."
                    print("You find an old rusted crowbar.")
                    self.player.inventory.append("Crowbar")
                    break
                case "3": # "Pick up the broken doll."
                    print("It looks like it's trying to tell you something.")
                    if self.player.intel >= 5:
                        print("You put the doll up to your ear and it says 'Find the tunnel'")
                    break
                case "4": # "Try the door behind you"
                    self.room_methods[random.choice(self.rooms)]()
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    def secret_tunnel(self):
        # Information on the room and options. 
        print("You see a dark underground passage leading out....or deeper into danger.")
        
        self.player.turn += 1
        input("Do you want to 1. Follow the rats., 2. Touch the mossy wall., or 3. Light your candle. Enter a choice between 1 and 3.")
        
        while True:
            option = input("Enter a choice. 1-3.")
            
            match option:
                case "1": # "Follow the rats."
                    print("You've escaped the mansion!")
                    break
                case "2": # "Touch the mossy wall."
                    print("You find an old lever that seems rusted and unusable.")
                    mossy_wall = input("Do you want to try to pull the lever? y or n")
                    if mossy_wall.lower() == "y" and self.player.strength >= 10:
                        print("The wall opens and another passage is revealed")
                        passage = input("Do you want to take the passage? y or n")
                        if passage.lower() == "y":
                            print("You've escaped the mansion!")
                        else:
                            print("You fall into a pit. HP has been reduced.")
                            self.player.hitpoints -= 10
                    break
                case "3": # "Light your candle."
                    if "candle" in self.player.inventory:
                        print("The candle light shows glowing symbols on the walls directing you down the passage.")
                        print("Following the passage leads you out of the mansion. You've escaped!")
                    else:
                        print("You have no candle to light.")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")
                    break