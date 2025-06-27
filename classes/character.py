class Character:
    #def __init__
    def __init__(self, name):
        self.name = name
        self.base_atk = 17
        self.base_hp = 100
        self.base_mana = 60
        self.level = 1
        self.armor = 0
        self.experience = 0
        self.overall_exp = 0

    #def __str__
    def __str__(self):
        return f"{self.name}: Base ATK: {self.base_atk} Base HP: {self.base_hp} Base Mana: {self.base_mana}"

    #def attack()
    def attack(self, enemy_armor):
        damage = (-self.base_atk) * enemy_armor
        return damage
    
    #def health()
    def health(self, change):
        self.base_hp += change

        if change < 0: 
            print(f"Took {change} damage! {self.name} Health: {self.base_hp}")
        else: 
            print(f"Got healed {self.base_hp} points! {self.name} Health: {self.base_hp}")


    #def mana()
    def mana(self, change):
        self.base_mana += change
        
        if change < 0: 
            print(f"Spent {change} mana! {self.name} mana: {self.base_mana}")

        else:
            print(f"Granted {change} mana! {self.name} mana: {self.base_mana}")

    #def exp_up()
    def exp_up(self, change):
        self.experience += change
        self.overall_exp += change

        if self.experience >= 50:
            self.experience = self.experience - 50
            self.level += 1
            print(f"{self.name} leveled up to LVL {self.level}!")
        
        else:
            print(f"{self.name} gained {change} EXP!")