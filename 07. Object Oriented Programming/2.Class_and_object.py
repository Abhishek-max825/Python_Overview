# Class  : Class is a blueprint of an object or template.
#Eg. Form for an exam that conatins name , age, electives ,father's name etc

# Object : A specific instance created from the class(template).
#Eg. Form which contains the data for Jhon Doe

class Employee:
    company = "HP"

    def get_salary(self):
        print(self)
        # self is important here because self is a way to reference the object of the class which is being created
        return 34000
    

e1 = Employee() # an object of class employee us created here
print(e1.company) # attribute is called here
print(e1.get_salary())# method is called here

# HP
# <__main__.Employee object at 0x00000268950C7230>
# 34000

e2 = Employee()
print(e2.get_salary())

# <__main__.Employee object at 0x0000026895358CD0>
# 34000

# In the above example, we have created a class Employee and an object e.
# The class Employee has a company attribute and a method get_salary()

# self is a reference to the current object.
# In here self is e and e2