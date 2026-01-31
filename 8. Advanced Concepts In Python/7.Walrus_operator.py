'''
Introduction :
-> The walrus operator (:=), introduced in Python 3.8, is an assignment expression operator.
-> It allows you to assign a value to a variable within an expression.
-> This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls.
-> The name "walrus operator" comes from the operator's resemblance to the eyes and tusks of a walrus.

'''
# Use cases : 

'''
1. Conditional Expressions:
   ->  The most common use case is within if statements, while loops, and list comprehensions, where you need to both test a condition and use the value that was tested.
'''

# example 1:

def very_slow_function():
    print("slow")
    print("slow")
    print("slow")
    print("slow")
    print("slow")
    return 70


# if very_slow_function() > 10:
#     print(very_slow_function())
# else:
#     print("not quite")    

'''
slow
slow
slow
slow
slow
slow
slow
slow
slow
slow
70

-> In here the function is called twice at first in if condition and second in printing
-> which is waste of time so to optimixe it we use " walrus " operator
'''    

#it goes like : 

if (a:=very_slow_function()) > 10:
    print(a)
else:
    print("not quite")    

'''
slow
slow
slow
slow
slow
70

-> look its solved as simple as that 
-> here it assigned the function call to "a" which reduced the function call and assigned the returned value
-> it like 70 > 10 -> print(a) {which means it calls funcion now for once}
'''  

# Example 2

# Without walrus operator
data = input("Enter a value (or 'quit' to exit): ")
while data != "quit":
    print(f"You entered: {data}")
    data = input("Enter a value (or 'quit' to exit): ")

# With walrus operator
while (data := input("Enter a value (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {data}")

'''
2. List Comprehensions:
   ->  You can avoid repeated calculations or function calls within a list comprehension
'''

numbers = [1, 2, 3, 4, 5]

# Without walrus operator:  calculate x * 2 twice
results = [x * 2 for x in numbers if x * 2 > 5]
print(results)
# [6, 8, 10]

# With walrus operator: calculate x * 2 only once
results = [y for x in numbers if (y := x * 2) > 5]
print(results)
# [6, 8, 10]

'''
3. Reading Files:
   ->  You can read lines from a file and process them within a loop
'''
# Without Walrus
with open("my_file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

# With Walrus
with open("my_file.txt", "r") as f:
    while (line := f.readline()):
        print(line.strip())