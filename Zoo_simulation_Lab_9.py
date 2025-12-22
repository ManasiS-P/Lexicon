class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 50 

    def eat(self):
        self.energy += 10
        print(f"{self.name} eats and gains energy. Energy is {self.energy}.")

    def sleep(self):
        self.energy += 20
        print(f"{self.name} sleeps. Energy is {self.energy}.")

    def interact(self):
        print(f"{self.name} looks around the zoo.")

class Herbivore(Animal):
    def eat(self):
        self.energy += 15
        print(f"{self.name} eats plants. Energy is {self.energy}.")

class Carnivore(Animal):
    def eat(self):
        self.energy += 20
        print(f"{self.name} eats meat. Energy is {self.energy}.")


class Lion(Carnivore):
    def interact(self):
        self.energy -= 5
        print(f"{self.name} roars and energy is {self.energy}.")
        
class Snake(Carnivore):
    def interact(self):
        self.energy -= 5
        print(f"{self.name} move around and energy is {self.energy}.")

class Elephant(Herbivore):
    def interact(self):
        self.energy -= 5
        print(f"{self.name} wanders and energy is {self.energy}.")

class Monkey(Herbivore):
    def interact(self):
        self.energy -= 10
        print(f"{self.name} jumps and energy is {self.energy}.")

class Visitor:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}.")
        animal.eat()

def simulate_zoo_day():
    lion = Lion("Leo", 5)
    snake = Snake("King Cobra",1)
    elephant = Elephant("Alpha", 7)
    monkey = Monkey("Tom", 3)

    animals = [lion, snake, elephant, monkey]

    
    visitor = Visitor("Bob")
    print("Morning: Animals are active")
    for animal in animals:
        animal.interact()

    print("Noon: Visitor feeds animals")
    for animal in animals:
        visitor.feed_animal(animal)

    print("Night: Animals sleep")
    for animal in animals:
        animal.sleep()

simulate_zoo_day()
