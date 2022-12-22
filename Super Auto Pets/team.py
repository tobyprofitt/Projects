"""
Class to define a team of 5 (nullable) pets
"""

from pet import Pet 

class Team:
    def __init__(self, p1=None, p2=None, p3=None, p4=None, p5=None):
        self.p1 = Pet(p1)
        self.p2 = Pet(p2)
        self.p3 = Pet(p3)
        self.p4 = Pet(p4)
        self.p5 = Pet(p5)
    
    def get_pets(self):
        return (self.p1, self.p2, self.p3, self.p4, self.p5)

    def __str__(self):
        return "Your pets are: {}, {}, {}, {} and {}, reverse order for battling".format(self.p1, self.p2, self.p3, self.p4, self.p5)
    
    def is_alive(self):
        pets = self.get_pets()
        for pet in pets:
            if not pet.is_alive():
                return False
        return True
    
    def get_front_pet(self):
        pets = self.get_pets()
        for pet in pets:
            if pet.is_alive():
                return pet