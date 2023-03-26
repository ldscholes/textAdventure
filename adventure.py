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

dragon = {
    "name": "Dragon",
    "health": 100,
    "attack": 20,
    "defense": 10,
    "gold": 50
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
        "exits": ["Forest", "Dungeon"]
    },
    "Dungeon": {
        "description": "You are in a massive dungeon with many twists and turns.",
        "enemies": [goblin, troll, dragon],
        "exits": ["Cave", "Castle"]
    },
    "Castle": {
        "description": "You are in the throne room of a great castle.",
        "enemies": [dragon],
        "exits": ["Dungeon"]
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
        damage = max(0, player["attack"] - enemy["defense"])
        print(f"You attack the {enemy['name']} for {damage} damage!")
        enemy["health"] -= damage
        if enemy["health"] <= 0:
            break
        # Enemy attacks
        damage = max(0, enemy["attack"] - player["defense"])
        print(f"The {enemy['name']} attacks you for {damage} damage!")
        player["health"] -= damage
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
    print(areas[player['
