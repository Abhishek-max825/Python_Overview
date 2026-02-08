'''
1. File I/O Basics
-> Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
-> Open notes.txt, read its content, and print it to the console.
'''


with open("9.File Handling/notes.txt","r")as f:
    sent  = f.read()
    print(sent)

# Output : Learning Python is fun!    

'''
2. Read, Write, and Append Files

-> Write a program that writes three lines of text to a file tasks.txt.
-> Open tasks.txt in append mode and add a new line "Task Completed!".
-> Read the file and print all lines as a list using readlines()
'''   

with open("9.File Handling/task.txt","w")as f:
    f.write("Hi i am Abhishek\ncurrently persuing BCA from ABC college\nAnd yeah here i am!!!")

with open("9.File Handling/task.txt","a")as f: 
    f.write("\nTask Completed!")

with open("9.File Handling/task.txt","r")as f:
    for i in f.readlines():
        print(i,end="")

'''
Output : 

Hi i am Abhishek
currently persuing BCA from ABC college
And yeah here i am!!!
Task Completed!
'''    


'''
3. OS and Shutil Modules

1. Use the os module to:

-> Print the current working directory
-> List all files and folders in the current directory
-> Create a new folder my_folder

2.Use the shutil module to:

-> Copy a file from one folder to another
-> Move a file to a new folder
-> Delete a file (careful: irreversible!)
'''
# 1.
import os

print(os.getcwd())
# C:\Users\abhis\OneDrive\ドキュメント\Python Bootcamp - 2025

print(os.listdir())
# ['.git', '.gitignore', '.venv', '1. Introduction To Python Programming', '10. Working With External Libraries', '11. Using AI As A Developer', '12. Hands On Python Projects', '13. Conclusion And Next Steps', '2. Python Fundamentals', '3. Control Flow And Loops', '4. Strings', '5. Functions And Modules', '6. Data Structures In Python', '7. Object Oriented Programming', '8. Advanced Concepts In Python', '9.File Handling', 'Python_handbook.pdf', '__pycache__']

# os.mkdir("9.File Handling/my_folder")

# 2.

import shutil

# shutil.copy("9.File Handling/dir/profile.txt","9.File Handling/my_folder/new.txt")
# shutil.move("9.File Handling/abhi.txt","9.File Handling/my_folder/")

shutil.rmtree("9.File Handling/dir")

'''
4. Creating Command Line Utilities
-> Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:
output :-
python count_lines.py tasks.txt
# Output: Number of lines: 4

'''

import argparse

parser = argparse.ArgumentParser(description="Lines checking")

parser.add_argument("path",help="enter the file name")

args = parser.parse_args()

count = 0
try:
    with open(args.path,"r")as f:
        for line in f.readlines():
            count += 1
        print(f"Number of lines : {count}")
except FileNotFoundError:
    print("File not found")   

# Output : Number of lines: 4             