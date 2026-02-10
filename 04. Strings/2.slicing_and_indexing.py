name = "harry"
print(name[0:2])
# ha
#it goes from 0 to n-1 / in this case we can call it as 2-1

print(name[2:-1])
# rr
#working criteria is like 2nd index to n - 1 = [(5-1)-1] = 3
#name[2:3] --> converted to positive form

#slicing with step
name_val = "abhi0123456789"
#print(name[start:end:skip]) #skip n-1 characters
print(name_val[0:10:1]) #skip 0 character
# abhi012345 
print(name_val[0:10:2]) #skip n-1 = 2-1 => 1 character
# ah024

#if we want to skip 3 character the index will be 0:10:4 where 4 = N  and skip = 4-1 = 3
print(name_val[0:10:4])
# a04

print(name_val[:4]) # replace the first empty value by 0
# abhi
print(name_val[1:]) # replace end value with length-1 which results in name[1:14-1]
# bhi0123456789