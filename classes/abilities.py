from math import ceil
import random

class Abilities:
    def __init__(self, name: str, user_level: int, level_req: int, ability_type: str = "Single-hit Ability", power = 0, mana_req = 5, num_hits = 1):
        self.name = name
        self.user_level = user_level
        self.level_req = level_req
        self.ability_type = ability_type
        self.power = power
        self.mana_req = mana_req
        self.num_hits = num_hits

    def __str__(self):
        return f"""
{self.name} ({self.ability_type}):
Power: {self.power}
Mana Requirement: {self.mana_req}
Number of hits: {self.num_hits}
"""
    
    def use_ability(self):
        if self.user_level >= self.level_req:

            miss_rng = random.randint(1,100)
            miss_chance = 13

            if self.ability_type == "Single-hit Ability":
                print(f"Using {self.name} for {self.power} damage!")
                if miss_rng <= miss_chance:
                    print(f"Oof! Casted {self.name} missed the enemy!")
                    return 0
                else:
                    return -(self.power)
            
            elif self.ability_type == "Multi-hit Ability":
                damage = 0
                hit_times = 0
                print(f"Using {self.name} to deal {self.num_hits} hits with {self.power} damage each!")

                for i in range(self.num_hits):
                    if miss_rng <= miss_chance:
                        print(f"Oof! Casted {self.name} missed the enemy!")
                    
                    else:
                        print(f"Casted {self.name} hit the enemy!")
                        hit_times += 1
                        damage += self.power
                    
                print(f"{self.name} hit {hit_times}x and dealt {damage} damage!")
                return -(damage)
            
        else:
            print(f"This ability is not available yet!")
            return None
        
    def check_avail(self):
        if self.user_level >= self.level_req:
            return True
        else:
            return False

