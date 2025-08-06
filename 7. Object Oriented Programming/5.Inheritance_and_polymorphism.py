class Animal: # Parent class (superclass)
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print("speaking now...")


class Dog(Animal): # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self): # We *override* the speak method (more on this later)
       super().speak()  #speaking now...  here we are using the speak function of parent class
       print("Woof!")


class Cat(Animal): # Cat also inherits from Animal
    def speak(self):
        print("Meow!")


 # Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")
# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name) # Output: Rover
print(my_cat.name) # Output: Fluffy
# They both have a 'speak' method, but it behaves differently:
my_dog.speak() # Output: Woof!
my_cat.speak() # Output: Meow!