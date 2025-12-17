# LAB 1 — Python Calculator (Numbers & Arithmetic)
# Create a program that:
# 1. Takes two numbers from the user
# 2. Calculates and prints:
# o Sum
# o Difference
# o Product
# o Division
# o Power
# 3. Print the results in a nicely formatted way.
# Goal: Practice numeric operations & print formatting.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))        

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
power_result = num1 ** num2 

print("\nResults:")
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {difference_result}")
print(f"Product: {num1} * {num2} = {product_result}")
print(f"Division: {num1} / {num2} = {division_result}")
print(f"Power: {num1} ** {num2} = {power_result}")


# LAB 2 — Variables & Reassignment
# Students must:
# 1. Create variables for salary, bonus, and tax_rate.
# 2. Calculate:
# o total income
# o taxes
# o net income
# 3. Reassign variables to simulate a raise and recalc everything.
# Goal: Understand variable assignment and updating values.

salary = 50000
bonus = 5000
tax_rate = 0.2

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes
print("\nInitial Income Calculation:")
print(f"Total Income: ${total_income}")
print(f"Taxes: ${taxes}")
print(f"Net Income: ${net_income}") 

salary += 10000  
bonus += 2000    

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes
print("\nAfter Raise Income Calculation:")
print(f"Total Income: ${total_income}")
print(f"Taxes: ${taxes}")
print(f"Net Income: ${net_income}")


# LAB 3 — String Indexing & Slicing Explorer
# Given the string:
# s = "ProgrammingIsFun"
# Students must extract:
# 1. The first letter
# 2. The last 3 letters
# 3. Every second letter
# 4. The word "Programming"
# 5. The word "Fun" without using indices directly (must use slicing)
# 6. The string reversed
# Goal: Practice indexing, slicing, stepping.

s = "ProgrammimgIsFun"

first_letter = s[0]
last_three_letters = s[-3:]
every_second_letter = s[::2]
word_programming = s[:11]
word_fun = s[-3:]
reversed_string = s[::-1]

print(s)
print("First letter:", first_letter)
print("Last 3 letters:", last_three_letters)
print("Every second letter:", every_second_letter)
print("The word 'Programming':", word_programming)
print("The word 'Fun':", word_fun)
print("Reversed string:", reversed_string)  

# LAB 4 — String Methods Investigation
# Using a string from user input, students must show:
# 1. Uppercase version
# 2. Lowercase version
# 3. How many characters the string has
# 4. Split the string into words
# 5. Replace one letter with another
# Goal: Practice built-in string methods & transformations.

user_string = input("Enter a string: ")     
uppercase_string = user_string.upper()
lowercase_string = user_string.lower()
string_length = len(user_string)
split_string = user_string.split()
replaced_string = user_string.replace('a', 'o')  

print("\nString Transformations:")
print("Uppercase:", uppercase_string)
print("Lowercase:", lowercase_string)
print("Length:", string_length)
print("Split into words:", split_string)
print("Replaced string (a -> o):", replaced_string)

# LAB 5 — Username Generator
# Ask the user for:
# • First name
# • Last name
# • Birth year
# Then generate a username using slicing, for example:
# first 2 letters of first name + last 3 letters of last name + last 2 digits of birth year
# Goal: Combine indexing, slicing, formatting, variables.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year (e.g., 1990): ")  

username = first_name[:2] + last_name[-3:] + birth_year[-2:]

print(f"Your generated username is: {username}")

# LAB 6 — List Builder
# Students must:
# 1. Create a list with 5 mixed-type elements
# 2. Use append() to add two new items
# 3. Use pop() to remove an element
# 4. Reverse the list
# 5. Sort the list (if possible)
# 6. Print the final result
# Goal: Practice list manipulation.


my_list = [42, "Hello", 3.14, True, "World"]

my_list.append("New Item 1")
my_list.append(99)

removed_element = my_list.pop(2)

my_list.reverse()

#In today's morning lecture we studied that to sort a list, all elements must be of the same type.

print("Final list after manipulations:", my_list)

# LAB 7 — Shopping Cart Program
# Simulate a shopping cart using lists.
# Steps:
# 1. 2. 3. Start with an empty list cart = []
# Ask user 5 times to input an item and append it
# After all items are added:
# o Print the full cart
# o Remove the last item
# o Show how many items remain
# o Print only the first and last items
# Goal: Combine lists, len(), append(), pop(), indexing.



cart = []

for i in range(5):
    item = input(f"Enter item {i + 1}: ").strip()
    cart.append(item)

print("\nFull cart:", cart)

removed_item = cart.pop()
print("Removed last item:", removed_item)

print("Items remaining:", len(cart))

first_item = cart[0]
last_item = cart[-1]

print("First item:", first_item)
print("Last item:", last_item)



# LAB 8 — Matrix Navigation
# Create three lists and nest them to form a matrix. Example:
# [ [1,2,3],
# [4,5,6],
# [7,8,9] ]
# Students must:
# 1. Print the number in row 1, column 2
# 2. Print the entire second row
# 3. Print the diagonal (1,5,9)
# 4. Create a new list of all first-column elements using indexing
# 5. Then repeat using a list comprehension
# Goal: Practice nesting + comprehensions.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Number in row 1, column 2:", matrix[0][1])

print("Entire second row:",matrix[1])

print("Diagonal elements:", matrix[0][0], matrix[1][1], matrix[2][2])

first_column = [matrix[0][0], matrix[1][0], matrix[2][0]]
print("First column elements (using indexing):", first_column)

first_column_comp = [row[0] for row in matrix]
print("First column elements (using list comprehension):", first_column_comp)

# LAB 9 — List Comprehension Transformations
# Given numbers = [1,2,3,4,5,6,7,8,9]
# Students must create using list comprehensions:
# 1. A list of squares
# 2. A list of only even numbers
# 3.A list of numbers doubled
# 4.A list of only numbers greater than 5
# 5.A list of strings: "Number: X" for each element
# Goal: Become comfortable with comprehensions.

given_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [n**2 for n in given_numbers]

evens = [n for n in given_numbers if n % 2 == 0]

doubled = [n * 2 for n in given_numbers]

greater_than_5 = [n for n in given_numbers if n > 5]

labels = [f"Number: {n}" for n in given_numbers]

print(squares)
print(evens)
print(doubled)
print(greater_than_5)
print(labels)

# LAB 10 — Mini Project: Student Information Formatter
# Ask user for:
# • Name
# • Age
# • Favorite subject
# • Favorite quote
# Then:
# 1. Use formatting (.format() or f-strings) to print a nicely formatted paragraph.
# 2. Capitalize the name.
# 3. Remove whitespace around inputs.
# 4. Create a list of the letters from the name.
# 5. Print the first and last letter from that list.
# Goal: Combine strings, formatting, indexing, list creation.

# 1. Ask user for inputs
name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
subject = input("Enter your favorite subject: ").strip()
quote = input("Enter your favorite quote: ").strip()


name = name.capitalize()

name_letters = list(name)

first_letter = name_letters[0]
last_letter = name_letters[-1]

paragraph = (
    f"\nHello {name}! You are {age} years old, and your favorite subject is {subject}. "
    f"One of your favorite quotes is: \"{quote}\".\n"
)

print(paragraph)

print("Letters in your name:", name_letters)
print("First letter:", first_letter)
print("Last letter:", last_letter)














