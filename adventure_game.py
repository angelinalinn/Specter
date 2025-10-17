#Specter (Text-Adventure game: Ghost Type Investigation) by Group ICT 
# updates:
# as of Tuesday, 17 September 2024, added anticheat feature to prevent abuse of front yard regen & improved formatting 

import random

# object classes
class Game:
    def __init__(self):
        # tracks running, used in while loop driver code
        self.running = True
        
        # delay ghost fights for a while after winning
        self.fightdelay = 0 
        self.anticheat = 0 # prevent player from abusing front yard's sanity regen

    def quit_specter(self):
        # quit game
        self.running = False

class Location:
    def __init__(self):
        #check if fingerprint has spawned
        self.fingerprint = False
    
    def update(self, location):
        # update location
        self.location = location
        print(f"You are now in the {currplace.location}.")

    def update_window(self): 
        # after fingerprint spawns, it stays
        self.fingerprint = True

class Player:
    def __init__(self):
        # add attribute
        self.name = ''
        self.sanity = 100
        # dmg reduction for each 15 sanity reduction
        self.dmg = random.randint(15,25) - int((100-self.sanity)/15)
        self.end = False


        # store player guess of ghost type for ending in endmenu()
        self.guess = '(none)'
    
    def askname(self):
        if self.name == '':
            self.name = input("\nPlease register your name: ").strip()
    
    def print_san(self):
        if self.sanity < 0:
            # prevents negative number for sanity
            self.sanity = 0

        print(f"\n{self.name}'s sanity: {self.sanity}/100.")

    def regen_san(self, x): 
        # heal sanity by +x points 
        self.sanity += x 

        # to keep sanity value within 100
        if self.sanity > 100:
            self.sanity = 100
    
    def player_stat(self): 
        #check if player is dead yet
        if self.sanity <= 0:
            # death msg
            print("\n...You have died.")
            self.print_san()

            
            
class Ghost: 
    def __init__(self, dmg):
        # dmg scaling for each 8 drop in player sanity
        self.dmg = dmg + int((100-player.sanity)/8)
        self.health = 90
    
    def print_hp(self):
        print(f"\nGhost HP: {self.health}/90.")

    def attack(self):
        player.sanity -= self.dmg 
        print(f"\nThe ghost has attacked you! (-{self.dmg} sanity points)")
        print(random.choice(("White noice pierces your ears. You stagger slightly before trying to collect yourself...",
                             "Your head throbs sharply. You try to shake the pain off...")))

        # regulates sanity symptoms & player status
        if player.sanity > 70: 
            print("Your flashlight flickers.")
            
        elif player.sanity <= 70 and player.sanity > 50: 
            print(random.choice(("You start to hear things that aren't there.",
                                 "You start to see things that aren't there.")))
            
        elif player.sanity <= 50 and player.sanity > 20:
            print(random.choice(("Relentless whispers cloud your mind...",
                                 "Your vision starts to blur..."
                                 "A hand rests on your shoulder. You refuse to look back.")))
            print("(Pro tip — use the Rosary to regain sanity.)")
        
        elif player.sanity < 20 and player.sanity > 0:
            print(random.choice(("Y o u  a r e  h a n g i n g  by  a  t h r e a d .",
                                 "The gh@ os t  s m i l e s at? y#ou!.")))
            print("(Friendly tip — use the Rosary to regain sanity.)")
        
        #death
        else:
            # returns death message, player status = False
            player.player_stat()

        
    def attacked(self):
        # player attacks ghost
        self.health -= player.dmg
        print(f"\nYou used holy water on the ghost! You did {player.dmg} damage.") 
        
        # print message according to ghost remaining hp
        if self.health > 0: 
            # if ghost still alive
            print("The ghost shrieks; it glares at you with deep resentment. The air thickens.")
        else:
            # if ghost is defeated
            print("The ghost lets out a long screech. You have successfully forced the ghost to dormancy!"
                  f"\nThe ghost's stat: 0 (dormant)")


#game
specter = Game()

# location system
currplace = Location()
indoor = ('hallway','living room','basement','dining room','kitchen','bedroom','bathroom') #also for ghostroom randomizer 
outdoor = 'front yard'

#initialize class object
player = Player()

#ghost type
polter = Ghost(10)
phantom = Ghost(12)
wendigo = Ghost(12)
egui = Ghost(10)

jumpscare = ("⠀⠀⠀⠀⠀⠀⠀⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌⡑⡕⡱⡸⠣⡀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑⠀⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⢠⠣⠐⠀ ⭕ ￼ ⠀⠀⢪⢺⣪⢣⠀⡀ ⭕.⠈⡈⠀⠀", 
             "⠀⠀⠀⠀⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊⠀⠀⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈⠀⠀⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁⠀⠀⠀⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀⠀⠀⠀⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈⠀⠀⠀⠀⠀⠀⠀⠀", 
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀")


# function for game start, process, end 
def startmenu():
    answ = input("\nWelcome to Specter."
                 "\n(Warning: This game contains jumpscares. Please proceed at your own discretion.)\n"
                 "\nWould you like to take up on a ghost investigation job? We will reward you handsomely."
                 "\n1) yes" 
                 "\n2) no"
                 "\n(1/2) - ")
    
    #input validation
    while answ != '1' and answ != '2':
        answ = input("\nPlease type 1 or 2. Would you like to take up on a ghost investigation job?"
                    "\n1) yes \n2) no \n(1/2) - ")

    if answ == '1':
        player.askname()

        print(f"\nWe're glad to have you, {player.name}.")
        answ = input("Would you like a short tutorial? \n1) yes \n2) no"
                     "\n(1/2) - ")
        
        while answ != '1' and answ != '2':
            answ = input("\nPlease type 1 or 2."
                         "\n(1/2) - ")
                     
        if answ == '1':
            input("""
You are a ghost investigator. 
                  
You have been tasked to a house that has reported ghost sightings.
                  
Goals: identify the ghost type, and survive.
                  
Every ghost type has 3 out of 4 common evidence: Freezing temperature, EMF 5, Spirit Box, and Fingerprint. 
To identify the ghost type, you should explore the house and find evidence by using the equipment in your bag. 
To find evidence, look for the ghost’s favorite room by using the EMF. If you find it, it will show EMF reading of 2.
Then, use your equipment in the ghost's favorite room. Read the Ghost Report for more information.
(Tip — some evidence may take several tries to get.)
                  
During your investigation, you may encounter the ghost once your sanity drops below a level threshold.
You must make the most out of holy items (Rosary, Crucifix, Holy Water) in your bag.
After collecting evidence, deduce the ghost type and write it down on the Ghost Report,
then return to the frontyard to end investigation.

Remember, keep your sanity above 0 to survive. (press 'enter' to end tutorial)""")

        input("\nWe will send you on your way shortly. Enjoy your trip. (press 'enter' to proceed)")
        
    else:
        print("That's a shame. Farewell, then.")
        quit()


def gameplay():
    # starts gameplay
    household = random.choice(('Smiths','Williams','Wang Family'))
    print("——————————————————————————————————")
    print(f"\nYou have arrived at the {household} house. (You have permanently equipped a flashlight.)")

    print("\nObjectives:"
          "\n1. Find the ghost's favorite room"
          "\n2. Collect evidence"
          "\n3. Write down ghost type in Ghost Report and return to the van\n"
          "\nPlease read the Ghost Report (in your bag) for more information on ghost types, equipment, "
          "available evidence, etc.\n")
    print("You step out of the van...\n")
    
    frontyard()


def endmenu():
    print("—————————————————")

    # if player alive
    if player.sanity > 0:
        print("Calculating results...")

        if player.guess == ghosttype_str:
            input(f"\nYour guess is correct: It's a {ghosttype_str}."
                  "\nYou've received a hefty sum of money!\n"
                  "\n(Good ending: Now, you're able to afford your living expenses and enjoy life. \n...For now.)\n"
                  "\n(press 'Enter' to proceed)")
        else:
            input(f"\nYour guess is incorrect: It's a {ghosttype_str}, not {player.guess}."
                  "\nYou feel disappointed... Better luck next time, I guess.\n"
                  "\n(Neutral ending: You're still alive, but... how will you pay your overdue bills now?)\n"
                  "\n(press 'Enter' to proceed)")
        
    else: #if player dead
        input("\n(You've received a bad ending: Death.)"
              "\n(press 'Enter' to proceed)")

    # restart or quit game
    answ = input("\nDo you want to start Specter again?"
                 "\n1) Yes."
                 "\n2) No."
                 "\n(1/2) - ")
    
    #input validation
    while answ not in ('1','2'):
        answ = input("\nPlease type 1 or 2. Start Specter?"
                 "\n1) Yes."
                 "\n2) No."
                 "\n(1/2) - ")
    
    # player restart
    if answ == '1':
        # reset settings to restart game
        player.sanity = 100
        player.guess = '(none)'
        specter.fightdelay = 0
        ghosttype.health = 90
        currplace.fingerprint = False
        player.end = False
        
        print("Restarting..."
              "\n——————————————————————————————————") #to add spacing before startmenu()

    # player quit
    else:
        print(f"\nThen farewell, {player.name}.")
        specter.quit_specter()


def ghost_fight(): # also know as ghost confrontation
    print("\nSuddenly, your flashlight flickers!\n")

    for x in (jumpscare):
        print(x)

    print("\nYou feel as if your heart would burst out of your chest."
          "\nThe ghost charges at you! But it's repelled by the Rosary you wear.\n"
          "\nThe ghost is angered. The air reeks of murderous intent.\n"
          "\n——————————————————")

    print("\nWarning: You are now in a confrontation with the ghost.\n"
          "\nObjective: Defeat the ghost. Don't die.\n"
          "\nHow to defeat the ghost:"
          "\n1. Repel the ghost's mental attacks with the crucifix (3 uses only)"
          "\n2. Force the ghost into dormancy by using holy water repeatedly"
          "\n3. Regain a bit sanity with the Rosary\n"
          "\n(Friendly tip — Before the ghost attacks, it may display certain behaviors.)")
    
    
    # limit crucifix use for every encounter
    crucifix_use = 3 

    # list item 
    items = ("Holy Water (attack)","Rosary (regain sanity)", "Crucifix (defend, limited)")

    # fight loop
    while ghosttype.health > 0 and player.sanity > 0:
        # print player & ghost stats
        print("———————————————————————")

        player.print_san()
        ghosttype.print_hp()

        # generate chance of ghost attacking player
        atkc = random.randint(1,3)

        # behavior before ghost attack or not atk
        if atkc == 1: 
            # ghost not attacking
            print(random.choice(("\nThe ghost looks at you warily.",
                                 "\nThe ghost is staring at you.")))   
        else:
            # ghost attacking
            print(random.choice(("\nThe ghost gave a distorted smile.",
                                 "\nThe ghost is glaring at you.",
                                 "\nThe ghost is staring at you.")))

        # player chooses action
        print("\nWhat will you do?")
        # prints list of items that can be used
        # numbering in listing
        n = 0 
        for x in (items):
            # skip listing crucifix as available option when reaches use limit
            if crucifix_use == 0 and x == 'Crucifix (defend, limited)':
                continue
            else: 
            # list player actions
                n += 1
                print(f"{n}) Use {x}")
        
        answ = input("- ")
        
        # input validation
        while answ not in ('1','2','3'):
            answ = input("\nInvalid. Please type a number from the options." 
                         "\n- ")
        
        # note: ghost attack function already tracks player status
        # player attack
        if answ == '1': 
            if atkc == 1: 
                # ghost no attack
                print("\nThe ghost is charging for its next attack...")
            else: 
                # ghost attack
                ghosttype.attack()
            
            # player attack
            ghosttype.attacked()

        # player regen san
        elif answ == '2':
            if atkc == 1: 
                # ghost no attack
                print("\nThe ghost is charging for its next attack...")
            else: 
                # ghost attack
                ghosttype.attack()
            
            use_rosary(7)

        # player defend
        elif answ == '3' and crucifix_use > 0:
            print("\nYou prepare the Crucifix while chanting prayers. You'll be immune to the next mental attack.")

            if atkc == 1: 
                # ghost no attack
                print("\nThe ghost didn't attack you; it's still looking at you warily. You put away the Crucifix. " 
                      f"({crucifix_use} use(s) left)")
            else:
                # ghost attack
                crucifix_use -= 1
                print(f"\nThe Crucifix has been used! You were shielded from the ghost's mental attack. ({crucifix_use} use(s) left)")
            
        else: 
            # if crucifix has no uses left 
            print("\nYou can't use the Crucifix. (0 use left)"
                  "\nToo bad, you missed your chance. You can only hope for the best.")

            if atkc == 1: 
                # ghost no attack
                print("\nThe ghost is charging for its next attack...")
            else: 
                # ghost attack
                ghosttype.attack()
    
    # when player wins against ghost
    
    if player.sanity > 0:
        print("\nYou win! You can now continue your investigation in peace... for now.")
        # delay ghost encounters for a while
        specter.fightdelay = 3 
        # allows player to better survive when moving around after a ghost fight
        player.regen_san(5) 
    else: 
        pass
    
    print("—————————————————")
        



        



# rooms in gameplay
def frontyard():
    print("—————————————————")
    currplace.update(outdoor)

    #scenery desc
    print("\nThe front yard is covered with tall grass, growing wildflowers here and there. The house lights are off.\n"
          "\nThe moon is bright tonight.\n")
    
    action_list()
    
    # location pathway
    answ = input("\nWhere do you want to go? \n1) Go inside the house \n2) Back to van"
                 "\n(1/2) - ")
    if answ == '1':
        print("\nYou walk for a while...")
        hallway()

    elif answ == '2':
        answ = input("\nAre you sure you want to end the investigation? "
                     "(You will not receive any money if your ghost-type identification is incorrect."
                     "\n1) Yes. \n2) I changed my mind."
                     "\n(1/2) - ")
        #input validation
        while answ not in ['1','2']:
            answ = input("\nPlease type 1 or 2. Are you sure you want to end the investigation?"
                         "\n(Remember to write down your ghost type guess on the Ghost Report in your bag.)"
                         "\n1) Yes. \n2) I changed my mind."
                         "\n(1/2) - ")
        if answ == '1':
            player.end = True
            # this will lead to endmenu()
        else: 
            # if player changed their mind 
            frontyard()

    else: 
        # input validation
        print("\nPlease type 1 or 2.")
        frontyard()

def hallway():
    print("—————————————————")
    # stops game if sanity reaches 0

    player.player_stat()

    currplace.update(indoor[0])
    
    # room desc
    print("""
The hallway stretches deep into the darkness, wooden floors and all. You shone your flashlight ahead of you.
Down the hallway leads to kitchen, further to the left connects to living room, and 
the stairs presumably leads down to the basement.
""")
    
    # hint that it's the ghost room, regardless of whether ghost has freezing temperature evidence
    if ghostroom == currplace.location:
        print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            # reminds player where they are 
            if player.sanity > 0:
                currplace.update(indoor[0])
    
    if player.sanity > 0:
        action_list()

        #if they answer 1) move, it will continue here
        answ = input("\nWhere do you want to go?"
                    "\n1) Living room" 
                    "\n2) Kitchen"
                    "\n3) Basement"
                    "\n4) Outside (Front yard)"
                    "\n(1/2/3/4) - ")
        # input validation
        while answ not in ('1','2','3','4'):
            answ = input("Please type 1, 2, 3, or 4."
                        "\n1) Living room" 
                        "\n2) Kitchen"
                        "\n3) Basement"
                        "\n4) Outside (Front yard)"
                        "\n(1/2/3/4) - ")
        # location pathway
        print("\nYou walk for a while...")
        if answ == '1': # living room
            player.sanity -=1
            if specter.fightdelay > 0:
                specter.fightdelay -= 1
            
            if specter.anticheat > 0:
                specter.anticheat -= 1
            
            living_room()

        elif answ == '2': # kitchen
            player.sanity -=1
            if specter.fightdelay > 0:
                specter.fightdelay -= 1
            if specter.anticheat > 0:
                specter.anticheat -= 1     

            kitchen()

        elif answ == '4': # front yard
            # regain sanity points by going outside the house
            if player.sanity < 100 and specter.anticheat == 0:
                player.regen_san(10)
                # prevents player from abusing heal when going to front yard
                specter.anticheat += 1
            
            frontyard()

        else: # basement
            player.sanity -=1
            if specter.fightdelay > 0:
                specter.fightdelay -= 1
            if specter.anticheat > 0:
                specter.anticheat -= 1
            
            basement()

def living_room():#Hendra
    print("—————————————————")
    # stops game if sanity reaches 0
    player.player_stat()

    currplace.update(indoor[1])

    # room desc
    print("""
Old sofas sat in the corner. Numerous family photos hung on the wall: some alone, some together.
Amongst the family members in the pictures, a white-haired child stood out.

You try to turn on the lights. It doesn't work. 
          
Well, you don't need to try to know the TV won't turn on, either.
          """)

    if ghostroom == currplace.location:
            print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            if player.sanity > 0:
                currplace.update(indoor[1])
    
    if player.sanity > 0:
        action_list()
        #if they answer 1) move, it will continue here
        answ = input("\nWhere do you want to go?"
                    "\n1) Dining room" 
                    "\n2) Hallway"
                    "\n(1/2) - ")
        
        while answ != '1' and answ != '2':
            answ = input("Please type 1 or 2."
                        "\n1) Dining room"
                        "\n2) Hallway"
                        "\n(1/2) - ")
        
        # reduce sanity when moving to other rooms
        player.sanity -=1
        if specter.fightdelay > 0:
            specter.fightdelay -= 1

        #location pathway
        print("\nYou walk for a while...")
        if answ == '1':
            dining_room()
        
        else:
            hallway()
        
def basement():#Hendra
    print("—————————————————")
    # stops game if sanity reaches 0
    player.player_stat()

    currplace.update(indoor[2])
    
    # room desc
    print("""
There's an old, yet clean, bicycle here. Other than a couple of dirty cardboard and bones, 
there's not really much to see.

You cough from the thick dust flying in the air.
          """)

    if ghostroom == currplace.location:
        print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            if player.sanity > 0:
                currplace.update(indoor[2])
    
    if player.sanity > 0:
        action_list()
        #if they answer 1) move, it will continue here
        answ = input("\nWhere do you want to go?"
                    "\n1) Hallway"
                    "\n(1) - ")
        
        #location pathway
        if answ == "1":
            player.sanity -=1
            if specter.fightdelay > 0:
                specter.fightdelay -= 1
            
            print("\nYou walk for a while...")
            hallway()
        else: 
            #input validation
            print("\nInvalid. Please type 1.")
            basement()

def dining_room():#jvn
    print("—————————————————")
    
    # stops game if sanity reaches 0
    player.player_stat()
    
    # update location
    currplace.update(indoor[3])
    
    # room desc
    print("""
A dining table is set in the center of the room along with 4 chairs. The tablecloth seems to be in bad condition. 
There are also broken shards and rotten food scraps all over the table, and even the floor; 
the stench is truly unbearable. You wonder why they're still there.
         """)

    if ghostroom == currplace.location:
        print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            if player.sanity > 0:
                currplace.update(indoor[3])
    
    if player.sanity > 0:
        action_list()
        #if they answer 1) move, it will continue here
        answ = input("\nWhere do you want to go?"
                    "\n1) Kitchen"
                    "\n2) Living room"
                    "\n(1/2) - ")
        
        while answ != '1' and answ != '2':
            answ = input("\nPlease type 1 or 2."
                        "\n1) Kitchen"
                        "\n2) Living room"
                        "\n(1/2) - ")
        
        player.sanity -=1
        if specter.fightdelay > 0:
            specter.fightdelay -= 1
        
        #location pathway
        print("\nYou walk for a while...")
        if answ == '1':
            kitchen()
        else:
            living_room()

def kitchen():#jvn
    print("—————————————————")

    # stops game if sanity reaches 0
    player.player_stat()

    currplace.update(indoor[4])
    
    # room desc
    print("""
The kitchen is like what you'd expect: a stove, a sink, and a fridge——albeit broken beyond repair.

Something glinted in the light. You peer inside the sink... A stained fork lay quietly. Seems like rust.

Cabinets line along the top walls, and some are broken open. There's a trail leading to the bathroom.

What a mess.""")

    if ghostroom == currplace.location:
        print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            if player.sanity > 0:
                currplace.update(indoor[4])

    if player.sanity > 0:
        action_list()
        #if they answer 1) move, it will continue here
        answ = input("\nWhere do you want to go?"
                    "\n1) Hallway"
                    "\n2) Dining room"
                    "\n3) Bathroom"
                    "\n4) Bedroom"
                    "\n(1/2/3/4) - ")

        while answ != '1' and answ != '2' and answ != '3' and answ != '4':
            answ = input("\nPlease type 1, 2, 3, or 4."
                        "\n1) Hallway"
                        "\n2) Dining room"
                        "\n3) Bathroom"
                        "\n4) Bedroom"
                        "\n(1/2/3/4) - ")
        
        player.sanity -=1
        if specter.fightdelay > 0:
                specter.fightdelay -= 1
        
        #location pathway
        print("\nYou walk for a while...")

        if answ == '1':
            hallway()
        elif answ == '2':
            dining_room()
        elif answ == '3':
            bathroom()
        else:
            bedroom()

def bedroom(): #lesha
    print("—————————————————")
    # stops game if sanity reaches 0
    player.player_stat()

    currplace.update(indoor[5])

    # room desc
    print("""
It's a large bedroom with tall ceilings. Dust hangs in the air, swirling in the faint light.
It appears to be an ordinary master bedroom——if not rather rich in taste——but something feels off.
          
Dominating the room was the presence of what would have been an extravagant bed 
if it were not for the faded, moth-eaten curtains and thick layers of dust.
On a shelf lining the far wall, sat rows upon rows of porcelain dolls. 

Perhaps they would've been looked pretty if they had a head. How unfortunate.

Nevertheless, you can't shake the feeling you are being watched.
          """)
    
    if ghostroom == currplace.location:
        print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            if player.sanity > 0:
                currplace.update(indoor[5])

    if player.sanity > 0:
        action_list()

        # player move rooms
        answ = input("\nWhere do you want to go?"
                    "\n1) Bathroom"
                    "\n2) Kitchen"
                    "\n(1/2) - ")
        
        while answ not in ('1','2'):
            answ = input("Please type 1 or 2."
                        "\n1) Bathroom"
                        "\n2) Kitchen"
                        "\n(1/2) - ")
        
        player.sanity -=1
        if specter.fightdelay > 0:
                specter.fightdelay -= 1
        
        #location pathway
        print("\nYou walk for a while...")

        if answ == '1':
            bathroom()
        else:
            kitchen()

def bathroom():
    print("—————————————————")
    currplace.update(indoor[6])
    
    # room desc
    print("""
Dim light broke through a small window near the bathroom ceiling. You tread around the broken tiles. 
The sink is rusted, the shower curtain is torn, and a foul, metallic odor lingers in the air. 

It smells familiar.

You looked away from the bathtub.
          """)
    
    if ghostroom == currplace.location:
            print("It feels rather chilly...\n")

    # generate chance of ghost confrontation
    if player.sanity < 85 and specter.fightdelay == 0:
        fightc = random.randint(1,2)
        if fightc == 1:
            ghost_fight()
            
            if player.sanity > 0:
                currplace.update(indoor[6])
    
    if player.sanity > 0:
        action_list()
        
        answ = input("\nWhere do you want to go?"
                    "\n1) Bedroom"
                    "\n2) Kitchen"
                    "\n(1/2) - ")
        
        while answ != '1' and answ != '2':
            answ = input("Please type 1 or 2."
                        "\n1) Bedroom"
                        "\n2) Kitchen"
                        "\n(1/2) - ")
        
        # reduce sanity when moving to other rooms
        player.sanity -=1
        if specter.fightdelay > 0:
            specter.fightdelay -= 1

        #location pathway
        print("\nYou walk for a while...")

        if answ == '1':
            bedroom()
        
        else:
            kitchen()


#functions for collecting evidence
def action_list():

    answ = input("\nWhat will you do next?"
                 "\n1) Move place"
                 "\n2) Check sanity"
                 "\n3) Check bag"
                 "\n4) Check the window(s)"
                 "\n(1/2/3/4) - ")

    # check sanity
    if answ == '2':
        player.print_san()
        action_list()

    # check bag/inventory
    elif answ == '3':
        print("\nYou opened your bag. There are a bunch of things and equipment inside.")

        answ = input("\nWhich one do you want to check?" 
                     "\n1) EMF Reader"
                     "\n2) Spirit Box"
                     "\n3) Thermometer"
                     "\n4) Ghost Report"
                     "\n5) Crucifix"
                     "\n6) Holy Water"
                     "\n7) Never mind"
                     "\n(1/2/3/4/5/6/7) - ")
        
        #input validation
        while answ not in ['1','2','3','4','5','6','7']:
            answ = input("\nPlease type 1, 2, 3, 4, 5, 6, or 7."
                         "\n1) EMF Reader"
                         "\n2) Spirit Box"
                         "\n3) Thermometer"
                         "\n4) Ghost Report"
                         "\n5) Crucifix"
                         "\n6) Holy Water"
                         "\n7) Never mind"
                         "\n(1/2/3/4/5/6/7) - ")
        
        # player uses equipment
        if answ == '1':
            use_emf()
        elif answ == '2':
            use_sb()
        elif answ == '3':
            use_thermo()
        elif answ == '4':
            read_journal()
        elif answ == '5':
            print("""
You inspect the Crucifix.
                  
A useful shield against ghost attacks. The metal cross does not have the figure of Holy Son, 
and yet it still emits a holy aura under the moonlight. It reminds you of the Rosary you wear.
                  
The priest told you to use it wisely.
                  
You place the Crucifix back in the bag.
                  """)
        elif answ == '6':
            print("""
You inspect the Holy Water container.
                  
You open the lid and peer inside. It's a little smaller than your palm, but it seems almost... bottomless.

You place the Holy Water back in the bag.
                  """)

        # after action or choosing 7, player is given action list
        action_list()
    
    # check window
    elif answ == '4':
        if currplace.location in indoor:
            check_window()
            action_list()
            
        else:
            # if player is outside
            print("\nYou look inside the house through the window. "
                  "The lights are turned off; nobody's home.")
            action_list()
    
    # move to other places
    elif answ == '1':
        print("\nYou start to walk...")
        # sanity reduction happens in if condition for location pathways, current room function
        # every room function includes 'if' pathway for moving to other rooms connected to it
    
    #input validation 
    else: 
        print("\nPlease type 1, 2, 3, or 4.")
        action_list()


def read_journal():
    # cover page
    input(f"""
    GHOST REPORT 
        written by the SPECTER Association
          
    Investigator: {player.name}
        
    (press 'Enter' to see next page)""")

    input("""
    ————————————————————————————————
    GENERAL GUIDE ON GHOST INVESTIGATION:
    
    The location an investigator is tasked with should be haunted by a ghost. Now, an investigator's job 
    is to identify the ghost type haunting the area and report back to the SPECTER Association.
    The ghost may be a wendigo, poltergeist, phantom, or egui. To be able to identify the type, 
    one must find three evidence in the ghost's favorite room. 
    Common evidence you should look out for are freezing temperatures, EMF 5, Spirit Box, and fingerprints.
    
    The ghost's favorite room is the room where it died. One can find it by using the EMF Reader; 
    if it shows EMF 2, the room has been found. Ghosts have a very strong attachment to the place
    where they died, so they cannot leave the immediate vicinity. One should take advantage of this, 
    as ghosts cannot harm someone outside the building. 
          
    Keep in mind that, once one steps into the building, one's sanity value will drop with every action made, 
    due to the ghost's influence. It's important to keep track of one's sanity value with the Watch provided. 
    As the value drops below a certain threshold, a human will become easier prey for supernatural creatures.
    Once a human's sanity drops to 0, they are on the point of no return. It is good practice to step outside
    once in a while to recover some sanity.
    
    When investigating, one may encounter the ghost. Do not let it drive you insane. Use the Rosary, Crucifix, 
    and Holy Water to defend yourself and force the ghost into dormancy. After a ghost has been forced to be dormant, 
    it may take some time to recover before attempting to kill again.
    
    After you have deduced the ghost type, write it down in the Ghost Report, then go outside and return to the van.
          
    (press 'Enter' to see next page)""")

    # page 2
    input("""
    ————————————————————————————————
    ITEMS & EQUIPMENT:
          
    Flashlight (auto-equipped)
    - A standard tool to illuminate dark areas.
    
    Sanity Watch (auto-equipped)
    — A special watch provided by the SPECTER Association to track your sanity in a number value.

    Ghost Journal
    - Use this to view information on ghost types and write down your guess.

    Thermometer
    - Check a room's temperature immediately to see if the ghost has freezing temperature evidence 
      in its favorite room.

    EMF Reader (1-5)
    * It provides a value from 1 to 5.
    — EMF 1: No energy detected.
    - EMF 2: You found the ghost's favorite room.
    — EMF 3-4: The ghost is growing active.
    - EMF 5: The ghost has EMF 5 evidence.

    Spirit Box
    - Use this in the ghost room to try to communicate with the ghost to check if the ghost responds. 
      If it does, the ghost has the Spirit Box evidence.

    Rosary Necklace
    - A sacred necklace that can regenerate a bit of your sanity during ghost encounters.

    Crucifix
    - Provides defense during a ghost encounter, shielding you from harm. It is limited to 3 uses for 
      each ghost encounter.
            
    Holy Water
        — Use this to subdue the ghost during ghost encounters. 
                
    (press 'Enter' to see next page)""")
    
    # page 3
    input("""
    ————————————————————————————————
    GUIDE ON HOW TO COLLECT EVIDENCE:
    
    To determine the ghost type, one must find the ghost's favorite room. Then, search for evidence in there.
    However, some evidence may take SOME TRIES to appear.
        1. Freezing Temperature
           Equipment: Thermometer
           Result: very cold temperatures (negative)
          
        2. EMF 5
           Equipment: EMF Reader
           Result: EMF reading of 5
        
        3. Spirit Box
           Equipment: Spirit Box
           Result: the ghost gives a response, such as "Hello"
          
        4. Fingerprint
           Equipment: None
           Result: fingerprint trace after checking the window 
       
    (press 'Enter' to see next page)""")

    # page 4
    input("""
    ————————————————————————————————
    Ghost Types:
            
    1. Poltergeist
        Description: Poltergeists are a 'loud ghost.' They are very active and often manipulates objects 
                     in its enviroment.
        Evidence: EMF 5 ✅, Spirit Box ✅, Fingerprint ✅
            
    2. Phantom
        Description: Phantoms are said to constantly lurk in the shadows, looking for prey. 
                     Its attacks drain more sanity than typical ghosts.
        Evidence: Freezing Temperature ✅, EMF 5 ✅, Fingerprint ✅
        
    3. Wendigo
        Description: The Wendigo is an evil spirit, originating in First Nations folklore in North America. 
                     It's described as a very violent ghost that likes to possess people and drive them to insanity,
                     eventually turning them into cannibals.
        Evidence: Freezing Temperature ✅, Spirit Box ✅, Fingerprint ✅
            
    4. Egui
        Description: Egui (餓鬼) is literally translated to 'hungry ghost.' 
                     They are believed to be spirits of people who committed sins out of greed when they were alive, 
                     thus condemned to suffer insatiable hunger after death.
        Evidence: Freezing Temperature ✅, EMF 5 ✅, Spirit Box ✅
        
    (press 'Enter' to see next page)""")
    
    # page 5
    # write down ghost type guess
    print("————————————————————————————————")
    player.guess = input("\nEnter your guess of the ghost type. (poltergeist/phantom/wendigo/egui)"
                         "\n(press 'enter' to skip)"
                         "\n- ").lower().strip()
        
    #input validation
    while player.guess not in ('poltergeist','phantom','egui','wendigo',''):
        player.guess = input("\nPlease type the name correctly. (poltergeist/phantom/wendigo/egui)"
                             "\n- ").lower().strip()
    
    print("Saved.")

def use_thermo():
    player.sanity -= 1
    
    print("\n—————————————————")
    print("You used the thermometer.")
    if ghostroom == currplace.location: 
        if ghosttype in (phantom,wendigo,egui):
            print(f"Thermometer reading: -{random.randrange(1,5)}°C")
        else:
            print(f"Thermometer reading: {random.randrange(1,5)}°C")
    else:
        print(f"Thermometer reading: {random.randrange(20,30)}°C"
              "\n(Pro tip — Use the Thermometer in the ghost's favorite room.)")
    print("—————————————————")

def use_emf():
    player.sanity -= 1
    
    print("\n—————————————————")
    print("You used the EMF Reader.")
    if ghostroom == currplace.location:
        level = random.choice((2,2,2,2,2,2,3,4))
        print(f"EMF reading: {level}")
        
        # chance of EMF 5 spawn
        if ghosttype in (phantom, polter, egui):
            emfc = random.randint(1,20) 
            if emfc <= 5: # 5/20 chance of emf 5
                print("Suddenly, it beeps louder and louder."
                    "\nEMF reading: 5")
    
    else:
        print("EMF reading: 1")
    print("—————————————————")

def use_sb(): #sb = spirit box
    player.sanity -= 1
    
    print("\n—————————————————")
    print("You used the Spirit Box...")
    ghostresponse = random.choice(["Hello", "Hi", "Help", "Get out", "Behind you", "Die", "Kill"])
    
    if currplace.location in indoor:
        #restricting spirit box's valid use in ghost room only
        if ghostroom == currplace.location: 
            #determine chance of ghost willing to communicate 
            sbc = random.randint(1,20) 
            if ghosttype in (wendigo,egui):
                if sbc <= 4:  #4/20 chance of ghost willing to communicate
                    print(f"Spirit Box: '{ghostresponse}'")
                else: 
                    print("...No response.")

            elif ghosttype == polter:
                if sbc <= 6:  #6/20 chance of ghost willing to communicate
                    print(f"Spirit Box: '{ghostresponse}'")
                else:
                    print("...No response.")
            else:
                print("...No response.")
        else: 
            print("No response."
                "\n(Pro tip — Use the Spirit Box in the ghost's favorite room.)")
    
    else: #when player uses equipment outside house
        print("No response. (Friendly tip — Obviously. Go in the house first.)")
    
    print("—————————————————")    

def use_rosary(x):
    print("\nThe rosary shimmers under the dim moonlight. You used the Rosary, holding it close to your heart...")
    player.regen_san(x)

    print(f"Your mind feels a little clearer. (+{x} sanity points)")
    
def check_window():
    player.sanity -= 1
    
    print("\n—————————————————")
    print("You check the window(s)...")

    scenery = random.choice(("...The moon shines bright in the dark sky.",
                             "...The wild flowers sway slightly in the wind.",
                             "...The trees sway slightly in the wind.", 
                             "It stares at you. You blink... Nothing's there.",
                             "...You heard a knock. Nothing's there...",
                             "...Nothing to see."))
    
    if ghostroom == currplace.location: 
        #check if fingerprint has spawned before
        if currplace.fingerprint == False: 
        #determine chance fingerprint spawns
            fpc = random.randint(1,20) 
            if ghosttype in (wendigo,phantom):
                if fpc <= 4:  #4/20 chance of fingerprint spawn
                    print("...There are traces of a fingerprint!")
                    
                    # update fingerprint spawn
                    currplace.update_window()
                else: 
                    print(scenery)

            elif ghosttype == polter:
                if fpc <= 5:  #5/20 chance of fingerprint spawn
                    print("...There are traces of a fingerprint!")
                    
                    # update fingerprint spawn
                    currplace.update_window()
                else:
                    print(scenery)

            else:
                print(scenery) # if ghost type no fingerprint evidence.
        else: 
            # if fingerprint = True (already spawned)
            print("There are still traces of a fingerprint.")
    else:
        print(scenery,
              "\n(Pro tip — Try checking in the ghost's favorite room.)")
    
    print("—————————————————")






# driver code
while specter.running == True:
    #randomization setup 
    ghostroom = random.choice(indoor)
    ghosttype = random.choice((polter,phantom,wendigo,egui))

    # turn ghosttype identity into string
    if ghosttype == polter:
        ghosttype_str = 'poltergeist'
    elif ghosttype == phantom:
        ghosttype_str = 'phantom'
    elif ghosttype == wendigo:
        ghosttype_str = 'wendigo'
    else: 
        ghosttype_str = 'egui'

    # start game
    startmenu()
    while player.sanity > 0 and player.end == False:
        gameplay()
    endmenu()
    # test if it really runs back to start menu()
