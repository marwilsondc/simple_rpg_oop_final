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