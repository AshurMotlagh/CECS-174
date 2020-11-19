class Mammal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("I am a " + self.species)


class Dog(Mammal):
    def makesounds(self):
        print("Woof! Woof!")


class Cat(Mammal):
    def makesounds(self):
        print("Meow")


dog = Dog("Dog")
cat = Cat("Cat")
pets = [dog, cat]
for obj in pets:
    obj.show_species()
    obj.makesounds()
