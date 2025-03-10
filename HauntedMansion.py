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
        self.has_escaped = False
        self.is_ghost = False
        self.is_possessed = False
        
    def __repr__(self):
        return "{name} has {hitpoints} HP, {intel} INT, {strength} STR, and {perc} PER.".format(name = self.name, hitpoints = self.hitpoints, intel = self.intel, strength = self.strength, perc = self.perc)
    
    # Used to determine how the player would like to start.
    def play_approach(self):
        while True:
            play_type = input("Enter a choice between 1-3. 1 is balanced play. 2 is RPG-style, and 3 is survival. ")
            
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
                    print("Invalid choice. Please enter a number between 1 and 3. ")

class Rooms:
    def __init__(self, current_room, player):
        self.current_room = current_room
        self.player = player
        self.rooms = ["Entrance Hall", "Library", "Dining Room", "Cellar", "Master Bedroom", "Attic", "Secret Tunnel"]
        self.lib = 0
        self.din = 0
        self.cel = 0 
        self.master = 0
        self.att = 0
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
        if self.player.turn == 0:
            print("You enter a grand, dusty hall with a locked front door.")
        else:
            print("You're back in the entrance hall.")
        
        # Increase amount of turns user has gone through
        self.player.turn += 1
        # Options to move forward in the game
        print("Do you want to 1. Try to open the door., 2. Examine the old painting., 3. Take the candle from the table., or 4. Climb up the stairs?")
        
        # Ensure user can select options.
        while True:
            option = input("Enter a choice. 1-4. ")
            
            match option:
                case "1": # "Try to open the door."
                    print("It's locked.")
                    break
                case "2": # "Examine the old painting."
                    print("You find a message that reads 'Up the stairs awaits the path.'")
                    break
                case "3": # "Take the candle from the table."
                    print("This might be useful later.")
                    self.player.inventory.append("candle")
                    break
                case "4": # "Climb up the stairs."
                    self.current_room = "Dining Room"
                    break # Exit this room after moving to the next one.
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")

    # Triggered when "library" is selected.
    def library(self):  
        print("You enter a massive, dimly lit room filled with books.")
        
        self.player.turn += 1
        self.current_room = "Library"
        print("Do you want to 1. Try to open the door behind you., 2. Read the strange book., 3. Blow out the candle on the table., 4. Move the ladder., or 5. Enter the East door?")
        
        while True:
            option = input("Enter a choice. 1-5. ")
            
            match option:
                case "1": # "Try to open the door behind you."
                    print("The door is locked. ")
                    break
                case "2": # "Read a strange book."
                    print("A secret door is exposed.")
                    door = input("Do you want to walk through the door? y or n")
                    if door.lower() == "y":
                        self.current_room = random.choice(self.rooms)
                        break
                    else:
                        print("You walk away from the door.")
                    break
                case "3": # "Move the ladder."
                    print("A ghost appears and wants to speak with you.")
                    self.ghost("library")               
                    break
                case "4": # "Move the ladder."
                    print("A note reads 'I thought you would save me.'.")
                    break
                case "5": # "Enter the East door."
                    self.current_room = "Master Bedroom"
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    # Triggered when "dining room" is selected.
    def dining(self):
        print("You enter a room where there is a long table with untouched food.")
        
        self.current_room = "Dining Room"
        self.player.turn += 1
        print("Do you want to 1. Try to open the door behind you., 2. Eat the mysterious food., 3. Look under the tablecloth., 4. Inspect the portraits., or 5. Climb up the stairs.")
        
        while True:
            option = input("Enter a choice. 1-5. ")
            
            match option:
                case "1": # "Try to open the door behind you."
                    print("The door is locked.")
                    break
                case "2": # "Eat the mysterious food."
                    choices = ["poison", "hint"]
                    meal = random.choice(choices)
                    if meal == "poison":
                        if self.player.hitpoints <= 50:
                            print("You've become the new ghost of this mansion.")
                            self.player.is_ghost = True
                        else:
                            self.player.hitpoints -= 50
                            print("You've been poisoned. You've lost HP. Your HP is now at {hitpoints},".format(hitpoints = self.player.hitpoints))
                    else:
                        print("A note reads 'Go through the North door'.")
                    break
                case "3": # "Look under the tablecloth."
                    print("You find a dusty engagement ring.")
                    self.player.inventory.append("ring")
                    print(self.player.inventory)     
                    break
                case "4": # "Inspect the portraits on the wall."
                    print("One is missing an eye.")
                    break
                case "5": # "Climb up the stairs."
                    self.current_room = "Attic"
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    def cellar(self):
        print("You enter a cold, damp room with a strong smell of decay.")
        
        self.current_room = "Cellar"
        self.player.turn += 1
        print("Do you want to 1. Listen carefully., 2. Examine the old wine bottles., or 3. Light a match.?")
        
        while True:
            option = input("Enter a choice. 1-3. ")
            
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
                                self.player.is_possessed = True
                        else:
                            self.current_room = random.choice(self.rooms)
                            break
                    else:
                        print("A ghost is now possessing your body. Your soul has moved onto the Underworld.")
                        self.player.is_possessed = True
                    break
                case "2": # "Examine the old wine bottles."
                    print("A secret door is opened.")
                    secret_door = input("Would you like to go through it? y or n")
                    if secret_door.lower() == "y":
                        self.current_room = random.choice(self.rooms)
                        break
                    break
                case "3": # "Light a match."
                    print("A hidden passage is shown.")
                    hidden_passage = input("Would you like to follow it? y or n")
                    if hidden_passage.lower() == "y":
                        secret_door = input("Would you like to go through it? y or n")
                        match secret_door.lower():
                            case "y":
                                self.current_room = random.choice(self.rooms)
                                break
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")
    
    def master_bedroom(self):
        print("You find yourself in a room with a four-poster bed and a dusty mirror.")
        
        self.current_room = "Master Bedroom"
        self.player.turn += 1
        print("Do you want to 1. Open the wardrobe., 2. Look under the bed., 3. Stare into the mirror., or 4. Try the door behind you.?")
        
        while True:
            option = input("Enter a choice. 1-4. ")
            
            match option:
                case "1": # "Open the wardrobe."
                    print("A ghost appears and wants to speak with you.")
                    self.ghost("master")  
                    break
                case "2": # "Look under the bed."
                    if self.player.hitpoints <= 50:
                        print("You've become the new ghost of this mansion after being attacked by a ghoul.")
                        end_game(self.player)
                    else:
                        self.player.hitpoints -= 50
                        print("You've been attacked! You've lost HP. Your HP is now at {hitpoints}.".format(hitpoints = self.player.hitpoints))
                        ghoul_fight = input("Will you run or fight the ghoul? y or n ")
                        if ghoul_fight.lower() == "y":
                            if self.player.strength >= 8:
                                print("You won the fight! The ghoul left behind a key.")
                                self.player.inventory.append("Ghoul Key")
                            elif self.player.strength >= 4:
                                print("The fight is evenly matched.")
                                fight_option = input("Choose a number between 1 & 5. ")
                                random_num = random.randint(1, 5)
                                if random_num == fight_option:
                                    print("You won the fight! The ghoul left behind a key.")
                                    self.player.inventory.append("Ghoul Key")
                                else:
                                    print("You've lost! You've become the newest ghost of this mansion.")
                                    self.player.is_ghost = True
                            else:
                                print("You've lost! You've become the newest ghost of this mansion.")
                                self.player.is_ghost = True
                    break
                case "3": # "Stare into the mirror."
                    print("Your reflection is....different.")
                    break
                case "4": # "Try the door behind you"
                    self.current_room = random.choice(self.rooms)
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")
                    
    def attic(self):
        print("You find yourself in a dark room with long forgotten objects.")
        
        self.current_room = "Attic"
        self.player.turn += 1
        print("Do you want to 1. Look out the window., 2. Open the old chest., 3. Pick up the broken doll., or 4. Try the door behind you?")
        
        while True:
            option = input("Enter a choice. 1-4. ")
            
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
                    self.current_room = random.choice(self.rooms)
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")

    def secret_tunnel(self):
        # Information on the room and options. 
        print("You see a dark underground passage leading out....or deeper into danger.")
        
        self.player.current_room = "Secret Tunnel"
        self.player.turn += 1
        print("Do you want to 1. Follow the rats., 2. Touch the mossy wall., or 3. Light your candle?")
        
        while True:
            option = input("Enter a choice. 1-3. ")
            
            match option:
                case "1": # "Follow the rats."
                    print("You've escaped the mansion!")
                    self.player.has_escaped = True
                    break
                case "2": # "Touch the mossy wall."
                    print("You find an old lever that seems rusted and unusable.")
                    mossy_wall = input("Do you want to try to pull the lever? y or n ")
                    if mossy_wall.lower() == "y" and self.player.strength >= 10:
                        print("The wall opens and another passage is revealed")
                        passage = input("Do you want to take the passage? y or n ")
                        if passage.lower() == "y":
                            print("You've escaped the mansion!")
                            self.player.has_escaped = True
                        elif "Crowbar" in self.player.inventory:
                            print("Using the crowbar, you force the lever down. The passage opens!")
                            print("You've escaped the mansion!")
                            self.player.has_escaped = True
                        else:
                            print("You fall into a pit. HP has been reduced.")
                            self.player.hitpoints -= 10
                    break
                case "3": # "Light your candle."
                    if "candle" in self.player.inventory:
                        print("The candle light shows glowing symbols on the walls directing you down the passage.")
                        print("Following the passage leads you out of the mansion. You've escaped!")
                        self.player.has_escaped = True
                    else:
                        print("You have no candle to light.")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 3.")
                    break

    def ghost(self, room):
        if room == "library":
            print("A translucent figure in tattered robes, clutches an old book. His hollow eyes scan the shelves endlessly.")
            print("He was once a scholar who sought forbidden knowledge within the mansion’s ancient texts but became trapped in its curse.")
            print("Only those with wisdom may pass. Solve my riddle, and I shall aid you.")
            if self.player.intel >= 5:
                print("The mansion breathes, but its heart lies buried. Find the passage where the walls listen, and the rats lead the way.")
            else:
                print("Your intelligence is no match for the ghost. Some intelligence has been taken.")
                self.player.intel -= 1
        else:
            print("A shadowy female figure in a torn wedding dress, sobs into her hands.")
            print("She was once the mansion’s owner, betrayed and murdered on her wedding night. She lingers, searching for her lost engagement ring.")
            quest = input("I cannot leave without my ring... Will you find it for me? y or n ")
            if quest.lower() == "y":
                if "ring" in self.player.inventory:
                    self.player.hitpoints += 5
                    self.player.intel += 5
                    self.player.strength += 5
                    self.player.perc += 5
                    print("Thank you so much for finding it!")
                    print("All stats +5. Current stats are HP {hitpoints}, INT {intel}, STR {strength}, PERC {perc}".format(hitpoints = self.player.hitpoints, intel = self.player.intel, strength = self.player.strength, perc = self.player.perc))
                else:
                    print("She whispers... 'Try the attic...'")
            else:
                print("The ghost screams. HP has been lost.")
                self.player.hitpoints -= 20          

def start_game():
    ch_name = input("What is your character's name? ")
    player = Player(ch_name)
    player.play_approach()
    print(player.__repr__())
    
    room = Rooms("Entrance Hall", player)
    
    while not player.has_escaped and not player.is_ghost and not player.is_possessed:
        if room.current_room == "Entrance Hall":
            room.entrance_hall()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
        elif room.current_room == "Library":
            room.library()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
        elif room.current_room == "Dining Room":
            room.dining()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
        elif room.current_room == "Cellar":
            room.cellar()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
        
        elif room.current_room == "Master Bedroom":
            room.master_bedroom()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
        
        elif room.current_room == "Attic":
            room.attic()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
        
        elif room.current_room == "Secret Tunnel":
            room.secret_tunnel()
            
            if player.is_ghost or player.has_escaped or player.is_possessed:
                break
    
    end_game(player)

def end_game(player):
    if player.hitpoints == 0:
        print("You have died. Game over. You've lost! ")
    if player.has_escaped == True:
        print("You have escaped. Congratulations! You've won! ")
    if player.is_ghost == True:
        print("You've been trapped forever as a ghost in the mansion. Game over. You've lost! ")
    if player.is_possessed == True:
        print("You've been possessed by a ghost. Game over. You've lost. ")
        
    play_again = input("Would you like to play again? y or n ")
    if play_again.lower() == "y":
        start_game()
        
start = input("Would you like to play? y or n ")
if start.lower() == "y":
    start_game()
else:
    print("Thank you for playing!")