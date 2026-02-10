#Positional Arguments

def add(a, b):#these are parameters
    return a + b

c = add(5, 6)# these are called arguments
print(c)

#Default Arguments
def add(a, b = 10):
    return a + b

c = add(5)#in this case default argument is used because 'b' value is not given in function calling
print(c)

c = add(5, 6)#here default argument is overridden by '6' as b value in function calling
print(c)

#keyword arguments
#Keyword arguments allow you to specify arguments by their parameter names when calling a function, which makes the code more readable and allows you to pass arguments in any order.

def calculate_rectangle(length, width, color="white"):
    area = length * width
    print(f"A {color} rectangle with length {length} and width {width} has area: {area}")

# Using keyword arguments
calculate_rectangle(length=5, width=3)  # color will use default value "white"
calculate_rectangle(width=4, length=6, color="blue")  # arguments can be in any order
calculate_rectangle(color="red", length=7, width=2)  # another order example
