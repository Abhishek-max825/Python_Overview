#-->LOCAL ABD GLOBAL VARIABLES

def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1 # it creates a local variable called z which is not the same as the global variables
    print(z) # 1 and it will be destroyed after the function is executed
    print(globals()) # it prints all the global variables
    '''
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000024F5844CC00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\abhis\\OneDrive\\ドキュメント\\Python Bootcamp - 2025\\5. Functions And Modules\\6.Variable_scope_and_Docstrings.py', '__cached__': None, 'sum': <function sum at 0x0000024F58261440>, 'greet': <function greet at 0x0000024F58483EC0>, 'z': 8}
    '''
    return c

def greet():
    z = 32 # local variable
    print("hello")
    print(f"local z value : {z}")


z = 8 # global variable
print(sum(4,6)) # 10
print(z) # 8 

greet()
# hello
# local z value : 32


def changing_global_variable_value():
    print("hello")
    global z # please modify global variable value z
    z = 0 #this will refer to global z and not create a local variable
    print(f"the value of z is : {z}")


z = 23
changing_global_variable_value()
print(z)

# -->before using global keyword
# hello
# the value of z is : 0
# 23

# -->after using global variable 
# hello
# the value of z is : 0
# 0


# -->DOCSTRINGS
def docstring(a,b):
    '''sum of two numbers'''
    c = a+b
    return c

print(docstring.__doc__)
#--> it is used right after the function is declared and mostly it is used to give information about function working
# sum of two numbers