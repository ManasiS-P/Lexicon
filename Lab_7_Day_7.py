# LAB 1 — Discover Duck Typing
# Objective
# Understand that shared behavior, not shared type, enables polymorphism.
# Instructions
# 1. Write a function that:
# o accepts a single argument
# o calls one method on that argument
# 2. Call the function with:
# o a built-in type
# o a custom class you create yourself
# 3. The function must work without modification for both.
# Constraints
# • Do NOT use isinstance
# • Do NOT check types explicitly


# def make_it_upper(obj):
#     return obj.upper()

# text = "python"
# print(make_it_upper(text))

# class Shout:
#     def __init__(self, message):
#         self.message = message

#     def upper(self):
#         return self.message.upper() 


# custom = Shout("python programming")
# print(make_it_upper(custom))


# LAB 2 — Break Duck Typing on Purpose
# Objective
# Understand the risk of duck typing.
# Instructions
# 1. Take your function from Lab 1.
# 2. Pass an object that does not implement the expected behavior.
# 3. Observe the error.
# 4. Explain:
# o when the error occurs

# def make_it_upper(obj):
#     return obj.upper()

# number = 42
# make_it_upper(number)

#The error occurs at runtime, not when the function is defined.


# LAB 3 — EAFP vs LBYL
# Objective
# Practice EAFP-style error handling.
# Instructions
# 1. Write a function that:
# o performs an operation on two inputs
# o may fail depending on the inputs
# 2. Implement it using:
# o try
# o except
# 3. Test the function with:
# o valid inputs
# o invalid inputs
# o edge cases
# Constraints
# • Do NOT use isinstance
# • Do NOT pre-check types

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Error: division by zero"
#     except Exception as e:
#         return f"Error: {e}"


# print(divide(10, 2))
# print(divide(5.0, 2))
# print(divide(10, 0))
# print(divide("10", 2))
# print(divide(0, 5))     

# LAB 4 — Build Polymorphism with Inheritance
# Objective
# Understand method overriding and runtime dispatch.
# Instructions
# 1. Design a base class representing a general concept.
# 2. The base class must define a method but not implement it.
# 3. Create at least three subclasses that:
# o inherit from the base class
# o override the method with different behavior
# 4. Write a function that:
# o accepts the base class
# o calls the method
# o does NOT use conditionals
# 5. Call the function with each subclass.
# Constraints
# • Do NOT use if, elif, or isinstance


# class Animal:
#     def speak(self):
#         raise NotImplementedError

# class Dog(Animal):
#     def speak(self):
#         return "Bark"

# class Cat(Animal):
#     def speak(self):
#         return "Meow"

# class Cow(Animal):
#     def speak(self):
#         return "Moo"

# def animal_speak(animal):
#     print(animal.speak())

# animal_speak(Dog())
# animal_speak(Cat())
# animal_speak(Cow())

# LAB 5 — Feel the Pain of isinstance
# Objective
# Recognize why type-check chains do not scale.
# Instructions
# 1. Write a function that:
# o accepts an object
# o behaves differently depending on the object’s type
# o uses isinstance
# 2.Add a new class that should be supported.
# 3.Identify all places that must be modified.
# 4.Redesign the solution using polymorphism so:
# o new classes require no changes to existing functions

# class Dog:
#     def speak(self):
#         return "Woof"

# class Cat:
#     def speak(self):
#         return "Meow"


# def make_sound(animal):
#     if isinstance(animal, Dog):
#         return animal.speak()
#     elif isinstance(animal, Cat):
#         return animal.speak()
#     else:
#         return "Unknown animal"

# #A new supported function
# class Cow:
#     def speak(self):
#         return "Moo"
# #Modification to be done
# # elif isinstance(animal, Cow):
# #     return animal.speak()

# #using polymorphism
# class Animal:
#     def speak(self):
#         raise NotImplementedError

# class Dog(Animal):
#     def speak(self):
#         return "Woof"

# class Cat(Animal):
#     def speak(self):
#         return "Meow"

# class Cow(Animal):
#     def speak(self):
#         return "Moo"
# #Function added afterwards
# class Sheep(Animal):
#     def speak(self):
#         return "Baa"
    
# def make_sound(animal):
#     return animal.speak()


# LAB 6 — Abstract Base Class Enforcement
# Objective
# Understand why ABCs exist.
# Instructions
# 1. Design an abstract base class that:
# o represents a role or capability
# o defines at least one abstract method
# 2. Attempt to:
# o create a subclass that does not implement the method
# o instantiate it
# 3. Observe and explain the error.
# 4. Create:
# o one valid subclass
# o a second valid subclass with different behavior
# 5. Write a function that:
# o accepts the abstract base class
# o calls the abstract method


# from abc import ABC, abstractmethod

# class Button(ABC):
#     @abstractmethod
#     def click(self):
#         pass

# class BrokenButton(Button):
#     pass
# #b = BrokenButton()

# class SaveButton(Button):
#     def click(self):
#         return "File saved"

# class CancelButton(Button):
#     def click(self):
#         return "Action cancelled"

# def press(button):
#     print(button.click())

# press(SaveButton())
# press(CancelButton())


# LAB 7 — Duck Typing vs ABCs (Comparison Lab)
# Objective
# Compare flexibility vs safety.
# Instructions
# 1. Solve the same problem twice:
# o once using duck typing
# o once using an abstract base class
# 2. Intentionally violate the expected interface in both versions.
# 3. Compare:
# o error timing
# o error messages
# o developer experience

# #Duck Typing
def start_device(device):
    device.start()

# class Phone:
#     def start(self):
#         print("Phone started")
# start_device(Phone())


# class Rock:
#     pass
# start_device(Rock())


#Abstract Base Class
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def start(self):
        pass

class Laptop(Device):
    def start(self):
        print("Laptop started")

start_device(Laptop())

class BrokenDevice(Device):
    pass

bad = BrokenDevice()







