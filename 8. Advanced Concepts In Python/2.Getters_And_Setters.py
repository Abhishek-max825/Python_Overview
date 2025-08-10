#To make an attribute read-only,define just the @property decorator(the getter) 
# And leave out the @name.setter method.
#Trying to set the attribute will result an AttributeError

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property 
    #it makes the first name to work like an attribute or property
    def first_name(self):
        l = self.name.split(" ")
        # print(l)
        return l[0]#this returned value will be passed as an argument in setter function like def first_name(self,"John")
    
    @first_name.setter
    def first_name(self,first): # getter and setter name should be same 
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    


e = Employee("Jack Doe", 34555)
# print(e.first_name())
# ['Jack', 'Doe']
# Jack

# e.projects = 6
# print(e.projects)
# 6

# e.set_first_name("John")
# print(e.name)
# John Doe

# instead of using this type of things use this
print(e.first_name)# Jack
e.first_name = "John"
print(e.name)# John Doe
# print(e.first_name) will call the getter
# e.first_name = "John" will call the setter
# print(e.name) will show "John Doe"
