# 1. Introduction to Lists

fruits = ["apple", "banana", "cherry"]

print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))

new_list = []
for i in range(1,11):
    new_list.append(i)

print(new_list)    
print(new_list[0:3])
print(new_list[-1:-4:-1])

# 2. List Methods

numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)

numbers.append(10)
print(numbers)

numbers.remove(2)
print(numbers)

names = ["Alice", "Bob", "Charlie"]

names.insert(1,"David")
print(names)

# 3. Tuples and Operations on Tuples

coordinates = (10,20)

list_values = list(coordinates)
print(list_values)

list_values[0] = 50
print(list_values)

coordinates = tuple(list_values)
print(coordinates,type(coordinates),sep=" and ")

# 4. Sets and Set Methods

my_set = {1, 2, 3, 3, 4}
print(my_set)#returns only unique values

value = {5}
my_set.update(value)
my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

print(4 in my_set) #True

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(b-a)# {4, 5}
print(a-b)# {1, 2}

# 5. Dictionaries and Dictionary Methods

student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])

student["grade"] = "A+"
print(student)

print(dir(dict))

student.update({"city" : "Delhi"})
print(student)

print(student.keys())
# dict_keys(['name', 'age', 'grade', 'city'])

print(student.values())
# dict_values(['John', 20, 'A+', 'Delhi'])

print(student.items())
# dict_items([('name', 'John'), ('age', 20), ('grade', 'A+'), ('city', 'Delhi')])

new_dict = {"apple" : 50, "car" : 3000, "mobile" : 800}

check = new_dict.get
print(check)
# <built-in method get of dict object at 0x000002025BC820C0>

max_key = max(new_dict, key=new_dict.get)
print(max_key, ":", new_dict[max_key])
# car : 3000
