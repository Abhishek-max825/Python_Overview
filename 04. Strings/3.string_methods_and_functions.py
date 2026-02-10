#strings are immutable
#when we use string functions actual function would not be changed but it creates new string
name  = "hello world"

# name[0] = "r" #you cannot change
#     name[0] = "r" #you cannot change
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment

a = len(name)
print(a)
# 5

#string methods

print(name.upper(),name,sep=" and ") 
#-->returns capital letters
#note : -> orginal name value is not changed because of immutability in action
# HELLO WORLD and hello world

print(name.lower()) 
# hello world

print(name.capitalize())
#-->capitalize first letter of the string
# Hello world

print(name.title())
#-->First chracter of every word will be capitalized
# Hello World

text = " \nhello world "
print(text.strip())
#removes leading and tralling whitespaces from a string
#"hello world"
print(text.lstrip())
#-->removes left side whitespace only
#"hello world "
print(text.rstrip())
#-->removes right side whitespace only and it adds it in new line because it only focused on right side
#" hello world"

#-->find() and replace() methods
#-->The find() method in Python returns the index of the first occurrence of the substring you're searching for.
#-->The replace() method is used to replace a substring with another substring in a string
text = "Python is fun"
print(text.find("is"))  # returns 7 because "is" starts at index 7
print(text.find("s"))   # returns 8 because "s" is at index 8
print(text.find("fun")) # returns 9 because "fun" starts at index   
print(text.replace("fun","awesome"))
# --> it replace all the occurences of fun with awesome

#-->split() method
# which is used to split a string into a list based on a specified delimiter
text = "apples,Bananas,pineapples"
print(text.split(','))  # splits at comma
# ['apples', 'Bananas', 'pineapples']

# More examples of split()
sentence = "Hello World Python"
print(sentence.split())  # splits at whitespace by default
# ['Hello', 'World', 'Python']

date = "2024-03-20"
print(date.split('-'))  # splits at hyphen
# ['2024', '03', '20']

# split() with maxsplit parameter
text = "one:two:three:four"
print(text.split(':', 2))  # splits only first 2 occurrences
# ['one', 'two', 'three:four']

#join() method
# joins elements of a list into a single string using a specified separator
# join() method, which is the opposite of split() - it joins elements of a list into a single string using a specified separator

print(",".join(['apples', 'Bananas', 'pineapples']))
# apples,Bananas,pineapples

# More examples of join()
words = ['Hello', 'World', 'Python']
print(" ".join(words))  # joins with space
# Hello World Python

numbers = ['1', '2', '3', '4']
print("-".join(numbers))  # joins with hyphen
# 1-2-3-4

# join() with different separators
print("".join(['a', 'b', 'c']))  # no separator
# abc

print("...".join(['one', 'two', 'three']))  # custom separator
# one...two...three

text = "python1234"
print(text.isalpha())
# False
print(text.isdigit())
# False
print(text.isalnum())
# True
print(text.isspace())
# False

