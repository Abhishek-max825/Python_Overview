# In Python, variables are used to store data that can be used and manipulated throughout a program. A variable is created the moment you assign a value to it using the assignment operator (=).

# Rule of defining a variable in Python  
# Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# They can contain letters, numbers, and underscores.
# Variable names are case-sensitive (age and Age are different).
# Avoid using Python keywords (e.g., if, for, while) as variable names.

age = 34 #integer
name = "abhishek" #string
cgpa = 4.33 #float

# 34age = 32 
# invalid because variable cannot begin with a number

age = 32 
# valid because variable can start with a number

#a$$e = 45 
#invalid because variables cannot contain special characters other than underscore

#underscore is a valid version according to rules
_age_ = 45
print(_age_) 
_nice_45 = 45
print(_nice_45)
a_b_c_7 = "abhi"
print(a_b_c_7)

# Variable names should be descriptive and meaningful to improve code readability.
# For example, instead of using a generic name like "x", use "age" or "student_name" to indicate what the variable represents.


# Python supports several built-in data types:
#     Integers (int): Whole numbers (e.g., 10, -5).
#     Floats (float): Decimal numbers (e.g., 3.14, -0.001).
#     Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
#     Booleans (bool): Represents True or False.
#     Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
#     Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
#     Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
#     Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).

age = 3 
print(age)
print(type(age))

cgpa = 8.2
print(cgpa)
print(type(cgpa))

name = "Harry"
print(name)
print(type(name))

is_completed = True # can also be False
print(is_completed)
print(type(is_completed))