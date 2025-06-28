from math import ceil
import random 
from character import Character

class Warrior(Character):
    def __init__(self, name = "Bob"):
        super().__init__(name)
        self.base_hp = 120
        self.current_hp = self.base_hp
        self.base_mana = 50
        self.current_mana = self.base_mana

    
    def __str__(self):
        return f"""
Name: {self.name}
Class: Warrior
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
        miss_chance = 5

        if rand_num_gen <= self.crit_rate:
            damage = -((self.base_atk + (self.base_atk * self.crit_dmg)) - ceil(enemy_armor * 0.2))
            print(f"Critical hit! {self.name} put all their strength on this attack and did {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name} swung his sword and missed!")
            return 0
        
        else:
            damage = -(self.base_atk - ceil(enemy_armor * 0.25))
            print(f"{self.name} slashed their sword on the enemy and dealt {damage} damage!")
            return damage