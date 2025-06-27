class Character:
    #def __init__
    def __init__(self):
        self.base_atk = 17
        self.base_hp = 100
        self.base_mana = 60
        self.level = 1
        self.armor = 0
        self.experience = 0

    #def __str__
    def __str__(self):
        return f"{self}: Base ATK: {self.base_atk} Base HP: {self.base_hp} Base Mana: {self.base_mana}"

    #def attack()
    def attack(self, enemy_armor):
        damage = (-self.base_atk) * enemy_armor
        return damage
    
    #def health()
    def health(self, change):
        self.base_hp += change

        if change < 0: 
            print(f"Took {change} damage! {self} Health: {self.base_hp}")
        else: 
            print(f"Got healed {self.base_hp} points! {self} Health: {self.base_hp}")


    #def mana()
    def mana(self, change):
        self.base_mana += change
        
        if change < 0: 
            print(f"Spent {change} mana! {self} mana: {self.base_mana}")

        else:
            print(f"Granted {change} mana! {self} mana: {self.base_mana}")

    #def level_up()
    def level_up(self):
        pass
    #def 