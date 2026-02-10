## 1. Create a Simple Class and Object
# class car:
#     def drive(self):
#          print("car is moving")

# c = car()
# c.drive()

# # 2. Constructor and Attributes
# # Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# # Create an object and print the person’s name and age.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p = Person("abhi",20)
# print(p.name)
# print(p.age)

# 3. Simple Inheritance

class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("some sound")


class Dog(Animal):
    def __init__(self):
        pass

    def sound(self):
        super().sound()
        print("barki")


d = Dog()
d.sound()
# some sound
# barki