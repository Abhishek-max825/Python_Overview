# Map
'''
Map

The map() function applies a given function to each item of an iterable and returns an iterator that yields the results.

Syntax: map(function, iterable, ...)

-> function: The function to apply to each item.
-> iterable: The iterable (e.g., list, tuple) whose items will be processed.
-> ...: map can take multiple iterables. The function must take the same number of arguments
'''
numbers = [1,2,3,4,5,6,7,8,9,10]

# def product(x):
#     return x*x

# new = list(map(product,numbers))    
# print(new)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# we can also perform it in 2 lines 

new = list(map(lambda x : x * x, numbers ))
print(new)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Note :  
# -> Basically the function like map,filter and reduce returns its object
# -> For getting the values we use to convert it to list.
# -> Major thing to keep in mind whether it is readable or not.

# Filter 

'''
Filter

The filter() function constructs an iterator from elements of an iterable for which a function returns True. In other words, it filters the iterable based on a condition.

Syntax: filter(function, iterable)

-> function: A function that returns True or False for each item. If None is passed, it defaults to checking if the element is True (truthy value).
-> iterable: The iterable to be filtered.
'''

value = [2, 43, 5, 53, 65 , 8, 9, 10]
def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False
    
result = filter(is_greater_than_9,value)
print(result) # <filter object at 0x000001EAF3F7C2B0>
# -> as i said it returning object of filter so we need to typecasting 

result = list(filter(is_greater_than_9,value))
print(result)
# [43, 53, 65, 10]

# shortcut method
result = list(filter(lambda x : x > 9,value))
print(result) 

# Another umportant example

numbers = [1, 2, 3, 4, 5, 6]

# Get even numbers using filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Equivalent list comprehension:
even_numbers_lc = [x for x in numbers if x % 2 == 0]
print(even_numbers_lc) # Output: [2, 4, 6]

# Example with None as function
values = [0, 1, [], "hello", "", None, True, False]
truthy_values = filter(None, values)
print(list(truthy_values)) # Output: [1, 'hello', True]

# Reduce

'''
Reduce

The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.

Syntax: reduce(function, iterable[, initializer])

-> function: A function that takes two arguments.
-> iterable: The iterable to be reduced.
-> initializer (optional): If provided, it's placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.
'''

#-> Basically it converts a given iterable to single number/value
from functools import reduce

a = [1, 2, 3, 4, 5, 6]

def sum(a,b):
    return a+b

# it works like :-
# [1 + 2, 3, 4, 5, 6]
# [3 + 3, 4, 5, 6]
# [6 + 4, 5, 6]
# [10 + 5, 6]
# [15 + 6]
# 21

# -> here we need not to0 convert into list 
# -> because it returns the single value
# Note : if we try to type caste it will return error

result_value = reduce(sum,a)
print(result_value)# 21

# Another Example

numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers using reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

# Calculate the product of all numbers using reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120

#reduce with initializer
empty_list_sum = reduce(lambda x,y: x+y, [], 0)
print(empty_list_sum) # 0

# Without the initializer:
# empty_list_sum = reduce(lambda x,y: x+y, []) # raises TypeError

# Equivalent using a loop (for sum):
total = 0
for x in numbers:
    total += x
print(total)  # 15