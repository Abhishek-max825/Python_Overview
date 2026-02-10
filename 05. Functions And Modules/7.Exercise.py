import math as m
import my_utlis as mu

# def full_name(first,last):
#     return f"{first}{last}"

# name = full_name("nayan ","patel")
# print(name)

# def calculate_area(length, width=10):
#     return length*width

# area = calculate_area(5)
# print(area)
# print(calculate_area(5,4))

# list_value = [1,2,3,4,5]

# new_list = list(map(lambda x : x*x,list_value))
# print(new_list)

# def sum_of_digits(n):
#     '''Return the sum of digits from 1 to n using recursion'''
#     if n == 1:
#         return 1
#     else:
#         return n + sum_of_digits(n-1)
    
# result = sum_of_digits(5)
# print(result) 
# print(sum_of_digits.__doc__)   

# print(m.sin(90))

# count = 0

# def val():
#     global count
#     count += 1
#     print(count)

    
# val()
# val()       
# val()

# def fib(n):
#     value = []
#     if n <= 0:
#        return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)    
    
# value = fib(5)
# for i in range(value):
#     print(i,end=" ")

print(mu.is_even(4))