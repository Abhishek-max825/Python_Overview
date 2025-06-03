#while loop is used to execute a block of code repeatedly until a condition is met
# while condition:
#   statement1
# statement2

i = 1
while i < 6:
    print(i)
    i += 1
print("Done")

# 1
# 2
# 3
# 4
# 5
# Done

#infinite loop

# i = 1
# while True:
#     print(i)
    
# infinite values will be printed
# RAM will be full
# CPU will be 100%
# System will be crashed
# to avoid infinite loop we can use break statement

i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
