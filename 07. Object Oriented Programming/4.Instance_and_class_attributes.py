class Employee:
    company = "Asus" # this is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_Salary(self):
        return self.salary
    
    def print_details(self):
        print(f"Name is {self.name}")
        print(f"salary is {self.salary}")
        print(f"bond is {self.bond}")


e1 = Employee(34000, "John", 4, "Tesla")
print(e1.company) # will alaways print instance attrobute whenever present
#Tesla
print(Employee.company) # this will always print the class attribute
#Asus

#object introspection
#its a way of finding all the methods present in an object
print(dir(e1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bond', 'company', 'get_Salary', 'name', 'print_details', 'salary']

