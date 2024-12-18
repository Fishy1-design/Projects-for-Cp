#Final Project


import random

# Game start
def start_game():
    print("Welcome to the world of Eyouis!")
    player_stats = {"health": 100, "attack": 10, "defense": 5, "level": 1, "experience": 0}
    inventory = []
    quests_completed = []
    green_dragon_defeated = False

    # Main Game Loop
    while not green_dragon_defeated:
        print("\nChoose an action: Explore, Quest, Inventory, Stats, Exit")
        player_action = input("Your choice: ").strip().lower()

        if player_action == "explore":
            explore(player_stats, inventory)

        elif player_action == "quest":
            green_dragon_defeated = quest_menu(player_stats, inventory, quests_completed)

        elif player_action == "inventory":
            print("Inventory:", inventory)

        elif player_action == "stats":
            print("Player Stats:", player_stats)

        elif player_action == "exit":
            print("Thank you for playing!")
            break

        else:
            print("Invalid action, try again.")

# This is the loop for when you want to explore

def explore(player_stats, inventory):
    print("You venture into the wilderness.")
    encounter = random.choice(["Mob", "Flower", "Nothing"])

    if encounter == "Mob":
        print("You encountered a mob!")
        battle("Random Mob", player_stats, inventory)

    elif encounter == "Flower":
        stat = random.choice(["health", "attack", "defense"])
        boost = random.randint(1, 5)
        player_stats[stat] += boost
        print(f"You found a flower that boosts your {stat} by {boost}!")

    else:
        print("You found nothing this time.")

# Quest Menu

def quest_menu(player_stats, inventory, quests_completed):
    quests = {
        "hornet's rawth": hornets_rawth,
        "stop invading our town!": stop_invading_our_town,
        "what's on top?": whats_on_top,
        "nessie, is that you?": nessie_quest,
        "side quest town": side_quest_town,
        "side quest no. 2": side_quest_2
    }

    print("\nAvailable Quests:")
    for quest in quests.keys():
        print(f"- {quest}")

    chosen_quest = input("Choose a quest: ").strip().lower()
    if chosen_quest in quests:
        quests[chosen_quest](player_stats, inventory, quests_completed)

    else:
        print("Invalid quest selection.")

    # Check for endgame condition
    required_quests = ["hornet's rawth", "stop invading our town!", "what's on top?", "nessie, is that you?"]
    if all(quest in quests_completed for quest in required_quests):
        print("The path to the green dragon is clear!")
        if battle("Green Dragon", player_stats, inventory):
            print("Congratulations, you saved Eyouis!")
            return True
        else:
            print("The dragon defeated you. Try again!")

    return False

# Quest Functions

def hornets_rawth(player_stats, inventory, quests_completed):
    print("You face the queen hornet!")
    if battle("Queen Hornet", player_stats, inventory):
        inventory.append("Queen Hornet's Poison")
        print("Quest Completed: Hornet's Rawth.")
        quests_completed.append("hornet's rawth")

def stop_invading_our_town(player_stats, inventory, quests_completed):
    print("You face the Orc King!")
    if battle("Orc King", player_stats, inventory):
        inventory.append("Dragon's Location Data")
        print("Quest Completed: STOP INVADING OUR TOWN!")
        quests_completed.append("stop invading our town!")

def whats_on_top(player_stats, inventory, quests_completed):
    print("You arrive at the small island guarded by giant spiders.")
    if battle("Giant Spiders", player_stats, inventory):
        inventory.append("Glittering Stone")
        print("Quest Completed: What's on Top?")
        quests_completed.append("what's on top?")

def nessie_quest(player_stats, inventory, quests_completed):
    print("You encounter the giant sea monster!")
    print("Solve the riddles or prepare to battle.")
    player_answer = input("What is Nessie's riddle answer? ").strip().lower()
    if player_answer == "correct answer":
        inventory.append("Dragon Weak Spot Info")
        print("Quest Completed: Nessie, is that you?")
        quests_completed.append("nessie, is that you?")
    else:
        battle("Nessie", player_stats, inventory)

def side_quest_town(player_stats, inventory, quests_completed):
    print("You dive into the lake, but sirens attack!")
    if battle("Sirens", player_stats, inventory):
        inventory.append("Lake Water")
        print("Quest Completed: Side quest Town.")
        quests_completed.append("side quest town")

def side_quest_2(player_stats, inventory, quests_completed):
    print("You venture to the enchanted forest and face orcs!")
    if battle("Orcs", player_stats, inventory):
        inventory.append("Life Flower Seeds")
        print("Quest Completed: Side quest No. 2.")
        quests_completed.append("side quest no. 2")

# Battle System
def battle(enemy, player_stats, inventory):
    print(f"Battle starts: {enemy}")
    enemy_health = random.randint(30, 100)
    while player_stats["health"] > 0 and enemy_health > 0:
        print(f"Player Health: {player_stats['health']}, Enemy Health: {enemy_health}")
        action = input("Choose an action: Attack, Defend, Use Item: ").strip().lower()

        if action == "attack":
            damage = max(1, player_stats["attack"] - random.randint(0, 5))
            enemy_health -= damage
            print(f"You dealt {damage} damage to the {enemy}.")

        elif action == "defend":
            print("You brace for the enemy's attack.")

        elif action == "use item" and inventory:
            print("Inventory:", inventory)
            item = input("Choose an item to use: ").strip()
            if item in inventory:
                print(f"You used {item}.")
                inventory.remove(item)
            else:
                print("Invalid item.")

        else:
            print("Invalid action.")

        # Enemy attack
        if enemy_health > 0:
            enemy_damage = max(1, random.randint(5, 15) - player_stats["defense"])
            player_stats["health"] -= enemy_damage
            print(f"The {enemy} dealt {enemy_damage} damage to you.")

    if player_stats["health"] > 0:
        print(f"You defeated the {enemy}!")
        player_stats["experience"] += 20
        return True
    else:
        print("You were defeated. Retrieve your items to continue.")
        return False

# Start the Game
if __name__ == "__main__":
    start_game()
