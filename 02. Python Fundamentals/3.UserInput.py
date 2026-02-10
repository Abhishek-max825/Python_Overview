a = input("enter a number : ")
print(a)

b = input("enter your name : ")
print(b)


# input() function always returns a string, so we need to convert it to int if we want to perform arithmetic operations

a = int(input("enter the 1st number : "))
print(a)

b = int(input("enter the 2nd number : "))
print(b)

print(f"sum of {a} and {b} is : {a+b}") # f-string formatting
# f-string formatting is a way to format strings in Python. 
# It allows you to embed expressions inside string literals, using curly braces {}.
#  The expressions are evaluated at runtime and formatted using the format() method. 