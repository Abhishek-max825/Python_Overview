# Static & Class Methods
# Explore static and class methods in Python. 
# Static methods, defined with the @staticmethod decorator, don't require access to instance or class data, making them ideal for utility functions. 
# Class methods, defined with the @classmethod decorator, take the class as their first argument and can modify class-level attributes. 
# Learn how to use both to improve your class design.

class Employee:
    # CLASS VARIABLE (also called class attribute) - shared by all instances
    # This variable belongs to the class itself, not individual objects
    company = "Hp"
    
    def __init__(self, name, salary):
        # INSTANCE VARIABLES (also called instance attributes) - unique to each object
        # These variables belong to individual objects created from the class
        self.name = name
        self.salary = salary

    # INSTANCE METHOD (default method type) - requires an instance to be called
    # The 'self' parameter refers to the specific object instance
    # This method can access both instance variables and class variables
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # STATIC METHOD - doesn't need instance or class context
    # Decorated with @staticmethod - acts like a regular function inside the class
    # Cannot access 'self' or class variables - purely utility function
    # Called using: Employee.sum(5,6) or e1.sum(5,6)
    @staticmethod
    def sum(a, b):
        return a+b    

    # CLASS METHOD - takes the class itself as first parameter (cls)
    # Decorated with @classmethod - can access and modify class variables
    # The 'cls' parameter refers to the class, not an instance
    # Used when you want to work with class-level data, not instance data
    @classmethod
    def print_company(cls):
        print(cls.company)

    # Another CLASS METHOD example - modifies class variable
    # Changes the class variable 'company' for ALL instances
    # This affects the class itself, not just one object
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
      

# Creating INSTANCES (objects) of the Employee class
e1 = Employee("Jack", 3455)  # e1 is an instance/object
e2 = Employee("Jill", 3980)  # e2 is another instance/object

# Accessing CLASS VARIABLE through class name
print(Employee.company)  # Output: Hp
# Class variables can be accessed directly from the class

# Accessing CLASS VARIABLE through instance (also works)
print(e1.company)  # Output: Hp
print(e2.company)  # Output: Hp

# This would cause an AttributeError because 'salary' is an INSTANCE VARIABLE
# Instance variables can only be accessed through instances, not the class
# print(Employee.salary)  # ❌ Error!

# Calling INSTANCE METHOD - requires an instance
print(e1.print_info())  # Output: The name is Jack and the salary is 3455
print(e2.print_info())  # Output: The name is Jill and the salary is 3980

# Calling STATIC METHOD - can be called on class or instance
print(e2.sum(5,6))  # Output: 11
print(Employee.sum(5,6))  # Output: 11 (also works!)

# Calling CLASS METHOD - can be called on class or instance
e2.print_company()  # Output: Hp

# Modifying CLASS VARIABLE using class method
e2.change_company("acer")  # Changes company for ALL instances
e2.print_company()  # Output: acer
print(e1.company)   # Output: acer (e1 also affected!)
print(Employee.company)  # Output: acer (class variable changed)