try : 
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    print("select the operation to perform : ")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice : "))
    match choice :
        case 1 : 
            print(f"the sum of {a} and {b} is : {a+b}")
        case 2 : 
            print(f"the difference of {a} and {b} is : {a-b}")
        case 3 : 
            print(f"the product of {a} and {b} is : {a*b}")
        case 4 : 
            print(f"the quotient of {a} and {b} is : {a/b}")
        case _ :
            print("invalid choice")

except Exception as e:
    print("enter a valid number : ")

    
