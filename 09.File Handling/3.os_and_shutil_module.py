'''
OS and Shutil Modules in Python

-> Python's os module provides functions for interacting with the operating system, such as working with directories and files.
-> The shutil module offers higher-level file operations.
'''
# os module:-
import os

a = os.listdir("9.File Handling/dir")#it returns the names of the files present inside dir in form of list
print(a)# Output : ['1.sample1.txt', '2.sample2.txt', 'sub dir']

print(os.getcwd())# Output : C:\Users\abhis\OneDrive\ドキュメント\Python Bootcamp - 2025
#it returns the current working directory

print(os.path.exists("9.File Handling/dir"))# True
#it returns true if path exist otherwise returns false

#it helps to remove the file from the directory
os.remove("9.File Handling/write.txt")

os.rmdir("9.File Handling/dir/sub_dir")#it helps to remove the empty directory 
#if it has some text it wont delete that directory

#Another example

import os

# Get the current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)

# Create a new directory
# os.mkdir("new_directory")  # creates only one level of directory
# os.makedirs("path/to/new_directory") # creates nested directories

# Change the current directory
# os.chdir("new_directory")

# List files and directories in a directory
files = os.listdir(".") # "." represents current directory
print("Files in current directory:", files)

# Remove a file or directory
# os.remove("my_file.txt")
# os.rmdir("new_directory") # removes empty directory
# shutil.rmtree("path/to/new_directory") # removes non-empty directory (use with caution)

# Rename a file or directory
# os.rename("old_name.txt", "new_name.txt")

# Check if a file or directory exists
if os.path.exists("my_file.txt"):
    print("File exists")

# Join path components in a platform-independent way
path = os.path.join("folder", "subfolder", "file.txt")
print("Joined path:", path)

'''
shutil :-
'''

import shutil

#shutil.rmtree("9.File Handling/dir")
## it removes the firectory at any cost it wont check whether directory is empty or not
## it just delete everythinhg inside that directory

shutil.copy("9.File Handling/abhi.txt","9.File Handling/profile.txt")
#it helps to copy the file from source to destination

shutil.move("9.File Handling/profile.txt","9.File Handling/dir/")
#it helps to move file from one directory to other

# shutil module examples:

import shutil

# Copy a file
# shutil.copy("my_file.txt", "my_file_copy.txt")

# Move a file or directory
# shutil.move("my_file.txt", "new_directory/")