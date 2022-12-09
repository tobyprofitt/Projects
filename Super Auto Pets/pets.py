# Pet Class

PET_IDS = {1:('Ant', 2, 1, None, 1, 1), 2:'Mosquito', 3:'Fish', 4:'Pig', 5:'Beaver'}

class Pet:
    def __init__(self, name, attack, health, item, tier, level):
        self.health = health
        self.attack = attack
        self.item = item
        self.tier = tier
        self.level = level
        self.name = name

class Team:
    def __init__(self, p1=None, p2=None, p3=None, p4=None, p5=None):
        self.p1 = Pet(p1)
        self.p2 = Pet(p2)
        self.p3 = Pet(p3)
        self.p4 = Pet(p4)
        self.p5 = Pet(p5)

def main():
    ant = Pet(1, 2, None, 1, 1, 'Ant')

    print(ant)


if __name__ == '__main__':
    main()