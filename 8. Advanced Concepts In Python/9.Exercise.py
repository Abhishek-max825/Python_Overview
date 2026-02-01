'''
1. Decorators in Python

Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".
Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
'''

def decorator(func):
    print("decorator invoked")
    def wrapper():
        print("wrapper function started")
        func()
        print("wrapper ended")
    return wrapper

@decorator
def say_hello():
    print("Function is being called")    
  
say_hello()
    

import time as t 

def decorator(func):
    def wrapper():
        start = t.time()
        func()
        end = t.time()
        print(f"The time it takes to count from 1 to 10,00,000 is : {end-start : .2f}")
    return wrapper    

@decorator
def counting_number():
    count = 0
    for i in range(1,1000001):  
        count += 1

counting_number()
#The time it takes to count from 1 to 10,00,000 is :  0.06

'''
2. Getters and Setters

Create a class Employee with a private attribute _salary.

Use @property to define a getter for salary.
Use @salary.setter to prevent setting negative values (print a warning instead).
Create an object and test by setting positive and negative salaries.
'''
class Employee:

    def __init__(self):
       self.__salary = 0

    @property
    def salary_value(self):
       return self.__salary
    
    @salary_value.setter
    def salary_value(self,amount):
        if amount < 0:
            print("Dont waste our time give the correct input :")
        else:
            self.__salary = amount
            print(f"You initialized the salary as {self.__salary}")


e = Employee()
e.salary_value = int(input("Enter your salary : "))

'''
3. Static & Class Methods
Create a class MathUtils with:

A @staticmethod called add(a, b) that returns a + b.
A @classmethod called description(cls) that prints "This is a utility class for math operations."
Call both methods without creating an object
'''

class MathUtils:

    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

sum = MathUtils.add(4,5)
print(sum)

MathUtils.description()

'''
4. Magic/Dunder Methods
Create a class Book with attributes title and author.

Implement __str__() so that printing the object displays "Title by Author".
Implement __len__() so that len(book) returns the length of the title.
Create two Book objects and test these methods.
'''

class Book:
   def __init__(self,title,author):
      self.title = title
      self.author = author

   def __str__(self):
      return f"Title : {self.title} ,Author : {self.author}"

   def __len__(self):
       length = len(self.title)
       return length
   
b1 = Book("Seven wonders","Habibi")
print(f"Title by Author : {str(b1)}")
print(f"Length : {len(b1)}")
# Title by Author : Title : Seven wonders ,Author : Habibi
# Length : 13

b2 = Book("Revolution","Blacky")
print(f"Title by Author : {str(b2)}")
print(f"Length : {len(b2)}")
# Title by Author : Title : Revolution ,Author : Blacky
# Length : 10

'''
5. Exception Handling and Custom Errors

 -> Write a program that asks the user to enter a number and handles:
    -> ValueError if the input is not a number
    -> ZeroDivisionError if you try to divide by zero

 -> Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

'''
# 1.Given Problem
def Exception_handling(value1,value2):
      try:
        solution = value1/value2
        print(solution)
      except ValueError:
        print("Dont give other input except numbers") 
      except ZeroDivisionError:
        print("When we divide any number by zero we get zero my brother")  
      finally:
         print("end") 

# 2.Custom Exception
value1 = int(input("enter the first number : "))
value2 = int(input("enter the second number : "))
Exception_handling(value1,value2)     

class NegativeNumberError(Exception):
    def __init__(self, message = "Negative values are not allowed"):
       self.message = message
       super().__init__(message)

def check():
    while number := int(input("Enter the number :")):  
      if number >= 0:
         print("allowed")
      else:
         raise NegativeNumberError
         break

try:      
    check()
except NegativeNumberError as n:
   print(n)          
         

'''
6. map(), filter(), and reduce()

-> Use map() to convert [1, 2, 3, 4, 5] into their cubes.
-> Use filter() to get only even numbers from [10, 11, 12, 13, 14].
-> Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].
'''     

value1 = [1,2,3,4,5]

new_list = list(map(lambda x : pow(x,3),value1))
print(f"Using map to find cube : {new_list}")
# Output : Using map to find cube : [1, 8, 27, 64, 125]

value2 = [10, 11, 12, 13, 14]

new_list2 = list(filter(lambda x : x % 2 == 0,value2))
print(f"Using filter to find even values : {new_list2}")
# Output : Using filter to find even values : [10, 12, 14]

from functools import reduce

value3 = [1, 2, 3, 4]

new_sol = reduce(lambda x,y : x * y,value3)
print(f"using reduce to finding product : {new_sol}")
# Output : 24

'''
7. Walrus Operator

1. Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.
2. Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.
'''

# 1.

while (data := input("Enter a value (or 'quit'/'exit' to exit): ")) != "quit" or "exit":
    print(f"You entered: {data}")

# 2.

def walrus_related():
    list_value = ["python", "rocks", "ai","java"]  
    item = [] 

    item = [item for item in list_value if len(item) <= 4]
    print(item,sep=",")

    #or

    result = [(item, l) for item in list_value if (l := len(item)) <= 4]
    print(result)

# walrus_related()

# '''
# 8. *args and **kwargs

# -> Write a function sum_all(*args) that accepts any number of integers and returns their sum.
# -> Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
# '''

# #1.
def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total    


number = int(input("enter the total number of integers : "))

values = []
for i in range(number):
    val = int(input(f"Enter value {i+1}: "))
    values.append(val)
  
total = sum_all(*values)
print(f"The sum of given {number} integer is : {total}")

#2.

def print_details(**kwargs):
    for details in kwargs.keys():
        print(f"{details} : {kwargs[details]}")

print_details(name="Alice", age=25, city="Delhi")        
# Output:
# name: Alice
# age: 25
# city: Delhi


'''
9. Bonus Challenges
-> Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
-> Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
-> Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing.

'''
#1.
def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: before function call")
        result = func(*args, **kwargs)
        print("Decorator: after function call")
        return result
    return wrapper

@universal_decorator
def greet():
    print("hello")
    #you can us any number of arguments / keyword for work 

greet()  
# Decorator: before function call
# hello
# Decorator: after function call  

#2.

class Vector:
    def __init__(self,vector):
        self.vector = vector

    def __add__(self,other):
       return Vector(
            [a + b for a, b in zip(self.vector, other.vector)]
        ) 
    
    def __str__(self):
        return str(self.vector)

vector1 = [1,2,3,4,5]
vector2 = [9,8,7,6,5]
v1 = Vector(vector1) 
v2 = Vector(vector2)  
v3 = v1 + v2
print(v3)
# Output : [10, 10, 10, 10, 10]

# Note : For 3rd one its already done check custom exception above 