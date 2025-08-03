# A set is a collection of well defined objects which contains unique elementspi
#they are unordered and wont allow duplicate value so accessing by their index is not possible
# important : - it storesthe value in a random way not in ordered manner
#for example :- the set contains apple , banana and pineapple but theres nothing to gurantee apple should be first element
#it stors in a random manner

fruits = {'apple', 'banana', 'pineapple'}
print(fruits, type(fruits) , sep= " and ")
# {'pineapple', 'banana', 'apple'} and <class 'set'>
# print(fruits[2])
# TypeError: 'set' object is not subscriptable

#set methods:=

s = {1, 32 , 54 , 43}

print(s)
# {32, 1, 43, 54}

s.add(49)
print(s)
# {32, 1, 43, 49, 54}

s.remove(32)
print(s)
# {1, 43, 49, 54}

# s.remove(100) --> throws error
s.discard(100) # it does not raise any exception if 100 is not found in set but if use remove it will raise exception
print(s)
# {1, 43, 49, 54}

s.pop() #--> remove randome element from set
print(s)
# {43, 49, 54}

# set operations :-

a = {1, 2, 3}
b = {2, 3, 5, 6, 43, 987}

# union operation :
# basically it combines two sets into a single set that contains both a and b 
# important: -- >it does not allo w duplicatin
c = a.union(b)
print(c)
# {1, 2, 3, 5, 6, 987, 43}

# intersection :
# basically it returns common values which present in both a and b
d = a.intersection(b)
print(d)
# {2, 3}