# --- System ---

# Imports modules

import random
import time
import json

# Universal Commands

def help():
    print("move [cardinal direction]\ntake [item]\ntalk [npc]\nleave\ninspect [thing]\nmap\nenter\nopen chest\nswitch spell")

def heal():
    global playerhp
    playerhp += random.choice(range(1, 10)) * playerlevel
    if playerhp > 50 + ((constitution * playerlevel) * 2):
        playerhp = 50 + ((constitution * playerlevel) * 2)
    print("Player HP:", playerhp)
        
def map():
    if bank == "forest1":
        print("""            [15}
        [11][12][13]
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
        print("""    [2 ][1 ]
[8 ]    [3 ][4 ][ 5]
[9 ][10][11]    [6 ][7 ]
[12]    [13]
    [14][15][16][17]
    [19]        [18]""")
    
    elif bank == "peatbogs":
        print("""    [9 ][10][11]
        [8 ][12][13]
    [17][7 ][14]
    [3 ][5 ][15][16]
[1 ][2 ]    [18]
    [6 ][4 ]
        [19][20]
            [21][22]
                [23][24][25]""")
    
    elif bank == "dungeon3":
        print("""                [1 ]
        [2 ][3 ][4 ][5 ][6 ]
            [7 ]    [8 ]
[9 ][10][11][12]    [13][14]
[15]    [16]        [17]
[18]    [19][20]    [21][22][23]
            [24]            [25]""")

    elif bank == "avernus":
        print("""            [19][11]
    [13][14][15][16][17][18]
[1 ][2 ][3 ][4 ]    [5 ][6 ]
    [7 ][8 ][9 ]        [10][20]
    [12]""")

    elif bank == "dungeon4":
        print("""        [4 ]
[1 ][2 ][3 ][6 ][7 ][8 ][11][12][13][14]
        [5 ]        [9 ][10]    [15][16]
                                    [17]""")

    elif bank == "highlands":
        print(""""    [24][23]
        [21][22]
[15][16][17][18][19][20]
[13][14]        [9 ][10][11][12]
            [6 ][7 ][8 ]
            [4 ][5 ]
            [3 ]
            [2 ][1 ]""")
        
    elif bank == "cursedmarsh":
        print("""            [1 ]
        [2 ][3 ][4 ][5 ]
    [6 ][7 ][8 ][9 ][10][11][12]
[13][14][15][16][17][18]    [19]
        [20][21]
            [22]""")
        
    elif bank == "village3":
        print("""        [12]
    [11][10][9 ]
[13][8 ][7 ][6 ]
[14][4 ][3 ][2 ][1 ]
            [5 ]""")
        
    elif bank == "graveyard2":
        print("""    [14][15][16]
        [11][12][13]
[7 ][8 ][9 ][10]
[4 ][5 ][6 ]
[1 ][2 ][3 ]""")
        
    elif bank == "dungeon5":
        print("""            [25]
    [20][21][22][23][24]
    [17]    [18]    [19]
[1 ][2 ][3 ][4 ][5 ][6 ][7 ]
    [8 ]    [9 ]    [10]
    [11][12][15][14][13]
            [16]""")

def stat():
    print("+--- STATS ---+")
    print("STR:", strength)
    print("DEX:", dexterity)
    print("CON:", constitution)
    print("INT:", intelligence)
    print("WIS:", wisdom)
    print("CHA:", charisma)
    print()
    print("HP:", playerhp)
    print("Weapon:", weapon)
    print("Level:", playerlevel)
    print("Gold:", playergold)
    print("EXP:", playerexp)
    print("Class:", playerclass)
    print()
    print("Spell slots open:\nStall:", spellslot1, "\nFire Bolt:", spellslot2, "\nFull Heal:", spellslot3, "\nDisintegration:", spellslot4, "\nMagic Missile:", spellslot5, "\nEntrance:", spellslot6, "\nIce Beam:", spellslot7, "\nAttract:", spellslot8, "\nLightning Bolt:", spellslot9, "\nTimestop:", spellslot10, "\n--- WIZARD SPELLS ---", "\nThunder:", spellslot11, "\nGambler:", spellslot12, "\nNecromancy:", spellslot13, "\nTorrent:", spellslot14, "\nChroma:", spellslot15, "\n--- DRUID SPELLS ---", "\nNecromancy:", spellslot16, "\nHeal of the wild:", spellslot17, "\nAncientpower:", spellslot18) # type: ignore
    print()
    print("Current spell slot:", currentspellslot)

def switch_spell():
    global userinput
    global currentspellslot
    global currentowspellslot
    print("What battlespell slot would you like to use? (1 - 15)")
    try:
        userinput = int(input("Slot?"))
        currentspellslot = userinput
        print("Current Spell Slot:", currentspellslot)
    except ValueError:
        print("Invalid Spell!")

# Variables

import random

game = {
    # Setting Variables
    "bank": "village1",
    "staff": 0,
    "weapon": "fists",
    "first_weapon": 0,
    "playerlevel": 1,
    "enemylevel": 1,
    "enemyhp": 1,
    "playerexp": 0,
    "playergold": 50,
    "swordupgrade": 1,
    "bowupgrade": 1,
    "fistupgrade": 1,
    "staffupgrade": 1,
    "bosslevel": 1,
    "strength": random.choice(range(3, 21)),
    "dexterity": random.choice(range(3, 21)),
    "constitution": random.choice(range(3, 21)),
    "intelligence": random.choice(range(3, 21)),
    "wisdom": random.choice(range(3, 21)),
    "charisma": random.choice(range(3, 21)),
    "playerhp": 50,
    "stallcountdown": 0,
    "bosshp": 1,
    "enemyhp": 1,
    "forcedencounter": 0,

    # Setting Boss Variables
    "boss1flag": True,
    "boss2flag": True,
    "boss3flag": True,
    "boss4flag": True,
    "boss5flag": True,
    "boss6flag": True,
    "boss7flag": True,
    "boss8flag": True,
    "boss9flag": True,
    "boss10flag": True,
    "boss11flag": True,
    "boss12flag": True,
    "boss13flag": True,
    "boss14flag": True,
    "boss15flag": True,
    "boss16flag": True,
    "boss17flag": True,
    "boss18flag": True,

    "lolthflag": True,
    "odiaflag": True,
    "belphegorflag": True,
    "luciferflag": True,
    "vecnaflag": True,
    "tarrasqueflag": True,
    "tarragonflag": True,
    "kildrenflag": True,
    "trumpetflag": True,
    "theyorkgoblincleaver": True,

    "tarostrength": random.choice(range(10, 15)),
    "tarodexterity": random.choice(range(10, 15)),
    "taroconstitution": random.choice(range(10, 15)),
    "tarointelligence": random.choice(range(10, 15)),
    "tarowisdom": random.choice(range(10, 15)),
    "tarocharisma": random.choice(range(10, 15)),

    "mindflowerstrength": random.choice(range(5, 11)),
    "mindflowerdexterity": random.choice(range(10, 15)),
    "mindflowerconstitution": random.choice(range(10, 15)),
    "mindflowerintelligence": random.choice(range(12, 15)),
    "mindflowerwisdom": random.choice(range(12, 15)),
    "mindflowercharisma": random.choice(range(12, 15)),

    "draculastrength": random.choice(range(10, 17)),
    "draculadexterity": random.choice(range(10, 15)),
    "draculaconstitution": random.choice(range(10, 15)),
    "draculaintelligence": random.choice(range(12, 15)),
    "draculawisdom": random.choice(range(12, 15)),
    "draculacharisma": random.choice(range(17, 20)),

    "sebekstrength": random.choice(range(15, 20)),
    "sebekdexterity": random.choice(range(10, 15)),
    "sebekconstitution": random.choice(range(10, 15)),
    "sebekintelligence": random.choice(range(12, 17)),
    "sebekwisdom": random.choice(range(12, 15)),
    "sebekcharisma": random.choice(range(1, 5)),

    # Major Bosses
    "lolthstrength": random.choice(range(15, 17)),
    "lolthdexterity": random.choice(range(15, 20)),
    "lolthconstitution": random.choice(range(15, 18)),
    "lolthintelligence": random.choice(range(15, 20)),
    "lolthwisdom": random.choice(range(15, 17)),
    "lolthcharisma": random.choice(range(15, 20)),

    # Setting Chest/Item Flags
    "chest1flag": True,
    "chest2flag": True,
    "chest3flag": True,
    "chest4flag": True,
    "chest5flag": True,

    # Setting Puzzle Flags
    "puzzle1flag": True,
    "puzzle2flag": True,
    "puzzle3flag": True,
    "puzzle4flag": True,
    "puzzle5flag": True,
    "puzzle6flag": True,
    "puzzle7flag": True,
    "puzzle8flag": True,
    "puzzle9flag": True,
    "puzzle10flag": True,

    # Setting Spellslots
    "spellslot1": False,
    "spellslot2": False,
    "spellslot3": False,
    "spellslot4": False,
    "spellslot5": False,
    "spellslot6": False,
    "spellslot7": False,
    "spellslot8": False,
    "spellslot9": False,
    "spellslot10": False,
    "spellslot11": False,
    "spellslot12": False,
    "spellslot13": False,
    "spellslot14": False,
    "spellslot15": False,
    "spellslot16": False,
    "spellslot17": False,
    "spellslot18": False,
    "spellslot19": False,
    "spellslot20": False,
    "spellslot21": False,
    "spellslot22": False,
    "spellslot23": False,
    "spellslot24": False,
    "spellslot25": False,
    "spellslot26": False,
    "spellslot27": False,
    "spellslot28": False,
    "spellslot29": False,
    "spellslot30": False,
    "spellslot31": False,
    "spellslot32": False,
    "spellslot33": False,
    "spellslot34": False,
    "spellslot35": False,

    "currentspellslot": 1,
    "playerparalyze": 0,

    # Seals
    "seal1": True,
    "seal2": True,
    "seal3": True,
    "seal4": True,
    "seal5": True,
    "seal6": True,
    "seal7": True,

    # Quest Flags

    "quest1": 1,
    "quest2": 1,
    "quest3": 1,
    "quest4": 1,
    "quest5": 1,
    "quest6": 1,
    "quest7": 1,
    "quest8": 1,
    "quest9": 1,
    "quest10": 1,
    "quest11": 1,
    "quest12": 1,
    "quest13": 1,
    "quest14": 1,
    "quest15": 1,
    "quest16": 1,
    "quest17": 1,
    "quest18": 1,
    "quest19": 1,
    "quest20": 1,
    "quest21": 1,

    # Cell Setting
    "forestcell": 1,
    "gravecell": 1,
    "dungeon1cell": 1,
    "dungeon2cell": 1,
    "dungeon3cell": 1,
    "dungeon4cell": 1,
    "village2cell": 1,
    "peatbogscell": 1,
    "marshcell": 1,
    "mountaincell": 1,
    "avernuscell": 1,
    "village3cell": 1,
    "dungeon5cell": 1,

    # Misc.
    "classflag": True,
    "introflag": True,
    "playerclass": "placeholder"
}

for key, value in game.items():
    globals()[key] = value

# Enemies
            
def generic_boss():
    global enemyhp
    global playerhp
    global turn
    global stallcountdown
    print("Enemy:", enemyhp)
    time.sleep(1)
    miss = random.choice(range(1, 11))
    if miss == 10 or stallcountdown > 0:
        print("Miss!")
        turn = 1
        stallcountdown -= 1
    else:
        enemypower = random.choice(range(5, 11)) * enemylevel
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        stallcountdown -= 1
        
def encounter():
    global enemylevel
    global turn
    global enemyhp
    global playerpower
    global monster
    global playerexp
    global playerlevel
    global playergold
    global forcedencounter
    global enemystrength
    global enemydexterity
    global enemyconstitution
    global enemyintelligence
    global enemywisdom
    global enemycharisma
    global playerparalyze
    global revivalflag
    monsterencounter = random.choice(range(1, 11))
    if monsterencounter == 10 or forcedencounter == 1:
        enemystrength = random.choice(range(10, 15))
        enemydexterity = random.choice(range(10, 15))
        enemyconstitution = random.choice(range(10, 15))
        enemyintelligence = random.choice(range(10, 15))
        enemywisdom = random.choice(range(10, 15))
        enemycharisma = random.choice(range(10, 15))
        turn = 1
        print(monster, "attacks!")
        enemyhp = 40 + (enemylevel * enemyconstitution)
        while not (enemyhp < 1):
            while turn == 1:
                if playerparalyze < 1:
                    userinput = input("Choice?>")
                    if userinput == "help":
                        print("List of commands:\nfight\nrun\nheal\ncast spell\nswitch spell")
                        turn = 1
                    elif userinput == "fight":
                        weapon_values()
                        enemyhp -= playerpower
                        print("Player did:", playerpower, "damage dealt!")
                        turn = 2
                    elif userinput == "heal":
                        heal()
                        turn = 2
                    elif userinput == "run":
                        print("You ran away.")
                        time.sleep(1)
                        return
                    elif userinput == "cast spell":
                        spells()
                        turn = 2
                    elif userinput == "switch spell":
                        switch_spell()
                        turn = 1
                    break
                else:
                    playerparalyze -= 1
                    print("Player is paralyzed!")
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
                forcedencounter -= 1
                break
            elif playerhp < 1:
                if revivalflag == True:
                    print("You were saved by Necromancy!")
                    playerhp = round(((50 + (playerlevel * constitution)) * 2) / 4)
                    revivalflag = False
                else:
                    print("You lost...")
                    exit()
                
def leveling():
    global playerexp
    global playerlevel
    if playerexp > 100 and playerlevel < 2:
        playerlevel = 2
        print("You reached level", playerlevel, "!")
    elif playerexp > 300 and playerlevel < 3:
        playerlevel = 3
        print("You reached level", playerlevel, "!")
    elif playerexp > 700 and playerlevel < 4:
        playerlevel = 4
        print("You reached level", playerlevel, "!")
    elif playerexp > 1200 and playerlevel < 5:
        playerlevel = 5
        print("You reached level", playerlevel, "!")
    elif playerexp > 1600 and playerlevel < 6:
        playerlevel = 6
        print("You reached level", playerlevel, "!")
    elif playerexp > 2200 and playerlevel < 7:
        playerlevel = 7
        print("You reached level", playerlevel, "!")
    elif playerexp > 2800 and playerlevel < 8:
        playerlevel = 8
        print("You reached level", playerlevel, "!")
    elif playerexp > 3600 and playerlevel < 9:
        playerlevel = 9
        print("You reached level", playerlevel, "!")
    elif playerexp > 5000 and playerlevel < 10:
        playerlevel = 10
        print("You reached level", playerlevel, "!")
    elif playerexp > 6000 and playerlevel < 11:
        playerlevel = 11
        print("You reached level", playerlevel, "!")
    elif playerexp > 7200 and playerlevel < 12:
        playerlevel = 12
        print("You reached level", playerlevel, "!")
    elif playerexp > 10000 and playerlevel < 13:
        playerlevel = 13
        print("You reached level", playerlevel, "!")
    elif playerexp > 12200 and playerlevel < 14:
        playerlevel = 14
        print("You reached level", playerlevel, "!")
    elif playerexp > 14400 and playerlevel < 15:
        playerlevel = 15
        print("You reached level", playerlevel, "!")
    elif playerexp > 17000 and playerlevel < 16:
        playerlevel = 16
        print("You reached level", playerlevel, "!")
    elif playerexp > 20000 and playerlevel < 17:
        playerlevel = 17
        print("You reached level", playerlevel, "!")
    elif playerexp > 25000 and playerlevel < 18:
        playerlevel = 18
        print("You reached level", playerlevel, "!")
    elif playerexp > 32500 and playerlevel < 19:
        playerlevel = 19
        print("You reached level", playerlevel, "!")
    elif playerexp > 40000 and playerlevel < 20:
        playerlevel = 20
        print("You reached level", playerlevel, "!")
    elif playerexp > 50000 and playerlevel < 21:
        playerlevel = 21
        print("You reached level", playerlevel, "!")
        
def enemyscale():
    global enemylevel
    global playerlevel
    enemylevel = round(playerlevel / 2)
    
# Bosses

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
    global taroconstitution
    global playerparalyze
    global spellslot5
    global revivalflag
    if boss1flag == True:
        turn = 1
        bosshp = 80 + (bosslevel * taroconstitution)
        while not (bosshp < 1):
            while turn == 1:
                if playerparalyze < 1:
                    userinput = input("Choice?>")
                    if userinput == "help":
                        print("List of commands:\nfight\nrun\nheal\ncast spell\nswitch spell")
                        turn = 1
                    elif userinput == "fight":
                        weapon_values()
                        bosshp -= playerpower
                        print("Player did:", playerpower, "damage dealt!")
                        turn = 2
                    elif userinput == "heal":
                        heal()
                        turn = 2
                    elif userinput == "run":
                        print("You ran away.")
                        time.sleep(1)
                        return
                    elif userinput == "cast spell":
                        spells()
                        turn = 2
                    elif userinput == "switch spell":
                        switch_spell()
                        turn = 1
                    break
                else:
                    playerparalyze -= 1
                    print("Player is paralyzed!")
                    turn = 2
                    break
            while turn == 2:
                taro_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 100
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                leveling()
                boss1flag = False
                spellslot5 = True
                print("You gained the spell Magic Missile!")
                break
            elif playerhp < 1:
                if revivalflag == True:
                    print("You were saved by Necromancy!")
                    playerhp = round(((50 + (playerlevel * constitution)) * 2) / 4)
                    revivalflag = False
                else:
                    print("You lost...")
                    exit()
                
def taro_boss():
    global bosshp
    global playerhp
    global turn
    global bosslevel
    global fistupgrade
    global tarostrength
    global enemypower
    global stallcountdown
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10 or stallcountdown > 0:
        print("Miss!")
        turn = 1
        stallcountdown -= 1
    else:
        enemypower = (3 * bosslevel) + (random.choice(range(1, 10))) + (fistupgrade * 11) + round(tarostrength / 10)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        stallcountdown -= 1

def mindflower_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global playerexp
    global playerlevel
    global playergold
    global boss2flag
    global mindflowerconstitution
    global playerparalyze
    global revivalflag
    if boss2flag == True:
        turn = 1
        bosshp = 60 + (bosslevel * mindflowerconstitution)
        while not (bosshp < 1):
            while turn == 1:
                if playerparalyze < 1:
                    userinput = input("Choice?>")
                    if userinput == "help":
                        print("List of commands:\nfight\nrun\nheal\ncast spell\nswitch spell")
                        turn = 1
                    elif userinput == "fight":
                        weapon_values()
                        bosshp -= playerpower
                        print("Player did:", playerpower, "damage dealt!")
                        turn = 2
                    elif userinput == "heal":
                        heal()
                        turn = 2
                    elif userinput == "run":
                        print("You ran away.")
                        time.sleep(1)
                        return
                    elif userinput == "cast spell":
                        spells()
                        turn = 2
                    elif userinput == "switch spell":
                        switch_spell()
                        turn = 1
                    break
                else:
                    playerparalyze -= 1
                    print("Player is paralyzed!")
                    turn = 2
                    break
            while turn == 2:
                mindflower_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 100
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                boss2flag = False
                leveling()
                break
            elif playerhp < 1:
                if revivalflag == True:
                    print("You were saved by Necromancy!")
                    playerhp = round(((50 + (playerlevel * constitution)) * 2) / 4)
                    revivalflag = False
                else:
                    print("You lost...")
                    exit()
                
def mindflower_boss():
    global bosshp
    global playerhp
    global turn
    global bosslevel
    global mindflowerintelligence
    global staffupgrade
    global mindflowerwisdom
    global enemypower
    global stallcountdown
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10 or stallcountdown > 0:
        print("Miss!")
        turn = 1
        stallcountdown -= 1
    else:
        enemypower = (bosslevel * 8) + ((bosslevel * staffupgrade) / 2) + round((mindflowerintelligence + mindflowerwisdom) / 10)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        stallcountdown -= 1
	    
def dracula_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    global boss3flag
    global draculaconstitution
    global playerparalyze
    global spellslot3
    global revivalflag
    if boss3flag == True:
        turn = 1
        bosshp = 60 + (bosslevel * draculaconstitution)
        while not (bosshp < 1):
            while turn == 1:
                if playerparalyze < 1:
                    userinput = input("Choice?>")
                    if userinput == "help":
                        print("List of commands:\nfight\nrun\nheal\ncast spell\nswitch spell")
                        turn = 1
                    elif userinput == "fight":
                        weapon_values()
                        bosshp -= playerpower
                        print("Player did:", playerpower, "damage dealt!")
                        turn = 2
                    elif userinput == "heal":
                        heal()
                        turn = 2
                    elif userinput == "run":
                        print("You ran away.")
                        time.sleep(1)
                        return
                    elif userinput == "cast spell":
                        spells()
                        turn = 2
                    elif userinput == "switch spell":
                        switch_spell()
                        turn = 1
                    break
                else:
                    playerparalyze -= 1
                    print("Player is paralyzed!")
                    turn = 2
                    break
            while turn == 2:
                dracula_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 150
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                boss3flag = False
                leveling()
                spellslot3 = True
                print("You gained the spell Full Heal!")
                break
            elif playerhp < 1:
                if revivalflag == True:
                    print("You were saved by Necromancy!")
                    playerhp = round(((50 + (playerlevel * constitution)) * 2) / 4)
                    revivalflag = False
                else:
                    print("You lost...")
                    exit()

def dracula_boss():
    global bosshp
    global playerhp
    global turn
    global bosslevel
    global draculacharisma
    global staffupgrade
    global enemypower
    global stallcountdown
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10 or stallcountdown > 0:
        print("Miss!")
        turn = 1
        stallcountdown -= 1
    else:
        enemypower = (bosslevel * 7) + bosslevel + round((draculacharisma) / 10)
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        stallcountdown -= 1

def sebek_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    global boss4flag
    global sebekconstitution
    global playerparalyze
    global revivalflag
    if boss4flag == True:
        turn = 1
        print(boss, "attacks!")
        bosshp = 80 + (bosslevel * sebekconstitution)
        while not (bosshp < 1):
            while turn == 1:
                if playerparalyze < 1:
                    userinput = input("Choice?>")
                    if userinput == "help":
                        print("List of commands:\nfight\nrun\nheal\ncast spell\nswitch spell")
                        turn = 1
                    elif userinput == "fight":
                        weapon_values()
                        bosshp -= playerpower
                        print("Player did:", playerpower, "damage dealt!")
                        turn = 2
                    elif userinput == "heal":
                        heal()
                        turn = 2
                    elif userinput == "run":
                        print("You ran away.")
                        time.sleep(1)
                        return
                    elif userinput == "cast spell":
                        spells()
                        turn = 2
                    elif userinput == "switch spell":
                        switch_spell()
                        turn = 1
                    break
                else:
                    playerparalyze -= 1
                    print("Player is paralyzed!")
                    turn = 2
                    break
            while turn == 2:
                sebek_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 100
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                boss4flag = False
                leveling()
                break
            elif playerhp < 1:
                if revivalflag == True:
                    print("You were saved by Necromancy!")
                    playerhp = round(((50 + (playerlevel * constitution)) * 2) / 4)
                    revivalflag = False
                else:
                    print("You lost...")
                    exit()
                
def sebek_boss():
    global bosshp
    global playerhp
    global turn
    global bosslevel
    global staffupgrade
    global enemypower
    global stallcountdown
    global sebekintelligence
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 21))
    if miss == 10 or stallcountdown > 0:
        print("Miss!")
        turn = 1
        stallcountdown -= 1
    else:
        enemypower = sebekintelligence * 2
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        stallcountdown -= 1

# Major Bosses

def lolth_boss_encounter():
    global bosslevel
    global turn
    global bosshp
    global playerpower
    global boss
    global playerexp
    global playerlevel
    global playergold
    global lolthflag
    global lolthconstitution
    global playerparalyze
    global revivalflag
    if lolthflag == True:
        turn = 1
        bosshp = 100 + (bosslevel * lolthconstitution)
        while not (bosshp < 1):
            while turn == 1:
                if playerparalyze < 1:
                    userinput = input("Choice?>")
                    if userinput == "help":
                        print("List of commands:\nfight\nrun\nheal\ncast spell\nswitch spell")
                        turn = 1
                    elif userinput == "fight":
                        weapon_values()
                        bosshp -= playerpower
                        print("Player did:", playerpower, "damage dealt!")
                        turn = 2
                    elif userinput == "heal":
                        heal()
                        turn = 2
                    elif userinput == "run":
                        print("You ran away.")
                        time.sleep(1)
                        return
                    elif userinput == "cast spell":
                        spells()
                        turn = 2
                    elif userinput == "switch spell":
                        switch_spell()
                        turn = 1
                    break
                else:
                    playerparalyze -= 1
                    print("Player is paralyzed!")
                    turn = 2
                    break
            while turn == 2:
                lolth_boss()
                print("Player HP:", playerhp)
                turn = 1
                break
            if bosshp < 1:
                print("You won!")
                playerexp += bosslevel * 200
                print("You have", playerexp, "EXP!")
                playergold += bosslevel * random.choice(range(1, 300))
                print("You have", playergold, "gold!")
                lolthflag = False
                leveling()
                spellslot4 = True
                print("The first seal has been broken.")
                seal1 = False
                print("You gained the spell Disintegration.")
                break
            elif playerhp < 1:
                if revivalflag == True:
                    print("You were saved by Necromancy!")
                    playerhp = round(((50 + (playerlevel * constitution)) * 2) / 4)
                    revivalflag = False
                else:
                    print("You lost...")
                    exit()

def lolth_boss():
    global bosshp
    global playerhp
    global turn
    global bosslevel
    global enemypower
    global stallcountdown
    global lolthstrength
    print("Enemy:", bosshp)
    time.sleep(1)
    miss = random.choice(range(1, 41))
    if miss == 10 or stallcountdown > 0:
        print("Miss!")
        turn = 1
        stallcountdown -= 1
    else:
        enemypower = (bosslevel * 4.5) + (lolthstrength * 1.5) + random.choice(range(5, 15))
        playerhp -= enemypower
        print(enemypower, "damage dealt!")
        turn = 1
        stallcountdown -= 1

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
    global playerclass
    if weapon == "fists":
        playerpower = (playerlevel * 2.5) + random.randint(3, 8) + (fistupgrade * 10) + round(strength / 8)
        if playerclass == "barbarian":
            playerpower += (playerlevel * 2)
    elif weapon == "sword":
        playerpower = (playerlevel * 3.5) + (random.randint(5, 15)) + (swordupgrade * 7) + round(strength / 6)
    elif weapon == "bow":
        playerpower = ((playerlevel * 2) + random.randint(5, 12)) * 1.4 + (bowupgrade * 4) + round(dexterity / 4.5)
    elif weapon == "staff":
        playerpower = (playerlevel * 2) + ((playerlevel * staffupgrade) * 1.2) + round((intelligence + wisdom) / 10)
    playerpower = round(playerpower)

def spells():
    global currentspellslot
    global enemyhp
    global bosshp
    global playerpower
    if currentspellslot == 1:
        spell1_stall()
    elif currentspellslot == 2:
        spell2_firebolt()
    elif currentspellslot == 3:
        spell3_heal()
    elif currentspellslot == 4:
        spell4_disintegration()
        try:
            enemyhp -= playerpower
            bosshp -= playerpower
        except NameError:
            print()
    elif currentspellslot == 5:
        spell5_magicmissile()
        enemyhp -= playerpower
        bosshp -= playerpower
    elif currentspellslot == 6:
        spell6_entrance()
    elif currentspellslot == 7:
        spell7_icebeam()
        enemyhp -= playerpower
        bosshp -= playerpower
    elif currentspellslot == 8:
        spell8_attract()
    elif currentspellslot == 9:
        spell9_lightningbolt()
    elif currentspellslot == 10:
        spell10_timestop()
    elif currentspellslot == 11:
        spell11_thunder()
    elif currentspellslot == 12:
        spell12_gambler()
    elif currentspellslot == 13:
        spell13_necromancy()
    elif currentspellslot == 14:
        spell14_torrent()
    elif currentspellslot == 15:
        spell15_chroma()
    elif currentspellslot == 16:
        spell16_necromancy()
    elif currentspellslot == 17:
        spell17_healofthewild()
    elif currentspellslot == 18:
        spell18_ancientpower()
        enemyhp -= playerpower
        bosshp -= playerpower
    elif currentspellslot == 19:
        spell19_()
    elif currentspellslot == 20:
        spell20_()
    elif currentspellslot == 21:
        spell21_necromancy()
    elif currentspellslot == 22:
        spell22_exorcism()
    elif currentspellslot == 23:
        spell23_()
    elif currentspellslot == 24:
        spell24_()
    elif currentspellslot == 25:
        spell25_()
    elif currentspellslot == 26:
        spell26_necromancy()
    elif currentspellslot == 27:
        spell27_widespreadruin()
        enemyhp -= playerpower
        bosshp -= playerpower
    elif currentspellslot == 28:
        spell28_()
    elif currentspellslot == 29:
        spell29_()
    elif currentspellslot == 30:
        spell30_()
    elif currentspellslot == 31:
        spell31_necromancy()
    elif currentspellslot == 32:
        spell32_char()
        enemyhp -= playerpower
        bosshp -= playerpower
    elif currentspellslot == 33:
        spell33_()
    elif currentspellslot == 34:
        spell34_()
    elif currentspellslot == 35:
        spell35_()

# General Spells

def spell1_stall():
    global stallcountdown
    global playerhp
    global playerlevel
    global spellslot1
    if spellslot1 == True:
        stallcountdown = 4
        playerhp -= 20 * playerlevel
        print("Player lost", (20 * playerlevel), "HP!")
    else:
        print("Spell failed!")

def spell2_firebolt():
    global playerpower
    global playerhp
    global playerlevel
    global bosshp
    global enemyhp
    global spellslot2
    if spellslot2 == True:
        playerpower = playerlevel * 40
        playerhp -= playerlevel * 20
        try:
            bosshp -= playerpower
            enemyhp -= playerpower
            if enemyhp < 1 or bosshp < 1:
                enemyhp = 1
                bosshp = 1
            print(playerpower, "damage dealt!")
            print("Player got burned with", (playerlevel * 20), "damage!")
            print("The enemy endured the burn with 1 HP!")
        except NameError:
            print()
    else:
        print("Spell Failed!")

def spell3_heal():
    global playerhp
    global playerlevel
    global constitution
    global playergold
    global spellslot3
    if spellslot3 == True:
        print("Fully healed!")
        playergold -= playerhp
        playerhp = 50 + ((playerlevel * constitution) * 2)
        print("Player lost", playerhp, "gold!")
    else:
        print("Spell Failed!")

def spell4_disintegration():
    global playerpower
    global spellslot4
    d20 = random.choice(range(1, 21))
    if spellslot4 == True:
        if d20 == 20:
            playerpower = random.choice(range(600000, 24000000))
            print(playerpower, "damage dealt! The enemy was atomized!")
        else:
            print("The ray fizzled out...")
            playerpower = 1
            print("1 damage dealt.")
    else:
        print("Spell failed!")

def spell5_magicmissile():
    global playerpower
    global playerlevel
    global spellslot5
    if spellslot5 == True:
        playerpower = random.choice(range(1, 11) * playerlevel)
    else:
        print("Spell failed!")

def spell6_entrance():
    global stallcountdown
    global playerhp
    global spellslot6
    global charisma
    global playerlevel
    if spellslot6 == True:
        d10 = random.choice(range(1, round((charisma + 1) / 2)))
        if d10 < round((charisma) / 2):
            stallcountdown = 2
            playerhp -= 10 * playerlevel
            print("You entranced the enemy!")
        else:
            print("The enemy wasn't horny enough!")
    else:
        print("Spell failed!")

def spell7_icebeam():
    global playerpower
    global playerhp
    global playerlevel
    global bosshp
    global enemyhp
    global stallcountdown
    global intelligence
    global spellslot7
    if spellslot7 == True:
        playerpower = playerlevel * 2 + (intelligence * 2)
        playerhp -= round(playerpower * .75)
        d10 = random.choice(range(1, 11))
        try:
            bosshp -= playerpower
            enemyhp -= playerpower
            if d10 == 10:
                stallcountdown = random.choice(range(1, 4))
                print("Enemy Frozen!")
        except NameError:
            print()
    else:
        print("Spell Failed!")

def spell8_attract():
    global forcedencounter
    global playerlevel
    global playerhp
    global spellslot8
    if spellslot8 == True:
        forcedencounter = 2
        playerhp -= 10 * playerlevel
    else:
        print("Spell failed!")

def spell9_lightningbolt():
    global playerpower
    global playerhp
    global playerlevel
    global bosshp
    global enemyhp
    global stallcountdown
    global wisdom
    global playerparalyze
    global spellslot9
    if spellslot9 == True:
        playerpower = playerlevel * 2 + (wisdom * 3)
        playerparalyze = 2
        d10 = random.choice(range(1, 11))
        try:
            print("Player Paralyzed!")
            bosshp -= playerpower
            enemyhp -= playerpower
            if d10 == 10:
                stallcountdown = random.choice(range(1, 4))
                print("Enemy Paralyzed!")
        except NameError:
            print()
    else:
        print("Spell Failed!")

def spell10_timestop():
    global spellslot10
    global playerparalyze
    global stallcountdown
    if spellslot10 == True:
        playerparalyze = 2
        stallcountdown = 3
        print("Time has been stopped!")
    else:
        print("Spell failed!")

# Wizard Spells

def spell11_thunder():
    global playerpower
    global playerhp
    global playerlevel
    global bosshp
    global enemyhp
    global stallcountdown
    global wisdom
    global playerparalyze
    global spellslot11
    global playerclass
    if playerclass == "wizard":
        if spellslot11 == True:
            playerpower = playerlevel * 3 + (wisdom * 3)
            d10 = random.choice(range(1, 6))
            try:
                bosshp -= playerpower
                enemyhp -= playerpower
                if d10 == 5:
                    stallcountdown = random.choice(range(1, 6))
                    print("Enemy Paralyzed!")
                elif d10 == 1:
                    playerparalyze = random.choice(range(1, 5))
                    print("Player Paralyzed!")
            except NameError:
                print()
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

def spell12_gambler():
    global spellslot12
    global playerparalyze
    global stallcountdown
    global playerclass
    if playerclass == "wizard":
        if spellslot12 == True:
            playerparalyze = random.choice(range(1, 6))
            stallcountdown = random.choice(range(1, 6))
            print("Time has been stopped! It's not equal on both adversaries, however...")
        else:
            print("Spell failed!")
    else:
        print("This spell is incompatible with your class!")

def spell13_necromancy():
    global revivalflag
    global spellslot13
    global playerclass
    if playerclass == "wizard":
        if spellslot13 == True:
            revivalflag = True
        else:
            print("Spell failed!")
    else:
        print("This spell is incompatible with your class!")

def spell14_torrent():
    global playerpower
    global playerhp
    global playerlevel
    global bosshp
    global enemyhp
    global intelligence
    global playerparalyze
    global spellslot14
    global playerclass
    if playerclass == "wizard":
        if spellslot14 == True:
            playerpower = playerlevel * 3 + (intelligence * 3)
            try:
                bosshp -= playerpower
                enemyhp -= playerpower
                playerparalyze = 1
            except NameError:
                print()
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

def spell15_chroma():
    global playerclass
    global spellslot15
    global stallcountdown
    global playerparalyze
    if playerclass == "wizard":
        if spellslot15 == True:
            stallcountdown = 4
            playerparalyze = random.choice(range(1, 8))
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

# Druid Spells

def spell16_necromancy():
    global revivalflag
    global spellslot13
    global playerclass
    if playerclass == "druid":
        if spellslot13 == True:
            revivalflag = True
        else:
            print("Spell failed!")
    else:
        print("This spell is incompatible with your class!")

def spell17_healofthewild():
    global playerhp
    global playerlevel
    global constitution
    global playergold
    global spellslot3
    global playerparalyze
    if playerclass == "druid":
        if spellslot3 == True:
            print("Fully healed!")
            playergold -= playerhp
            playerhp = 50 + ((playerlevel * constitution) * 2)
            playerparalyze = 2
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

def spell18_ancientpower():
    global playerpower
    global playerclass
    global spellslot18
    global bank
    global playerlevel
    if playerclass == "druid":
        if spellslot18 == True:
            if not bank in ["dungeon1", "dungeon2", "dungeon3", "dungeon4", "avernus"]:
                playerpower = (playerlevel * 10) + random.choice(range(1, 21))
            else:
                playerpower = (playerlevel * 7) + random.choice(range(1, 14))
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

def spell19_():
    print("Under Construction")

def spell20_():
    print("Under Construction")

# Cleric Spells

def spell21_necromancy():
    global revivalflag
    global spellslot13
    global playerclass
    if playerclass == "cleric":
        if spellslot13 == True:
            revivalflag = True
        else:
            print("Spell failed!")
    else:
        print("This spell is incompatible with your class!")

def spell22_exorcism():
    global spellslot22
    global playerhp
    global playerclass
    global playergold
    global playerparalyze
    global constitution
    global playerlevel
    if playerclass == "cleric":
        if spellslot22 == True:
            playerhp = 100 + ((constitution * playerlevel) * 4)
            playergold -= playerhp
            playerparalyze = 6
            if playergold < 0:
                print("You're in debt. The demons take some of your HP as payment.")
                playerhp += playergold * 2
                playergold = 0
            else:
                print("The angels have blessed you.")
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

def spell23_():
    print("Under Construction")

def spell24_():
    print("Under Construction")

def spell25_():
    print("Under Construction")

# Paladin Spells

def spell26_necromancy():
    global revivalflag
    global spellslot13
    global playerclass
    if playerclass == "paladin":
        if spellslot13 == True:
            revivalflag = True
        else:
            print("Spell failed!")
    else:
        print("This spell is incompatible with your class!")

def spell27_widespreadruin():
    global playerpower
    global spellslot4
    global playerclass
    if playerclass == "paladin":
        d10 = random.choice(range(1, 11))
        if spellslot4 == True:
            if d10 == 10:
                playerpower = random.choice(range(600000, 24000000))
                print(playerpower, "damage dealt! The enemy was atomized!")
            else:
                print("The ray fizzled out...")
                playerpower = 1
                print("1 damage dealt.")
        else:
            print("Spell failed!")

def spell28_():
    print("Under Construction")

def spell29_():
    print("Under Construction")

def spell30_():
    print("Under Construction")

# Bard Spells

def spell31_necromancy():
    global revivalflag
    global spellslot13
    global playerclass
    if playerclass == "bard":
        if spellslot13 == True:
            revivalflag = True
        else:
            print("Spell failed!")
    else:
        print("This spell is incompatible with your class!")

def spell32_char():
    global playerclass
    global spellslot32
    global playerpower
    if playerclass == "bard":
        if spellslot32 == True:
            playerpower = charisma * 4
        else:
            print("Spell Failed!")
    else:
        print("This spell is incompatible with your class!")

def spell33_():
    print("Under Construction")

def spell34_():
    print("Under Construction")

def spell35_():
    print("Under Construction")

def savedata():
    for key in game.keys():
        if key in globals():
            game[key] = globals()[key]
    
    with open("yorkgoblinsave.json", "w") as file:
        json.dump(game, file)
    print("Rested at bonfire. Game saved.")

def loaddata():
    global game
    try:
        with open("yorkgoblinsave.json", "r") as file:
            game = json.load(file)

        for key, value in game.items():
            globals()[key] = value

        print("You woke up at a bonfire. Game loaded.")
    except FileNotFoundError:
        print("Starting a new game.")

# --- Main Game ---
loaddata()

if introflag == True:
    playerclasspicker = ["fighter", "wizard", "paladin", "cleric", "rogue", "druid", "bard", "barbarian"]
    print("Hello, Player.")
    time.sleep(1)
    print("It's time to choose your class.")
    time.sleep(1)
    print("""List of classes:
    Fighter (+4, +4, +1, +0, +0, -3)
    Wizard (-3, +0, +1, +5, +4, +0)
    Paladin (+3, +2, +1, +4, +1, -3)
    Cleric (-2, +1, +4, +4, +3, +0)
    Rogue (-2, +4, +2, +3, +1, +2)
    Druid (-1, +1, +4, +3, +2, +0)
    Bard (-2, +1, +2, +3, +3, +5)
    Barbarian (+4, +3, +3, -2, -1, -2)""")
    if classflag == True:
        userinput = input("Choice?>")
        if userinput in playerclasspicker:
            playerclass = userinput
            if playerclass == "fighter":
                strength += 4
                dexterity += 4
                constitution += 1
                intelligence += 0
                wisdom += 0
                charisma -= 3
            elif playerclass == "wizard":
                strength -= 3
                dexterity += 0
                constitution += 1
                intelligence += 5
                wisdom += 4
                charisma += 0
            elif playerclass == "paladin":
                strength += 3
                dexterity += 2
                constitution += 1
                intelligence += 4
                wisdom += 1
                charisma -= 3
            elif playerclass == "cleric":
                strength -= 2
                dexterity += 1
                constitution += 4
                intelligence += 4
                wisdom += 3
                charisma += 0
            elif playerclass == "rogue":
                strength -= 2
                dexterity += 4
                constitution += 2
                intelligence += 3
                wisdom += 1
                charisma += 2
            elif playerclass == "druid":
                strength -= 1
                dexterity += 1
                constitution += 4
                intelligence += 3
                wisdom += 2
                charisma += 0
            elif playerclass == "bard":
                strength -= 2
                dexterity += 1
                constitution += 2
                intelligence += 3
                wisdom += 3
                charisma += 5
            elif playerclass == "barbarian":
                strength -= 4
                dexterity += 3
                constitution += 3
                intelligence -= 2
                wisdom -= 1
                charisma += -2
            classflag = False
            introflag = False
        else:
            print("Invalid class!")

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
    introflag = False

def manualsavedata():
    # Place your stats from your last playthrough here. You could also use this to cheat, but that's no fun at all, is it?
    print() # Replace this print with setting your variables to the right values, do the same with bank and cell number

manualsavedata() # This loads your data

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
                print("There are two people in the room. One is a girl named May. The other is her husband Thomas. They seem to be very cheerful and happy. What do you do?")
                userinput = input("May's Cottage> ")
                if userinput == "talk may":
                    print("May: Well, hello there! Yes, I'm very happy with my husband.")
                    time.sleep(1)
                    print("May: Oh? The forest? Oh, I advise you don't go there. Many an adventurer have gone, and none have returned.")
                elif userinput == "talk thomas":
                    print("Thomas: Hey man. How ya doin?")
                    time.sleep(1)
                    print("Thomas: Listen to my wife, kid.")
                elif userinput == "leave":
                    print("You leave the cottage.")
                    break
                else:
                    print("Invalid command!")
        elif userinput == "move north":
            print("You exit the town, and push forward further. You wonder what awaits you...")
            bank = "forest1"
            forestcell = 1
        elif userinput == "help":
            help()
        elif userinput == "stats":
            stat()
        elif userinput == "switch spell":
            switch_spell()
        else:
            print("Invalid Command!")
            
    # Forest 1 (this has a quest now)
    
    elif bank == "forest1":
        enemylevel = round(playerlevel * 0.75)
        if forestcell == 1:
            print("Forest. Cell 1. East, West, North, South. A bonfire sits here, where you can rest.")
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
            elif userinput == "rest":
                savedata()
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
                
        # Cell 9
                
        elif forestcell == 9:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 9. East, South, West, North. A lone druid sits atop a branch.")
            userinput = input("Forest>")
            if userinput == "move west":
                forestcell = 10
            elif userinput == "move north":
                forestcell = 11
            elif userinput == "move east":
                forestcell = 8
            elif userinput == "move south":
                forestcell = 4
            elif userinput == "talk druid":
                if quest1 == 1 and boss1flag == True:
                    print("Druid: Hello, adventurer.")
                    time.sleep(1)
                    print("Druid: I have a quest for you.")
                    time.sleep(1)
                    print("Druid: There is a blue dragon named Taro that is disturbing the land near him.")
                    time.sleep(1)
                    print("Druid: I will send you to kill him.")
                    time.sleep(1)
                    print("Druid: Good luck, adventurer.")
                    quest1 = 2
                elif quest1 == 1 and boss1flag == False:
                    print("Druid: Oh? You've slain Taro already! Thank you!")
                    playerexp += 500
                    print("You gained 500 EXP!")
                    quest1 = 3
                elif quest1 == 2 and boss1flag == True:
                    print("Druid: Go, slay Taro!")
                elif quest1 == 2 and boss1flag == False:
                    print("Druid: You've slain him! I knew you could do it!")
                    playerexp += 500
                    print("You've gained 500 EXP!")
                    quest1 = 3
                elif quest1 == 3:
                    print("Druid: Haha! Are you proud of yourself as a warrior?")
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
                
        elif forestcell == 15:
            monster = random.choice(["Bear", "Goblin", "Baby Dragon", "Spider"])
            encounter()
            print("Forest. Cell 15. There is an entrance in the ground. East, South.")
            userinput = input("Forest>")
            if userinput == "move east":
                bank = "peatbogs"
                peatbogscell = 1
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
                bank = "dungeon3"
                dungeon3cell = 1
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command1!")
                
    # Village 2
                
    elif bank == "village2":
        enemylevel = round(playerlevel * 0.75)
        if village2cell == 1:
            print("Welcome to Roark Town! Cell 1 (Trail). South, North, Northwest, Southwest, West. You can rest in this town.")
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
            elif userinput == "rest":
                savedata()
            elif userinput == "switch spell":
                switch_spell()
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
                                break
                            else:
                                print("There we go! A nice accessory!")
                                fistupgrade = 1
                                gold -= 100
                                break
                        elif weapon == "sword":
                            if gold < 120:
                                print("You don't have enough money! Come back a little richer!")
                                break
                            else:
                                print("There we go! A nice accessory!")
                                swordupgrade = 1
                                gold -= 120
                                break
                        elif weapon == "bow":
                            if gold < 175:
                                print("You don't have enough money! Come back a little richer!")
                                break
                            else:
                                print("There we go! A nice accessory!")
                                bowupgrade = 1
                                gold -= 175
                                break
                        elif weapon == "staff":
                            if gold < 500:
                                print("You don't have enough money! Come back a little richer!")
                                break
                            else:
                                print("There we go! A nice accessory!")
                                staffupgrade = 1
                                gold -= 500
                                break
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 11 ---
        
        elif dungeon1cell == 11:
            print("Taro's Dungeon. Cell 11. West, North. There is a chest in the room.")
            monster = random.choice(["Goblin", "Spider"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move east":
                dungeon1cell = 10
            elif userinput == "move north":
                dungeon1cell = 12
            elif userinput == "open chest":
                if chest1flag == True:
                    print("You found 250 gold!")
                    playergold += 250
                    chest1flag = False
                else:
                    print("There is nothing in the chest.")
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 16 ---
        
        elif dungeon1cell == 16:
            print("Taro's Dungeon. Cell 16. South, North. There is a chest in the room.")
            monster = random.choice(["Slime", "Knight"])
            userinput = input("Taro's Dungeon> ")
            encounter()
            if userinput == "move south":
                dungeon1cell = 17
            elif userinput == "move north":
                dungeon1cell = 6
            elif userinput == "open chest":
                if chest2flag == True:
                    print("You found a magic scroll!")
                    spellslot1 = True
                    chest2flag = False
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 18 ---
        
        elif dungeon1cell == 18:
            print("Taro's Dungeon. Cell 18. North.")
            boss = "Taro"
            userinput = input("Taro's Dungeon> ")
            encounter()
            if boss1flag == True:
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
                elif userinput == "switch spell":
                    switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
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
                elif userinput == "switch spell":
                    switch_spell()
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
                
    # Peatbogs
                
    elif bank == "peatbogs":
        enemylevel = round(0.75 * playerlevel)
        if peatbogscell == 1:
            print("Peatbogs. Cell 1. East, West.")
            monster = random.choice(["Ghost", "Shade"])
            userinput = input("Peatbogs>")
            encounter()
            if userinput == "move east":
                peatbogscell = 2
            elif userinput == "move west":
                bank = "forest1"
                forestcell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
                
            # --- Cell 2 ---
        elif peatbogscell == 2:
            print("Peatbogs. Cell 2. North, South, West.")
            monster = random.choice(["Bogling", "Leech"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move north":
                peatbogscell = 3
            elif userinput == "move south":
                peatbogscell = 6
            elif userinput == "move west":
                peatbogscell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 3 ---
        elif peatbogscell == 3:
            print("Peatbogs. Cell 3. East, South, North.")
            monster = random.choice(["Swamp Slime", "Wisp"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 5
            elif userinput == "move south":
                peatbogscell = 2
            elif userinput == "move north":
                peatbogscell = 17
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 4 ---
        elif peatbogscell == 4:
            print("Peatbogs. Cell 4. West, South.")
            monster = random.choice(["Bogling", "Leech"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move south":
                peatbogscell = 19
            elif userinput == "move west":
                peatbogscell = 6
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 5 ---
        elif peatbogscell == 5:
            print("Peatbogs. Cell 5. West, East, North.")
            monster = random.choice(["Leech", "Swamp Slime"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 3
            elif userinput == "move east":
                peatbogscell = 15
            elif userinput == "move north":
                peatbogscell = 7
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 6 ---
        elif peatbogscell == 6:
            print("Peatbogs. Cell 6. North, East.")
            monster = random.choice(["Bogling", "Swamp Slime"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move north":
                peatbogscell = 2
            elif userinput == "move east":
                peatbogscell = 4
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 7 ---
        elif peatbogscell == 7:
            print("Peatbogs. Cell 7. North, West, East, South.")
            monster = random.choice(["Witch", "Swamp Drake"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move north":
                peatbogscell = 8
            elif userinput == "move west":
                peatbogscell = 17
            elif userinput == "move east":
                peatbogscell = 14
            elif userinput == "move south":
                peatbogscell = 5
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 8 ---
        elif peatbogscell == 8:
            print("Peatbogs. Cell 8. East, South, North.")
            monster = random.choice(["Leech", "Wisp"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 12
            elif userinput == "move south":
                peatbogscell = 7
            elif userinput == "move north":
                peatbogscell = 10
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 9 ---
        elif peatbogscell == 9:
            print("Peatbogs. Cell 9. East.")
            monster = random.choice(["Bogling", "Peat Horror"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 10
            elif userinput == "move west":
                bank = "highlands"
                mountaincell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 10 ---
        elif peatbogscell == 10:
            print("Peatbogs. Cell 10. East, West, South.")
            monster = random.choice(["Swamp Slime", "Leech"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 11
            elif userinput == "move west":
                peatbogscell = 9
            elif userinput == "move south":
                peatbogscell = 8
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 11 ---
        elif peatbogscell == 11:
            print("Peatbogs. Cell 11. West, South.")
            monster = random.choice(["Swamp Drake", "Peat Horror"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 10
            elif userinput == "move south":
                peatbogscell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 12 ---
        elif peatbogscell == 12:
            print("Peatbogs. Cell 12. West, East, South, North.")
            monster = random.choice(["Leech", "Wisp"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 8
            elif userinput == "move east":
                peatbogscell = 13
            elif userinput == "move south":
                peatbogscell = 14
            elif userinput == "move north":
                peatbogscell = 11
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 13 ---
        elif peatbogscell == 13:
            print("Peatbogs. Cell 13. West.")
            monster = random.choice(["Swamp Drake", "Bogling"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 14 ---
        elif peatbogscell == 14:
            print("Peatbogs. Cell 14. West, South, North.")
            monster = random.choice(["Witch", "Peat Horror"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 7
            elif userinput == "move south":
                peatbogscell = 15
            elif userinput == "move north":
                peatbogscell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 15 ---
        elif peatbogscell == 15:
            print("Peatbogs. Cell 15. West, East, South, North.")
            monster = random.choice(["Leech", "Swamp Slime"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 5
            elif userinput == "move east":
                peatbogscell = 16
            elif userinput == "move south":
                peatbogscell = 18
            elif userinput == "move north":
                peatbogscell = 14
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 16 ---
        elif peatbogscell == 16:
            print("Peatbogs. Cell 16. West.")
            monster = random.choice(["Swamp Drake", "Witch"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 17 ---
        elif peatbogscell == 17:
            print("Peatbogs. Cell 17. East, South.")
            monster = random.choice(["Peat Horror", "Bogling"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 7
            elif userinput == "move south":
                peatbogscell = 3
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cell 18 ---
        elif peatbogscell == 18:
            print("Peatbogs. Cell 18. North.")
            monster = random.choice(["Peat Horror", "Bogling"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move north":
                peatbogscell = 17
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        # --- Cells 19–25 ---
        elif peatbogscell == 19:
            print("Peatbogs. Cell 19. North, East.")
            monster = random.choice(["Leech", "Wisp"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move north":
                peatbogscell = 4
            elif userinput == "move east":
                peatbogscell = 20
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        elif peatbogscell == 20:
            print("Peatbogs. Cell 20. West, South.")
            monster = random.choice(["Bogling", "Leech"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 19
            elif userinput == "move south":
                peatbogscell = 21
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        elif peatbogscell == 21:
            print("Peatbogs. Cell 21. North, East.")
            monster = random.choice(["Swamp Drake", "Witch"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move north":
                peatbogscell = 20
            elif userinput == "move east":
                peatbogscell = 22
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        elif peatbogscell == 22:
            print("Peatbogs. Cell 22. West, South.")
            monster = random.choice(["Bogling", "Swamp Slime"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 21
            elif userinput == "move south":
                peatbogscell = 23
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        elif peatbogscell == 23:
            print("Peatbogs. Cell 23. East, North.")
            monster = random.choice(["Peat Horror", "Witch"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 24
            elif userinput == "move north":
                peatbogscell = 22
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        elif peatbogscell == 24:
            print("Peatbogs. Cell 24. East, West.")
            monster = random.choice(["Wisp", "Leech"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move east":
                peatbogscell = 25
            elif userinput == "move west":
                peatbogscell = 23
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
    
        elif peatbogscell == 25:
            print("Peatbogs. Cell 25. West. The bog bubbles ominously here, and the air smells of death.")
            monster = random.choice(["Swamp Drake", "Peat Horror"])
            userinput = input("Peatbogs> ")
            encounter()
            if userinput == "move west":
                peatbogscell = 24
            elif userinput == "move south":
                bank == "cursedmarsh"
                marshcell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
                
    # Abandoned Old House
    
    elif bank == "dungeon3":
        enemylevel = round(0.8 * playerlevel)
        if dungeon3cell == 1:
            print("Old House. Cell 1. South, North.")
            monster = random.choice(["Poltergeist", "Ghoul"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move south":
                dungeon3cell = 4
            elif userinput == "move north":
                bank = "graveyard1"
                gravecell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        elif dungeon3cell == 2:
            print("Old House. Cell 2. East.")
            monster = random.choice(["Ghoul", "Haunted Armor"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move east":
                dungeon3cell = 3
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 3:
            print("Old House. Cell 3. West, East, South.")
            monster = random.choice(["Ghoul", "Specter"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 2
            elif userinput == "move east":
                dungeon3cell = 4
            elif userinput == "move south":
                dungeon3cell = 7
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 4:
            print("Old House. Cell 4. West, East, South.")
            monster = random.choice(["Poltergeist", "Wraith"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 3
            elif userinput == "move east":
                dungeon3cell = 5
            elif userinput == "move north":
                dungeon3cell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 5:
            print("Old House. Cell 5. West, East, South.")
            monster = random.choice(["Ghoul", "Haunted Candle"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 4
            elif userinput == "move east":
                dungeon3cell = 6
            elif userinput == "move south":
                dungeon3cell = 8
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 6:
            print("Old House. Cell 6. West.")
            monster = random.choice(["Spirit", "Cursed Doll"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 5
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 7:
            print("Old House. Cell 7. North, South.")
            monster = random.choice(["Phantom", "Specter"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 3
            elif userinput == "move south":
                dungeon3cell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 8:
            print("Old House. Cell 8. North, South.")
            monster = random.choice(["Ghoul", "Haunted Candle"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 5
            elif userinput == "move south":
                dungeon3cell = 13
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 9:
            print("Old House. Cell 9. East, South.")
            monster = random.choice(["Shade", "Wraith"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move east":
                dungeon3cell = 10
            elif userinput == "move south":
                dungeon3cell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 10:
            print("Old House. Cell 10. West, East.")
            monster = random.choice(["Ghoul", "Haunted Armor"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 9
            elif userinput == "move east":
                dungeon3cell = 11
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 11:
            print("Old House. Cell 11. West, East, South.")
            monster = random.choice(["Specter", "Poltergeist"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 10
            elif userinput == "move east":
                dungeon3cell = 12
            elif userinput == "move south":
                dungeon3cell = 16
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
                
        elif dungeon3cell == 12:
            print("Old House. Cell 12. West, North. A chest lies in the room.")
            monster = random.choice(["Haunted Armor", "Specter"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 11
            elif userinput == "move north":
                dungeon3cell = 7
            elif userinput == "open chest":
                if chest3flag == True:
                    print("You found an ancient scroll!")
                    spellslot3 = True
                    print("You gained Fire Bolt!")
                    chest3flag = False
                else:
                    print("The chest is already open!")
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 13:
            print("Old House. Cell 13. North, East, South.")
            monster = random.choice(["Spirit", "Shade"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 8
            elif userinput == "move east":
                dungeon3cell = 14
            elif userinput == "move south":
                dungeon3cell = 17
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 14:
            print("Old House. Cell 14. West.")
            monster = random.choice(["Poltergeist", "Haunted Candle"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 13
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 15:
            print("Old House. Cell 15. North, South.")
            monster = random.choice(["Ghoul", "Cursed Doll"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 9
            elif userinput == "move south":
                dungeon3cell = 18
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 16:
            print("Old House. Cell 16. North, South. A bed sits near the wall, neatly made.")
            monster = random.choice(["Wraith", "Specter"])
            userinput = input("Old House>")
            if userinput == "move north":
                dungeon3cell = 11
            elif userinput == "move south":
                dungeon3cell = 19
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
            elif userinput == "rest":
                savedata()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 17:
            print("Old House. Cell 17. North, South.")
            monster = random.choice(["Haunted Armor", "Phantom"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 13
            elif userinput == "move south":
                dungeon3cell = 21
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 18:
            print("Old House. Cell 18. North. A staircase leading to some kind of entrance lies here.")
            monster = random.choice(["Specter", "Ghoul"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 15
            elif userinput == "enter":
                bank = "avernus"
                avernuscell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 19:
            print("Old House. Cell 19. North, East.")
            monster = random.choice(["Shade", "Wraith"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 16
            elif userinput == "move east":
                dungeon3cell = 20
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 20:
            print("Old House. Cell 20. West, South.")
            monster = random.choice(["Spirit", "Phantom"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 19
            elif userinput == "move south":
                dungeon3cell = 24
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 21:
            print("Old House. Cell 21. North, East.")
            monster = random.choice(["Haunted Candle", "Specter"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 17
            elif userinput == "move east":
                dungeon3cell = 22
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 22:
            print("Old House. Cell 22. West, East.")
            monster = random.choice(["Cursed Doll", "Poltergeist"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 21
            elif userinput == "move east":
                dungeon3cell = 23
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 23:
            print("Old House. Cell 23. West, South.")
            monster = random.choice(["Phantom", "Haunted Armor"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move west":
                dungeon3cell = 22
            elif userinput == "move south":
                dungeon3cell = 25
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 24:
            print("Old House. Cell 24. North.")
            monster = random.choice(["Wraith", "Shade"])
            userinput = input("Old House>")
            encounter()
            if userinput == "move north":
                dungeon3cell = 20
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon3cell == 25:
            print("Old House. Cell 25. North.")
            monster = random.choice(["Specter", "Haunted Candle"])
            userinput = input("Old House>")
            encounter()
            if boss3flag == True:
                print("The air becomes cold around you.")
                time.sleep(1)
                print("You feel a strange presence.")
                time.sleep(1)
                print("A cloak appears in front of you.")
                time.sleep(1)
                print("Then teeth appear.")
                time.sleep(2)
                print("It's Dracula!")
                time.sleep(0.5)
                print("Dracula attacks!")
                dracula_boss_encounter()
            else:
                if userinput == "move north":
                    dungeon3cell = 23
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
                elif userinput == "switch spell":
                    switch_spell()
                else:
                    print("Invalid Command!")

    # Avernus (First Major Boss Area)

    elif bank == "avernus":
        enemylevel = round(1.2 * playerlevel)
        if avernuscell == 1:
            print("Avernus. Cell 1. East.")
            monster = random.choice(["Demon", "Imp"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 2
            elif userinput == "leave":
                bank = "dungeon3"
                dungeon3cell = 18
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 2:
            print("Avernus. Cell 2. East, West, North, South.")
            monster = random.choice(["Imp", "Ash Hound"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 3
            elif userinput == "move west":
                avernuscell = 1
            elif userinput == "move north":
                avernuscell = 13
            elif userinput == "move south":
                avernuscell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 3:
            print("Avernus. Cell 3. East, West, North, South.")
            monster = random.choice(["Imp", "Lava Serpent"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 4
            elif userinput == "move west":
                avernuscell = 2
            elif userinput == "move north":
                avernuscell = 14
            elif userinput == "move south":
                avernuscell = 8
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 4:
            print("Avernus. Cell 4. South, West, North.")
            monster = random.choice(["Hellhound", "Imp"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move south":
                avernuscell = 9
            elif userinput == "move west":
                avernuscell = 3
            elif userinput == "move north":
                avernuscell = 15
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 5:
            print("Avernus. Cell 5. East, North.")
            monster = random.choice(["Ash Hound", "Magma Fiend"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 6
            elif userinput == "move north":
                avernuscell = 17
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 6:
            print("Avernus. Cell 6. West, South, North.")
            monster = random.choice(["Hell Bat", "Imp"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move west":
                avernuscell = 5
            elif userinput == "move south":
                avernuscell = 10
            elif userinput == "move north":
                avernuscell = 18
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 7:
            print("Avernus. Cell 7. East, South, North.")
            monster = random.choice(["Imp", "Flame Spirit"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 8
            elif userinput == "move south":
                avernuscell = 12
            elif userinput == "move north":
                avernuscell = 2
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 8:
            print("Avernus. Cell 8. East, West, North.")
            monster = random.choice(["Hellhound", "Infernal Bug"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 9
            elif userinput == "move west":
                avernuscell = 7
            elif userinput == "move north":
                avernuscell = 3
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 9:
            print("Avernus. Cell 9. North, West.")
            monster = random.choice(["Flame Spirit", "Ash Hound"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move north":
                avernuscell = 4
            elif userinput == "move west":
                avernuscell = 8
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 10:
            print("Avernus. Cell 10. East, North.")
            monster = random.choice(["Infernal Bug", "Magma Fiend"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 20
            elif userinput == "move north":
                avernuscell = 6
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 11:
            print("Avernus. Cell 11. South, West.")
            monster = random.choice(["Demon", "Lava Serpent"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move south":
                avernuscell = 16
            elif userinput == "move west":
                avernuscell = 19
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 12:
            print("Avernus. Cell 12. North.")
            monster = random.choice(["Imp", "Hell Bat"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move north":
                avernuscell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 13:
            print("Avernus. Cell 13. East, South.")
            monster = random.choice(["Flame Spirit", "Hellhound"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 14
            elif userinput == "move south":
                avernuscell = 2
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 14:
            print("Avernus. Cell 14. East, West, South.")
            monster = random.choice(["Ash Hound", "Magma Fiend"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 15
            elif userinput == "move west":
                avernuscell = 13
            elif userinput == "move south":
                avernuscell = 3
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 15:
            print("Avernus. Cell 15. East, West, North, South.")
            monster = random.choice(["Demon", "Flame Spirit"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 16
            elif userinput == "move west":
                avernuscell = 14
            elif userinput == "move north":
                avernuscell = 19
            elif userinput == "move south":
                avernuscell = 4
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 16:
            print("Avernus. Cell 16. East, West, North.")
            monster = random.choice(["Hell Bat", "Infernal Bug"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 17
            elif userinput == "move west":
                avernuscell = 15
            elif userinput == "move north":
                avernuscell = 11
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 17:
            print("Avernus. Cell 17. East, West, South.")
            monster = random.choice(["Imp", "Lava Serpent"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move east":
                avernuscell = 18
            elif userinput == "move west":
                avernuscell = 16
            elif userinput == "move south":
                avernuscell = 5
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 18:
            print("Avernus. Cell 18. West, South.")
            monster = random.choice(["Demon", "Ash Hound"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move west":
                avernuscell = 17
            elif userinput == "move south":
                avernuscell = 6
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 19:
            print("Avernus. Cell 19. South, East.")
            monster = random.choice(["Imp", "Magma Fiend"])
            userinput = input("Avernus>")
            encounter()
            if userinput == "move south":
                avernuscell = 15
            elif userinput == "move east":
                avernuscell = 11
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif avernuscell == 20:
            print("Avernus. Cell 20. West.")
            monster = random.choice(["Flame Spirit", "Hell Bat"])
            userinput = input("Avernus>")
            if userinput == "move west":
                avernuscell = 10
            elif userinput == "move east":
                bank = "dungeon5"
                dungeon5cell = 1
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

    # Pharaoh's Tomb

    elif bank == "dungeon4":
        enemylevel = round(0.9 * playerlevel)
        if dungeon4cell == 1:
            print("Pharaoh's Tomb. Cell 1. East. A staircase leads up to a dark sky.")
            monster = random.choice(["Mummy", "Husk"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move east":
                dungeon4cell = 2
            elif userinput == "leave":
                bank = "graveyard1"
                gravecell = 16
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon4cell == 2:
            print("Pharaoh's Tomb. Cell 2. West, East.")
            monster = random.choice(["Mummy", "Sand Serpent", "Husk"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 1
            elif userinput == "move east":
                dungeon4cell = 3
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
            
        elif dungeon4cell == 3:
            print("Pharaoh's Tomb. Cell 3. West, East, North, South.")
            monster = random.choice(["Scarab Swarm", "Mummy", "Husk"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 2
            elif userinput == "move east":
                dungeon4cell = 6
            elif userinput == "move north":
                dungeon4cell = 4
            elif userinput == "move south":
                dungeon4cell = 5
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 4:
            print("Pharaoh's Tomb. Cell 4. South.")
            monster = random.choice(["Anubian Shade", "Dust Wraith"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move south":
                dungeon4cell = 3
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 5:
            print("Pharaoh's Tomb. Cell 5. North.")
            monster = random.choice(["Mummy Priest", "Husk"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move north":
                dungeon4cell = 3
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 6:
            print("Pharaoh's Tomb. Cell 6. West, East.")
            monster = random.choice(["Sand Golem", "Scarab Swarm"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 3
            elif userinput == "move east":
                dungeon4cell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 7:
            print("Pharaoh's Tomb. Cell 7. West, East.")
            monster = random.choice(["Cursed Spirit", "Scarab Swarm"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 6
            elif userinput == "move east":
                dungeon4cell = 8
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 8:
            print("Pharaoh's Tomb. Cell 8. West, South.")
            monster = random.choice(["Mirror Shade", "Husk"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 7
            elif userinput == "move south":
                dungeon4cell = 9
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 9:
            print("Pharaoh's Tomb. Cell 9. North, East.")
            monster = random.choice(["Husk", "Sand Serpent"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move north":
                dungeon4cell = 8
            elif userinput == "move east":
                dungeon4cell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 10:
            print("Pharaoh's Tomb. Cell 10. West, North.")
            monster = random.choice(["Glyph Wraith", "Mummy Priest"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 9
            elif userinput == "move north":
                dungeon4cell = 11
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 11:
            print("Pharaoh's Tomb. Cell 11. South, East.")
            monster = random.choice(["Cultist of Ra", "Dust Wraith"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move south":
                dungeon4cell = 10
            elif userinput == "move east":
                dungeon4cell = 12
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 12:
            print("Pharaoh's Tomb. Cell 12. West, East.")
            monster = random.choice(["Mummy", "Mask Horror"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 11
            elif userinput == "move east":
                dungeon4cell = 13
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 13:
            print("Pharaoh's Tomb. Cell 13. West, East.")
            monster = random.choice(["Scarab Swarm", "Sand Serpent"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 12
            elif userinput == "move east":
                dungeon4cell = 14
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 14:
            print("Pharaoh's Tomb. Cell 14. West, South.")
            monster = random.choice(["Husk", "Priest of Set"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 13
            elif userinput == "move south":
                dungeon4cell = 16
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 15:
            print("Pharaoh's Tomb. Cell 15. East.")
            monster = random.choice(["Sand Golem", "Cursed Spirit"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move east":
                dungeon4cell = 16
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 16:
            print("Pharaoh's Tomb. Cell 16. West, South, North.")
            monster = random.choice(["Mummy Lord", "Pharaoh Shade"])
            userinput = input("Tomb>")
            encounter()
            if userinput == "move west":
                dungeon4cell = 15
            elif userinput == "move south":
                dungeon4cell = 17
            elif userinput == "move north":
                dungeon4cell = 14
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
        
        elif dungeon4cell == 17:
            print("Pharaoh's Tomb. Cell 17. North.")
            userinput = input("Tomb>")
            encounter()
            if boss4flag == True:
                print("A strange presence fills the air.")
                time.sleep(1)
                print("Dust starts to float.")
                time.sleep(1)
                print("A sarchopagus starts to open.")
                time.sleep(1)
                print("A hand reaches out.")
                time.sleep(2)
                print("It's Sebek, the forgotten Pharaoh!")
                time.sleep(0.5)
                print("Sebek attacks!")
                sebek_boss_encounter()
            else:
                if userinput == "move north":
                    dungeon4cell = 16
                elif userinput == "help":
                    help()
                elif userinput == "heal":
                    heal()
                elif userinput == "map":
                    map()
                elif userinput == "wait":
                    print("You waited.")
                    encounter()
                elif userinput == "stats":
                    stat()
                elif userinput == "switch spell":
                    switch_spell()
                else:
                    print("Invalid Command!")

    # Highlands

    elif bank == "highlands":
        enemylevel = round(0.8 * playerlevel)
        if mountaincell == 1:
            print("Dwarves' Highlands. Cell 1. East, West. The wind at this height is cold but serene.")
            monster = random.choice(["Green Dragon", "Red Dragon"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move east":
                bank = "peatbogs"
                peatbogscell = 9
            elif userinput == "move west":
                mountaincell = 2
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 2:
            print("Dwarves' Highlands. Cell 2. North, East.")
            monster = random.choice(["Dwarf Soldier", "Orc Marauder"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move north":
                mountaincell = 3
            elif userinput == "move east":
                mountaincell = 1
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 3:
            print("Dwarves' Highlands. Cell 3. South, North.")
            monster = random.choice(["Orc Raider", "Cave Spider"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move south":
                mountaincell = 2
            elif userinput == "move north":
                mountaincell = 4
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 4:
            print("Dwarves' Highlands. Cell 4. South, East, North.")
            monster = random.choice(["Orc Raider", "Frost Goblin"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move south":
                mountaincell = 3
            elif userinput == "move east":
                mountaincell = 5
            elif userinput == "move north":
                mountaincell = 6
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 5:
            print("Dwarves' Highlands. Cell 5. West, North.")
            monster = random.choice(["Dwarf Soldier", "Frost Goblin"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 4
            elif userinput == "move north":
                mountaincell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 6:
            print("Dwarves' Highlands. Cell 6. South, East.")
            monster = random.choice(["Snow Wolf", "Frost Goblin"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move south":
                mountaincell = 5
            elif userinput == "move east":
                mountaincell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 7:
            print("Dwarves' Highlands. Cell 7. West, East, North, South.")
            monster = random.choice(["Snow Wolf", "Wyvern Whelp"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 6
            elif userinput == "move east":
                mountaincell = 8
            elif userinput == "move north":
                mountaincell = 9
            elif userinput == "move south":
                mountaincell = 5
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 8:
            print("Dwarves' Highlands. Cell 8. West, North.")
            monster = random.choice(["Wyvern Whelp", "Frost Troll"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 7
            elif userinput == "move north":
                mountaincell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 9:
            print("Dwarves' Highlands. Cell 9. North, East, South.")
            monster = random.choice(["Wyvern", "Frost Troll"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move north":
                mountaincell = 19
            elif userinput == "move east":
                mountaincell = 10
            elif userinput == "move south":
                mountaincell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 10:
            print("Dwarves' Highlands. Cell 10. West, East, North, South.")
            monster = random.choice(["Wyvern", "Frost Drake"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 9
            elif userinput == "move east":
                mountaincell = 11
            elif userinput == "move north":
                mountaincell = 20
            elif userinput == "move south":
                mountaincell = 8
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 11:
            print("Dwarves' Highlands. Cell 11. West, East.")
            monster = random.choice(["Frost Drake", "Young Dragon"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 10
            elif userinput == "move east":
                mountaincell = 12
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 12:
            print("Dwarves' Highlands. Cell 12. West.")
            monster = random.choice(["Young Dragon", "Frost Drake"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 11
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 13:
            print("Dwarves' Highlands. Cell 13. East, North.")
            monster = random.choice(["Mountain Goat", "Cave Troll"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move east":
                mountaincell = 14
            elif userinput == "move north":
                mountaincell = 15
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 14:
            print("Dwarves' Highlands. Cell 14. West, North.")
            monster = random.choice(["Cave Troll", "Frost Troll"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 13
            elif userinput == "move north":
                mountaincell = 16
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 15:
            print("Dwarves' Highlands. Cell 15. South, East, West. Somehow, there is a bonfire here.")
            monster = random.choice(["Cave Troll", "Frost Drake"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move south":
                mountaincell = 13
            elif userinput == "move east":
                mountaincell = 16
            elif userinput == "move west":
                bank = "village3"
                village3cell = 1
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "rest":
                savedata()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 16:
            print("Dwarves' Highlands. Cell 16. West, East, South.")
            monster = random.choice(["Frost Drake", "Wyvern"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 15
            elif userinput == "move east":
                mountaincell = 17
            elif userinput == "move south":
                mountaincell = 14
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 17:
            print("Dwarves' Highlands. Cell 17. West, East, North.")
            monster = random.choice(["Wyvern", "Frost Drake"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 16
            elif userinput == "move east":
                mountaincell = 18
            elif userinput == "move north":
                mountaincell = 21
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 18:
            print("Dwarves' Highlands. Cell 18. West, East, North.")
            monster = random.choice(["Frost Drake", "Young Dragon"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 17
            elif userinput == "move east":
                mountaincell = 19
            elif userinput == "move north":
                mountaincell = 22
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 19:
            print("Dwarves' Highlands. Cell 19. West, East, South.")
            monster = random.choice(["Young Dragon", "Ancient Wyvern"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 18
            elif userinput == "move east":
                mountaincell = 20
            elif userinput == "move south":
                mountaincell = 9
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 20:
            print("Dwarves' Highlands. Cell 20. West, South.")
            monster = random.choice(["Ancient Wyvern", "Elder Dragon"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 19
            elif userinput == "move south":
                mountaincell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 21:
            print("Dwarves' Highlands. Cell 21. South, East, North.")
            monster = random.choice(["Elder Dragon", "Frost Hydra"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move south":
                mountaincell = 17
            elif userinput == "move east":
                mountaincell = 22
            elif userinput == "move north":
                mountaincell = 23
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 22:
            print("Dwarves' Highlands. Cell 22. West, South.")
            monster = random.choice(["Frost Hydra", "Dracolich"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move west":
                mountaincell = 21
            elif userinput == "move south":
                mountaincell = 18
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif mountaincell == 23:
            print("Dwarves' Highlands. Cell 23. South, West.")
            monster = random.choice(["Dracolich", "Ancient Dragon"])
            userinput = input("Highlands>")
            encounter()
            if userinput == "move south":
                mountaincell = 21
            elif userinput == "move west":
                mountaincell = 24
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

    # Cursed Marsh

    elif bank == "cursedmarsh":
        if marshcell == 1:
            print("Cursed Marsh. Cell 1. North, South.")
            monster = random.choice(["Poltergeist", "Treant"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move north":
                bank = "peatbogs"
                peatbogscell = 25
            elif userinput == "move south":
                marshcell = 3
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 2:
            print("Cursed Marsh. Cell 2. East, South.")
            monster = random.choice(["Poltergeist", "Treant"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 3
            elif userinput == "move south":
                marshcell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 3:
            print("Cursed Marsh. Cell 3. East, West, North, South.")
            monster = random.choice(["Leechling", "Vine Beast", "Marsh Frog"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 4
            elif userinput == "move west":
                marshcell = 2
            elif userinput == "move north":
                marshcell = 1
            elif userinput == "move south":
                marshcell = 8
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 4:
            print("Cursed Marsh. Cell 4. East, West, South.")
            monster = random.choice(["Marsh Frog", "Mire Serpent", "Vine Beast"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 5
            elif userinput == "move west":
                marshcell = 3
            elif userinput == "move south":
                marshcell = 9
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 5:
            print("Cursed Marsh. Cell 5. West, South.")
            monster = random.choice(["Swamp Wolf", "Leechling", "Mire Serpent"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move west":
                marshcell = 4
            elif userinput == "move south":
                marshcell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 6:
            print("Cursed Marsh. Cell 6. East, South.")
            monster = random.choice(["Mire Serpent", "Swamp Wolf", "Treant"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 7
            elif userinput == "move south":
                marshcell = 14
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 7:
            print("Cursed Marsh. Cell 7. East, West, North, South.")
            monster = random.choice(["Treant", "Bog Mummy", "Leechling"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 8
            elif userinput == "move west":
                marshcell = 6
            elif userinput == "move north":
                marshcell = 2
            elif userinput == "move south":
                marshcell = 15
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 8:
            print("Cursed Marsh. Cell 8. East, West, North, South.")
            monster = random.choice(["Marsh Wraith", "Bog Mummy", "Poltergeist"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 9
            elif userinput == "move west":
                marshcell = 7
            elif userinput == "move north":
                marshcell = 3
            elif userinput == "move south":
                marshcell = 16
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 9:
            print("Cursed Marsh. Cell 9. East, West, North, South.")
            monster = random.choice(["Treant", "Cursed Knight", "Poltergeist"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 10
            elif userinput == "move west":
                marshcell = 8
            elif userinput == "move north":
                marshcell = 4
            elif userinput == "move south":
                marshcell = 17
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 10:
            print("Cursed Marsh. Cell 10. East, West, North, South.")
            monster = random.choice(["Marsh Wraith", "Banshee", "Bog Mummy"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 11
            elif userinput == "move west":
                marshcell = 9
            elif userinput == "move north":
                marshcell = 5
            elif userinput == "move south":
                marshcell = 18
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 11:
            print("Cursed Marsh. Cell 11. East, West.")
            monster = random.choice(["Cursed Knight", "Putrid Slime", "Banshee"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 12
            elif userinput == "move west":
                marshcell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 12:
            print("Cursed Marsh. Cell 12. West, South.")
            monster = random.choice(["Drowned Priest", "Putrid Slime", "Marsh Wraith"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move west":
                marshcell = 11
            elif userinput == "move south":
                marshcell = 19
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 13:
            print("Cursed Marsh. Cell 13. East.")
            monster = random.choice(["Poltergeist", "Treant", "Bog Mummy"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 14
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 14:
            print("Cursed Marsh. Cell 14. East, West, North.")
            monster = random.choice(["Bog Mummy", "Mirefang Serpent", "Poltergeist"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 15
            elif userinput == "move west":
                marshcell = 13
            elif userinput == "move north":
                marshcell = 6
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 15:
            print("Cursed Marsh. Cell 15. East, West, North, South.")
            monster = random.choice(["Banshee", "Treant", "Putrid Slime"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 16
            elif userinput == "move west":
                marshcell = 14
            elif userinput == "move north":
                marshcell = 7
            elif userinput == "move south":
                marshcell = 20
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 16:
            print("Cursed Marsh. Cell 16. East, West, North, South.")
            monster = random.choice(["Mirefang Serpent", "Poltergeist", "Cursed Knight"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 17
            elif userinput == "move west":
                marshcell = 15
            elif userinput == "move north":
                marshcell = 8
            elif userinput == "move south":
                marshcell = 21
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 17:
            print("Cursed Marsh. Cell 17. East, West, North.")
            monster = random.choice(["Marsh Wraith", "Banshee", "Bog Mummy"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 18
            elif userinput == "move west":
                marshcell = 16
            elif userinput == "move north":
                marshcell = 9
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 18:
            print("Cursed Marsh. Cell 18. West, North.")
            monster = random.choice(["Putrid Slime", "Marsh Wraith", "Treant"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move west":
                marshcell = 17
            elif userinput == "move north":
                marshcell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 19:
            print("Cursed Marsh. Cell 19. North.")
            monster = random.choice(["Cursed Knight", "Drowned Priest", "Bog Mummy"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move north":
                marshcell = 12
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 20:
            print("Cursed Marsh. Cell 20. East, North.")
            monster = random.choice(["Putrid Slime", "Treant", "Poltergeist"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move east":
                marshcell = 21
            elif userinput == "move north":
                marshcell = 15
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 21:
            print("Cursed Marsh. Cell 21. South, West, North.")
            monster = random.choice(["Banshee", "Marsh Wraith", "Cursed Knight"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move south":
                marshcell = 22
            elif userinput == "move west":
                marshcell = 20
            elif userinput == "move north":
                marshcell = 16
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif marshcell == 22:
            print("Cursed Marsh. Cell 22. West, North.")
            monster = random.choice(["Drowned Priest", "Treant", "Mirefang Serpent"])
            userinput = input("Cursed Marsh>")
            encounter()
            if userinput == "move north":
                marshcell = 21
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
                encounter()
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

    # Dwarf Village

    elif bank == "village3":
        if village3cell == 1:
            print("Dwarves' Highlands. Cell 1. East, West.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                bank = "highlands"
                mountaincell = 15
            elif userinput == "move west":
                village3cell = 2
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 2

        elif village3cell == 2:
            print("Dwarves' Highlands. Cell 2. East, West, South, North.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 1
            elif userinput == "move west":
                village3cell = 3
            elif userinput == "move south":
                village3cell = 5
            elif userinput == "move north":
                village3cell = 6
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 3

        elif village3cell == 3:
            print("Dwarves' Highlands. Cell 3. East, West, North.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 2
            elif userinput == "move west":
                village3cell = 4
            elif userinput == "move north":
                village3cell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 4

        elif village3cell == 4:
            print("Dwarves' Highlands. Cell 4. East, North, West. A merchant dwarf sits near you. (merchant)")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 3
            elif userinput == "move north":
                village3cell = 8
            elif userinput == "move west":
                village3cell = 14
            elif userinput == "talk merchant":
                print("Merchant: Hi there!")
                time.sleep(1)
                print("Merchant: I have spells you can buy!")
                time.sleep(1)
                print("Merchant: Come here, come here!")
                time.sleep(1)
                print("Merchant: I have six spells you can buy.")
                time.sleep(1)
                print("Merchant: Would you like to buy?")
                time.sleep(1)
                print("Buy?\nyes\nno")
                while True:
                    userinput = input("Choice?>")
                    if userinput == "yes":
                        print("Merchant: What would you like to buy?")
                        print("List of spells available:\nTimestop\nEntrance\nIcebeam\n---Wizard Only---\nThunder\nNecromancy\nTorrent")
                        userinput = input("Choice?>")
                        if userinput in ["timestop", "entrance", "icebeam", "thunder", "necromancy", "torrent"]:
                            if gold >= 600:
                                print("Thanks for buying!")
                                gold -= 600
                                if userinput == "timestop":
                                    spellslot10 = True
                                elif userinput == "entrance":
                                    spellslot6 = True
                                elif userinput == "icebeam":
                                    spellslot7 = True
                                elif userinput == "thunder":
                                    spellslot11 = True
                                elif userinput == "necromancy":
                                    spellslot13 = True
                                elif userinput == "torrent":
                                    spellslot14 = True
                                break
                            else:
                                print("You don't have enough money!")
                                break
                    else:
                        print("Merchant: Well, until next time then!")
                        break
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 5

        elif village3cell == 5:
            print("Dwarves' Highlands. Cell 5. North.")
            userinput = input("Highland Village>")
            if userinput == "move north":
                village3cell = 2
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 6

        elif village3cell == 6:
            print("Dwarves' Highlands. Cell 6. South, West, North.")
            userinput = input("Highland Village>")
            if userinput == "move south":
                village3cell = 2
            elif userinput == "move west":
                village3cell = 7
            elif userinput == "move north":
                village3cell = 9
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 7

        elif village3cell == 7:
            print("Dwarves' Highlands. Cell 7. East, West, North, South. A girl named Tam stands across of you.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 6
            elif userinput == "move west":
                village3cell = 8
            elif userinput == "move north":
                village3cell = 10
            elif userinput == "move south":
                village3cell = 3
            elif userinput == "talk tam":
                print("Tam: Oh, hi! How are you doing today?")
                time.sleep(1)
                if playergold < 500:
                    print("Tam: Oh, I see you're kinda poor. Here, let me help!")
                    gold += 750
                    print("Tam: Here, have 750 gold!")
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 8

        elif village3cell == 8:
            print("Dwarves' Highlands. Cell 8. East, West, North, South.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 7
            elif userinput == "move west":
                village3cell = 13
            elif userinput == "move north":
                village3cell = 11
            elif userinput == "move south":
                village3cell = 4
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 9

        elif village3cell == 9:
            print("Dwarves' Highlands. Cell 9. West, South.")
            userinput = input("Highland Village>")
            if userinput == "move west":
                village3cell = 10
            elif userinput == "move south":
                village3cell = 6
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 10

        elif village3cell == 10:
            print("Dwarves' Highlands. Cell 10. East, West, North, South.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 9
            elif userinput == "move west":
                village3cell = 11
            elif userinput == "move north":
                village3cell = 12
            elif userinput == "move south":
                village3cell = 7
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 11

        elif village3cell == 11:
            print("Dwarves' Highlands. Cell 11. East, South.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 10
            elif userinput == "move south":
                village3cell = 8
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 12

        elif village3cell == 12:
            print("Dwarves' Highlands. Cell 12. South.")
            userinput = input("Highland Village>")
            if userinput == "move south":
                village3cell = 10
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 13

        elif village3cell == 13:
            print("Dwarves' Highlands. Cell 13. East, South. A wizard named Gandalf sits on a tree stump.")
            userinput = input("Highland Village>")
            if userinput == "move east":
                village3cell = 8
            elif userinput == "move south":
                village3cell = 14
            elif userinput == "talk gandalf":
                print("Hello. Have a spell.")
                spellslot12 = True
                print("Now fly, fool.")
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        # Cell 14

        elif village3cell == 14:
            print("Dwarves' Highlands. Cell 14. North, East.")
            userinput = input("Highland Village>")
            if userinput == "move north":
                village3cell = 13
            elif userinput == "move east":
                village3cell = 4
            elif userinput == "help":
                help()
            elif userinput == "heal":
                heal()
            elif userinput == "map":
                map()
            elif userinput == "wait":
                print("You waited.")
            elif userinput == "stats":
                stat()
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

    # Graveyard 2

    elif bank == "graveyard2":
        enemylevel = round(playerlevel * 0.70)
        if grave2cell == 1:
            monster = random.choice(["Zombie", "Goblin", "Poltergeist", "Spider"])
            encounter()
            print("Graveyard. Cell 1. East, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move north":
                grave2cell = 4
            elif userinput == "move east":
                grave2cell = 2
            elif userinput == "move south":
                bank = "village3"
                village3cell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 2:
            monster = random.choice(["Zombie", "Skeleton", "Bat", "Spider"])
            encounter()
            print("Graveyard. Cell 2. East, West, North.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 3
            elif userinput == "move west":
                grave2cell = 1
            elif userinput == "move north":
                grave2cell = 5
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 3:
            monster = random.choice(["Ghoul", "Vampire Bat", "Skeleton"])
            encounter()
            print("Graveyard. Cell 3. West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                grave2cell = 2
            elif userinput == "move north":
                grave2cell = 6
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 4:
            monster = random.choice(["Zombie", "Ghoul", "Bat"])
            encounter()
            print("Graveyard. Cell 4. East, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 5
            elif userinput == "move south":
                grave2cell = 1
            elif userinput == "move north":
                grave2cell = 7
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 5:
            monster = random.choice(["Skeleton", "Cursed Knight", "Wraith"])
            encounter()
            print("Graveyard. Cell 5. East, West, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 6
            elif userinput == "move west":
                grave2cell = 4
            elif userinput == "move south":
                grave2cell = 2
            elif userinput == "move north":
                grave2cell = 8
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 6:
            monster = random.choice(["Wraith", "Poltergeist", "Bat"])
            encounter()
            print("Graveyard. Cell 6. West, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                grave2cell = 5
            elif userinput == "move south":
                grave2cell = 3
            elif userinput == "move north":
                grave2cell = 9
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 7:
            monster = random.choice(["Zombie", "Wraith", "Grave Rat"])
            encounter()
            print("Graveyard. Cell 7. East, South.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 8
            elif userinput == "move south":
                grave2cell = 4
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 8:
            monster = random.choice(["Skeleton", "Vampire Bat", "Grave Rat"])
            encounter()
            print("Graveyard. Cell 8. East, West, South.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 9
            elif userinput == "move west":
                grave2cell = 7
            elif userinput == "move south":
                grave2cell = 5
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 9:
            monster = random.choice(["Cursed Knight", "Wraith", "Poltergeist"])
            encounter()
            print("Graveyard. Cell 9. East, West, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 10
            elif userinput == "move west":
                grave2cell = 8
            elif userinput == "move south":
                grave2cell = 6
            elif userinput == "move north":
                grave2cell = 11
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 10:
            monster = random.choice(["Vampire Bat", "Skeleton", "Cursed Knight"])
            encounter()
            print("Graveyard. Cell 10. West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                grave2cell = 9
            elif userinput == "move north":
                grave2cell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 11:
            monster = random.choice(["Skeleton", "Zombie", "Cursed Knight"])
            encounter()
            print("Graveyard. Cell 11. East, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 12
            elif userinput == "move south":
                grave2cell = 9
            elif userinput == "move north":
                grave2cell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 12:
            monster = random.choice(["Ghoul", "Poltergeist", "Bat"])
            encounter()
            print("Graveyard. Cell 12. East, West, South, North.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 13
            elif userinput == "move west":
                grave2cell = 11
            elif userinput == "move south":
                grave2cell = 10
            elif userinput == "move north":
                grave2cell = 16
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 13:
            monster = random.choice(["Poltergeist", "Cursed Knight", "Bat"])
            encounter()
            print("Graveyard. Cell 13. West, North.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                grave2cell = 12
            elif userinput == "move north":
                bank = "forest2"
                forest2cell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 14:
            monster = random.choice(["Skeleton", "Wraith", "Vampire Bat"])
            encounter()
            print("Graveyard. Cell 14. East.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 15:
            monster = random.choice(["Cursed Knight", "Wraith", "Poltergeist"])
            encounter()
            print("Graveyard. Cell 15. East, West, South.")
            userinput = input("Graveyard>")
            if userinput == "move east":
                grave2cell = 16
            elif userinput == "move west":
                grave2cell = 14
            elif userinput == "move south":
                grave2cell = 11
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif grave2cell == 16:
            monster = random.choice(["Cursed Knight", "Lich", "Vampire Bat"])
            encounter()
            print("Graveyard. Cell 16. West, South.")
            userinput = input("Graveyard>")
            if userinput == "move west":
                grave2cell = 15
            elif userinput == "move south":
                grave2cell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

    # Lolth's Lair

    elif bank == "dungeon5":
        enemylevel = round(1.2 * playerlevel)
        if dungeon5cell == 1:
            print("Lolth's Lair. Cell 1. East, West.")
            monster = random.choice(["Demon", "Imp"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 2
            elif userinput == "move west":
                bank = "dungeon3"
                avernuscell = 20
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 2:
            print("Lolth's Lair. Cell 2. East, West.")
            monster = random.choice(["Abyssal Spider", "Webspawn Imp", "Demon"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 3
            elif userinput == "move west":
                dungeon5cell = 1
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 3:
            print("Lolth's Lair. Cell 3. East, West.")
            monster = random.choice(["Drider", "Abyssal Spider", "Cave Demon"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 4
            elif userinput == "move west":
                dungeon5cell = 2
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 4:
            print("Lolth's Lair. Cell 4. East, West, North, South.")
            monster = random.choice(["Drider", "Imp", "Shadowling"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 5
            elif userinput == "move west":
                dungeon5cell = 3
            elif userinput == "move north":
                dungeon5cell = 18
            elif userinput == "move south":
                dungeon5cell = 9
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 5:
            print("Lolth's Lair. Cell 5. West.")
            monster = random.choice(["Dark Webspinner", "Abyssal Spider", "Cursed Acolyte"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move west":
                dungeon5cell = 4
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 6:
            print("Lolth's Lair. Cell 6. East, South.")
            monster = random.choice(["Shadowling", "Drider", "Venom Priestess"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 7
            elif userinput == "move south":
                dungeon5cell = 10
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 7:
            print("Lolth's Lair. Cell 7. West.")
            monster = random.choice(["Abyssal Spider", "Drider", "Demon"])
            userinput = input("Ship of Lolth>")
            encounter()
            if lolthflag == True:
                print("Lolth: You think you could escape so easily?")
                time.sleep(1)
                print("Lolth: Oh, mortal. That won't be the case.")
                print("Lolth attacks!")
                lolth_boss_encounter()
            else:
                if userinput == "move west":
                    dungeon5cell = 6
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
                elif userinput == "switch spell":
                    switch_spell()
                else:
                    print("Invalid Command!")

        elif dungeon5cell == 8:
            print("Lolth's Lair. Cell 8. South.")
            monster = random.choice(["Dark Webspinner", "Imp", "Venom Priestess"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move south":
                dungeon5cell = 11
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 9:
            print("Lolth's Lair. Cell 9. North, South.")
            monster = random.choice(["Shadowling", "Drider", "Abyssal Spider"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 4
            elif userinput == "move south":
                dungeon5cell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 10:
            print("Lolth's Lair. Cell 10. North, South.")
            monster = random.choice(["Venom Priestess", "Cave Demon", "Dark Webspinner"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 6
            if userinput == "move south":
                dungeon5cell = 13
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 11:
            print("Lolth's Lair. Cell 11. North, East.")
            monster = random.choice(["Imp", "Cursed Acolyte", "Venom Priestess"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 8
            elif userinput == "move east":
                dungeon5cell = 12
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 12:
            print("Lolth's Lair. Cell 12. East, West.")
            monster = random.choice(["Abyssal Spider", "Drider", "Shadowling"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 15
            elif userinput == "move west":
                dungeon5cell = 11
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 13:
            print("Lolth's Lair. Cell 13. West, North.")
            monster = random.choice(["Drider", "Dark Webspinner", "Venom Priestess"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move west":
                dungeon5cell = 14
            elif userinput == "move north":
                dungeon5cell = 10
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 14:
            print("Lolth's Lair. Cell 14. East, West.")
            monster = random.choice(["Cursed Acolyte", "Demon", "Shadowling"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 13
            elif userinput == "move west":
                dungeon5cell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 15:
            print("Lolth's Lair. Cell 15. East, West, North, South.")
            monster = random.choice(["Venom Priestess", "Dark Webspinner", "Drider"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 14
            elif userinput == "move west":
                dungeon5cell = 12
            elif userinput == "move north":
                dungeon5cell = 9
            elif userinput == "move south":
                dungeon5cell = 16
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 16:
            print("Lolth's Lair. Cell 16. North.")
            monster = random.choice(["Abyssal Spider", "Shadowling", "Venom Priestess"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 15
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 17:
            print("Lolth's Lair. Cell 17. North.")
            monster = random.choice(["Dark Webspinner", "Drider", "Imp"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 20
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 18:
            print("Lolth's Lair. Cell 18. North, South.")
            monster = random.choice(["Venom Priestess", "Drider", "Shadowling"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 22
            elif userinput == "move south":
                dungeon5cell = 4
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 19:
            print("Lolth's Lair. Cell 19. North.")
            monster = random.choice(["Drider", "Abyssal Spider", "Cursed Acolyte"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move north":
                dungeon5cell = 24
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 20:
            print("Lolth's Lair. Cell 20. East, North.")
            monster = random.choice(["Venom Priestess", "Webspawn Imp", "Abyssal Spider"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 21
            elif userinput == "move south":
                dungeon5cell = 17
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 21:
            print("Lolth's Lair. Cell 21. East, West.")
            monster = random.choice(["Drider", "Shadowling", "Dark Webspinner"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 22
            elif userinput == "move west":
                dungeon5cell = 20
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 22:
            print("Lolth's Lair. Cell 22. East, West, North, South.")
            monster = random.choice(["Venom Priestess", "Cursed Acolyte", "Drider"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 23
            elif userinput == "move west":
                dungeon5cell = 21
            elif userinput == "move north":
                dungeon5cell = 25
            elif userinput == "move south":
                dungeon5cell = 18
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 23:
            print("Lolth's Lair. Cell 23. East, West.")
            monster = random.choice(["Abyssal Spider", "Dark Webspinner", "Cave Demon"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move east":
                dungeon5cell = 24
            elif userinput == "move west":
                dungeon5cell = 22
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 24:
            print("Lolth's Lair. Cell 24. South, West.")
            monster = random.choice(["Venom Priestess", "Drider", "Cursed Acolyte"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move south":
                dungeon5cell = 19
            elif userinput == "move west":
                dungeon5cell = 23
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")

        elif dungeon5cell == 25:
            print("Lolth's Lair. Cell 25. South.")
            monster = random.choice(["Abyssal Queen", "Drider Matriarch", "Venom Priestess"])
            userinput = input("Ship of Lolth>")
            encounter()
            if userinput == "move south":
                dungeon5cell = 24
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
            elif userinput == "switch spell":
                switch_spell()
            else:
                print("Invalid Command!")
