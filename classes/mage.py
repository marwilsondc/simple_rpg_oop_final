from math import ceil
import random 
from character import Character

class Mage(Character):
    def __init__(self, name = "Sucrose"):
        super().__init__()
        self.name = name
        self.base_atk = 19
        self.base_hp = 90
        self.current_hp = self.base_hp
        self.base_mana = 75
        self.current_mana = self.base_mana

    def __str__(self):
        return f"""
Name: {self.name}
Class: Mage
Level: {self.level}
ATK: {self.base_atk}
HP: {self.current_hp}/{self.base_hp}
MANA: {self.current_mana}/{self.base_mana}
Armor: {self.armor}
Exp.: {self.overall_exp}
CritRate: {self.crit_rate}
CritDmg: {self.crit_dmg}
"""
    
    def attack(self, enemy_armor):
        rand_num_gen = random.randint(1, 100)
        miss_rng = random.randint(1,100)
        miss_chance = 8

        if rand_num_gen <= self.crit_rate:
            damage = -((self.base_atk + (self.base_atk * self.crit_dmg)) - ceil(enemy_armor * 0.17))
            print(f"Critical hit! {self.name} was favored by the gods and dealt {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name}'s magic swayed to a side and missed!")
            return 0
        
        else:
            damage = -(self.base_atk - ceil(enemy_armor * 0.21))
            print(f"{self.name} cast their fireball toward the enemy and dealt {damage} damage!")
            return damage