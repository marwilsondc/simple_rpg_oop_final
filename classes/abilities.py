from math import ceil
import random

class Abilities:
    def __init__(self, name, power = 20, mana_req = 5, num_hits = 1):
        self.name = name
        self.power = power
        self.mana_req = mana_req
        self.num_hits = num_hits

    