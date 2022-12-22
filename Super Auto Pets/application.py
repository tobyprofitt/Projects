# Imports
import json
import random

from pet import Pet
from team import Team

# Constant variables
with open('pet_stats.json') as f:
    PETS = json.load(f)
ID_TO_PET = {'1':"Ant", '2':"Pig", '3':"Fish", '4':"Cricket", '5':"Mosquito", '6':"Beaver", '7':"Otter", '8':"Duck", '9':"Horse"}
PET_TO_ID = {}
for k, v in ID_TO_PET.items():
    PET_TO_ID[v] = k
AVAILABLE_PETS = {'1': ('1', '2', '3', '4', '5', '6', '7', '8', '9')}

# Helper functions
def make_pet_from_id(id):
    stats = PETS[id]
    pet = Pet(name=stats['Name'], attack=stats['Attack'], health=stats['Health'], item=None, tier=stats['Tier'], level=1, trigger=stats['Trigger'])
    return(pet)

def make_pet_from_name(name):
    id = PET_TO_ID[name]
    return make_pet_from_id(id)

def generate_shop(tier, pet_slots):
    shop_pet_ids = random.sample(AVAILABLE_PETS[tier], pet_slots)
    shop_pets = [make_pet_from_id(pet) for pet in shop_pet_ids]
    return shop_pets

def battle(team1: Team, team2: Team):
    turn = 0
    while team1.is_alive() and team2.is_alive():
        turn += 1

        # start of battle affects

        p1 = team1.get_front_pent()
        p2 = team2.get_front_pent()

        # attack
        attack(pet1=p1, pet2=p2)
        pass

def attack(pet1: Pet, pet2: Pet):
    p1_attack = pet1.get_attack()
    p1_health = pet1.get_health()
    p1_trigger= pet1.get_trigger()
    p2_attack = pet2.get_attack()
    p2_health = pet2.get_health()
    p2_trigger= pet2.get_trigger()

    # before attack effects
    pass

    # damage calc
    pet1.add_health(-p2_attack)
    pet2.add_health(-p1_attack)

    # before faint
    pass

    # pet faint
    pass



def main():
    pet1 = Pet(name='Ant')
    p1 = make_pet_from_name('Ant')
    p2 = make_pet_from_name('Ant')
    p3 = make_pet_from_name('Duck')
    team = Team(p1, p2, p3)

    print(team)

    p1.add_health(-5)
    print(p1.get_health())
    print(p1.is_alive())

    shop1 = generate_shop('1', 3)
    for pet in shop1:
        print(PETS[PET_TO_ID[pet.name]])
        


if __name__ == '__main__':
    main()