#SECTION 1 — Pythonic Classes & Properties 
# 1. Create a class with a property and setter. 
# Create a class with one attribute that can only be accessed and modified through a property and setter. 
# Include a method that performs a calculation using the attribute.

class Rectangle:
    def __init__(self, width):
        self.width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = value

    def area(self):
        return self._width ** 2
    

rect = Rectangle(5)
print(rect.width)      
print(rect.area())     

rect.width = 10
print(rect.area())     
    
# Create a class with a clean __str__ representation. Create a class with at least
# three attributes and implement __str__ to make printed objects readable and
# nicely formatted.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (
            f"Book Information\n"
            f"Title : {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages : {self.pages}"
        )
book = Book("1984", "George Orwell", 328)
print(book)
  
# 3. Create a class with a meaningful __repr__. Create a class where __repr__ returns
# a string that could realistically recreate the object.

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name!r}, role={self.role!r}, salary={self.salary!r})"
    
emp = Employee("Alice", "Software Engineer", 95000)

print(emp)

emp_copy = eval(repr(emp))
print(emp_copy)

# Create a class that initializes from **kwargs. Write a class where attributes are
# automatically created from keyword arguments, even when di erent objects
# receive di erent arguments.

class FlexibleObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

obj1 = FlexibleObject(name="Alice", age=30)
obj2 = FlexibleObject(title="Engineer", salary=90000, remote=True)

print(obj1.name)      
print(obj1.age)       

print(obj2.title)     
print(obj2.salary)    
print(obj2.remote)    

# Create a class that builds its string using a comprehension. 
# Write a class whose __str__ method constructs its output using a comprehension and join().


class Person:
    def __init__(self, **attributes):
        self.attributes = attributes

    def __str__(self):
        lines = (
            f"{key}: {value}"
            for key, value in self.attributes.items()
        )
        return "\n".join(lines)
    
p = Person(name="Alice", age=30, city="New York")
print(p)


# SECTION 2 — Dunder Methods
# 6. Implement __eq__. Create a class where two objects are equal if their attributes
# match.
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__dict__ == other.__dict__

s1 = Student("Alice", "S123", "Computer Science")
s2 = Student("Alice", "S123", "Computer Science")
s3 = Student("Bob", "S456", "Math")

print(s1 == s2)  
print(s1 == s3)  

# 7. Implement __lt__. Create a class where objects can be compared using < based
# on one chosen attribute.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price


p1 = Product("Laptop", 1200)
p2 = Product("Tablet", 600)
p3 = Product("Phone", 900)

print(p2 < p1)   
print(p1 < p3)   

# Sorting works automatically
products = [p1, p2, p3]
print(sorted(products))

# 8. Implement __add__. Create a class where adding two objects with + produces a
# new combined object.
class CartItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __add__(self, other):
        if not isinstance(other, CartItem):
            return NotImplemented

        if self.name != other.name:
            raise ValueError("Can only add items with the same name")

        return CartItem(
            self.name,
            self.quantity + other.quantity
        )

    def __repr__(self):
        return f"CartItem(name={self.name!r}, quantity={self.quantity})"

item1 = CartItem("Apple", 3)
item2 = CartItem("Apple", 5)

combined = item1 + item2
print(combined)


# Implement __len__. Create a class where len(object) returns a meaningful
# numeric value based on internal data.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)
    
playlist = Playlist(["Song A", "Song B", "Song C"])

print(len(playlist))

# 10. Implement __contains__. Create a class where you can check "value in object"
# using __contains__.

class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books

library = Library(["1984", "Brave New World", "Fahrenheit 451"])

print("1984" in library)        
print("The Hobbit" in library) 


# 11. Implement __getitem__. Create a class that allows indexing with square brackets
# to access internal data.

class GradeBook:
    def __init__(self, grades):
        self.grades = grades

    def __getitem__(self, index):
        return self.grades[index]

gb = GradeBook([85, 90, 78, 92])

print(gb[0])    
print(gb[2])    

# SECTION 3 — Comprehension Exercises
# 12. Rewrite a loop using a list comprehension. Convert any loop-based list
# transformation into a single list comprehension.

numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers]

print(squared_numbers)  

# 13. Create a filtered list comprehension. Make a comprehension that filters elements
# based on a condition.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)  # [2, 4, 6, 8, 10]


# 14. Create a dictionary using a dict comprehension. Use two lists and combine them
# into a dictionary via comprehension.

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

# Combine into a dictionary
person_dict = {k: v for k, v in zip(keys, values)}

print(person_dict)

# 15. Build a formatted string using a comprehension. Generate a formatted string
# from object or dictionary data using comprehension and join().

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

formatted_string = "\n".join(f"{key}: {value}" for key, value in person.items())

print(formatted_string)

# 16. Create a nested comprehension. Generate a two-dimensional structure (like a
# table or grid) with nested comprehensions. 
# Generate a 5x5 multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

for row in table:
    print(row)

# SECTION 4 — Combined OOP + Scope + Pythonic Techniques
# 17. Demonstrate LEGB with nested functions. Create a function that contains
# another function. Use variables with the same name at multiple levels and
# demonstrate which is used where. Modify the enclosing variable using nonlocal.

# # Global scope
x = "global x"

def outer():
    # Enclosing (outer) scope
    x = "enclosing x"

    def inner():
        nonlocal x  # refers to 'x' in outer()
        x = "modified enclosing x"  # modifies enclosing variable
        y = "local y"
        print("Inside inner():")
        print("x =", x)  # enclosing variable modified
        print("y =", y)  # local variable

    print("Before calling inner():")
    print("x =", x)
    inner()
    print("After calling inner():")
    print("x =", x)  # reflects modification by inner()

print("Global x before outer():", x)
outer()
print("Global x after outer():", x)

# 18. Create a class that processes input using a comprehension. Write a class that
# receives a list or dictionary and transforms or filters the data internally using a
# comprehension.

class NumberProcessor:
    def __init__(self, numbers):
        """
        numbers: list of integers
        Stores only the squares of even numbers internally.
        """
        self.processed = [n ** 2 for n in numbers if n % 2 == 0]

    def get_processed(self):
        return self.processed

numbers = [1, 2, 3, 4, 5, 6]
processor = NumberProcessor(numbers)

print(processor.get_processed())

# 19. Create a class that builds itself from a dictionary. Write a class that receives a
# dictionary and turns every key/value pair into attributes. Build __str__ using a
# comprehension.
class DynamicObject:
    def __init__(self, data):
        """
        data: dictionary
        Each key/value pair becomes an instance attribute
        """
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self):
        # Build formatted string from all attributes
        return "\n".join(f"{k}: {v}" for k, v in self.__dict__.items())

data = {"name": "Alice", "age": 30, "city": "New York"}
obj = DynamicObject(data)

print(obj)

# 20. Combine kwargs, property, and a dunder method. Create a class that: - accepts
# all attributes via **kwargs - includes at least one property with getter and setter -
# implements one or more dunder methods - includes a method that performs a
# # calculation using its data
class BankAccount:
    def __init__(self, **kwargs):
        # Accept any attributes via kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        # Ensure balance exists
        if not hasattr(self, "_balance"):
            self._balance = 0

    # Property with getter and setter
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    # Method performing a calculation
    def apply_interest(self, rate):
        """Apply interest to the balance (rate as decimal, e.g., 0.05 for 5%)"""
        self._balance += self._balance * rate
        return self._balance

    # Dunder method for clean string representation
    def __str__(self):
        attrs = ", ".join(f"{k}: {v}" for k, v in self.__dict__.items() if not k.startswith("_"))
        return f"BankAccount({attrs}, balance: {self._balance})"

    # Dunder method for equality comparison
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance == other._balance



# Create account with dynamic attributes
account = BankAccount(owner="Alice", account_type="Savings", _balance=1000)

print(account)  
# BankAccount(owner: Alice, account_type: Savings, balance: 1000)

# Access and modify balance through property
account.balance += 500
print(account.balance)  # 1500

# Apply interest
account.apply_interest(0.05)
print(account.balance)  # 1575.0

# Compare accounts
account2 = BankAccount(owner="Bob", _balance=1575)
print(account == account2)  # True


