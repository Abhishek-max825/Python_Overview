#break statement
for i in range(0,21):
   print(i)
   if i == 11:
      print("execution is stopped forcefully")
      break

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# execution is stopped forcefully

#continue statement

for i in range(1,20):
   if i == 10:
      continue 
      #continue the loop for the next iteration here itself, when it countered it will ignore all the statements under it
   print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19  


#pass statements
#its a placeholder that does nothing

i = 3

if i == 3 :
   pass
  #do nothing
print("end of program")