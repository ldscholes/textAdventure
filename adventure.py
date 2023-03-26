import random

# Define player attributes
player = {
    "name": "",
    "health": 100,
    "attack": 10,
    "defense": 5,
    "gold": 0
}

# Define enemy attributes
goblin = {
    "name": "Goblin",
    "health": 30,
    "attack": 5,
    "defense": 2,
    "gold": 10
}

# Define game functions
def get_input(choices):
    while True:
        choice = input("> ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice.")

def combat(player, enemy):
    print(f"A wild {enemy['name']} appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        # Player attacks
        print(f"You attack the {enemy['name']} for {player['attack']} damage!")
        enemy["health"] -= player["attack"]
        if enemy["health"] <= 0:
            break
        # Enemy attacks
        print(f"The {enemy['name']} attacks you for {enemy['attack']} damage!")
        player["health"] -= enemy["attack"]
        if player["health"] <= 0:
            break
    if player["health"] > 0:
        print(f"You defeated the {enemy['name']} and earned {enemy['gold']} gold!")
        player["gold"] += enemy["gold"]
        return True
    else:
        print("You were defeated...")
        return False

# Start the game
print("Welcome to the adventure game!")
print("What is your name?")
player["name"] = input("> ")

# Main game loop
while True:
    print(f"\n{player['name']}, you have {player['health']} health and {player['gold']} gold.")
    print("What would you like to do?")
    print("1. Fight a goblin")
    print("2. Quit")
    choice = get_input(["1", "2"])
    if choice == "1":
        # Start combat with a goblin
        if combat(player, goblin):
            # Player won the battle, heal the player
            player["health"] = min(player["health"] + 10, 100)
    else:
        # Quit the game
        print("Thanks for playing!")
        break
