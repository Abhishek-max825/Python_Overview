#Match case is a new feature in Python 3.10.
#It is a way to handle multiple conditions in a single statement.

#Syntax
#match variable:
#    case pattern:
#        code block


a = int(input("Enter a number between 1 and 10: "))

while  True:
 if a>=1 and a<=10:
  match a:
    case 1:
         print("you won 1000$")
         break
    case 4:
         print("you won 2000$")
         break
    case 8:
         print("you won 3000$")
         break
    case 9:
         print("you won 4000$")
         break
    case _:
         # _ is a wildcard character that matches any value(default case)
         print("Better luck next time")
         break
 else:
    print("Invalid input")
    break
