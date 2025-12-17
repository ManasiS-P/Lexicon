# Inheritance & OOP – Exercise Set
# 1. Constructor Execution Order
# Create a base class and two subclasses that form an inheritance chain.
# Each class must print a message from its constructor.
# Create an object of the most derived class and observe the order in which the constructors are executed.
# Use super() in all constructors.

class Animal:
    def __init__(self):
        print("Animal called")

class Mammal(Animal):
    def __init__(self):
        super().__init__()  
        print("Mammal called")

class Dog(Mammal):
    def __init__(self):
        super().__init__()  
        print("Dog called")

x = Dog()


# 2. Modifying State Through super()
# Create a base class that stores a numeric value.
# Create two subclasses that modify this value in di erent ways inside their
# constructors.
# Use super() so that each class in the inheritance chain contributes to the final value.
# Print the final result.

class Number:
    def __init__(self, value):
        self.value = value
        print("Number constructor: value =", self.value)



class AddFive(Number):
    def __init__(self, value):
        super().__init__(value)
        self.value += 5
        print("AddFive constructor: value =", self.value)



class AddTen(AddFive):
    def __init__(self, value):
        super().__init__(value)
        self.value += 10
        print("AddTen constructor: value =", self.value)



result = AddTen(10)

print("Final value:", result.value)


# 3. Multiple Inheritance and MRO
# Create two parent classes that both modify the same attribute in their constructors.
# Create a child class that inherits from both parents.
# Use super() in all constructors.
# Print the final value and print the MRO of the child class.
# Explain why the final value is produced.

class Number:
    def __init__(self):
        self.value = 0
        print("Number constructor: value =", self.value)

class AddFive(Number):
    def __init__(self):
        super().__init__()
        self.value += 5
        print("AddFive constructor: value =", self.value)

class AddTen(Number):
    def __init__(self):
        super().__init__()
        self.value += 10
        print("AddTen constructor: value =", self.value)

class Result(AddFive, AddTen):
    def __init__(self):
        super().__init__()
        print("Result constructor: value =", self.value)


# Create object
r = Result()

print("Final value:", r.value)
print("MRO:", Result.mro())

# 4. Predict and Verify MRO
# Create a diamond-shaped inheritance structure with four classes.
# Before running the program, write down what you believe the MRO will be.
# Then print the actual MRO and compare it with your prediction.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

#Prediction = D,B,C,A
print(D.mro())


# 5. Overriding a Method and Calling the Parent
# Create a base class with a method that prints a message.
# Override this method in a subclass.
# Inside the overridden method, call the parent version using super() and then add
# additional behavior.
# Call the method and show both outputs.



class Animal:
    def bark(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        super().bark()
        print("Dog barks")

dog = Dog()

dog.bark()

# 6. Class Variables Across Inheritance
# Create a base class with a class variable.
# Create two subclasses.
# Override the class variable in one subclass but not the other.
# Create objects from all classes and show how the value differs depending on which
# class is used.

class Vehicle:
    wheels = 4 

    def show_wheels(self):
        print(f"{self.__class__.__name__} wheels:", self.wheels)

class Car(Vehicle):
    pass

class Bike(Vehicle):
    wheels = 2

vehicle = Vehicle()
car = Car()
bike = Bike()

vehicle.show_wheels()
car.show_wheels()
bike.show_wheels()

# 7. Protected Attributes
# Create a base class that uses a protected attribute (single underscore).
# Access and modify this attribute from a subclass.
# Demonstrate that the attribute can be accessed, and explain why this is allowed but discouraged outside the class hierarchy.

class Person:
    def __init__(self, name):
        self._name = name   

class Employee(Person):
    def show_name(self):
        print("Employee name:", self._name)

x = Person("Alice")
y = Employee("Bob")

y.show_name()
print("Person name:", x._name)

#They should not be used as they might give the internal details of the class

# 9. Overriding __str__ in a Subclass
# Create a base class with a meaningful __str__ method.
# Override __str__ in a subclass.
# Use super().__str__() inside the subclass and add subclass-specific information.
# Print objects of both classes to show the difference.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) 
        self.salary = salary

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, salary={self.salary}"

x = Person("Alice", 30)
y = Employee("Bob", 40, "45000")


print(x)  
print(y)  

# 8. Private Attributes and Name Mangling
# Create a base class with a private attribute using double underscores.
# Attempt to access the attribute directly and observe what happens.
# Then access it using name mangling and explain how Python handles private
# attributes internally.

# Base class
class Account:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def show_balance(self):
        print("Balance:", self.__balance)


# Create object
acc = Account(1000)

# Attempt to access directly (will fail)
try:
    print(acc.__balance)
except AttributeError as e:
    print("Error:", e)

# Access using name mangling (works)
print("Access using name mangling:", acc._Account__balance)

# Use class method to show balance (recommended)
acc.show_balance()


# # 10. Design Task – Controlled Inheritance
# Design a small inheritance hierarchy that models a real-world concept.
# Requirements:
# - Use inheritance and super() correctly
# - Override at least one method
# - Include at least one class variable
# - Include either a protected or private attribute
# - Do not use polymorphism or duck typing
# Create objects and demonstrate that the inheritance structure works as intended.

# Base class
class Animal:
    species = "Unknown"  # class variable

    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected attribute
        print(f"Animal created: {self.name}, age: {self._age}")

    def speak(self):
        return f"{self.name} makes a sound."


# Subclass
class Dog(Animal):
    species = "Dog"  # override class variable

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        print(f"Dog created: {self.name}, breed: {self.breed}")

    # Override speak method
    def speak(self):
        base_speak = super().speak()
        return f"{base_speak} {self.name} barks."


# Subclass of Dog
class Husky(Dog):
    species = "Husky"  # override class variable

    def __init__(self, name, age, breed, color):
        super().__init__(name, age, breed)
        self.color = color
        print(f"Husky created: {self.name}, fur color: {self.color}")

    # Override speak method
    def speak(self):
        base_speak = super().speak()
        return f"{base_speak} {self.name} howls like a Husky."


# Create objects
a = Animal("GenericAnimal", 5)
d = Dog("Buddy", 3, "Labrador")
h = Husky("Ghost", 2, "Husky", "White")

# Demonstrate method overriding
print("\nSpeaks:")
print(a.speak())
print(d.speak())
print(h.speak())

# Show class variable usage
print("\nSpecies:")
print(a.species, d.species, h.species)

# Access protected attribute (allowed in subclass)
print("\nAges (protected attribute):")
print(a._age, d._age, h._age)




