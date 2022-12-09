# Pet Class
import json

with open('Super Auto Pets\pet_stats.json') as f:
    PETS = json.load(f)

ID_TO_PET = {'1':"Ant", '2':"Pig", '3':"Fish", '4':"Cricket", '5':"Mosquito", '6':"Beaver", '7':"Otter", '8':"Duck", '9':"Horse"}
PET_TO_ID = {}
for k, v in ID_TO_PET.items():
    PET_TO_ID[v] = k

class Pet:
    def __init__(self, name=None, attack=0, health=0, item=None, tier=0, level=0):
        self.health = health
        self.attack = attack
        self.item = item
        self.tier = tier
        self.level = level
        self.name = name

    def __str__(self):
        return str(self.name)

class Team:
    def __init__(self, p1=None, p2=None, p3=None, p4=None, p5=None):
        self.p1 = Pet(p1)
        self.p2 = Pet(p2)
        self.p3 = Pet(p3)
        self.p4 = Pet(p4)
        self.p5 = Pet(p5)

    def __str__(self):
        return "Your pets are: {}, {}, {}, {} and {}, in that order".format(self.p1, self.p2, self.p3, self.p4, self.p5)
        


    
def make_pet_from_id(id):
    stats = PETS[id]
    pet = Pet(name=stats['Name'], attack=stats['Attack'], health=stats['Health'], item=None, tier=stats['Tier'], level=1)
    return(pet)

def make_pet_from_name(name):
    id = PET_TO_ID[name]
    return make_pet_from_id(id)

def main():
    pet1 = Pet(name='Ant')
    p1 = make_pet_from_name('Ant')

    p2 = make_pet_from_name('Ant')
    p3 = make_pet_from_name('Duck')
    team = Team(p1, p2, p3)

    print(team)
    


if __name__ == '__main__':
    main()