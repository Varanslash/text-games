import random

print("Russian Roulette")

print("Would you like interactive mode or rapid mode?")
mode = input("Type 'interactive' or 'rapid': ")

if mode == "interactive":
    chambers = [0, 0, 0, 0, 0, 1]
    random.shuffle(chambers)
    current_chamber = 0

    while True:
        action = input("Type 'spin' to spin the cylinder or 'pull' to pull the trigger: ")
        if action == "spin":
            random.shuffle(chambers)
            current_chamber = 0
            print("You spun the cylinder.")
        elif action == "pull":
            if chambers[current_chamber] == 1:
                print("Bang! You're dead.")
                break
            else:
                print("Click! You're safe.")
                current_chamber += 1
                if current_chamber >= len(chambers):
                    print("You've survived all chambers! You win!")
                    break
        else:
            print("Invalid action. Please type 'spin' or 'pull'.")

elif mode == "rapid":
    chambers = [0, 0, 0, 0, 0, 1]
    random.shuffle(chambers)
    for i in range(len(chambers) * 30):
        print(f"Pulling trigger for chamber {i + 1}...")
        if chambers[i] == 1:
            print("Bang! You're dead.")
            break
        else:
            print("Click! You're safe.")
    else:
        print("You've survived all chambers! You win!")