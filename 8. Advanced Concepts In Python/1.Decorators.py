# Decorators in Python
# Discover decorators in Python, a powerful feature that allows you to modify or enhance the behavior of functions or methods without changing their actual code.
#  Learn how to create and apply decorators to add functionality such as logging, access control, or performance monitoring to existing functions

#Decorator is a function that takes a function, it creates a new function inside its body(wrapper),
#Then it returns that new function

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("the function has been executed")
    return wrapper    

@decorator
def say_hello():
    print("Hello !")


# f = decorator(say_hello)
# f()
# # I am about to execute a function...
# # Hello !
# # the function has been executed

'''
f will look like this : -->
  
   def f():
       I am about to execute a function...
       Hello !
       the function has been executed
 
'''
say_hello()
# I am about to execute a function...
# Hello !
# the function has been executed


def repeat(n):
 def decorator(func):    
    def wrapper(a):
            for _ in range(n):
                func(a)
    return wrapper
 return decorator


@repeat(3)
def greet(name):
 print(f"Hello, {name}!")
greet("world")
