from abc import ABC, abstractmethod

class Character:
    #def __init__
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.base_atk = 17
        self.base_hp = 100 
        self.current_hp = self.base_hp
        self.base_mana = 60
        self.current_mana = self.base_mana
        self.armor = 0
        self.experience = 0
        self.overall_exp = 0
        self.crit_rate = 15
        self.crit_dmg = 0.5

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
            print(f"Spent {change} mana! {self.name} mana: {self.base_mana}")
            self.current_mana += change
        elif change > 0:
            print(f"Granted {change} mana! {self.name} mana: {self.base_mana}")
            self.current_mana += change
        else:
            print(f"The action failed!")

    #def exp_up()
    def exp_up(self, change):
        self.experience += change
        self.overall_exp += change

        if self.experience >= 50:
            self.experience = self.experience - 50
            self.level += 1
            self.base_atk = 17 + (self.level * 3)
            self.base_hp = 100 + (self.level * 15)
            self.base_mana = 60 + (self.level * 5)
            self.current_hp = self.base_hp
            self.current_mana = self.base_mana

            print(f"{self.name} leveled up to LVL {self.level}!")
        
        else:
            print(f"{self.name} gained {change} EXP!")

    #def equip_armor()
    def equip_armor(self, amount):
        self.armor = amount
