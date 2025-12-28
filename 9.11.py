# 1. Count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for ch in s if ch in vowels)
    return count

# Example
print(count_vowels("Hello World"))  # Output: 3

# 2. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(13))  # Output: True

# 3. Factorial (Iterative and Recursive)
# Iterative
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example
print(factorial_iterative(5))  # Output: 120
print(factorial_recursive(5))  # Output: 120

# 4. Maximum element from a list (without using max())
def find_max(lst):
    if not lst:
        return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# Example
print(find_max([3, 7, 2, 9, 5]))  # Output: 9

# 5. Reverse a string using slicing
def reverse_string(s):
    return s[::-1]

# Example
print(reverse_string("Python"))  # Output: nohtyP

# 6. Count words in a file
# Assume file.txt exists
def count_words_in_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)

# Example
# print(count_words_in_file("file.txt"))

# 7. Script importing a custom module
# main.py
import math_utils

result = math_utils.add(5, 3)
print("Addition:", result)

# 8. Create math_utils.py module
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Then in another file (like main.py above), import and use it.

# 9. Extract even numbers using list comprehension
def extract_even(nums):
    return [x for x in nums if x % 2 == 0]

# Example
print(extract_even([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]

# 10. Using os and sys modules
import os
import sys

print("Current Working Directory:", os.getcwd())
print("Command-line Arguments:", sys.argv)


# 💡 Run it from terminal as:

# python script_name.py arg1 arg2


# Output Example:

# Current Working Directory: C:\Users\Arya
# Command-line Arguments: ['script_name.py', 'arg1', 'arg2']