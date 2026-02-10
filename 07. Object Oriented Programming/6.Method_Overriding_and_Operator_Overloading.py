#Method Overriding and Operator Overloading
# Learn about method overriding and operator overloading in Python. Method overriding allows a subclass to provide a specific implementation of a method inherited from a parent class, while operator overloading lets you define custom behavior for operators (like +, -, etc.) in your classes, enhancing code readability and functionality.
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self,p):
        return point(self.x + p.x , self.y + p.y)   
    
    def print_point(self):
        print(f"x is {self.x} and y is {self.y}")

    def __add__(self,p):
        return point(self.x + p.x , self.y + p.y)   
    
p1 = point(3, 2)
p2 = point(6, 3)    

# p = p1.sum(p2) # returns a new point which is sum of p1 and p2
# print(p.print_point())
# x is 9 and y is 5

p = p1 + p2 # we overloaded the + operator by using __add__ operator
p.print_point()
# x is 9 and y is 5
