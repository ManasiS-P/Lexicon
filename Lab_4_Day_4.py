# <!-- Python Tasks: Scope, LEGB, and Basic OOP

# 1. Local vs Global Variable
#    Create a program that demonstrates the difference between a local variable and a global variable. The program should clearly show both values. -->

global_v = 10

def my_function(): 
   local_v = 5

   print("Inside the function:")
   print(global_v)   
   print(local_v)    

my_function()

print(f"Outside the function: {global_v}")
#print(f"Outside the function: {local_v}") #Throws a NameError as it is a loccal variable defined in the function, Can't be accessed out of function


# <!-- 2. Function Using a Global Variable
#    Write a function that reads the value of a global variable without changing it. Show in the output that the global value remains the same after the function call. -->

global_v = 10

def global_a():
    print("Inside the function, global_v =", global_v)

global_a()

print("Outside the function, global_v =", global_v)


# <!-- 3. Function That Modifies a Global Variable
#    Write a program where a function changes the value of a global variable using the global keyword.Display the value before and after the function call. -->

x = 5

def key_global():
    global x      
    x = 20        
    print("Inside the function, x =", x)

print("Before calling the function, x =", x)

key_global()

print("After calling the function, x =", x)


# <!-- 4. Local Variable Shadowing a Global Variable
#    Create an example where a global variable and a local variable have the same name. The program should demonstrate which value is used inside the function and which is used outside. -->

name = "Global Python"

def show_value_name():
    name = "Local Python"
    print("Inside the function, name =", name)

print("Outside the function, name =", name)

show_value_name()

print("After calling the function, name =", name)






# 5. Inner Function and the LEGB Rule
#    Write a function that contains an inner function. Use print statements to show which version of a name is being used (local, enclosing, or global). -->

name = "Global_N"

def outer_func():
    name = "Enclosing_N"

    def inner_func():
        name = "Local_N"

        print("Inside inner_func, name =", name)

    print("Inside outer_function, before calling inner_function, name =", name)
    inner_func()
    print("Inside outer_function, after calling inner_function, name =", name)

print("Outside all functions, name =", name)
outer_func()
print("After calling outer_function, name =", name)


# <!-- 6. Using nonlocal
#    Create an example where an inner function modifies a variable in the enclosing function using the nonlocal keyword. Show the change before and after. -->

def outer_func():
    x = 10  
    print("Before inner_function call, x =", x)

    def inner_func():
        nonlocal x   
        x = 20       
        print("Inside inner_function, x =", x)

    inner_func()
    print("After inner_function call, x =", x)

outer_func()


# <!-- 7. Creating Your Own Class
#    Write a class with at least two instance attributes and a method that prints or returns information based on those attributes. Create at least two objects and demonstrate that they can have different values. -->

class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def show_info(self):
        print(f"This Dog is of {self.breed} breed and it's name is {self.name}.")

dog1 = Dog("Husky", "Mike")
dog2 = Dog("Lab", "Tommy")

dog1.show_info()   
dog2.show_info()  



# <!-- 8. Class Attribute vs Instance Attribute
#    Create a program demonstrating a class attribute shared across multiple objects. Then change the attribute for only one object and show that the other objects still use the original class attribute. -->


class Dog:
    species = "Mammal"

    def __init__(self, breed,name):
        self.breed = breed 
        self.name = name  

# Create two objects
dog1 = Dog("Husky", "Mike")
dog2 = Dog("Lab", "Tommy")

print(f"This Dog is of {dog1.breed} breed and it's name is {dog1.name} and it's species are {dog1.species}.")
print(f"This Dog is of {dog2.breed} breed and it's name is {dog2.name} and it's species are {dog2.species}.")

dog1.species = "Human"   

print(f"This Dog is of {dog1.breed} breed and it's name is {dog1.name} and it's species are {dog1.species}.")
print(f"This Dog is of {dog2.breed} breed and it's name is {dog2.name} and it's species are {dog2.species}.")







# <!-- 9. Class With a Calculation Method
#    Write a class with one attribute and a method that calculates something based on that attribute (for example area, price, or length). Show how changing the attribute affects the calculation. -->

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return 3.14 * self.radius ** 2 
    
circle = Circle(3)

print("Area of circle is :", circle.area())


circle.radius = 5

print("Updated area of circle:", circle.area())








# <!-- 10. Method for Updating an Attribute
#     Write a class where an attribute can be updated through a custom method. Demonstrate how the updated attribute changes the behavior of another method in the class. -->

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2  

    def setRadius(self, radius):
        self.radius = radius  

    def getRadius(self):
        return self.radius

c = Circle()
print("Radius:", c.getRadius())
print("Area:", c.area())

c.setRadius(2)
print("Updated radius:", c.getRadius())
print("Updated area:", c.area())  



# <!-- Challenge Tasks
# Challenge 1 – Tracking Variable Changes Across Scopes
# Create a program that uses three nested functions. Each function should have a variable with the same
# name but different values. Use print statements to show exactly which value is used at each level, and
# experiment with both nonlocal and global to change the outcome. -->

name = "Global_N"

def outer_func():
    
    name = "Enclosing_N"

    def inner_func():
        nonlocal name 
        name = "Local_N"
        print("Inside inner_func before nonlocal change, name =", name)

         
        name = "Inner changed Enclosing_N"
        print("Inside inner_func after nonlocal change, name =", name)

    print("Inside outer_func before calling inner_func, name =", name)
    inner_func()
    print("Inside outer_func after calling inner_func, name =", name)

print("Outside all functions, name =", name)
outer_func()
print("After calling outer_func, name =", name)

# Using global to modify the global variable
def change_global():
    global name
    print("Inside change_global before change, name =", name)
    name = "Global_N changed"
    print("Inside change_global after change, name =", name)

change_global()
print("Global name after change_global call:", name)


# <!--
# Challenge 2 – Class With Both Class-Level and Instance-Level Behavior
# Write a class that uses:

# - at least one class attribute
# - at least one instance attribute
# - at least one method that uses the class attribute
# - at least one method that uses only the instance attributes
#   Then add a way to change the class attribute and show how this affects all existing objects. Also show
#   how changing an instance attribute affects only one object. -->


class BankAccount:
    # Class attribute (shared by all objects)
    bank_name = "Global Bank"

    def __init__(self, account_holder, balance):
        # Instance attributes (unique to each object)
        self.account_holder = account_holder
        self.balance = balance

    # Method using the class attribute
    def show_bank_name(self):
        print(f"Bank name: {BankAccount.bank_name}")

    # Method using only instance attributes
    def show_account_info(self):
        print(f"Account holder: {self.account_holder}, Balance: ${self.balance}")

# Create two objects
acc1 = BankAccount("Alice", 500)
acc2 = BankAccount("Bob", 1000)

# Show initial state
print("Initial state:")
acc1.show_bank_name()
acc1.show_account_info()
acc2.show_bank_name()
acc2.show_account_info()

# Change the class attribute
BankAccount.bank_name = "New Global Bank"
print("\nAfter changing the class attribute:")
acc1.show_bank_name()
acc2.show_bank_name()

# Change an instance attribute
acc1.balance = 800
print("\nAfter changing acc1's balance:")
acc1.show_account_info()  # Only acc1's balance changes
acc2.show_account_info()  # acc2 remains the same

#   <!-- Challenge 3 – Object Interaction
#   Create two different classes where objects from one class interact with objects from the other.
#   Demonstrate how these interactions work and how changing attributes in one object affects the result in
#   the other. -->
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []  # List of enrolled courses

    def enroll(self, course):
        self.courses.append(course)   # Add course to student's list
        course.add_student(self)      # Add student to course's list

    def show_courses(self):
        course_names = [course.name for course in self.courses]
        print(f"{self.name} is enrolled in: {course_names}")


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # List of enrolled students

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        student_names = [student.name for student in self.students]
        print(f"Course {self.name} has students: {student_names}")


# Create some courses
math = Course("Math")
science = Course("Science")

# Create some students
alice = Student("Alice")
bob = Student("Bob")

# Students enroll in courses
alice.enroll(math)
alice.enroll(science)
bob.enroll(math)

# Show enrollments
alice.show_courses()
bob.show_courses()
math.show_students()
science.show_students()

# Change an attribute in one object
math.name = "Advanced Math"
print("\nAfter changing course name:")
alice.show_courses()   # Alice's course list still references the updated course name
math.show_students()   # Shows updated course name in interaction
