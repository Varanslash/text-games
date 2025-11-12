currentcell = 1

def moving(northposition, southposition, eastposition, westposition):
    global currentcell
    match userinput:
        case "move north":
            if northposition > 0:
                currentcell = northposition
            else:
                print("You can't go that way!")
        case "move south":
            if southposition > 0:
                currentcell = southposition
            else:
                print("You can't go that way!")
        case "move east":
            if eastposition > 0:
                currentcell = eastposition
            else:
                print("You can't go that way!")
        case "move west":
            if westposition > 0:
                currentcell = westposition
            else:
                print("You can't go that way!")
        case "help":
            print("List of commands:\nmove [cardinal direction]\nhelp")
        case "map":
            print("""    [2 ]
[5 ][1 ][4 ]
    [3 ]""")
        case "exit":
            print("Goodbye!")
            exit()
        case _:
            print("Invalid Command!")

while True:
    match currentcell:
        case 1:
            print("Room 1 of Yorkshire Dungeon. North, South, West, East.")
            userinput = input(">>>")
            moving(2, 3, 4, 5)
        case 2:
            print("Room 2 of Yorkshire Dungeon. South.")
            userinput = input(">>>")
            moving(0, 1, 0, 0)
        case 3:
            print("Room 3 of Yorkshire Dungeon. North.")
            userinput = input(">>>")
            moving(1, 0, 0, 0)
        case 4:
            print("Room 4 of Yorkshire Dungeon. West.")
            userinput = input(">>>")
            moving(0, 0, 0, 1)
        case 5:
            print("Room 5 of Yorkshire Dungeon. East.")
            userinput = input(">>>")
            moving(0, 0, 1, 0)