from classes.abilities import Abilities
from classes.character import Character
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

    if user_select.isnumeric() and int(user_select) in range(1,4):
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

room_level = 0
heal_cooldown = 0
battle_heal_cooldown = 0

while True:
    enemies = {
        "goblin": Enemy("Goblin", level = user_hero.stats["Level"] - random.randint(0,2), armor = 4),
        "wolf": Enemy("Wolf", level = user_hero.stats["Level"] - random.randint(0,2), atk = 14, hp = 65, armor = 5),
        "slime": Enemy("Slime", level = user_hero.stats["Level"] - random.randint(0,2), atk = 8, hp = 60),
        "kobold": Enemy("Kobold", level = user_hero.stats["Level"] - random.randint(0,2), hp = 40, armor = 7),
        "twiglings": Enemy("Twiglings", level = user_hero.stats["Level"] - random.randint(0,2), atk = 12, hp = 75, armor = 8),
        "bog frogs": Enemy("Bog Frogs", level = user_hero.stats["Level"] - random.randint(0,2), atk = 7, hp = 85, armor = 3),
        "bandit": Enemy("Bandit", level = user_hero.stats["Level"] - random.randint(0,2), atk = 12, hp = 50, armor = 5),
        "cultist": Enemy("Cultist", level = user_hero.stats["Level"] - random.randint(0,2), hp = 65, armor = 4),
        "flame spores": Enemy("Flame Spores", level = user_hero.stats["Level"] - random.randint(0,2), atk = 15, hp = 25),
    }

    mid_enemies = {
        "shadow duelist": Enemy("Shadow Duelist", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 19, hp = 110, armor = 5),
        "mercenary brute": Enemy("Mercenary Brute", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 21, hp = 95, armor = 10),
        "basilisk hatchling": Enemy("Basilisk Hatchling", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 18, hp = 70, armor = 4),
        "chasm leaper": Enemy("Chasm Leaper", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 20, hp = 80),
        "golem": Enemy("Golem", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 14, hp = 140, armor = 5),
        "sorrowbound": Enemy("Sorrowbound", level = user_hero.stats["Level"] + random.randint(-1,1), atk = 18, hp = 115),
    }

    boss_enemies = {
        "hollow king": Enemy("Hollow King", level = user_hero.stats["Level"] + random.randint(0,2), atk = 24, hp = 150, armor = 15),
        "clockwork oracle": Enemy("Clockwork Oracle", level = user_hero.stats["Level"] + random.randint(0,2), atk = 18, hp = 160, armor = 10),
        "leviathan": Enemy("Leviathan", level = user_hero.stats["Level"] + random.randint(0,2), atk = 19, hp = 130, armor = 10),
    }

    print(f"""
Health: {user_hero.current_hp}/{user_hero.stats["HP"]}
Mana: {user_hero.current_mana}/{user_hero.stats["Mana"]}

1. Move to next room
2. View Hero stats
3. Use heal ability
4. Quit
""")

    while True: 
        try:
            user_select = int(input("Select from the options above: "))
            break

        except ValueError:
            print("Error: Invalid input")
            continue

    if user_select == 1:
        if room_level < 5 or room_level > 5:
            monster_call = Events.normal_battle()
            print(f"A {monster_call} appeared!")
            actual_mon = enemies[monster_call]
            actual_mon.apply_level()

            while True:
                battle_heal_cooldown -= 0

                print(f"""
{user_hero}, choose from the actions:
HP: {user_hero.current_hp}/{user_hero.stats["HP"]}
Mana: {user_hero.current_mana}/{user_hero.stats["Mana"]}
Enemy HP: {actual_mon.current_hp}/{actual_mon.stats["HP"]}

1. Attack
2. Use ability
3. Defend & Heal
4. Run
""")
                while True:
                    try:
                        user_select = int(input("Select from the options above: "))
                        if user_select < 5 and user_select > 0:
                            break

                    except ValueError:
                        print("Error: Invalid input")
                        continue
                
                if user_select == 1:
                    damage = user_hero.attack(actual_mon.stats["Armor"])
                    actual_mon.health(damage)

                    if actual_mon.current_hp <= 0:
                        gained_exp = 12 + (random.randint(2,4))
                        print(f"{user_hero} has slain {actual_mon}! Gained {gained_exp}")
                        user_hero.exp_up(gained_exp)
                        armor_loot = Events.looting()
                        user_select = input("Do you want to equip this?: y/n?")
                        if user_select == "y":
                            user_hero.equip_armor(armor_loot)
                            break

                        elif user_select == "n":
                            break
                        

                
                elif user_select == 2:
                    print("Use which ability?: ")
                    count = 0

                    for i in user_hero.abilities:
                        print(count, i, i.check_avail(), "\n")
                        count += 1
                    
                    while True:
                        try:
                            user_select = int(input("Select from the options above: "))
                            if user_select <= count and user_select >= 0:
                                break

                        except ValueError:
                            print("Error: Invalid input")
                            continue
                    
                    print(f"Using {user_hero.abilities[user_select].name}...")

                    damage = user_hero.abilities[user_select].use_ability()
                    spent_mana = -(user_hero.abilities[user_select].mana_req)
                    user_hero.mana(spent_mana)
                    actual_mon.health(damage)

                    if actual_mon.current_hp <= 0:
                        gained_exp = 12 + (random.randint(2,4))
                        print(f"{user_hero} has slain {actual_mon}! Gained {gained_exp}")
                        user_hero.exp_up(gained_exp)
                        armor_loot = Events.looting()
                        user_select = input("Do you want to equip this?: y/n?")
                        if user_select == "y":
                            user_hero.equip_armor(armor_loot)
                            break

                        elif user_select == "n":
                            break

                elif user_select == 3:
                    if battle_heal_cooldown <= 0:
                        user_hero.health(user_hero.stats["HP"]*0.25)
                        print(f"{user_hero} defended himself from attacks and blocked the attack!")
                        battle_heal_cooldown = 3
                        continue

                    else:
                        print(f"Heal is in cooldown: Wait for {battle_heal_cooldown} more turn/s.")

                else:
                    print(f"{user_hero} chickened out! No exp gained.")
                    break

                print(f"{actual_mon} attacked {user_hero}")
                damage = actual_mon.attack(user_hero.stats["Armor"])
                user_hero.health(damage)

                if user_hero.current_hp <= 0:
                    print(f"Game Over! {user_hero} was slain by {actual_mon}!")
                    print(f"{user_hero} was taken back to the past, and heard \"Continue your journey\"")
                    user_hero.reset_stats()
                    break

            room_level += 1
            heal_cooldown -= 1

        elif room_level == 5:
            monster_call = Events.mid_battle()
            print(f"A mid-boss: {monster_call} appeared!")
            actual_mon = mid_enemies[monster_call]
            actual_mon.apply_level()

            while True:
                battle_heal_cooldown -= 1

                print(f"""
{user_hero}, choose from the actions:
HP: {user_hero.current_hp}/{user_hero.stats["HP"]}
Mana: {user_hero.current_mana}/{user_hero.stats["Mana"]}
Enemy HP: {actual_mon.current_hp}/{actual_mon.stats["HP"]}

1. Attack
2. Use ability
3. Defend & Heal
4. Run
""")
                while True:

                    try:
                        user_select = int(input("Select from the options above: "))
                        if user_select < 5 and user_select > 0:
                            break

                    except ValueError:
                        print("Error: Invalid input")
                        continue
                
                if user_select == 1:
                    damage = user_hero.attack(actual_mon.stats["Armor"])
                    actual_mon.health(damage)

                    if actual_mon.current_hp <= 0:
                        gained_exp = 12 + (random.randint(2,4))
                        print(f"{user_hero} has slain {actual_mon}! Gained {gained_exp}")
                        user_hero.exp_up(gained_exp)
                        armor_loot = Events.looting()
                        user_select = input("Do you want to equip this?: y/n?")
                        if user_select == "y":
                            user_hero.equip_armor(armor_loot)
                            break

                        elif user_select == "n":
                            break
                
                elif user_select == 2:
                    print("Use which ability?: ")
                    count = 0

                    for i in user_hero.abilities:
                        print(count, i, count, i, i.check_avail(), "\n")
                        count += 1
                    
                    while True:

                        try:
                            user_select = int(input("Select from the options above: "))
                            if user_select <= count and user_select >= 0:
                                break

                        except ValueError:
                            print("Error: Invalid input")
                            continue
                    
                    print(f"Using {user_hero.abilities[user_select].name}...")

                    damage = user_hero.abilities[user_select].use_ability()
                    spent_mana = -(user_hero.abilities[user_select].mana_req)
                    user_hero.mana(spent_mana)
                    actual_mon.health(damage)

                    if actual_mon.current_hp <= 0:
                        gained_exp = 12 + (random.randint(2,4))
                        print(f"{user_hero} has slain {actual_mon}! Gained {gained_exp}")
                        user_hero.exp_up(gained_exp)
                        armor_loot = Events.looting()
                        user_select = input("Do you want to equip this?: y/n?")
                        if user_select == "y":
                            user_hero.equip_armor(armor_loot)
                            break

                        elif user_select == "n":
                            break

                elif user_select == 3:
                    if battle_heal_cooldown <= 0:
                        user_hero.health(user_hero.stats["HP"]*0.25)
                        print(f"{user_hero} defended himself from attacks and blocked the attack!")
                        battle_heal_cooldown = 3
                        continue

                else:
                    print(f"{user_hero} chickened out! No exp gained.")
                    break

                print(f"{actual_mon} attacked {user_hero}")
                damage = actual_mon.attack(user_hero.stats["Armor"])
                user_hero.health(damage)

                if user_hero.current_hp <= 0:
                    print(f"Game Over! {user_hero} was slain by {actual_mon}!")
                    print(f"{user_hero} was taken back to the past, and heard \"Continue your journey\"")
                    user_hero.reset_stats()
                    break

            room_level += 1
            heal_cooldown -= 1

        elif room_level == 10:
            monster_call = Events.boss_battle()
            print(f"A boss: {monster_call} appeared!")
            actual_mon = boss_enemies[monster_call]
            actual_mon.apply_level()

            while True:
                battle_heal_cooldown -= 1

                print(f"""
{user_hero}, choose from the actions:
HP: {user_hero.current_hp}/{user_hero.stats["HP"]}
Mana: {user_hero.current_mana}/{user_hero.stats["Mana"]}
Enemy HP: {actual_mon.current_hp}/{actual_mon.stats["HP"]}

1. Attack
2. Use ability
3. Defend & Heal
4. Run
""")
                while True:

                    try:
                        user_select = int(input("Select from the options above: "))
                        if user_select < 5 and user_select > 0:
                            break

                    except ValueError:
                        print("Error: Invalid input")
                        continue
                
                if user_select == 1:
                    damage = user_hero.attack(actual_mon.stats["Armor"])
                    actual_mon.health(damage)

                    if actual_mon.current_hp <= 0:
                        gained_exp = 12 + (random.randint(2,4))
                        print(f"{user_hero} has slain {actual_mon}! Gained {gained_exp}")
                        user_hero.exp_up(gained_exp)
                        armor_loot = Events.looting()
                        user_select = input("Do you want to equip this?: y/n?")
                        if user_select == "y":
                            user_hero.equip_armor(armor_loot)
                            break

                        elif user_select == "n":
                            break

                
                elif user_select == 2:
                    print("Use which ability?: ")
                    count = 0

                    for i in user_hero.abilities:
                        print(count, i, count, i, i.check_avail(), "\n")
                        count += 1
                    
                    while True:

                        try:
                            user_select = int(input("Select from the options above: "))
                            if user_select <= count and user_select >= 0:
                                break

                        except ValueError:
                            print("Error: Invalid input")
                            continue
                    
                    print(f"Using {user_hero.abilities[user_select].name}...")

                    damage = user_hero.abilities[user_select].use_ability()
                    spent_mana = -(user_hero.abilities[user_select].mana_req)
                    user_hero.mana(spent_mana)
                    actual_mon.health(damage)

                    if actual_mon.current_hp <= 0:
                        gained_exp = 12 + (random.randint(2,4))
                        print(f"{user_hero} has slain {actual_mon}! Gained {gained_exp}")
                        user_hero.exp_up(gained_exp)
                        armor_loot = Events.looting()
                        user_select = input("Do you want to equip this?: y/n?")
                        if user_select == "y":
                            user_hero.equip_armor(armor_loot)
                            break

                        elif user_select == "n":
                            break

                elif user_select == 3:
                    if battle_heal_cooldown <= 0:
                        user_hero.health(user_hero.stats["HP"]*0.25)
                        print(f"{user_hero} defended himself from attacks and blocked the attack!")
                        battle_heal_cooldown = 3
                        continue

                else:
                    print(f"{user_hero} chickened out! No exp gained.")
                    break

                print(f"{actual_mon} attacked {user_hero}")
                damage = actual_mon.attack(user_hero.stats["Armor"])
                user_hero.health(damage)

                if user_hero.current_hp <= 0:
                    print(f"Game Over! {user_hero} was slain by {actual_mon}!")
                    print(f"{user_hero} was taken back to the past, and heard \"Continue your journey\"")
                    user_hero.reset_stats()
                    break

            room_level = 0
            heal_cooldown -= 1

    elif user_select == 2:
        print(f"Showing {user_hero}'s Stats:")
        
        for stat, value in user_hero.stats.items():
            print(f"{stat}: {value}")

    elif user_select == 3:
        if heal_cooldown <= 0:
            user_hero.health(user_hero.stats["HP"] - user_hero.current_hp)
            heal_cooldown = 3
        else:
            print(f"Heal is in cooldown: {heal_cooldown} more battle/s.")

    elif user_select == 4:
        break

    else:
        continue