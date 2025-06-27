from math import ceil
import random 
from character import Character

class Warrior(Character):
    def __init__(self, name = "Bob"):
        super().__init__()
        self.name = name

    
    def __str__(self):
        return f"""
Name: {self.name}
Class: Warrior
Level: {self.level}
ATK: {self.base_atk}
HP: {self.base_hp}
MANA: {self.base_mana}
Armor: {self.armor}
Exp.: {self.overall_exp}
CritRate: {self.crit_rate}
CritDmg: {self.crit_dmg}
"""
    
    def attack():
        pass