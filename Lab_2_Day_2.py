# # 1. String Indexing
# # Given the string s = 'Python', use indexing to print the following:
# # - 'o'
# # - 'Pyth'
# # - 'yth'
# # - 'nohtyP'

# s = 'Python'
# print(f"String is: {s}")
# a = s[4]
# print(f"Extracted only 'o' from {s}: {a}")
# b = s[:4]
# print(f"Extracted only 'Pyth' from {s}: {b}")
# c = s[1:4]
# print(f"Extracted only 'yth' from {s}: {c}")
# d = s[::-1]
# print(f"Reversed {s}: {d}")


# # 2. Nested List
# # Given the list l = [3, 7, [1, 4, 'hello']], change the value 'hello' to 'goodbye'.

# l = [3, 7, [1, 4, 'hello']]
# print(f"Whole list before changing the value is {l}")

# l[2][2] = 'goodbye'
# print(f"After changing the value the list becomes {l}")

# # 3. Dictionaries – Access Values
# # Using keys and indexing, retrieve the value 'hello' from the following dictionaries:
# d1 = {'simple_key':'hello'}
# d2 = {'k1':{'k2':'hello'}}
# d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# print(f"Dict d1 is {d1}")
# a = d1['simple_key']
# print (f"Print 'hello' from d1: {a}")

# print(f"Dict d1 is {d2}")
# b = d2['k1']['k2']
# print (f"Print 'hello' from d2: {b}")

# print(f"Dict d1 is {d3}")
# c = d3['k1'][0]['nest_key'][1][0]
# print (f"Print 'hello' from d3: {c}")


# # 4. Sets – Unique Values
# # Use a set to find the unique values in the list:
# mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

# print(f"Before duplicates {mylist}")
# x = set(mylist)
# print(f"After removing duplicates {x}")


# # 5. Print Formatting
# # You are given the variables:
# age = 4
# name = 'Sammy'
# # Use print formatting to display:
# # "Hello my dog's name is Sammy and he is 4 years old"

# print(f"Hello my dog's name is {name} and he is {age} years old.")
# print("Hello my dog's name is {} and he is {} years old".format(name, age))

# #6. Loop – Power Calculation
# #Write a program that takes two integers as input (base and exponent) and calculates the power using loops.

# base = int(input("Enter the first number: "))
# exponent = int(input("Enter the second number: "))

# result = 1

# for i in range(exponent):
#     result = result * base

# print(f"{base} to the power {exponent} is {result}")

# #7. Tuple – Sum of Elements
# #Write a program that calculates the sum of all elements in a given tuple.

# test_tuple = (1, 2, 3, 4, 5)

# total = 0

# for num in test_tuple:
#     total = total + num  

# print(f"The sum of all elements in the tuple is: {total}")

# #8. Tuple with Condition
# #Create a new tuple that contains only the even numbers from a given tuple of integers.

# test_tuple = (1,2,3,4,5,6,7,8,9,10)

# even_num = ()

# for num in test_tuple:
#     if num % 2 == 0:    
#       even_num += (num,)
# # I found difficult to get the even elements in tuple, so I referred w3 schools Python tuples - Create tuple with one element
# print(f"The even numbers are: {even_num}")

# # 9. Dictionaries – Merge
# # Write a program that merges two dictionaries into one. If a key exists in both, the value from the second dictionary should be used.


# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 20, 'd': 4}

# merged_dict = dict1.copy()  

# for key, value in dict2.items():
#     merged_dict[key] = value  

# print("Merged dictionary:", merged_dict)

# # 11. String – Reverse
# # Write a program that takes a string as input and prints the reversed string.

# str = input("Enter a string: ")

# reversed_str = str[::-1]

# print("Reversed string:", reversed_str)

# 10. List Comprehension – Even Numbers
# Write a program that takes a list of integers and uses list comprehension to create a new list containing only the even numbers.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in num if x % 2 == 0]

print("Even numbers:", even_numbers)