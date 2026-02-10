# name = "abhi"
# name = 'abhi'
name = '''abhi'''
print(name)

msg = '''hello
i am abhishek'''
print(msg)
# hello
# i am abhishek

#string indexing

name_string = "abhishek"
print(name[0])
# a

for i in range(len(name_string)):
    print("name_string[",i,"] = ", name_string[i])
# name_string[ 0 ] =  a
# name_string[ 1 ] =  b
# name_string[ 2 ] =  h
# name_string[ 3 ] =  i
# name_string[ 4 ] =  s
# name_string[ 5 ] =  h
# name_string[ 6 ] =  e
# name_string[ 7 ] =  k

#negative indexing
name = "H  a  r  r  y"
#       0  1  2  3  4
#       -5 -4 -3 -2 -1
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])#name_string[-4+5] = name_string[1]
# 5 is length of name


for i in range(len(name_string)-1, -1, -1):
    print("name_string[",i,"] = ", name_string[i])
# name_string[ 7 ] =  k 
# name_string[ 6 ] =  e
# name_string[ 5 ] =  h
# name_string[ 4 ] =  s
# name_string[ 3 ] =  i
# name_string[ 2 ] =  h
# name_string[ 1 ] =  b
# name_string[ 0 ] =  a    