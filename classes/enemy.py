from character import Character
from math import ceil
import random

class Enemy(Character):
    #def __init__(self):
    def __init__(self, name = None, level = 1, atk = 10, hp = 45, mana = 35, armor = 0, crit_rt = 15, crit_dmg = 0.5):
        super().__init__()
        self.name = name 
        self.level = level
        self.base_atk = atk
        self.base_hp = hp
        self.current_hp = self.base_hp
        self.base_mana = mana
        self.current_mana = self.base_mana
        self.armor = armor
        self.crit_rate = crit_rt
        self.crit_dmg = crit_dmg

    #def __str__(self):
    def __str__(self):
        return f"""
Name: {self.name}
Level: {self.level}
"""
    
    #def attack()
    def attack(self, enemy_armor):
        rand_num_gen = random.randint(1, 100)
        miss_rng = random.randint(1, 100)
        miss_chance = 8

        if rand_num_gen <= self.crit_rate:
            damage = -((self.base_atk + (self.base_atk * self.crit_dmg)) - ceil(enemy_armor * 0.3))
            print(f"OOF! Critical hit! {self.name} did {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name} fortunately missed!")
            return 0

        else:
            damage = -(self.base_atk - ceil(enemy_armor * 0.35))
            return damage