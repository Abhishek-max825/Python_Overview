# dictionaries store key-value pairs and allow fast lookups
# we cannot have "list" as keys because they are not hashable

marks = {"harry" : 34, "abhi" : 63, "rajath" : 73}

print(marks, type(marks), sep=" and ")
# {'harry': 34, 'abhi': 63, 'rajath': 73} and <class 'dict'>

#Accessing and modifying the dictionary:-
print(marks["abhi"])
# 63

marks["harry"] = 92
print(marks)
# {'harry': 92, 'abhi': 63, 'rajath': 73}

# methods of dictionary

print(marks.keys())
# dict_keys(['harry', 'abhi', 'rajath'])
print(marks.values())
# dict_values([92, 63, 73])
marks.pop("abhi")
print(marks)
# {'harry': 92, 'rajath': 73}
# marks.clear()
# print(marks)
# {}

# -->dictionary comprehensions

table_of_5 = {i : i*5 for i in range(1,11)}
print(table_of_5)
# {1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}