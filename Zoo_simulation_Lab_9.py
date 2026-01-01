# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.energy = 50 

#     def eat(self):
#         self.energy += 10
#         print(f"{self.name} eats and gains energy. Energy is {self.energy}.")

#     def sleep(self):
#         self.energy += 20
#         print(f"{self.name} sleeps. Energy is {self.energy}.")

#     def interact(self):
#         print(f"{self.name} looks around the zoo.")

# class Herbivore(Animal):
#     def eat(self):
#         self.energy += 15
#         print(f"{self.name} eats plants. Energy is {self.energy}.")

# class Carnivore(Animal):
#     def eat(self):
#         self.energy += 20
#         print(f"{self.name} eats meat. Energy is {self.energy}.")


# class Lion(Carnivore):
#     def interact(self):
#         self.energy -= 5
#         print(f"{self.name} roars and energy is {self.energy}.")
        
# class Snake(Carnivore):
#     def interact(self):
#         self.energy -= 5
#         print(f"{self.name} move around and energy is {self.energy}.")

# class Elephant(Herbivore):
#     def interact(self):
#         self.energy -= 5
#         print(f"{self.name} wanders and energy is {self.energy}.")

# class Monkey(Herbivore):
#     def interact(self):
#         self.energy -= 10
#         print(f"{self.name} jumps and energy is {self.energy}.")

# class Visitor:
#     def __init__(self, name):
#         self.name = name

#     def feed_animal(self, animal):
#         print(f"{self.name} feeds {animal.name}.")
#         animal.eat()

# def simulate_zoo_day():
#     lion = Lion("Leo", 5)
#     snake = Snake("King Cobra",1)
#     elephant = Elephant("Alpha", 7)
#     monkey = Monkey("Tom", 3)

#     animals = [lion, snake, elephant, monkey]

    
#     visitor = Visitor("Bob")
#     print("Morning: Animals are active")
#     for animal in animals:
#         animal.interact()

#     print("Noon: Visitor feeds animals")
#     for animal in animals:
#         visitor.feed_animal(animal)

#     print("Night: Animals sleep")
#     for animal in animals:
#         animal.sleep()

# simulate_zoo_day()


#Extended Requirements (Improved Design & Behavior)
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 50
#         self.alive = True

#     def change_energy(self, amount):
#         self.energy += amount
#         if self.energy <= 0:
#             self.energy = 0
#             self.alive = False
#             print(self.name, "has no energy left and is exhausted!")

#     def sleep(self):
#         print(self.name, "is sleeping.")
#         self.change_energy(+20)

#     def can_act(self):
#         return self.energy > 10 and self.alive


# class Herbivore(Animal):
#     def eat(self):
#         print(self.name, "eats plants.")
#         self.change_energy(+15)

#     def play(self, other):
#         if self.can_act() and other.can_act():
#             print(self.name, "plays with", other.name)
#             self.change_energy(-10)
#             other.change_energy(-10)


# class Carnivore(Animal):
#     def eat(self):
#         print(self.name, "eats meat.")
#         self.change_energy(+20)

#     def hunt(self, prey):
#         if self.can_act() and prey.alive:
#             print(self.name, "hunts", prey.name)
#             self.change_energy(-15)
#             prey.change_energy(-30)


# class Visitor:
#     def __init__(self, name):
#         self.name = name

#     def feed(self, animal):
#         if animal.alive:
#             print(self.name, "feeds", animal.name)
#             animal.eat()


# class Zoo:
#     def __init__(self, animals, visitor):
#         self.animals = animals
#         self.visitor = visitor
#         self.day = 1

#     def simulate_day(self):
#         print("\n--- Day", self.day, "at the Zoo ---")

#         # Animals interact
#         for animal in self.animals:
#             if not animal.alive:
#                 continue

#             if isinstance(animal, Carnivore):
#                 for target in self.animals:
#                     if isinstance(target, Herbivore) and target.alive:
#                         animal.hunt(target)
#                         break

#             elif isinstance(animal, Herbivore):
#                 for friend in self.animals:
#                     if friend != animal and isinstance(friend, Herbivore):
#                         animal.play(friend)
#                         break

#         # Visitor feeds animals
#         print("\nVisitor time:")
#         for animal in self.animals:
#             self.visitor.feed(animal)

#         # Animals sleep
#         print("\nNight time:")
#         for animal in self.animals:
#             if animal.alive:
#                 animal.sleep()

#         self.day += 1

#     def simulate(self, days):
#         for _ in range(days):
#             self.simulate_day()

# lion = Carnivore("Leo the Lion")
# tiger = Carnivore("Shera the Tiger")
# elephant = Herbivore("Ella the Elephant")
# monkey = Herbivore("Momo the Monkey")

# animals = [lion, tiger, elephant, monkey]

# visitor = Visitor("Bob")

# zoo = Zoo(animals, visitor)

# zoo.simulate(days=2)



# Advanced Requirements (High-Quality Simulation Design)
# - Make it easy to add new animal species without modifying existing logic.
# - Maintain a balanced predator-prey system that avoids unrealistic extinction.
# - Separate simulation logic from execution logic.
# - Handle edge cases gracefully, regardless of interaction order.
# - Write clean, readable code with clear structure and comments where needed.
# - Demonstrate deliberate and well-reasoned design choices.
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 50
#         self.alive = True

#     def change_energy(self, amount):
#         self.energy += amount
#         if self.energy <= 0:
#             self.energy = 0
#             self.alive = False
#             print(self.name, "has no energy left and is exhausted!")

#     def sleep(self):
#         print(self.name, "is sleeping.")
#         self.change_energy(+20)

#     def can_act(self):
#         return self.energy > 10 and self.alive

#     def act(self, zoo):
#         pass   # to be overridden

# class Herbivore(Animal):
#     def eat(self):
#         print(self.name, "eats plants.")
#         self.change_energy(+15)

#     def play(self, other):
#         print(self.name, "plays with", other.name)
#         self.change_energy(-10)
#         other.change_energy(-10)

#     def act(self, zoo):
#         if not self.can_act():
#             self.sleep()
#             return

#         friend = zoo.find_herbivore(exclude=self)
#         if friend:
#             self.play(friend)
#         else:
#             self.eat()

# class Carnivore(Animal):
#     def eat(self):
#         print(self.name, "eats meat.")
#         self.change_energy(+20)

#     def hunt(self, prey):
#         print(self.name, "hunts", prey.name)
#         self.change_energy(-15)
#         prey.change_energy(-30)

#     def act(self, zoo):
#         if not self.can_act():
#             self.sleep()
#             return

#         prey = zoo.find_herbivore()
#         if prey:
#             self.hunt(prey)
#         else:
#             self.sleep()

# class Visitor:
#     def __init__(self, name):
#         self.name = name

#     def feed(self, animal):
#         if animal.alive:
#             print(self.name, "feeds", animal.name)
#             animal.eat()


# class Zoo:
#     def __init__(self, animals, visitor):
#         self.animals = animals
#         self.visitor = visitor
#         self.day = 1

#     def find_herbivore(self, exclude=None):
#         for animal in self.animals:
#             if isinstance(animal, Herbivore) and animal.alive and animal != exclude:
#                 return animal
#         return None

#     def simulate_day(self):
#         print("\n--- Day", self.day, "at the Zoo ---")

#         for animal in self.animals:
#             if animal.alive:
#                 animal.act(self)

#         print("\nVisitor time:")
#         for animal in self.animals:
#             self.visitor.feed(animal)

#         print("\nNight time:")
#         for animal in self.animals:
#             if animal.alive:
#                 animal.sleep()

#         self.day += 1

# lion = Carnivore("Leo")
# tiger = Carnivore("Shera")
# elephant = Herbivore("Ella")
# monkey = Herbivore("Momo")

# animals = [lion, tiger, elephant, monkey]

# visitor = Visitor("Bob")

# zoo = Zoo(animals, visitor)

# zoo.simulate_day()


class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 30
        self.alive = True

    def change_energy(self, amount):
        self.energy += amount
        if self.energy <= 0:
            self.energy = 0
            self.alive = False
            print(self.name, "has no energy left and is exhausted!")

    def sleep(self):
        print(self.name, "is sleeping.")
        self.change_energy(+20)

    def can_act(self):
        return self.energy > 10 and self.alive

    def act(self, zoo):
        pass


class Herbivore(Animal):
    def eat(self):
        print(self.name, "eats plants.")
        self.change_energy(+15)

    def play(self, other):
        print(self.name, "plays with", other.name)
        self.change_energy(-10)
        other.change_energy(-10)

    def act(self, zoo):
        if not self.can_act():
            self.sleep()
            return

        friend = zoo.find_herbivore(exclude=self)
        if friend and self.energy > 20:
            self.play(friend)
        else:
            self.eat()

class Carnivore(Animal):
    def eat(self):
        print(self.name, "eats meat.")
        self.change_energy(+20)

    def hunt(self, prey):
        print(self.name, "hunts", prey.name)
        self.change_energy(-15)
        prey.change_energy(-30)

    def act(self, zoo):
        if not self.can_act():
            self.sleep()
            return

        # DAY 2 LOGIC: hunt only if hungry
        if self.energy < 40:
            prey = zoo.find_herbivore()
            if prey:
                self.hunt(prey)
            else:
                self.sleep()
        else:
            self.sleep()

class Visitor:
    def __init__(self, name):
        self.name = name

    def feed(self, animal):
        if animal.alive:
            print(self.name, "feeds", animal.name)
            animal.eat()

class Zoo:
    def __init__(self, animals, visitor):
        self.animals = animals
        self.visitor = visitor
        self.day = 1

    def find_herbivore(self, exclude=None):
        for animal in self.animals:
            if isinstance(animal, Herbivore) and animal.alive and animal != exclude:
                return animal
        return None

    def simulate_day(self):
        print("\n--- Day", self.day, "at the Zoo ---")

        for animal in self.animals:
            if animal.alive:
                animal.act(self)

        print("\nVisitor time:")
        for animal in self.animals:
            self.visitor.feed(animal)

        print("\nNight time:")
        for animal in self.animals:
            if animal.alive:
                animal.sleep()

        self.day += 1

lion = Carnivore("Leo")
tiger = Carnivore("Shera")
elephant = Herbivore("Ella")
monkey = Herbivore("Momo")

animals = [lion, tiger, elephant, monkey]

visitor = Visitor("Bob")

zoo = Zoo(animals, visitor)

zoo.simulate_day()
zoo.simulate_day()
zoo.simulate_day()





