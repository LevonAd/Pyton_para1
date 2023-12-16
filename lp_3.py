class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} makes {self.sound} sound")

    def give_birth(self):
        print(f"{self.name} gives birth to live young")


class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying with {self.wingspan} wingspan")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs")