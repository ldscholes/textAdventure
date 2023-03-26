import random

# Player information
player = {
    "name": "",
    "hp": 100,
    "max_hp": 100,
    "mana": 50,
    "max_mana": 50,
    "attack": 10,
    "defense": 5,
    "gold": 0,
    "level": 1,
    "xp": 0,
    "next_level_xp": 100,
    "spells": [
        {"name": "Fireball", "damage": 20, "mana": 10},
        {"name": "Ice Bolt", "damage": 15, "mana": 5},
        {"name": "Thunder Strike", "damage": 25, "mana": 15}
    ],
    "area": "town"
}

areas = {
    "town": {
        "name": "Town",
        "description": "You are in a small town. There are some shops and people around.",
        "enemies": [],
        "shop": {
            "weapons": [
                {"name": "Sword", "attack": 10, "price": 100},
                {"name": "Axe", "attack": 12, "price": 120},
                {"name": "Mace", "attack": 15, "price": 150}
            ],
            "spells": [
                {"name": "Heal", "mana": 10, "hp": 20, "price": 100},
                {"name": "Shield", "mana": 20, "defense": 5, "price": 200},
                {"name": "Fireball", "mana": 30, "damage": 25, "price": 300}
            ]
        }
    },
    "forest": {
        "name": "Forest",
        "description": "You are in a dark forest. It's hard to see anything.",
        "enemies": [
            {"name": "Goblin", "hp": 20, "attack": 8, "defense": 2, "gold": 30},
            {"name": "Wolf", "hp": 15, "attack": 10, "defense": 3, "gold": 20}
        ],
        "shop": None
    },
    "cave": {
        "name": "Cave",
        "description": "You are in a deep cave. It's damp and eerie.",
        "enemies": [
            {"name": "Orc", "hp": 30, "attack": 12, "defense": 5, "gold": 50},
            {"name": "Troll", "hp": 40, "attack": 15, "defense": 8, "gold": 80}
        ],
        "shop": None
    }
}

def level_up(player):
    print("Level up!")
    player["level"] += 1
    player["xp"] -= player["next_level_xp"]
    player["next_level_xp"] *= 2
    player["max_hp"] += 10
    player["hp"] = player["max_hp"]
    player["max_mana"] += 5
    player["mana"] = player["max_mana"]
    player["attack"] += 5
    player["defense"] += 2
    print(f"You are now level {player['level']}!")
    print(f"You need {player['next_level_xp']} XP to reach the next level.")

# Define game functions
def get_input(choices):
    while True:
        choice = input("> ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice.")

def combat(player, enemy):
    print(f"A wild {enemy['name']} appeared!")
    while player["hp"] > 0 and enemy["hp"] > 0:
        print(f"Player HP: {player['hp']}")
        print(f"Enemy HP: {enemy['hp']}")
        print("What do you want to do?")
        print("1. Attack")
        if len(player["spells"]) > 0:
            print("2. Cast spell")
        choice = input("> ")
        if choice == "1":
            damage = player["attack"] - enemy["defense"]
            if damage < 0:
                damage = 0
            enemy["hp"] -= damage
            print(f"You dealt {damage} damage to the {enemy['name']}!")
        elif choice == "2" and len(player["spells"]) > 0:
            print("Which spell do you want to cast?")
            for i, spell in enumerate(player["spells"]):
                print(f"{i+1}. {spell['name']} ({spell['mana_cost']} mana)")
            spell_choice = int(input("> "))
            spell = player["spells"][spell_choice-1]
            if player["mana"] < spell["mana_cost"]:
                print("Not enough mana!")
                continue
            player["mana"] -= spell["mana_cost"]
            damage = spell["damage"]
            enemy["hp"] -= damage
            print(f"You cast {spell['name']} and dealt {damage} damage to the {enemy['name']}!")
        else:
            print("Invalid choice!")
            continue
        if enemy["hp"] <= 0:
            print(f"You defeated the {enemy['name']}!")
            xp_reward = enemy["defense"] * 10
            print(f"You gained {xp_reward} XP!")
            player["xp"] += xp_reward
            if player["xp"] >= player["next_level_xp"]:
                level_up(player)
            return True
        damage = enemy["attack"] - player["defense"]
        if damage < 0:
            damage = 0
        player["hp"] -= damage
        print(f"The {enemy['name']} attacked you and dealt {damage} damage!")
    if player["hp"] <= 0:
        print("You died!")
        player["gold"] = 0
        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]
        return False

# Start the game
print("Welcome to the adventure game!")
print("What is your name?")
player["name"] = input("> ")

current_area = areas["town"]

# Welcome message
print("Welcome to the text adventure game!")
print("You find yourself in a small town. You have a sword and some gold.")
print("You can explore the town, go to the forest or the cave, or visit the shop.")

# Main game loop
while True:
    print(f"\n--- {player['name']}, level {player['level']} ({player['xp']}/{player['next_level_xp']} XP) ---")
    print(f"HP: {player['hp']}/{player['max_hp']}   Mana: {player['mana']}/{player['max_mana']}   Gold: {player['gold']}")
    print(current_area["description"])

    # Display options
    print("What do you want to do?")
    print("1. Explore")
    print("2. Visit shop")
    print("3. Change area")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Explore
        if len(current_area["enemies"]) > 0:
            # Combat
            enemy = random.choice(current_area["enemies"])
            if combat(player,enemy):
                # Player wins
                print(f"You found {enemy['gold']} gold!")
                player["gold"] += enemy["gold"]
                current_area["enemies"].remove(enemy)
            else:
                # Player loses
                print("You wake up in the town with all your gold gone.")
                player["gold"] = 0
                current_area = areas["town"]
        else:
            # No enemies
            print("There's nothing here.")
    elif choice == "2":
        # Visit shop
        if current_area["shop"] is None:
            print("There's no shop here.")
        else:
            print("Welcome to the shop!")
            while True:
                print("What do you want to buy?")
                print("1. Weapons")
                print("2. Spells")
                print("3. Leave shop")
                shop_choice = input("Enter your choice: ")
                if shop_choice == "1":
                    # Weapons
                    for i, weapon in enumerate(current_area["shop"]["weapons"]):
                        print(f"{i+1}. {weapon['name']} (attack: {weapon['attack']}, price: {weapon['price']})")
                    weapon_choice = int(input("Enter your choice: "))
                    weapon = current_area["shop"]["weapons"][weapon_choice-1]
                    if player["gold"] >= weapon["price"]:
                        player["gold"] -= weapon["price"]
                        player["attack"] = weapon["attack"]
                        print(f"You bought a {weapon['name']}!")
                        print(f"Your attack is now {player['attack']}.")
                    else:
                        print("Not enough gold!")
                elif shop_choice == "2":
                    # Spells
                    for i, spell in enumerate(current_area["shop"]["spells"]):
                        print(f"{i+1}. {spell['name']} (mana: {spell['mana']}, price: {spell['price']})")
                    spell_choice = int(input("Enter your choice: "))
                    spell = current_area["shop"]["spells"][spell_choice-1]
                    if player["gold"] >= spell["price"]:
                       player["gold"] -= spell["price"]
                       player["spells"].append(spell)
                       print(f"You bought {spell['name']}!")
                       print(f"You have {len(player['spells'])} spells: ")
                       for s in player['spells']:
                          print(f"{s['name']} (mana: {s['mana']})")
                    else:
                        print("Not enough gold!")
                elif shop_choice == "3":
                    # Leave shop
                    break
                else:
                    print("Invalid choice.")
    elif choice == "3":
        # Change area
        print("Where do you want to go?")
        for i, area in enumerate(areas.values()):
            print(f"{i+1}. {area['name']}")
        area_choice = int(input("Enter your choice: "))
        current_area = list(areas.values())[area_choice-1]
    elif choice == "4":
        # Quit
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
