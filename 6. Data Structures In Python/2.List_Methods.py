# List Methods
# Explore the various built-in list methods in Python that allow you to manipulate and interact with lists.
# Learn how to use methods like .append(), .remove(), .pop(), .sort(), and more to modify and manage your list data efficiently.

marks = [5, 2, 21, 5 ,7]

#if we run any methods on list it will change original list
marks.append(6)
print(marks)#[5, 2, 21, 5, 7, 6]

marks.pop()#it will remove the mlast element from the list
print(marks)
# [5, 2, 21, 5, 7]

extra_marks = [53,32,43]
marks.extend(extra_marks) #it will append the value at original list
print(marks)
# [5, 2, 21, 5, 7, 53, 32, 43]

marks.sort()
print(marks)
# [2, 5, 5, 7, 21, 32, 43, 53]

#-->List comprehension

#create a list containing the table of 5

a = 5
table = []

for i in range(1,11):
    table.append(a * i)

print(table)   
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 

#--> in alternative of that we can use list comprehension

# syntax :- 
#       list_name = [expression for value in range(start,end,skip)]
table = [a * i for i in range(1,11)]
print(table)
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]