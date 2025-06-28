from .character import Character
from math import floor
import random

class Enemy(Character):
    #def __init__(self):
    def __init__(self, name = None, level = 1, atk = 10, hp = 45, mana = 35, armor = 0, crit_rt = 15, crit_dmg = 0.5):
        super().__init__(name)
        self.stats = {
            "Level": level,
            "Attack": atk,
            "HP": hp,
            "Mana": mana,
            "Armor": armor,
            "Crit Rate": crit_rt,
            "Crit Dmg": crit_dmg,
        }
    #def __str__(self):
    def __str__(self):
        return self.name
    
    #def attack()
    def attack(self, enemy_armor: int):
        rand_num_gen = random.randint(1, 100)
        miss_rng = random.randint(1, 100)
        miss_chance = 8

        if rand_num_gen <= self.stats["Crit Rate"]:
            damage = -((self.stats["Attack"] + (self.stats["Attack"] * self.stats["Crit Dmg"])) * (1 - floor(enemy_armor / 110)))
            print(f"OOF! Critical hit! {self.name} did {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name} fortunately missed!")
            return 0

        else:
            damage = -(self.stats["Attack"] * (1 - floor(enemy_armor / 110)))
            return damage