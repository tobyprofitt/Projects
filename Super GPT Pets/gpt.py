import random

class Pet:
    def __init__(self, name, species, health, attack, defense):
        self.name = name
        self.species = species
        self.health = health
        self.attack = attack
        self.defense = defense

class Battle:
    def fight(self, pet1, pet2):
        while pet1.health > 0 and pet2.health > 0:
            damage = pet1.attack - pet2.defense
            pet2.health -= damage
            print(f"{pet1.name} attacks {pet2.name} for {damage} damage")
            print(f"{pet2.name} has {pet2.health} health remaining")
            if pet2.health <= 0:
                break
            damage = pet2.attack - pet1.defense
            pet1.health -= damage
            print(f"{pet2.name} attacks {pet1.name} for {damage} damage")
            print(f"{pet1.name} has {pet1.health} health remaining")
        if pet1.health > 0:
            return pet1
        else:
            return pet2

def main():
    pets = [
        Pet("Rufus", "dog", 100, 20, 10),
        Pet("Whiskers", "cat", 80, 15, 15),
        Pet("Thunderbolt", "horse", 120, 25, 5),
        # Add more pets here...
    ]

    for pet in pets:
        print(f"{pet.name} ({pet.species}) has {pet.health} health")

    while len(pets) > 1:
        pet1, pet2 = random.sample(pets, 2)
        battle = Battle()
        winner = battle.fight(pet1, pet2)
        print(f"{winner.name} wins!")
        pets.remove(pet1)
        pets.remove(pet2)
        pets.append(winner)

    print(f"{pets[0].name} is the ultimate winner!")

if __name__ == "__main__":
    main()
