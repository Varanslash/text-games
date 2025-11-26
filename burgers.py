buns = ["sesame seed bun", "brioche bun", "lettuce wrap", "gluten-free bun", "pretzel bun", "whole wheat bun", "potato bun", "ciabatta bun", "keto bun", "bagel bun", "average eczema cream"]
ingredients = ["lettuce", "tomato", "onion", "pickles", "cheddar cheese", "swiss cheese", "bacon", "avocado", "mushrooms", "jalapenos", "ketchup", "mustard", "mayo", "barbecue sauce", "ranch dressing", "fried egg", "pineapple slice", "caramelized onions", "spinach", "arugula", "average eczema cream"]
drinks = ["water", "soda", "lemonade", "iced tea", "milkshake", "smoothie", "coffee", "tea", "beer", "wine", "coofee", "average eczema cream"]
desserts = ["ice cream", "cake", "brownie", "cookie", "pie", "pudding", "fruit salad", "cheesecake", "cupcake", "donut", "average eczema cream"]
summary = []

print("borgurs ingedimediants")
print("buns")
for bun in buns:
    print(f"- bun: {bun}")
print("ingredients")
for ingredient in ingredients:
    print(f"  - ingredient: {ingredient}")
print("drinks")
for drink in drinks:
    print(f"- drink: {drink}")
print("desserts")
for dessert in desserts:
    print(f"- dessert: {dessert}")

userinput = input("chooz> ")
if userinput in buns:
    print(f"You chose the bun: {userinput}")
    summary.append(f"bun: {userinput}")

for _ in range(4):
    userinput = input("ingred> ")
    if userinput in ingredients:
        print(f"You chose the ingredient: {userinput}")
        summary.append(f"ingredient: {userinput}")

userinput = input("drink> ")
if userinput in drinks:
    print(f"You chose the drink: {userinput}")
    summary.append(f"drink: {userinput}")

userinput = input("desert> ")
if userinput in desserts:
    print(f"You chose the dessert: {userinput}")
    summary.append(f"dessert: {userinput}")

print("summary:")
for item in summary:
    print(f"- {item}")