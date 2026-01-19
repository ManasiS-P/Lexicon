# Functional Programming, Decorators & Recursion – Exercises
# Task 1: Execution-time decorator
# Create a decorator that measures how long a function takes to execute.
# The decorator should print the execution time after the function has finished.
# Apply the decorator to a function that processes a list of numbers.

# import time
# def execution_time_decorator(func):
#     def wrapper():
#         start_time = time.time()      
#         func()                         
#         end_time = time.time()        
#         print("Execution time:", end_time - start_time, "seconds")
#     return wrapper

# @execution_time_decorator
# def process_numbers():
#     numbers = list(range(1, 100))  
#     result = [n * n for n in numbers]

# process_numbers()



# Task 2: Functional list transformation
# Use a functional approach to transform a list of numbers.
# Apply one operation that changes the values and one operation that filters values.
# The solution must use lambda expressions together with built-in higher-order functions.

# numbers = [1, 2, 3, 4, 5, 6]

# result = list(
#     filter(lambda x: x > 5,
#            map(lambda x: x * 2, numbers))
# )

# print(result)











# Task 3: Closure-based configuration
# Create a function that returns another function.
# The returned function should behave differently depending on a value captured from the
# outer function.
# Create at least two functions from the same factory function and demonstrate the difference
# in behavior.


# def make_multiplier(number):
#     def multiplier(x):
#         return x * number
#     return multiplier

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))   
# print(triple(5))   









# Task 4: Decorator that modifies return values
# Create a decorator that intercepts the return value of a function.
# Modify the return value in some meaningful way before returning it.
# Apply the decorator to at least one function and demonstrate the effect.

# def double_result(func):
#     def wrapper():
#         result = func()      
#         return result * 2   
#     return wrapper

# @double_result
# def get_number():
#     return 10

# print(get_number())










# Task 5: Static utility methods
# Create a class that acts as a utility container.
# The class should contain multiple static methods.
# Each static method should perform a small, independent operation.
# Demonstrate usage without creating any class instances.



# class StringUtils:

#     @staticmethod
#     def make_upper(text):
#         return text.upper()

#     @staticmethod
#     def reverse(text):
#         return text[::-1]

#     @staticmethod
#     def is_empty(text):
#         return text == ""

# print(StringUtils.make_upper("hello"))
# print(StringUtils.reverse("python"))
# print(StringUtils.is_empty(""))



# Task 6: Higher-order function pipeline
# Create a function that takes another function as input.
# Chain multiple function calls together to process a value step by step.
# Use both named functions and lambda expressions in the pipeline.

# def pipeline(value, functions):
#     for func in functions:
#         value = func(value)
#     return value

# def add_two(x):
#     return x + 2

# def multiply_by_three(x):
#     return x * 3

# subtract_one = lambda x: x - 1


# functions = [
#     add_two,                  
#     multiply_by_three,        
#     lambda x: x - 1           
# ]

# result = pipeline(5, functions)
# print(result)









# Task 7: Preserving function metadata
# Create a decorator that wraps a function.
# Ensure that the wrapped function retains its original metadata.
# Verify this by inspecting the function’s name and documentation before and after
# decoration.


# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Before function")
#         func()
#     return wrapper

# @my_decorator
# def say_hi():
#     """This function says hi"""
#     print("Hi!")

# print(say_hi.__name__)
# print(say_hi.__doc__)


# Challenge Task 9: Recursive problem design
# Design a problem that can naturally be solved using recursion.
# Implement a recursive solution.
# Optimize the solution using memoization.
# Demonstrate the difference in performance or behavior.

import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


n = 35

start = time.time()
print("Recursive fib({}):".format(n), fib(n))
print("Time without memoization:", time.time() - start, "seconds")

start = time.time()
print("Memoized fib({}):".format(n), fib_memo(n))
print("Time with memoization:", time.time() - start, "seconds")

# Challenge Task 8: Flexible decorator with arguments
# Create a decorator that accepts its own arguments.
# The decorator should alter its behavior based on the provided arguments.
# Apply the decorator to multiple functions using different decorator arguments.

# def repeat(times):
#     def decorator(func):
#         def wrapper():
#             for _ in range(times):
#                 func()
#         return wrapper
#     return decorator

# @repeat(2)
# def say_hi():
#     print("Hi!")

# @repeat(4)
# def say_bye():
#     print("Bye!")

# say_hi()
# say_bye()










# Challenge Task 10: Decorators + recursion interaction
# Create a recursive function that performs a calculation.
# Apply a decorator that logs information about each function call.
# Observe how the decorator behaves during recursive execution and explain the result.

# from functools import wraps

# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}({', '.join(map(str,args))})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__}({', '.join(map(str,args))}) returned {result}")
#         return result
#     return wrapper

# @log_call
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print("Factorial result:", factorial(4))









