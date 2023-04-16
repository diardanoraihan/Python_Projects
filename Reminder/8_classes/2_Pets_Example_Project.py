"""
Created on Mon December 13 20:28:36 2020

@author: Diardano Raihan

"""

class Pet:
    def __init__(self, N='Bronx', A=2, H=True, P=True ):
        self.name = N
        self.age = A
        self.hunger = H
        self.playful = P

    # getters - everything below here is a get func
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getHunger(self):
        return self.hunger
    def getPlayful(self):
        return self.playful

    # setters - everything below here is a set func
    def setName(self, newName):
        self.name = newName
    def setAge(self, newAge):
        self.age = newAge
    def setHunger(self, newHunger):
        self.hunger = newHunger
    def setPlayful(self, newPlayful):
        self.playful = newPlayful

    def __str__(self):
        return self.name + " is " + str(self.age) + " year old"

class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, FavoriteToy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.FavoriteToy = FavoriteToy

    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " + self.FavoriteToy)
        else:
            return ("Dog doesn't want to play")

class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.FavoritePlaceToSit = place

    def wantsToSit(self):
        if self.playful == False:
            return ("Cat wants to sit in " + self.FavoritePlaceToSit)
        else:
            return ("Cat wants to play")

    def __str__(self):
        return self.name + " likes to sit in " + self.FavoritePlaceToSit

class Human:
    def __init__(self, name, pets):
        self.name = name
        self.Pets = pets

    def hasPets(self):
        if len(self.Pets) !=0:
            return "Yes"
        else:
            return "No"

huskyDog = Dog("Snowball", 5, False, True, "Husky", "Stick")
Play = huskyDog.wantsToPlay()
print(Play)

huskyDog.playful = False
Play = huskyDog.wantsToPlay()
print(Play)
print(huskyDog)

typicalCat = Cat("Fluffy", 3, False, False, "the sun ray")
Sit = typicalCat.wantsToSit()
print(Sit)
print(typicalCat)

yourAverageHuman = Human("Alice", [huskyDog, typicalCat])
hasPet = yourAverageHuman.hasPets()
print(hasPet)
print(yourAverageHuman.Pets[0])
print(yourAverageHuman.Pets[1].name)