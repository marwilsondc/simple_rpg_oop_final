from classes.abilities import Abilities
from classes.enemy import Enemy
from classes.warrior import Warrior
from classes.archer import Archer
from classes.mage import Mage
from classes.events import Events
import time
import random

print("Welcome to Dungeon Crawl!")
time.sleep(1)
print("This is a simple RPG I made, with 3 classes to choose from with abilities you can use!")
time.sleep(1)
print("At this point, please choose between the 3 classes:")
print("(1) Warrior, (2) Mage, (3) Archer")

while True:
    user_select = input("Select from the three classes (input the number): ")

    if user_select.isnumeric() and user_select in range(1,4):
        user_select = int(user_select)
        break
    else:
        continue

if user_select == 1:
    print("You chose the Warrior class!")
    user_name = input("Please input your hero's name: ")
    user_hero = Warrior(user_name)
    print(f"Welcome to the world! {user_hero}")

elif user_select == 2:
    print("You chose the Mage class!")
    user_name = input("Please input your hero's name: ")
    user_hero = Mage(user_name)
    print(f"Welcome to the world! {user_hero}")

else: 
    print("You chose the Archer class!")
    user_name = input("Please input your hero's name: ")
    user_hero = Archer(user_name)
    print(f"Welcome to the world! {user_hero}")

while True:
    enemies = {
        "goblin": Enemy("Goblin", level = user_hero.stats["Level"] - random.randint(0,2)),
        "wolf": Enemy("Wolf", level = user_hero.stats["Level"] - random.randint(0,2), atk = 14, hp = 65),
        "slime": Enemy("Slime", level = user_hero.stats["Level"] - random.randint(0,2), atk = 8, hp = 60),
        "kobold": Enemy("Kobold", level = user_hero.stats["Level"] - random.randint(0,2), hp = 40),
        "twiglings": Enemy("Twiglings", level = user_hero.stats["Level"] - random.randint(0,2), atk = 12, hp = 75),
        "bog frogs": Enemy("Bog Frogs", level = user_hero.stats["Level"] - random.randint(0,2), atk = 7, hp = 85),
        "bandit": Enemy("Bandit", level = user_hero.stats["Level"] - random.randint(0,2), atk = 12, hp = 50),
        "cultist": Enemy("Cultist", level = user_hero.stats["Level"] - random.randint(0,2), hp = 65),
        "flame spores": Enemy("Flame Spores", level = user_hero.stats["Level"] - random.randint(0,2), atk = 15, hp = 25),
    }

    mid_enemies = {
        "shadow duelist": Enemy("Shadow Duelist", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 19, hp = 110),
        "mercenary brute": Enemy("Mercenary Brute", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 21, hp = 95),
        "basilisk hatchling": Enemy("Basilisk Hatchling", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 18, hp = 70),
        "chasm leaper": Enemy("Chasm Leaper", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 20, hp = 80),
        "golem": Enemy("Golem", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 14, hp = 140),
        "sorrowbound": Enemy("Sorrowbound", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 18, hp = 115),
    }

    boss_enemies = {
        "hollow king": Enemy("Hollow King", level = user_hero.stats["Level"] + random.randint(0,2), atk = 24, hp = 150),
        "clockwork oracle": Enemy("Clockwork Oracle", level = user_hero.stats["Level"] + random.randint(0,2), atk = 18, hp = 160),
        "leviathan": Enemy("Leviathan", level = user_hero.stats["Level"] + random.randint(0,2), atk = 19, hp = 130),
    }

    room_level = 0

    print(f"""
Health: {user_hero.current_hp}/{user_hero.stats["HP"]}
Mana: {user_hero.current_mana}/{user_hero.stats["Mana"]}

Select from the options below!:
1. Move to next room
2. View Hero stats
3. Use heal ability
4. Quit
""")
    
    while True: 
        try:
            user_select = int("Select from the options above: ")
            break

        except TypeError:
            print("Error: Invalid input")
            continue

    if user_select == 1:
        if room_level < 5:
            print(f"A {Events.normal_battle()} appeared!")

    elif user_select == 2:
        pass

    elif user_select == 3:
        pass

    elif user_select == 4:
        break

    else:
        continue