'''
Args and kwargs

-> *args and **kwargs are special syntaxes in Python function definitions that allow you to pass a variable number of arguments to a function.
-> They are used when you don't know in advance how many arguments a function might need to accept.

*args: Allows you to pass a variable number of positional arguments.
**kwargs: Allows you to pass a variable number of keyword arguments.

'''

'''
*args (Positional Arguments) :-

-> *args collects any extra positional arguments passed to a function into a tuple. 
-> The name args is just a convention; you could use any valid variable name preceded by a single asterisk (e.g., *values, *numbers).
'''

# def sum(a,b):
#     return a+b

# print(sum(4,5))

# when we dont know how many arguments will be passed to a functions at that time we use *args

def sum(*values):
    # args will be a tuple of all the values passed to sum 
    total = 0
    print(values) # Output : (4, 5, 6, 7, 2, 1)

    for item in values:
        total += item
    return total
    

print(sum(4,5,6,7,2,1)) # Output : 25

# another example
def my_function(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello
my_function()  # No output (empty tuple)
my_function("a", "b")  # Output: a b

'''
**kwargs (Keyword Arguments) :-

-> **kwargs collects any extra keyword arguments passed to a function into a dictionary.
-> Again, kwargs is the conventional name, but you could use any valid variable name preceded by two asterisks (e.g., **data, **options).
'''

# Its used to pass key and value pairs

def marks(**score):
    print(score) #it stores in the format of dictionary
    # {'Abhi': 23, 'Akshay': 53, 'Sujay': 90, 'Ashish': 98, 'Rajath': 100} 
    for item in score.keys():
        print(f"{item} : {score[item]}",end = " , ")
        # Output : Abhi : 23 , Akshay : 53 , Sujay : 90 , Ashish : 98 , Rajath : 100 , None

print(marks(Abhi = 23, Akshay = 53, Sujay = 90, Ashish = 98, Rajath = 100))  

# Another Example 

def my_function(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

my_function()  # No output (empty dictionary)
my_function(a=1, b=2)
# Output:
# a: 1
# b: 2

'''
Combining *args and **kwargs

-> You can use both *args and **kwargs in the same function definition. 
-> The order is important: *args must come before **kwargs.
-> You can also include regular positional and keyword parameters.
'''

def my_function(a, b, *args, c=10, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"kwargs: {kwargs}")

my_function(1, 2, 3, 4, 5, c=20, name="Bob", country="USA")
# Output:
# a: 1
# b: 2
# args: (3, 4, 5)
# c: 20
# kwargs: {'name': 'Bob', 'country': 'USA'}

my_function(1,2)
# Output:
# a: 1
# b: 2
# args: ()
# c: 10
# kwargs: {}