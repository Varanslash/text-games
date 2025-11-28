import random

while True: # main loop
    pets = ["Fish", "Hamster", "Guinea Pig", "Rabbit", "Turtle", "Lizard", "Cat", "Dog", "Bird", "Ferret", "Hedgehog", "Fox", "Wolf", "Tiger", "\x1b[35mVaran", "\x1b[34mPoltergeist\x1b[0m", "\x1b[32mHedgelord\x1b[0m", "\x1b[31mDragon\x1b[0m", "\x1b[33mAny Radiance\x1b[0m"]
    happiness = 50
    current_pet = random.choice(pets)
    hunger = (2 * pets.index(current_pet)) + random.randint(1,10)
    money = 100
    food_stock = 20
    moves = 0
    weird_game_variable = True

    print("You have adopted a", current_pet + "!")
    print("What would you like to do? (feed/play/status/exit/help/work/buy/doomscroll)")

    while hunger <= 100 and hunger > -25 and happiness > 0 and weird_game_variable == True:
        moves += 1
        print("Moves:", moves)
        action = input("\x1b[36m>> \x1b[0m")
        if action == "feed":
            food_amount = int(input("\x1b[36mHow much food would you like to give your pet? (1-20)>> \x1b[0m"))
            if food_stock >= food_amount:
                hunger -= food_amount
                happiness += food_amount // 2
                food_stock -= food_amount
                print("You fed your", current_pet + ". \x1b[33mHunger\x1b[0m is now", hunger, "and \x1b[32mhappiness\x1b[0m is now", happiness + ".")
            else:
                print("You don't have enough food.")
        elif action == "play":
            play_time = int(input("\x1b[36mHow long would you like to play with your pet? (1-20)>> \x1b[0m"))
            happiness += play_time
            hunger += play_time // 2
            print("You played with your", current_pet + ". \x1b[32mHappiness\x1b[0m is now", happiness, "and \x1b[33mhunger\x1b[0m is now", hunger + ".")
        elif action == "status":
            print("Your", current_pet, "has a \x1b[33mhunger\x1b[0m level of", hunger, "and a \x1b[32mhappiness\x1b[0m level of", happiness + ".")
        elif action == "help":
            print("Available actions: feed, play, status, exit")
        elif action == "work":
            work_time = int(input("\x1b[36mHow long would you like to work? (1-20)>> \x1b[0m"))
            earned_money = work_time * 5
            money += earned_money
            print("\x1b[33mYou worked for\x1b[0m", work_time, "\x1b[33mhours and earned\x1b[0m", earned_money, "\x1b[32mmoney\x1b[0m. You now have", money, "\x1b[32mmoney\x1b[0m.")
            happiness -= work_time // 2
            hunger += work_time // 2
        elif action == "buy":
            food_to_buy = int(input("\x1b[36mHow much food would you like to buy? (1-20)>> \x1b[0m"))
            cost = food_to_buy * 2
            if money >= cost:
                food_stock += food_to_buy
                money -= cost
                print("\x1b[33mYou bought\x1b[0m", food_to_buy, "\x1b[33mfood. You now have\x1b[0m", food_stock, "\x1b[33mfood and\x1b[0m", money, "\x1b[32mmoney.\x1b[0m")
            else:
                print("You don't have enough money to buy that much food.")
        elif action == "doomscroll":
            print("You spent time doomscrolling on your phone. Happiness decreased.")
            happiness -= 10
            hunger += 10
            weirdcheck = random.randint(1,10)
            if weirdcheck == 1:
                weird_game_variable = False
        elif action == "stats":
            print("\x1b[32mMoney:\x1b[0m", money, "\n", "\x1b[33mFood Stock:\x1b[0m", food_stock)
        else:
            print("Invalid action. Please choose feed, play, status, exit, help, work, buy, or doomscroll.")
    if hunger >= 100:
        print("Your", current_pet, "has overeaten and passed away. Game over.")
    elif hunger <= -25:
        print("Your", current_pet, "has starved and passed away. Game over.")
    elif happiness <= 0:
        print("Your", current_pet, "has become too sad and ran away. Game over.")
    elif weird_game_variable == False:
        print("How did you even get here? Game over. You lost with -75843789258943092185934281905803428109581342 food and 29 SWAT officers at your door searching for every Gameboy in your house.")