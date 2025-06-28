from math import ceil
import random 
from .character import Character
from .abilities import Abilities

class Warrior(Character):
    def __init__(self, name = "Bob"):
        super().__init__(name)
        self.stats["HP"] = 120
        self.current_hp = self.stats["HP"]
        self.stats["Mana"] = 50
        self.current_mana = self.stats["Mana"]
        self.stats["Armor"] = 10
        self.abilities = [
            Abilities("Dual Strike", self.stats["Level"], 1, "Multi-hit Ability", 16, num_hits = 2),
            Abilities("God Slash", self.stats["Level"], 3, power = 35, mana_req = 10)
        ]
    
    def __str__(self):
        return self.name
    
    def attack(self, enemy_armor: int):
        rand_num_gen = random.randint(1, 100)
        miss_rng = random.randint(1,100)
        miss_chance = 5

        if rand_num_gen <= self.stats["Crit Rate"]:
            damage = -((self.stats["Attack"] + (self.stats["Attack"] * self.stats["Crit Dmg"])) - ceil(enemy_armor * 0.2))
            print(f"Critical hit! {self.name} put all their strength on this attack and did {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name} swung his sword and missed!")
            return 0
        
        else:
            damage = -(self.stats["Attack"] - ceil(enemy_armor * 0.25))
            print(f"{self.name} slashed their sword on the enemy and dealt {damage} damage!")
            return damage
        
    def reset_stats(self):
        self.stats = {
            "Level": 1,
            "Attack": 17,
            "HP": 120,
            "Mana": 50,
            "Armor": 10,
            "Crit Rate": 15,
            "Crit Dmg": 0.5,
            "Experience": 0,
            "Overall Exp": 0,
        }
        self.current_hp = self.stats["HP"]
        self.current_mana = self.stats["Mana"]