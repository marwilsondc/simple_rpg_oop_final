from abc import ABC, abstractmethod

class Character:
    #def __init__
    def __init__(self, name):
        self.name = name
        self.stats = {
            "Level": 1,
            "Attack": 17,
            "HP": 100,
            "Mana": 60,
            "Armor": 0,
            "Crit Rate": 15,
            "Crit Dmg": 0.5,
            "Experience": 0,
            "Overall Exp": 0,
        }
        self.current_hp = self.stats["HP"]
        self.current_mana = self.stats["Mana"]

    #def __str__
    @abstractmethod
    def __str__(self):
        pass

    #def attack()
    @abstractmethod
    def attack():
        pass
    
    #def health()
    def health(self, change):

        if change < 0: 
            print(f"Took {change} damage! {self.name} Health: {self.current_hp}")
            self.current_hp += change

        elif change > 0: 
            print(f"Got healed {change} points! {self.name} Health: {self.current_hp}")
            self.current_hp += change
        else:
            print("The action failed!")

    #def mana()
    def mana(self, change):
        
        if change < 0: 
            print(f"Spent {change} mana! {self.name} mana: {self.stats["Mana"]}")
            self.current_mana += change
        elif change > 0:
            print(f"Granted {change} mana! {self.name} mana: {self.stats["Mana"]}")
            self.current_mana += change
        else:
            print(f"The action failed!")

    #def exp_up()
    def exp_up(self, change):
        self.stats["Experience"] += change
        self.stats["Overall Exp"] += change

        if self.stats["Experience"] >= 50:
            self.stats["Experience"] = self.stats["Experience"] - 50
            self.stats["Level"] += 1
            self.stats["Attack"] = self.stats["Attack"] + (self.stats["Level"] * 3)
            self.stats["HP"] = self.stats["HP"] + (self.stats["Level"] * 15)
            self.stats["Mana"] = self.stats["Mana"] + (self.stats["Level"] * 5)
            self.current_hp = self.stats["HP"]
            self.current_mana = self.stats["Mana"]

            print(f"{self.name} leveled up to LVL {self.stats["Level"]}!")
        
        else:
            print(f"{self.name} gained {change} EXP!")

    #def equip_armor()
    def equip_armor(self, amount):
        self.stats["Armor"] = amount

    #This method is for enemies
    def apply_level(self):
        self.stats["Attack"] = self.stats["Attack"] + (self.stats["Level"] * 2)
        self.stats["HP"] = self.stats["HP"] + (self.stats["Level"] * 7)
        self.current_hp = self.stats["HP"]
        self.current_mana = self.stats["Mana"]