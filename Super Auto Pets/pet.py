"""
Pet class to define a pet and its attributes.
"""

class Pet:
    def __init__(self, name=None, attack=0, health=0, item=None, tier=0, level=0, trigger="NA"):
        self.health = health
        self.attack = attack
        self.item = item
        self.tier = tier
        self.level = level
        self.name = name
        self.trigger = trigger

    def __str__(self):
        return str(self.name)

    def add_attack(self, a):
        self.attack = self.attack + a

    def get_attack(self):
        return self.attack

    def add_health(self, h):
        self.health = self.health + h

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def get_trigger(self):
        return self.trigger

