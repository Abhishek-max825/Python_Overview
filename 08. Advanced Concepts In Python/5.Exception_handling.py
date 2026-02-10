'''
Exception Handling and Custom Errors

   -> Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions.
   -> Python provides a robust mechanism for handling exceptions using try-except blocks.
   -> This allows your program to gracefully recover from errors or unexpected situations, preventing crashes and providing informative error messages. 
   -> You can also define your own custom exceptions to represent specific error conditions in your application

'''

# while True:
#     try: 
#         a = int(input("Enter the first number : "))
#         b = int(input("Enter the second number : "))

#         print(f"the quotient of two numbers are {a/b}")
#     except ValueError:
#         print("given value is not proper ")  
#     except ZeroDivisionError:
#         print("cant divide by zero")      
#     except Exception as e :
#         print("something wrong ! ",e)
#     finally: 
#         print("excecuted")   


# raising an error 

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# if b == 0:
#     raise ValueError("Its not proper")
# else:
#     print(f"the quotient of two numbers are {a/b}")


# else and finally

# try:
#     a = 365/10
# except Exception as e:
#     print(e)
# else:# gets executed when there is no errors
#     print("executed") 



# def divide(a,b):
#     try:
#         c = a/b
#         print(c)
#     except ZeroDivisionError as e:
#         print(e)
#     # it is always executed no matter if try completely executes or not    
#     finally: 
#         print("executed finally")        


# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# divide(a,b)

# custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older!"):
        self.message = message
        super().__init__(self.message)

def verify_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise your custom exception
    return "Welcome!"

try:
    print(verify_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")

# example : 
class sample(Exception):
    def __init__(self, message = "Error you are doing it wrong dumbo!!!"):
        self.message = message
        super().__init__(message)  


def salary_check(salary):
    if salary > 50000:
        print("Correct")
    else:
        raise sample()   

try:
    salary_check(1000)
except sample as e:
    print(e)