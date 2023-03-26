import random

# Define player attributes
player = {
    "name": "",
    "health": 100,
    "attack": 10,
    "defense": 5,
    "gold": 0,
    "area": "Village"
}

# Define enemy attributes
goblin = {
    "name": "Goblin",
    "health": 30,
    "attack": 5,
    "defense": 2,
    "gold": 10
}

troll = {
    "name": "Troll",
    "health": 50,
    "attack": 10,
    "defense": 5,
    "gold": 20
}

# Define areas and their properties
areas = {
    "Village": {
        "description": "You are in a small village with a few shops and houses.",
        "enemies": [],
        "exits": ["Forest"]
    },
    "Forest": {
        "description": "You are in a dense forest with tall trees and thick underbrush.",
        "enemies": [goblin],
        "exits": ["Village", "Cave"]
    },
    "Cave": {
        "description": "You are in a dark cave with jagged walls and a damp floor.",
        "enemies": [troll],
        "exits": ["Forest"]
    }
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
    # Print the current area's description
    print(f"\n{player['name']}, you have {player['health']} health and {player['gold']} gold.")
    print(areas[player['area']]["description"])
    print("What would you like to do?")
    # Print the available exits for the current area
    for exit in areas[player['area']]["exits"]:
        print(f"{exit}")
    # Print the available actions for the current area
    print("1. Fight enemies")
    print("2. Quit")
    choice = get_input(["1", "2"] + areas[player['area']]["exits"])
    if choice == "1":
        # Start combat with a random enemy in the current area
        if areas[player['area']]["enemies"]:
            enemy = random.choice(areas[player['area']]["enemies"])
            if combat(player, enemy):
                # Player won the battle, heal
