class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_Salary(self):
        return self.salary
    
    def print_details(self):
        print(f"Name is {self.name}")
        print(f"salary is {self.salary}")
        print(f"bond is {self.bond}")


e1 = Employee(34000, "John", 4)
return_value =e1.get_Salary()
print(return_value)
# 34000 
e1.print_details()
# Name is John
# salary is 34000
# bond is 4