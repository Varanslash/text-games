# --- System ---

# Imports modules

import random
import time

# Universal Commands

def help():
    print("move [cardinal direction]\ntake [item]\ntalk [npc]\nleave\ninspect [thing]\nmap")

def heal():
    global playerhp
    playerhp += random.choice(range(1, 10)) * playerlevel
    if playerhp > 50 + (constitution * playerlevel):
        playerhp = 50 + (constitution * playerlevel)
    print("Player HP:", playerhp)
        
def map():
    if bank == "forest1":
        print("""        [11]{12}[13]
    [8 ][9 ][10][14]
{7 ][5 ][4 ][3 ]
    [6 ][1 ][2 ]""")

    elif bank == "graveyard1":
        print("""                [11][12}
                [9 ]    
            [6 ][4 ]    
        [7 ][3 ][1 }    
{15][14][8 ][5 ][2 ]
        [13][17][10]
        [16]""")

    elif bank == "village2":
        print("""   [4 ]                [3 ]
{###############
    [2 ]    ####Trail[1]########
                            ####
                            ####""")

    elif bank == "dungeon1":
        print("""[14][13][12]
[15]    [11][10]
            [1 }
[5 ][4 ][3 ][2 ]
[6 ]    [7 ]
[16]    [8 ][9 ]
[17]
[18]""")

    elif bank == "dungeon2":
        print("""   [2 ][1 ]
[8 ]    [3 ][4 ][ 5]
[9 ][10][11]    [6 ][7 ]
[12]    [13]
    [14][15][16][17]
    [19]        [18]""")
                            
def stat():
    print("STR:", strength)
    print("DEX:", dexterity)
    print("CON:", constitution)
    print("INT:", intelligence)
    print("WIS:", wisdom)
    print("CHA:", charisma)
    print("HP:", playerhp)
    print("Weapon:", weapon)
    print("Level:", playerlevel)
    print("Gold:", playergold)
    print("EXP:", playerexp)
    
# Setting Variables

bank = "village1"
staff = 0
weapon = "fists"
first_weapon = 0
playerlevel = 1
enemylevel = 1
enemyhp = enemylevel * 20
playerexp = 0
playergold = 50
swordupgrade = 1
bowupgrade = 1
fistupgrade = 1
staffupgrade = 1
bosslevel = playerlevel
strength = random.choice(range(3, 21))
dexterity = random.choice(range(3, 21))
constitution = random.choice(range(3, 21))
intelligence = random.choice(range(3, 21))
wisdom = random.choice(range(3, 21))
charisma = random.choice(range(3, 21))
playerhp = 50 + (constitution * playerlevel)
boss1flag = True

# Enemies
            
def generic_boss():
    global enemyhp
    global playerhp
    global turn
    print("Enemy:", enemyhp)
    time.sleep(1)
    miss = random.choice(range(1, 11))
    if miss == 10:
        print("Miss!")
        turn = 1
    else:
        enemypower = random.choice(range(5, 11)) * enemylevel
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        
def player_attack():
    global enemyhp
    global playerhp
    global turn
    print("Player:", playerhp)
    userinput = input("Choice?>")
    if userinput == "help":
        print("List of commands:\nfight\nrun\nheal")
    elif userinput == "fight":
        weapon_values()
        enemyhp -= playerpower
        print(playerpower, "damage dealt!")
    elif userinput == "heal":
        heal()
    elif userinput == "run":
        print("You ran away.")
        time.sleep(1)
    else:
        print("Invalid Action!")
    turn = 2
    if playerhp < 1:
        print("You lost!")
        exit()
        
def encounter():
    global enemylevel
    global turn
    global enemyhp
    global playerpower
    global monster
    global playerexp
    global playerlevel
    global playergold
    monsterencounter = random.choice(range(1, 11))
    if monsterencounter == 10:
        turn = 1
        print(monster, "attacks!")
        enemyhp = 40 * enemylevel
        while not (enemyhp < 1):
            while turn == 1:
                userinput = input("Choice?>")
                if userinput == "help":
                    print("List of commands:\nfight\nrun\nheal")
                elif userinput == "fight":
                    weapon_values()
                    enemyhp -= playerpower
                    print("Player did:", playerpower, "damage dealt!")
                elif userinput == "heal":
                    heal()
                elif userinput == "run":
                    print("You ran away.")
                    time.sleep(1)
                    return
                turn = 2
                break
            while turn == 2:
                generic_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if enemyhp < 1:
                print("You won!")
                playerexp += enemylevel * 10
                print("You have", playerexp, "EXP!")
                playergold += enemylevel * random.choice(range(1, 20))
                print("You have", playergold, "gold!")
                leveling()
                break
            elif playerhp < 1:
                print("You lost...")
                exit()
                
def leveling():
    global playerexp
    global playerlevel
    if playerexp > 50 and playerlevel < 2:
        playerlevel = 2
        print("You reached level", playerlevel, "!")
    elif playerexp > 150 and playerlevel < 3:
        playerlevel = 3
        print("You reached level", playerlevel, "!")
    elif playerexp > 350 and playerlevel < 4:
        playerlevel = 4
        print("You reached level", playerlevel, "!")
    elif playerexp > 600 and playerlevel < 5:
        playerlevel = 5
        print("You reached level", playerlevel, "!")
    elif playerexp > 800 and playerlevel < 6:
        playerlevel = 6
        print("You reached level", playerlevel, "!")
    elif playerexp > 1100 and playerlevel < 7:
        playerlevel = 7
        print("You reached level", playerlevel, "!")
    elif playerexp > 1400 and playerlevel < 8:
        playerlevel = 8
        print("You reached level", playerlevel, "!")
    elif playerexp > 1800 and playerlevel < 9:
        playerlevel = 9
        print("You reached level", playerlevel, "!")
    elif playerexp > 2500 and playerlevel < 10:
        playerlevel = 10
        print("You reached level", playerlevel, "!")
    elif playerexp > 3000 and playerlevel < 11:
        playerlevel = 11
        print("You reached level", playerlevel, "!")
    elif playerexp > 3600 and playerlevel < 12:
        playerlevel = 12
        print("You reached level", playerlevel, "!")
    elif playerexp > 5000 and playerlevel < 13:
        playerlevel = 13
        print("You reached level", playerlevel, "!")
    elif playerexp > 6100 and playerlevel < 14:
        playerlevel = 14
        print("You reached level", playerlevel, "!")
    elif playerexp > 7200 and playerlevel < 15:
        playerlevel = 15
        print("You reached level", playerlevel, "!")
    elif playerexp > 8500 and playerlevel < 16:
        playerlevel = 16
        print("You reached level", playerlevel, "!")
    elif playerexp > 10000 and playerlevel < 17:
        playerlevel = 17
        print("You reached level", playerlevel, "!")
    elif playerexp > 12500 and playerlevel < 18:
        playerlevel = 18
        print("You reached level", playerlevel, "!")
    elif playerexp > 17500 and playerlevel < 19:
        playerlevel = 19
        print("You reached level", playerlevel, "!")
    elif playerexp > 20000 and playerlevel < 20:
        playerlevel = 20
        print("You reached level", playerlevel, "!")
    elif playerexp > 25000 and playerlevel < 21:
        playerlevel = 21
        print("You reached level", playerlevel, "!")
        
def enemyscale():
    global enemylevel
    global playerlevel
    enemylevel = round(playerlevel / 2)

def taro_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    global boss1flag
    monsterencounter = 1
    if monsterencounter == 1:
        turn = 1
        print(boss, "attacks!")
        bosshp = 80 * bosslevel
        while not (bosshp < 1):
            while turn == 1:
                userinput = input("Choice?>")
                if userinput == "help":
                    print("List of commands:\nfight\nrun\nheal")
                elif userinput == "fight":
                    weapon_values()
                    bosshp -= playerpower
                    print("Player dealt", playerpower, "damage!")
                elif userinput == "heal":
                    heal()
                elif userinput == "run":
                    print("You can't escape!")
                turn = 2
                break
            while turn == 2:
                taro_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 200
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                leveling()
                boss1flag = 1
                break
            elif playerhp < 1:
                print("You lost...")
                exit()
                
def taro_boss():
    global bosshp
    global playerhp
    global turn
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10:
        print("Miss!")
        turn = 1
    else:
        enemypower = (2 * bosslevel) + (random.choice(range(1, 10))) + (fistupgrade * 11) + round(strength / 15)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        
def sword_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    monsterencounter = random.choice(range(1))
    if monsterencounter == 1:
        turn = 1
        print(boss, "attacks!")
        bosshp = 60 * bosslevel
        while not (bosshp < 1):
            while turn == 1:
                userinput = input("Choice?>")
                if userinput == "help":
                    print("List of commands:\nfight\nrun\nheal")
                elif userinput == "fight":
                    weapon_values()
                    bosshp -= playerpower
                    print("Player dealt", playerpower, "damage!")
                elif userinput == "heal":
                    heal()
                elif userinput == "run":
                    print("You can't escape!")
                turn = 2
                break
            while turn == 2:
                sword_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 270
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                leveling()
                break
            elif playerhp < 1:
                print("You lost...")
                exit()
                
def sword_boss():
    global bosshp
    global playerhp
    global turn
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10:
        print("Miss!")
        turn = 1
    else:
        enemypower = (bosslevel * 4) + (random.choice(range(1, 20)) / 2) + (swordupgrade * 5) + round(strength / 7)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        
def bow_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    monsterencounter = random.choice(range(1))
    if monsterencounter == 1:
        turn = 1
        print(boss, "attacks!")
        bosshp = 60 * bosslevel
        while not (bosshp < 1):
            while turn == 1:
                userinput = input("Choice?>")
                if userinput == "help":
                    print("List of commands:\nfight\nrun\nheal")
                elif userinput == "fight":
                    weapon_values()
                    bosshp -= playerpower
                    print("Player dealt", playerpower, "damage!")
                elif userinput == "heal":
                    heal()
                elif userinput == "run":
                    print("You can't escape!")
                turn = 2
                break
            while turn == 2:
                bow_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 220
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                leveling()
                break
            elif playerhp < 1:
                print("You lost...")
                exit()
                
def bow_boss():
    global bosshp
    global playerhp
    global turn
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10:
        print("Miss!")
        turn = 1
    else:
        enemypower = (bosslevel + (random.choice(range(1, 10)))) * 1.5 + (bowupgrade * 3) + round(dexterity / 5)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        
def mindflower_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    global boss2flag
    monsterencounter = random.choice(range(1))
    if boss2flag == True:
        turn = 1
        print(boss, "attacks!")
        bosshp = 60 * bosslevel
        while not (bosshp < 1):
            while turn == 1:
                userinput = input("Choice?>")
                if userinput == "help":
                    print("List of commands:\nfight\nrun\nheal")
                elif userinput == "fight":
                    weapon_values()
                    bosshp -= playerpower
                    print("Player dealt", playerpower, "damage!")
                elif userinput == "heal":
                    heal()
                elif userinput == "run":
                    print("You can't escape!")
                turn = 2
                break
            while turn == 2:
                mindflower_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 300
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                boss2flag = False
                leveling()
                break
            elif playerhp < 1:
                print("You lost...")
                exit()
                
def mindflower_boss():
    global bosshp
    global playerhp
    global turn
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10:
        print("Miss!")
        turn = 1
    else:
        enemypower = (bosslevel * 5) + ((bosslevel * staffupgrade) / 2) + round((intelligence + wisdom) / 15)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
	    
# Weapons

def weapon_values():
    global weapon
    global playerpower
    global fistupgrade
    global swordupgrade
    global bowupgrade
    global staffupgrade
    global strength
    global dexterity
    global intelligence
    global wisdom
    if weapon == "fists":
        playerpower = (2 * playerlevel) + (random.choice(range(1, 10))) + (fistupgrade * 13) + round(strength / 10)
    elif weapon == "sword":
        playerpower = (playerlevel * 4) + (random.choice(range(1, 20)) / 2) + (swordupgrade * 5) + round(strength / 7)
    elif weapon == "bow":
        playerpower = (playerlevel + (random.choice(range(1, 10)))) * 1.5 + (bowupgrade * 3) + round(dexterity / 5)
    elif weapon == "staff":
        playerpower = (playerlevel * 5) + ((playerlevel * staffupgrade) / 2) + round((intelligence + wisdom) / 15)
    playerpower = round(playerpower)

# --- Main Game ---

print("MYSTERIOUS PERSON: Hello there, adventurer.")
time.sleep(1)
print("MYSTERIOUS PERSON: The White Shrine has long since withered away.")
time.sleep(1)
print("MYSTERIOUS PERSON: And we start to feel the effects now.")
time.sleep(1)
print("MYSTERIOUS PERSON: The witch Kildren has awakened once again.")
time.sleep(1)
print("MYSTERIOUS PERSON: I will send you out to kill her.")
time.sleep(1)
print("MYSTERIOUS PERSON: Good luck, adventurer.")
time.sleep(1)
print("(Type 'help' to get started!)")
time.sleep(1)
while True:
    
    # Village 1
    
    if bank == "village1":
        enemyscale()
        print("\nWest = Weapons Shop\nEast = May's Cottage\nNorth = Forest\nWhat do you do?")
        userinput = input("Village> ")
        if userinput == "move west":
            print("You step into the small shop. On the walls, there are staves and blades galore. You admire the shininess of the weapons.")
            time.sleep(1)
            if first_weapon == 0:
                print("Shopkeeper: Hey! Welcome to my shop! You wanna buy some weapons?")
                time.sleep(1)
                print("Shopkeeper: Actually, because you're new, I'll give you a weapon for free!")
                time.sleep(1)
                print("Shopkeeper: I have a bow, a sword, and a staff. What would you like?")
            while True:
                userinput = input("Weapons Shop> ")
                if first_weapon == 0:
                    if userinput == "bow":
                        print("You remind me of someone I met who lived in a place called District 12.")
                        weapon = "bow"
                    elif userinput == "sword":
                        print("Shopkeeper: I see you're a slasher, eh?")
                        weapon = "sword"
                    elif userinput == "staff":
                        print("Shopkeeper: A magic user? Those are rare around here! Haha!")
                        staff = 1
                    elif userinput == "leave":
                        print("Shopkeeper: Goodbye!")
                        break
                    else:
                        print("Shopkeeper: I don't have that weapon!")
                    first_weapon = 1
                else:
                    if userinput == "leave":
                        print("Shopkeeper: Goodbye!")
                        break
                    elif userinput == "talk Shopkeeper":
                        print("Shopkeeper: Well, hello there!")
                    else:
                        print("Invalid command!")
        elif userinput == "move east":
            while True:
                print("Oh? A Visitor! Come in, come in!")
                time.sleep(1)
                print("There are two people in the room. One is a girl named May. The other is her husband Thomas. They seem to be very cheerful and happy. What do you do?")
                userinput = input("May's Cottage> ")
                if userinput == "talk May":
                    print("May: Well, hello there! Yes, I'm very happy with my husband.")
                    time.sleep(1)
                    print("May: Oh? The forest? Oh, I advise you don't go there. Many an adventurer have gone, and none have returned.")
                elif userinput == "talk Thomas":
                    print("Thomas: Hey man. How ya doin?")
                    time.sleep(1)
                    print("Thomas: Listen to my wife, kid.")
                elif userinput == "leave":
                    print("You leave the cottage.")
                    break
        elif userinput == "move north":
            print("You exit the town, and push forward further. You wonder what awaits you...")
            bank = "forest1"
            forestcell = 1
        elif userinput == "help":
            help()
        else:
            print("Invalid Command!")
            
    # Forest 1
    
    elif bank == "forest1":
        enemylevel = round(playerlevel * 0.75)
        if forestcell == 1:
            print("Forest. Cell 1. East, West, North, South")
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            userinput = input("Forest> ")
            encounter()
            if userinput == "move east":
                forestcell = 2
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "move south":
                bank = "village1"
            elif userinput == "move north":
                forestcell = 4
            elif userinput == "move west":
                forestcell = 6
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
            
        # Cell 3    
            
        elif forestcell == 3:
            print("Forest. Cell 3. North, South, West.")
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            userinput = input("Forest>")
            if userinput == "move north":
                forestcell = 10
            elif userinput == "move west":
                forestcell = 4
            elif userinput == "move south":
                forestcell = 2
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                    
        # Cell 4            
                    
        elif forestcell == 4:
            print("Forest. Cell 4. North, South, East, West.")
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            userinput = input("Forest>")
            if userinput == "move north":
                forestcell = 9
            elif userinput == "move east":
                forestcell = 3
            elif userinput == "move west":
                forestcell = 5
            elif userinput == "move south":
                forestcell = 1
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                    
        # Cell 2            
                    
        elif forestcell == 2:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 2. West, North.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 1
            elif userinput == "move north":
                forestcell = 3
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 5
        
        elif forestcell == 5:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 5. East, South, West, North.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 7
            elif userinput == "move north":
                forestcell = 8
            elif userinput == "move east":
                forestcell = 4
            elif userinput == "move south":
                forestcell = 6
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 6
        
        elif forestcell == 6:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 8. East, North.")
            userinput = input("Forest>")
            if userinput == "move north":
                forestcell = 5
            elif userinput == "move east":
                forestcell = 1
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 7
                
        elif forestcell == 7:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 7. East, West.")
            userinput = input("Forest>")
            if userinput == "move west":
                gravecell = 1
                bank = "graveyard1"
            elif userinput == "move east":
                forestcell = 5
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 8
                
        elif forestcell == 8:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 8. East, South.")
            userinput = input("Forest>")
            if userinput == "move east":
                forestcell = 9
            elif userinput == "move south":
                forestcell = 5
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 9
                
        elif forestcell == 9:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 9. East, South, West, North.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 10
            elif userinput == "move north":
                forestcell = 11
            elif userinput == "move east":
                forestcell = 8
            elif userinput == "move south":
                forestcell = 4
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 10
                
        elif forestcell == 10:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 10. East, South, West, North.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 9
            elif userinput == "move north":
                forestcell = 12
            elif userinput == "move east":
                forestcell = 14
            elif userinput == "move south":
                forestcell = 3
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 11
                
        elif forestcell == 11:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 11. East, South.")
            userinput = input("Forest>")
            if userinput == "move east":
                forestcell = 12
            elif userinput == "move south":
                forestcell = 9
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 12
                
        elif forestcell == 12:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 12. East, South, West, North. An old house sits in front of you, north.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 11
            elif userinput == "move north":
                forestcell = 15
            elif userinput == "move east":
                forestcell = 13
            elif userinput == "move south":
                forestcell = 10
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 13
                
        elif forestcell == 13:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 13. South, West.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 12
            elif userinput == "move south":
                forestcell = 14
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 14
                
        elif forestcell == 14:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 14. West, North.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 10
            elif userinput == "move north":
                forestcell = 13
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        elif forestcell == 15:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 15. There is an entrance in the ground. East, South.")
            userinput = input("Forest>")
            if userinput == "move east":
                forestcell = 10
            elif userinput == "move south":
                forestcell = 12
            elif userinput == "enter":
                bank = "dungeon2"
                dungeon2cell = 1
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
    # Graveyard 1
    
    elif bank == "graveyard1":
        enemylevel = round(playerlevel * 0.75)
        if gravecell == 1:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 1. East, South, West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 3
            elif userinput == "move north":
                gravecell = 4
            elif userinput == "move east":
                bank = "forest1"
                forestcell = 7
            elif userinput == "move south":
                gravecell = 2
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 2
                
        elif gravecell == 2:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 2. South, West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 5
            elif userinput == "move north":
                gravecell = 1
            elif userinput == "move south":
                gravecell = 10
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 3
                
        elif gravecell == 3:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 3. East, South, West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 7
            elif userinput == "move north":
                gravecell = 6
            elif userinput == "move east":
                gravecell = 1
            elif userinput == "move south":
                gravecell = 5
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 4
                
        elif gravecell == 4:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 4. South, West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 6
            elif userinput == "move north":
                gravecell = 9
            elif userinput == "move south":
                gravecell = 1
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 5
                
        elif gravecell == 5:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 5. South, West, North, East. A tombstone lies in the ground.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 8
            elif userinput == "move north":
                gravecell = 3
            elif userinput == "move south":
                gravecell = 17
            elif userinput == "move east":
                gravecell = 2
            elif userinput == "inspect tombstone":
                print("Goodbye Celeste. I will miss you.")
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 6
                
        elif gravecell == 6:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 6. South, East.")
            userinput = input("Graveyard>")
            if userinput == "move south":
                gravecell = 3
            elif userinput == "move east":
                gravecell = 4
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 7
                
        elif gravecell == 7:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 7. South, East.")
            userinput = input("Graveyard>")
            if userinput == "move south":
                gravecell = 8
            elif userinput == "move east":
                gravecell = 3
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
        # Cell 8
                
        elif gravecell == 8:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 8. South, North, West, East.")
            userinput = input("Graveyard>")
            if userinput == "move south":
                gravecell = 13
            elif userinput == "move east":
                gravecell = 5
            elif userinput == "move north":
                gravecell = 7
            elif userinput == "move west":
                gravecell = 14
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
            # Cell 9
                
        elif gravecell == 9:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 9. South, North. A cross sits nearly buried in the ground.")
            userinput = input("Graveyard>")
            if userinput == "move south":
                gravecell = 4
            elif userinput == "move north":
                gravecell = 11
            elif userinput == "inspect cross":
                print("WORSHIP JESUS")
                for _ in range(10):
                    heal()
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
            # Cell 9
                
        elif gravecell == 10:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 9. West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 17
            elif userinput == "move north":
                gravecell = 2
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
                # Cell 11
                
        elif gravecell == 11:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 11. East, South. A tombstone sits in the ground.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                gravecell = 12
            elif userinput == "move south":
                gravecell = 9
            elif userinput == "inspect tombstone":
                print("REST IN PEACE COLTON\nYOU LIVED A GREAT LIFE")
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")

        # Cell 12
                
        elif gravecell == 12:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 12. West, South, East.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                gravecell = 11
            elif userinput == "move east":
                village2cell = 1
                bank = "village2"
            elif userinput == "help":
                help()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")

        # Cell 13
                
        elif gravecell == 13:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 13. North, East, South.")
            userinput = input("Graveyard>")
            if userinput == "move north":
                gravecell = 8
            elif userinput == "move east":
                gravecell = 17
            elif userinput == "move south":
                gravecell = 16
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")

        # Cell 14
                
        elif gravecell == 14:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 14. East, West.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                gravecell = 8
            elif userinput == "move west":
                gravecell = 15
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")

        # Cell 15
                
        elif gravecell == 15:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 15. East, West. A tombstone lies in the ground.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                gravecell = 14
            elif userinput == "move west":
                bank = "forest2"
                print("End of demo.")
                exit()
            elif userinput == "inspect tombstone":
                print("There is no tunnel to Atlantis.")
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")

        # Cell 16
                
        elif gravecell == 16:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 16. North.")
            userinput = input("Graveyard>")
            if userinput == "move north":
                gravecell = 13
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")

        # Cell 17
                
        elif gravecell == 17:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 17. North, West, East.")
            userinput = input("Graveyard>")
            if userinput == "move north":
                gravecell = 5
            elif userinput == "move west":
                gravecell = 13
            elif userinput == "move east":
                gravecell = 10
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command1!")
                
    # Village 2
                
    elif bank == "village2":
        enemylevel = round(playerlevel * 0.75)
        if village2cell == 1:
            print("Welcome to Roark Town! Cell 1 (Trail). South, North, Northwest, Southwest, West.")
            userinput = input("Roark Town>")
            if userinput == "move north":
                village2cell = 3
            elif userinput == "move southwest":
                gravecell = 12
                bank = "graveyard1"
            elif userinput == "move south":
                village2cell = 2
            elif userinput == "move northwest":
                village2cell = 4
            elif userinput == "move west":
                bank = "dungeon1"
                dungeon1cell = 1
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
        
        elif village2cell == 2:
            print("Accessories Shop. Here, you can buy improvements to your weapons. The 'shopkeeper' sits at his desk.")
            userinput = input("Accessories Shop>")
            if userinput == "leave":
                village2cell = 1
            elif userinput == "talk shopkeeper":
                print("Shopkeeper: Oh, hey man! How are you doing?")
                time.sleep(1)
                print("Shopkeeper: Oh? You want to buy an accessory?")
                time.sleep(1)
                print("Shopkeeper: Sure!")
                if weapon == "fists":
                    print("Shopkeeper: For your fists, I have a magic ring. I think this could work to increase your attack power. For only 100 gold!")
                elif weapon == "sword":
                    print("Shopkeeper: For your sword, I have a rock to sharpen it. I think this could work to slice those monsters, eh? For only 120 gold!")
                elif weapon == "bow":
                    print("Shopkeeper: For your bow, I have silver arrows. I think this could work to increase your range. For only 175 gold!")
                elif weapon == "staff":
                    print("Shopkeeper: For your staff, I have ancient elf magic. I think this could work to make your spells more powerful. For only 500 gold!")
                print("Shopkeeper: Would you like to buy?")
                print("Buy?\nyes\nno")
                while True:
                    userinput = input("Choice?>")
                    if userinput == "yes":
                        if weapon == "fists":
                            if gold < 100:
                                print("You don't have enough money! Come back a little richer!")
                            else:
                                print("There we go! A nice accessory!")
                                fistupgrade = 1
                                gold -= 100
                        elif weapon == "sword":
                            if gold < 120:
                                print("You don't have enough money! Come back a little richer!")
                            else:
                                print("There we go! A nice accessory!")
                                swordupgrade = 1
                                gold -= 120
                        elif weapon == "bow":
                            if gold < 175:
                                print("You don't have enough money! Come back a little richer!")
                            else:
                                print("There we go! A nice accessory!")
                                bowupgrade = 1
                                gold -= 175
                        elif weapon == "staff":
                            if gold < 500:
                                print("You don't have enough money! Come back a little richer!")
                            else:
                                print("There we go! A nice accessory!")
                                staffupgrade = 1
                                gold -= 500
                    else:
                        print("Well, until next time then!")
                        break
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
        
        elif village2cell == 3:
            print("Tommy's cottage. He sits in his chair.")
            userinput = input("Tom's Cottage>")
            if userinput == "leave":
                village2cell = 1
            elif userinput == "talk tommy":
                print("Oh hey man! Yea, I'm doin good.")
                time.sleep(1)
                print("You should go check out the weapons shop.")
                time.sleep(1)
                print("They have good stuff.")
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
        
        elif village2cell == 4:
            print("Anna's cottage. She's in the kitchen, cleaning.")
            userinput = input("Anna's Cottage>")
            if userinput == "leave":
                village2cell = 1
            elif userinput == "talk anna":
                print("Hi there!")
                time.sleep(1)
                print("I'm busy cleaning my kitchen.")
            elif userinput == "help":
                help()
            elif userinput == "stats":
                stat()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            else:
                print("Invalid Command!")
                
    # Dungeon 1
    
    elif bank == "dungeon1":
        enemylevel = round(playerlevel * 0.75)
        bosslevel = playerlevel
        if dungeon1cell == 1:
            print("Taro's Dungeon. Cell 1. East, North, South")
            monster = random.choice(["Bear", "Knight"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                bank = "village2"
                village2cell = 1
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "move south":
                dungeon1cell = 2
            elif userinput == "move north":
                dungeon1cell = 10
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
                
        # --- Cell 2 ---
            
        elif dungeon1cell == 2:
            print("Taro's Dungeon. Cell 2. North, West.")
            monster = random.choice(["Goblin", "Wolf"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon1cell = 1
            elif userinput == "move west":
                dungeon1cell = 3
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 3 ---
        
        elif dungeon1cell == 3:
            print("Taro's Dungeon. Cell 3. West, South, East.")
            monster = random.choice(["Skeleton", "Bat"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move west":
                dungeon1cell = 4
            elif userinput == "move south":
                dungeon1cell = 7
            elif userinput == "move east":
                dungeon1cell = 2
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 4 ---
        
        elif dungeon1cell == 4:
            print("Taro's Dungeon. Cell 4. East, West.")
            monster = random.choice(["Slime", "Spider"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon1cell = 3
            elif userinput == "move west":
                dungeon1cell = 5
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 5 ---
        
        elif dungeon1cell == 5:
            print("Taro's Dungeon. Cell 5. South, East.")
            monster = random.choice(["Orc", "Bat"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 6
            elif userinput == "move east":
                dungeon1cell = 4
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 6 ---
        
        elif dungeon1cell == 6:
            print("Taro's Dungeon. Cell 6. South, North.")
            monster = random.choice(["Goblin", "Slime"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon1cell = 5
            elif userinput == "move south":
                dungeon1cell = 16
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 7 ---
        
        elif dungeon1cell == 7:
            print("Taro's Dungeon. Cell 7. South, North.")
            monster = random.choice(["Wolf", "Bat"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 8
            elif userinput == "move north":
                dungeon1cell = 3
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 8 ---
        
        elif dungeon1cell == 8:
            print("Taro's Dungeon. Cell 8. East, North.")
            monster = random.choice(["Slime", "Skeleton"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon1cell = 9
            elif userinput == "move north":
                dungeon1cell = 7
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 9 ---
        
        elif dungeon1cell == 9:
            print("Taro's Dungeon. Cell 9. West.")
            monster = random.choice(["Orc", "Bat"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move west":
                dungeon1cell = 8
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 10 ---
        
        elif dungeon1cell == 10:
            print("Taro's Dungeon. Cell 10. South, West.")
            monster = random.choice(["Knight", "Skeleton"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 1
            elif userinput == "move west":
                dungeon1cell = 11
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 11 ---
        
        elif dungeon1cell == 11:
            print("Taro's Dungeon. Cell 11. West, North.")
            monster = random.choice(["Goblin", "Spider"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon1cell = 10
            elif userinput == "move north":
                dungeon1cell = 12
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 12 ---
        
        elif dungeon1cell == 12:
            print("Taro's Dungeon. Cell 12. South, West.")
            monster = random.choice(["Slime", "Orc"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 11
            elif userinput == "move west":
                dungeon1cell = 13
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 13 ---
        
        elif dungeon1cell == 13:
            print("Taro's Dungeon. Cell 13. East, West.")
            monster = random.choice(["Knight", "Orc"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon1cell = 12
            elif userinput == "move west":
                dungeon1cell = 14
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 14 ---
        
        elif dungeon1cell == 14:
            print("Taro's Dungeon. Cell 14. East, South.")
            monster = random.choice(["Spider", "Skeleton"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon1cell = 13
            elif userinput == "move south":
                dungeon1cell = 15
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 15 ---
        
        elif dungeon1cell == 15:
            print("Taro's Dungeon. Cell 15. North.")
            monster = random.choice(["Orc", "Wolf"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon1cell = 14
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 16 ---
        
        elif dungeon1cell == 16:
            print("Taro's Dungeon. Cell 16. South, North.")
            monster = random.choice(["Slime", "Knight"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 17
            elif userinput == "move north":
                dungeon1cell = 6
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 17 ---
        
        elif dungeon1cell == 17:
            print("Taro's Dungeon. Cell 17. South, North.")
            monster = random.choice(["Spider", "Bat"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 18
            elif userinput == "move north":
                dungeon1cell = 16
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 18 ---
        
        elif dungeon1cell == 18:
            print("Taro's Dungeon. Cell 18. North.")
            boss = "Taro"
            userinput = input("Taro's Dungeon> ")
            encounter()
            if boss1flag == 1:
                print("You feel a mysterious prescence in the room.")
                time.sleep(1)
                print("A shadow looms in the corner.")
                time.sleep(1)
                print("You hear footsteps approach.")
                time.sleep(1)
                print("A draconic shape approaches...")
                time.sleep(2)
                print("It's Taro, the Blue Dragon!")
                time.sleep(0.5)
                print("Taro attacks!")
                taro_boss_encounter()
            else:
                if userinput == "move north":
                    dungeon1cell = 17
                elif userinput == "heal":
                    heal()
                elif userinput == "help":
                    help()
                elif userinput == "map":
                    map()
                elif userinput == "wait":
                    print("You waited.")
                    encounter()
                elif userinput == "stats":
                    stat()
                else:
                    print("Invalid Command!")

    # Dungeon 2

    elif bank == "dungeon2":
        enemylevel = round(playerlevel * 0.75)
        bosslevel = playerlevel
        if dungeon2cell == 1:
            print("Mindflower's Dungeon. Cell 1. You can leave the dungeon here. West, South.")
            monster = random.choice(["Bear", "Knight"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "leave":
                bank = "forest1"
                forestcell = 15
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "move south":
                dungeon2cell = 3
            elif userinput == "move west":
                dungeon2cell = 2
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
                
            # --- Cell 2 ---
        elif dungeon2cell == 2:
            print("Mindflower's Dungeon. Cell 2. East.")
            monster = random.choice(["Knight", "Shadow"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon2cell = 1
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 3 ---
        elif dungeon2cell == 3:
            print("Mindflower's Dungeon. Cell 3. North, East, South.")
            monster = random.choice(["Slime", "Spider"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 1
            elif userinput == "move east":
                dungeon2cell = 4
            elif userinput == "move south":
                dungeon2cell = 11
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 4 ---
        elif dungeon2cell == 4:
            print("Mindflower's Dungeon. Cell 4. East, West.")
            monster = random.choice(["Knight", "Bandit"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon2cell = 5
            elif userinput == "move west":
                dungeon2cell = 3
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 5 ---
        elif dungeon2cell == 5:
            print("Mindflower's Dungeon. Cell 5. West, South.")
            monster = random.choice(["Imp", "Knight"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move west":
                dungeon2cell = 4
            elif userinput == "move south":
                dungeon2cell = 6
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 6 ---
        elif dungeon2cell == 6:
            print("Mindflower's Dungeon. Cell 6. North, East.")
            monster = random.choice(["Shadow", "Wisp"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 5
            elif userinput == "move east":
                dungeon2cell = 7
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 7 ---
        elif dungeon2cell == 7:
            print("Mindflower's Dungeon. Cell 7. West.")
            monster = random.choice(["Imp", "Knight"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move west":
                dungeon2cell = 6
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 8 ---
        elif dungeon2cell == 8:
            print("Mindflower's Dungeon. Cell 8. South.")
            monster = random.choice(["Spider", "Shade"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon2cell = 9
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 9 ---
        elif dungeon2cell == 9:
            print("Mindflower's Dungeon. Cell 9. North, South, East.")
            monster = random.choice(["Spider", "Slime"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 8
            elif userinput == "move east":
                dungeon2cell = 10
            elif userinput == "move south":
                dungeon2cell = 12
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 10 ---
        elif dungeon2cell == 10:
            print("Mindflower's Dungeon. Cell 10. East, West.")
            monster = random.choice(["Knight", "Slime"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon2cell = 11
            elif userinput == "move west":
                dungeon2cell = 9
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 11 ---
        elif dungeon2cell == 11:
            print("Mindflower's Dungeon. Cell 11. North, South, West.")
            monster = random.choice(["Knight", "Specter"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 3
            elif userinput == "move south":
                dungeon2cell = 13
            elif userinput == "move west":
                dungeon2cell = 10
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 12 ---
        elif dungeon2cell == 12:
            print("Mindflower's Dungeon. Cell 12. North.")
            monster = random.choice(["Ghost", "Wraith"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 9
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 13 ---
        elif dungeon2cell == 13:
            print("Mindflower's Dungeon. Cell 13. North, South.")
            monster = random.choice(["Ghost", "Shade"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 11
            elif userinput == "move south":
                dungeon2cell = 15
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 14 ---
        elif dungeon2cell == 14:
            print("Mindflower's Dungeon. Cell 14. South, East.")
            monster = random.choice(["Shade", "Slime"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon2cell = 19
            elif userinput == "move east":
                dungeon2cell = 15
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 15 ---
        elif dungeon2cell == 15:
            print("Mindflower's Dungeon. Cell 15. North, East, West.")
            monster = random.choice(["Wisp", "Specter"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 13
            elif userinput == "move east":
                dungeon2cell = 16
            elif userinput == "move west":
                dungeon2cell = 14
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 16 ---
        elif dungeon2cell == 16:
            print("Mindflower's Dungeon. Cell 16. East, West.")
            monster = random.choice(["Specter", "Wisp"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon2cell = 17
            elif userinput == "move west":
                dungeon2cell = 15
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 17 ---
        elif dungeon2cell == 17:
            print("Mindflower's Dungeon. Cell 17. West, South.")
            monster = random.choice(["Shade", "Imp"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move west":
                dungeon2cell = 16
            elif userinput == "move south":
                dungeon2cell = 18
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
    
        # --- Cell 18 (Boss Room) ---
        elif dungeon2cell == 18:
            print("Mindflower's Dungeon. Cell 18. North.")
            boss = "Mindflower"
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if boss2flag == True:
                print("You feel psychic pressure building in the air...")
                time.sleep(1)
                print("A whisper echoes through your mind.")
                time.sleep(1)
                print("A jellyfish-like shape floats about in the darkness.")
                print("The Mindflower awakens!")
                mindflower_boss_encounter()
            else:
                if userinput == "move north":
                    dungeon2cell = 17
                elif userinput == "heal":
                    heal()
                elif userinput == "help":
                    help()
                elif userinput == "map":
                    map()
                elif userinput == "wait":
                    print("You waited.")
                    encounter()
                elif userinput == "stats":
                    stat()
                else:
                    print("Invalid Command!")
    
        # --- Cell 19 ---
        elif dungeon2cell == 19:
            print("Mindflower's Dungeon. Cell 19. North.")
            monster = random.choice(["Ghost", "Shade"])
            userinput = input("Mindflower's Dungeon> ")
            encounter()
            if userinput == "move north":
                dungeon2cell = 14
            elif userinput == "heal":
                heal()
            elif userinput == "help":
                help()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            else:
                print("Invalid Command!")
                