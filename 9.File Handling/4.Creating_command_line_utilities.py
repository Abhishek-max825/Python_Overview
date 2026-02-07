'''
Creating Command Line Utilities

-> You can use Python to create simple command-line utilities.
-> The argparse module makes it easier to handle command-line arguments.
'''

import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1",type=float,help="First number")
parser.add_argument("num2",type=float,help="second number")
parser.add_argument("operation",choices=['add','sub','mul','div'],help="Operation")

args = parser.parse_args()
print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")
elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")
elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")
else :
    print("some error occured")     

# Running prompts :-
# PS C:\Users\abhis\OneDrive\ドキュメント\Python Bootcamp - 2025> cd "9.File Handling"                                                                    
# PS C:\Users\abhis\OneDrive\ドキュメント\Python Bootcamp - 2025\9.File Handling> python ./4.Creating_command_line_utilities.py 10 2 mul    
# Output :- The result is 20.0   


#Another example

import argparse

parser = argparse.ArgumentParser(description="A simple command-line utility.")
parser.add_argument("filename", help="The file to process.")
parser.add_argument("-n", "--number", type=int, default=1, help="Number of times to repeat the output.")

args = parser.parse_args()

try:
    with open(args.filename, "r") as file:
        content = file.read()
        for _ in range(args.number):
            print(content)
except FileNotFoundError:
    print("File not found.")
