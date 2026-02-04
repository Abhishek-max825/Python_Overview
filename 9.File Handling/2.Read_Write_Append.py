'''
Read, Write, and Append Files :-

Python provides several modes for opening files:

-> 'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.
-> 'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
-> 'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.
'''

# Reading from a file

f = open("9.File Handling/abhi.txt","r")
content = f.read()
print(content)

f.close()

# Another Example
try:
    file = open("9.File Handling/abhi.txt", "r")  # Open in read mode
    content = file.read()  # Read the entire file content
    print(content)
    file.close()  # Close the file
except FileNotFoundError:
    print("File not found.")

# Reading line by line
try:
    file = open("my_file.txt", "r")
    for line in file: # Efficient for large files
        print(line.strip()) # Remove newline characters
    file.close()
except FileNotFoundError:
    print("File not found.")


# Write the file content

f = open("9.File Handling/write.txt","w")
f.write("whatsuppp!!!!\nIts about writing a file")
f.close()

# Another Example
file = open("new_file.txt", "w")  # Open in write mode (creates or overwrites)
file.write("Hello, world!\n")  # Write some text
file.write("This is a new line.\n")
file.close()

# Append the text to the file 

f = open("9.File Handling/write.txt","a")
f.write("\nnow its appending extra content at the end")
f.close()

# line by line

with open("9.File Handling/write.txt","r")as f:
    for line in f:
        print(line)

'''
Using with statement (recommended):

-> The with statement provides a cleaner way to work with files.
-> It automatically closes the file, even if errors occur.
'''  

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

with open("output.txt", "w") as file:
    file.write("Data written using 'with'.\n")