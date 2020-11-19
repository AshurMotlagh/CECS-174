## simple demo for object passing

class Dog:
    def bark(self):
        print("'woof woof'")

    def love(self):
        pass

class DogHouse:
    def __init__(self, pet_name):
        self.owner = pet_name
        print('The owner of this dog house is ' + self.owner)

    def defend(self, a_dog): # passing instance of obj
        a_dog.bark()

my_pooch = Dog()
dog_house_1 = DogHouse('Yogurt')
dog_house_1.defend(my_pooch)










