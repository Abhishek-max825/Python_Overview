# Tuples and Operations on Tuples
# Learn about tuples in Python, a collection type similar to lists but immutable. 
# This lesson covers how to create tuples, access elements, and perform operations like slicing, concatenation, and repetition. 
# Understand when to use tuples over lists for data that shouldn't change
a = (3, 2, 22, 13)

print(a)
# (3, 2, 22, 13)
print(a[2])
# 22

# when we need to create a tuple with single element we always need to add a comma after adding the element
t = (3)
print(type(t))
# <class 'int'>
#--> its giving int because paranthesis is used for grouping also

# so we need to do
t = (3,)
print(type(t))
# <class 'tuple'>

#tuple unpacking

tu = (3, 2, 45)

a, b, c = tu

print(a, b, c)
# 3 2 45

#tuple methods 

t = (3, 12, 1, 54, 23, 12)
print(t.count(12))
# 2
print(t.index(12))
# 1