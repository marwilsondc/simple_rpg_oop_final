from math import ceil
import random
from .character import Character
from .abilities import Abilities

class Archer(Character):
    #def __init__()
    def __init__(self, name = "Robin"):
        super().__init__(name)
        self.stats["Attack"] = 24
        self.stats["HP"] = 70
        self.current_hp = self.stats["HP"]
        self.stats["Mana"] = 65
        self.current_mana = self.stats["Mana"]
        self.stats["Crit Rate"] = 20
        self.abilities = [
            Abilities("Focus Shot", self.stats["Level"], 1, power = 30),
            Abilities("Rapid-Fire", self.stats["Level"], 3, "Multi-hit Ability", 15, 10, 3),
        ]

    #def __str__()
    def __str__(self):
        return self.name
    
    #def attack()
    def attack(self, enemy_armor: int):
        rand_num_gen = random.randint(1, 100)
        miss_rng = random.randint(1,100)
        miss_chance = 10

        if rand_num_gen <= self.stats["Crit Rate"]:
            damage = -((self.stats["Attack"] + (self.stats["Attack"] * self.stats["Crit Dmg"])) - ceil(enemy_armor * 0.2))
            print(f"Critical hit! {self.name} shot their bow through the enemy's head and dealt {damage} damage!")
            return damage
        
        elif miss_rng <= miss_chance:
            print(f"{self.name} miscalculated the wind direction and missed!")
            return 0
        
        else:
            damage = -(self.stats["Attack"] - ceil(enemy_armor * 0.25))
            print(f"{self.name} shot their bow and dealt {damage} damage!")
            return damage
        
    

    