# LAB 1 — Range & Loops (Numbers and Iteration)
# Create a program that:
# 1. Prints all odd numbers from 1–20
# 2. Calculates and prints the sum of numbers from 1–100
# 3. Asks the user for a number and prints its multiplication table (1–10)
# Goal: Practice range(), loops, and numeric iteration.

# 1. Print all odd numbers from 1–20
# print("Odd numbers from 1 to 20:")
# for num in range(1, 21):
#     if num % 2 != 0:
#         print(num)



# 2. Calculate and print the sum of numbers from 1–100
# print("\n")
# total_sum = 0
# for num in range(1, 101):
#     total_sum += num
# print(f"Total sum of digits from 1 to 100 is {total_sum}")


# 3. Ask the user for a number and print its multiplication table (1–10)
# n = int(input("Enter a number to see its multiplication table of it: "))

# print(f"Multiplication table for {n}:")
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# LAB 2 — Lists & Comprehensions
# Create a program that:
# 1. Takes a given list of numbers
# 2. Generates and prints:
# o A list of squares using a loop
# o A list of squares using a list comprehension
# o A list of positive numbers using a comprehension
# Goal: Practice list operations, loops, and list comprehensions.

# user_input = input("Enter numbers separated by spaces: ")
# x = [int(n) for n in user_input.split()]
# print (f"List of numbers is {x}")

# #A list of squares using a loop
# squares = []
# for n in x:
#     squares.append(n ** 2)
# print(f"List of squares of list numbers is using loop is {squares}")


# #A list of squares using a list comprehension
# squares_comp = [n**2 for n in x]
# print(f"List of squares of list numbers is using list comprehension is: {squares_comp}")


# LAB 3 — Functions & Conditionals
# Create functions that:
# 1.Return a greeting with a name

# def greeting(name):
#     print(f"Hello {name}, Have a nice day!")

# greeting(name='Krishna')

# 2.Return a default greeting if no name is given

# def greeting(name = "Default_name"):
#     print(f"Hello {name}, Have a nice day!")

# greeting()

# 3.Check if a number is even

# x = int(input("Enter a number to check if it is even: "))

# def evennum(num):
#     if num % 2 == 0:
#       print(num, "is even.")
#     else:
#       print(num, "is odd.")

# evennum(x)
    
# 4.Add two numbers only if both are even, otherwise return 0

# def addEvenOnly(num1,num2):
#    if (num1 % 2!= 0) or (num2 % 2!= 0):
#       return 0
#    else:
#       return (num1 + num2)
   
# y = addEvenOnly(2,4)
# print(y)
# x = addEvenOnly(1,4)
# print(x)
# a = addEvenOnly(1,3)
# print(a)
      
# Goal: Practice function creation, return values, and conditional logic.


#LAB 4 — Filter & Lambda Functions
#Create programs that:
#Use filter() + a function to keep only even numbers
#Use filter() + lambda to keep only even numbers
#Filter names that have 3 or more characters

# 1. Use filter() + a function to keep only even numbers
# nums = list(range(1, 11))

# def is_even(n):
#     return n % 2 == 0

# evens_with_func = list(filter(is_even, nums))
# print("Evens using filter + function:", evens_with_func)

# 2. Use filter() + lambda to keep only even numbers
# evens_with_lambda = list(filter(lambda x: x % 2 == 0, nums))
# print("Evens using filter + lambda:", evens_with_lambda)

# 3. Filter names that have 3 or more characters
# names = ["Al", "Bob", "Eve", "Sam", "Li", "Ana", "Tom"]
# a = list(filter(lambda s: len(s) >= 3, names))
# print("Names with 3+ characters:", a)

# 4. Filter words that contain the letter "a"

# words = ["apple", "banana", "pear", "kiwi", "grape", "orange", "fig"]

# def has_a(word):
#     return "a" in word

# filtered_words = list(filter(has_a, words))

# print("Words containing 'a':", filtered_words)



# **LAB 5 — *args and kwargs
# Create functions that:
# 1.Accept any number of values using *args and return their sum

# def sum_values(*args):
#     return sum(args)

# # Example:
# print(sum_values(1,2,3))

# 2.Accept any number of values using *args and return the maximum
# def max_values(*args):
#     return max(args)

# # Example:
# print(max_values(1,2,3))

# 3.Accept any number of keyword arguments using **kwargs and print them

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Example:
# print_kwargs(name="Alice", age=25, country="USA")

# 4.Combine a, *args, and **kwargs and print all arguments in a readable way
def show_all(a, *args, **kwargs):
    print("First argument (a):", a)

    print("\nAdditional positional arguments (*args):")
    for item in args:
        print(" -", item)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")


# Example usage:
show_all(
    10,
    20, 30, 40,
    name="Alice",
    age=25,
    country="USA"
)

# Goal: Practice flexible function parameters and argument unpacking.


# LAB 6 — Even Number Filter Tool (Mini Project)
# Create a program that:
# 1. Accepts a line of numbers from the user
# 2. Converts the input into a list of integers
# 3. Uses filter() + lambda to keep only even numbers
# 4. Prints:
# o The list of even numbers
# o The count of even numbers
# Goal: Practice input handling, list processing, and the filter() function.

# 1. Accept a line of numbers from the user
user_input = input("Enter numbers separated by spaces: ")

# 2. Convert input into a list of integers
numbers = [int(n) for n in user_input.split()]

# 3. Use filter() + lambda to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 4. Print results
print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))


