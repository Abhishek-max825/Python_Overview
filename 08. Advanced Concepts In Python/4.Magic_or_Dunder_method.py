# Dunder or Magic methods (dunder means double underscore)

"""
Magic (dunder) methods are a powerful feature of Python that allows you to:
   -> Customize how your objects interact with built-in operators and functions.
   -> Make your code more intuitive and readable by using familiar Python syntax.
   -> Implement operator overloading, container-like behavior, and other advanced
features.
   ->Define string representation.
   They are used to: 
        -> Customize object creation and initialization ( __init__ , __new__ )
        -> Enable operator overloading (e.g., + , - , * , == , < , > )
        -> Provide string representations of objects (__str__ , __repr__ ).
        -> Control attribute access (__getattr__ , __setattr__ , __delattr__ ).
        -> Make objects callable (__call__ ).
        -> Implement container-like behavior (__len__ , __getitem__ , __setitem__ ,__delitem__ , __contains__ ).
        -> Support with context managers (__enter__ ,__exit__ )
"""

# 1. __init__ – Object Initialization

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 30)
print(p.name, p.age) # Alice 30

'''

2. __str__ and  __repr__ – String Representation

__str__ : This method should return a human-readable, informal string
representation of the object. It’s used by the str() function and by print().

__repr__ : This method should return an unambiguous, official string
representation of the object. Ideally, this string should be a valid Python
expression that could be used to recreate the object. It’s used by the 
repr()function and in the interactive interpreter when you just type the object’s
name and press Enter

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})" # User-friendly

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})" # Unambiguous, for debugging


p = Person("Alice", 30)
print(str(p))
# Person(Alice, 30)
print(repr(p)) # Person(name='Alice', age=30)
print(p)
# Person(Alice, 30)  # print() uses __str__ if 

'''' 

3. __len__ – Define Behavior for len()

  -> This method allows objects of your class to work with the built-in 
len() function.
  -> It should return the “length” of the object (however you define that).

'''
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    

b = Book("Python 101", 250)
print(len(b)) # 250

# 4. __add__, __sub__, __mul__, etc. – Operator Overloading

class Vector:
    def __init__(self,x,y):
       self.x = x
       self.y = y

    def __add__(self,p):
        return Vector(self.x + p.x , self.y + p.y)   
    
    def __sub__(self,p):
        return Vector(self.x - p.x , self.y - p.y)
    
    def __mul__(self,scalar):
        return Vector(self.x * scalar.x , self.y * scalar.y)
    
    def __str__(self):
        return f"Vector ({self.x} and {self.y})"

v1 = Vector(2,4)
v2 = Vector(4,6)
 
v3 = v1 + v2
print(v3)# Vector (6 and 10)

v3 = v1 - v2
print(v3)# Vector (-2 and -2)

v3 = v1 * v2
print(v3)# Vector (8 and 24)


