import random
import os
import time


# Global Variables
global item_slot_1_amount
global item_slot_2_amount
global item_slot_3_amount


# Starting Variables
current_enemy = ""
current_enemy_health = 0
player_health = 100
item_slot_1 = "Health Potion"
item_slot_1_amount = 3
item_slot_2 = "Potion of Tongues"
item_slot_2_amount = 3
item_slot_3 = "Potion of Strength"
item_slot_3_amount = 3
weapon_slot_1 = "" # Initialized to avoid errors
weapon_slot_2 = "" # Initialized to avoid errors


def items_menu():
    if item_slot_1:
        print(f"1. {item_slot_1}")
    if item_slot_2:
        print(f"2. {item_slot_2}")
    if item_slot_3:
        print(f"3. {item_slot_3}")
    item_choise = input("> ")
    if item_choise == "1":
        if item_slot_1_amount > 0:
            print(f"You use a {item_slot_1}!")
            time.sleep(2)
            clear_screen()
            print("You heal for 50 health!")
            global player_health
            player_health += 50
            if player_health > 100:
                player_health = 100
            item_slot_1_amount -= 1
            time.sleep(2)
            clear_screen()
            enemy_attack()
        else:
            print("You don't have any more of that item!")
            time.sleep(2)
            clear_screen()
            items_menu()
    elif item_choise == "2":
        if item_slot_2_amount > 0:
            print(f"You use a {item_slot_2}!")
            time.sleep(2)
            clear_screen()
            print("You can now understand the language of the creatures around you!")
            item_slot_2_amount -= 1
            time.sleep(2)
            clear_screen()
            enemy_attack()
        else:
            print("You don't have any more of that item!")
            time.sleep(2)
            clear_screen()
            battle_menu()
    elif item_choise == "3":
        if item_slot_3_amount > 0:
            print(f"You use a {item_slot_3}!")
            time.sleep(2)
            clear_screen()
            print("You feel stronger!")
            item_slot_3_amount -= 1
            time.sleep(2)
            clear_screen()
            enemy_attack()
        else:
            print("You don't have any more of that item!")
            time.sleep(2)
            clear_screen()
            battle_menu()
    else:
        print("Invalid choice, try again.")
        time.sleep(2)
        clear_screen()
        items_menu()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_name():
    clear_screen()
    name_input = input("Jim: Then what is your name? ")
    clear_screen()
    confirmation = input(f"Jim: So you're {name_input}? ").lower()
    if confirmation == "yes":
        clear_screen()
        print("Jim: Ok, just making sure.")
        return name_input
    elif confirmation == "no":
        return get_name() 
    else:
        clear_screen()
        print("Jim: What did you say?")
        time.sleep(2)
        return get_name()

def battle_menu():
    # Added global access for display
    global current_enemy_health, player_health
    print(f"Enemy Health: {current_enemy_health}\n\nYour Health: {player_health}\n\n\n1. Weapons\n2. Items")
    battle_choise = input("> ")
    if battle_choise == "1":
        weapons_menu()
    elif battle_choise == "2":
        items_menu()

def weapons_menu():
    # Added global keywords so these can be modified/read
    global current_enemy_health, player_health, current_enemy, weapon_slot_1, weapon_slot_2
    
    if weapon_slot_1:
        print(f"1. {weapon_slot_1}")
    if weapon_slot_2:
        print(f"2. {weapon_slot_2}")
        
    weapon_choise = input("> ")
    
    if weapon_choise == "1":
        print(f"You attack the {current_enemy} with your {weapon_slot_1}!")
        time.sleep(2)
        damage = random.randint(10, 20)
        clear_screen()
        print(f"You deal {damage} damage!")
        time.sleep(2)
        
        current_enemy_health -= damage
        
        if current_enemy_health <= 0:
            print(f"You have defeated the {current_enemy}!")
            time.sleep(2)
            clear_screen()
            forest_trail_menu()
        else:
            print(f"The {current_enemy} has {current_enemy_health} health left.")
            time.sleep(2)
            clear_screen()
            enemy_attack()

    elif weapon_choise == "2":
        print(f"You attack the {current_enemy} with your {weapon_slot_2}!")
        time.sleep(2)
        damage = random.randint(15, 25) 
        clear_screen()
        print(f"You deal {damage} damage!")
        time.sleep(2)
        
        current_enemy_health -= damage
        
        if current_enemy_health <= 0:
            print(f"You have defeated the {current_enemy}!")
            time.sleep(2)
            clear_screen()
            forest_trail_menu()
        else:
            print(f"The {current_enemy} has {current_enemy_health} health left.")
            time.sleep(2)
            clear_screen()
            enemy_attack()
    else:
        print("Invalid choice, try again.")
        time.sleep(2)
        clear_screen()
        weapons_menu()

def enemy_attack():
    global player_health, current_enemy
    print(f"The {current_enemy} attacks you!")
    time.sleep(2)
    enemy_damage = random.randint(5, 15)
    print(f"The {current_enemy} deals {enemy_damage} damage to you!")
    player_health -= enemy_damage
    
    if player_health <= 0:
        print("You have been defeated! Game Over.")
        time.sleep(2)
        clear_screen()
    else:
        print(f"You have {player_health} health left.")
        time.sleep(2)
        clear_screen()
        battle_menu()

def forest_trail_menu():
    print("1. Move on\n2. Look Around\n3. Check Inventory")
    forest_trail_choise = input("> ")
    if forest_trail_choise == "1":
        print("You continue down the trail.")
        time.sleep(2)
        clear_screen()
        forest_trail_menu_move()
    elif forest_trail_choise == "2":
        print("You look around and see trees, bushes, and the trail continuing ahead.")
        time.sleep(3)
        clear_screen()
        forest_trail_menu()
    elif forest_trail_choise == "3":
        print(f"Inventory:\n\nWeapons:")
        if weapon_slot_1:
            print(f"- {weapon_slot_1}")
        if weapon_slot_2:
            print(f"- {weapon_slot_2}")
        print("\nItems:")
        if item_slot_1:
            print(f"- {item_slot_1} x{item_slot_1_amount}")
        if item_slot_2:
            print(f"- {item_slot_2} x{item_slot_2_amount}")
        if item_slot_3:
            print(f"- {item_slot_3} x{item_slot_3_amount}")
        input("\n\nPress Enter to go back.")
        clear_screen()
        forest_trail_menu()
    else:
        print("Invalid choice, try again.")
        time.sleep(2)
        clear_screen()
        forest_trail_menu()
    Demo_End()

def Demo_End():
    clear_screen()
    print("TO...")
    time.sleep(2)
    clear_screen()
    print("BE...")
    time.sleep(2)
    clear_screen()
    print("CONTINUED!")
    time.sleep(2)
    clear_screen()
    print("Thanks for playing the demo! The full game will be out soon!")
    time.sleep(3)
    clear_screen()
    print("THE END (for now)\n\nCreated by: Connor W.\n\nDemo Creation:\nFebruary of 2026 - May 12th, 2026")


# --- Intro Sequence ---
clear_screen()
print("???: He-... -an... -ear... -e!")
time.sleep(3)
clear_screen()
print("???: I... -epeat... ca-... you... -ear... -e!")
time.sleep(3.5)
clear_screen()
print("???: Wait... are you... you're waking up!")
time.sleep(2.5)
clear_screen()

b = input("???: Wait... say yes if you can hear me. Are you waking up? ").lower()
clear_screen()
if b == "yes":
    print("???: Oh thank God, I thought you DIED!")
elif b == "no":
    print("???: DON'T SAY THAT!!! I thought you DIED!")
else:
    print("???: I don't know what you said but at least you're alive.")

time.sleep(3)
clear_screen()
print("???: I found you on the trail outside.")
time.sleep(2)
clear_screen()

# --- Name Selection ---
initial_name = input("Jim: I'm Jim, what's your name? ")
clear_screen()
c = input(f"Jim: So you're {initial_name}? ").lower()

if c == "yes":
    clear_screen()
    print("Jim: Ok, just making sure.")
    player_name = initial_name
elif c == "no":
    player_name = get_name()
else:
    clear_screen()
    print("Jim: What did you say?")
    time.sleep(2)
    player_name = get_name()

time.sleep(2)
clear_screen()

# --- The Cliffhanger ---
print(f"Jim: So {player_name}, do you remember why you were on that path uncon-")
time.sleep(3)
clear_screen()
print("Jim: Oh no... How!?")
time.sleep(2)
clear_screen()

print("1. What?\n2. ...")
choice_1 = input("> ")
if choice_1 == "1":
    print(f"{player_name}: What?")
    time.sleep(2)
    clear_screen()
    print("Nothing...")
    time.sleep(2)
    clear_screen()
    print("Umm...")
else:
    print(f"{player_name}: ...")

time.sleep(2)
clear_screen()
print("Okay, just... umm... Oh! You need to take this sword and run.")
time.sleep(2)
clear_screen()
input("[!] +1 Stone Sword (Press Enter)")
clear_screen()

weapon_slot_1 = "Stone Sword"

print("Jim (still inside): AAHHHHHHH-")
time.sleep(2)
clear_screen()

forest_trail_enemies = ["Trailstalker", "Trailstalker", "Shadow Creeper", "Shadow Creeper", "Hollow Wanderer"]
current_enemy = random.choice(forest_trail_enemies)

print(f"[!] Suddenly, a {current_enemy} lunges from the shadows!")
time.sleep(2)
clear_screen()

if current_enemy == "Trailstalker":
    current_enemy_health = 35
elif current_enemy == "Shadow Creeper":
    current_enemy_health = 50
elif current_enemy == "Hollow Wanderer":
    current_enemy_health = 65

player_health = 100
battle_menu()