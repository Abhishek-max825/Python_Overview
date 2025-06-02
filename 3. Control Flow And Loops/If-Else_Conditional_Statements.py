#What exactly are conditional statements?
#Conditionals are the basic logic-building blocks of Python.
#They allow us to check if a certain condition is true and then respond to that condition.


#if statement
#The if statement is used to check a condition and if the condition is true, the code block is executed.

#Syntax
#if condition:
#    code block

#Example:
age = 18

if age >= 18:
    print("you are eligible to vote")

print("Thank you for using our service")

#if else statement
#The if else statement is used to check a condition and if the condition is true, the code block is executed, otherwise else will be executed.

#Syntax
#if condition:
#    code block
#else:              
#    code block

#Example:
age  = 32

if age >= 18:
    print("you are good to go")
else:
    print("you are not eligible to drive")

print("Thank you for using our service")

#if elif else statement // elif ladder
#The if elif else statement is used to check multiple conditions and if the condition is true, the code block is executed, otherwise else will be executed.

#Syntax
#if condition:
#    code block
#elif condition:
#    code block
#else:
#    code block 

#Example:
age = 20

if age >= 18:
    print("you are eligible to vote")
elif age >= 16:
    print("you are eligible to drive")
elif age >= 14:
    print("you are eligible to ride a bike")
else:
    print("you are not eligible to vote or drive")

print("Thank you for using our service")

#Nested if statement
#The nested if statement is used to check multiple conditions and if the condition is true, the code block is executed, otherwise else will be executed.

#Syntax
#if condition:
#    code block
#    if condition:
#        code block
#    else:
#        code block
#else:
#    code block

#Example:            
age = 20

if age >= 18:
    print("you are eligible to vote")
    if age >= 21:
        print("you are eligible to drive")
    else:
        print("you are not eligible to drive")  
else:
    print("you are not eligible to vote")

print("Thank you for using our service")
