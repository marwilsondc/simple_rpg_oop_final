import random

class Events:
    @staticmethod
    def normal_battle():
        grass = ["goblin", "kobold", "bandit"]
        forest = ["wolf", "twiglings", "cultist"]
        cave = ["slime", "flame spores"]
        swamp = ["slime", "bog frogs", "cultist"]
        area_set = [grass, forest, cave, swamp]

        area_select = random.choice(area_set)

        if area_select == grass:
            print("You notice that a smell of greenery is in the air, you entered a Grass room and encountered a monster!")
            monster = random.choice(grass)
            return monster

        elif area_select == forest:
            print("The next room is dark, filled with trees, and moonlit, you entered a Forest room and encountered a monster!")
            monster = random.choice(forest)
            return monster
        
        elif area_select == cave:
            print("The room is pitch black, you entered a cave room, but a light came out and you encountered a monster!")
            monster = random.choice(cave)
            return monster
        
        else:
            print("A musky scent meets you, you entered a Swamp room and encountered a monster!")
            monster = random.choice(swamp)
            return monster
        
    @staticmethod
    def mid_battle():
        grass = ["shadow duelist", "mercenary brute"]
        forest = ["chasm leaper", "sorrowbound"]
        cave = ["golem", "basilisk hatchling"]
        swamp = ["mercenary brute", "sorrowbound"]
        area_set = [grass, forest, cave, swamp]

        area_select = random.choice(area_set)

        if area_select == grass:
            print("You notice that a smell of greenery is in the air, you entered a Grass room and encountered a mid-monster!")
            monster = random.choice(grass)
            return monster

        elif area_select == forest:
            print("The next room is dark, filled with trees, and moonlit, you entered a Forest room and encountered a mid-monster!")
            monster = random.choice(forest)
            return monster
        
        elif area_select == cave:
            print("The room is pitch black, you entered a cave room, but a light came out and you encountered a mid-monster!")
            monster = random.choice(cave)
            return monster
        
        else:
            print("A musky scent meets you, you entered a Swamp room and encountered a mid-monster!")
            monster = random.choice(swamp)
            return monster
        
    @staticmethod
    def boss_battle():
        grass = ["hollow king"]
        forest = ["leviathan"]
        cave = ["clockwork oracle", "hollow king"]
        swamp = ["leviathan"]
        area_set = [grass, forest, cave, swamp]

        area_select = random.choice(area_set)

        if area_select == grass:
            print("You notice that a smell of greenery is in the air, you entered a Grass room and encountered a Boss monster!")
            monster = random.choice(grass)
            return monster

        elif area_select == forest:
            print("The next room is dark, filled with trees, and moonlit, you entered a Forest room and encountered a Boss monster!")
            monster = random.choice(forest)
            return monster
        
        elif area_select == cave:
            print("The room is pitch black, you entered a cave room, but a light came out and you encountered a Boss monster!")
            monster = random.choice(cave)
            return monster
        
        else:
            print("A musky scent meets you, you entered a Swamp room and encountered a Boss monster!")
            monster = random.choice(swamp)
            return monster

    @staticmethod    
    def looting(level):
        random_number = random.randint(1,100)
        common_armor = range(1,61)
        rare_armor = range(61,81)
        legendary_armor = range(81,96)
        mythical_armor = range(96,101)

        if random_number in common_armor:
            print("You have found leather armor (Common)!")
            return 10 + random.randint(1,10)
        
        elif random_number in rare_armor:
            print("You have found chainmail armor (Rare)!")
            return 20 + random.randint(1,30)

        elif random_number in legendary_armor:
            print("You have found alloy armor (Legendary)!")
            return 50 + random.randint(1,20)
        
        elif random_number in mythical_armor:
            print("You have found Ancient Magical Armor (Mythical)!")
            return 70 + random.randint(1,30)