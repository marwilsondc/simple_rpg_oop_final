from math import floor
import random 
from .character import Character
from .abilities import Abilities

class Mage(Character):
    def __init__(self, name = "Sucrose"):
        super().__init__(name)
        self.stats["Attack"] = 19
        self.stats["HP"] = 90
        self.current_hp = self.stats["HP"]
        self.stats["Mana"] = 75
        self.current_mana = self.stats["Mana"]
        self.abilities = [
            Abilities("Arcane Comet", self.stats["Level"], 1, power = 23, mana_req = 10),
            Abilities("Rain Meteor", self.stats["Level"], 3, "Multi-hit Ability", power = 14, mana_req = 15, num_hits = 4)
        ]

    def __str__(self):
        return self.name
    
    def attack(self, enemy_armor: int):
        rand_num_gen = random.randint(1, 100)
        miss_rng = random.randint(1,100)
        miss_chance = 8

        if rand_num_gen <= self.stats["Crit Rate"]:
            damage = -((self.stats["Attack"] + (self.stats["Attack"] * self.stats["Crit Dmg"])) * (1 - floor(enemy_armor / 110)))
            print(f"Critical hit! {self.name} was favored by the gods and dealt {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name}'s magic swayed to a side and missed!")
            return 0
        
        else:
            damage = -(self.stats["Attack"] * (1 - floor(enemy_armor / 110)))
            print(f"{self.name} cast their fireball toward the enemy and dealt {damage} damage!")
            return damage
        
    def reset_stats(self):
        self.stats = {
            "Level": 1,
            "Attack": 19,
            "HP": 90,
            "Mana": 75,
            "Armor": 0,
            "Crit Rate": 15,
            "Crit Dmg": 0.5,
            "Experience": 0,
            "Overall Exp": 0,
        }
        self.current_hp = self.stats["HP"]
        self.current_mana = self.stats["Mana"]