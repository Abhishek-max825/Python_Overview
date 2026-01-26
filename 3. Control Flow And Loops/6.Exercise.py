# If-Else Conditional Statements

# def even_or_odd(number):
#     if num%2 == 0:
#         return "even"
#     return  "odd"

# num = int(input("Enter a number: "))
# result = even_or_odd(num)
# print(result)

#For loop

# sum = 0
# for i in range(1,101):
#     sum += i

# print("sum of first 100 numbers is :",sum)    


  #patter printing

# for i in range(4):
#     for j in range(i+1):
#        print("*",end="")    
#     print()   

# While loop

num = 123456789
i = 0

while num > 0:
    digit = num % 10
    print(digit,end="")
    num = num // 10
    i += 1

#pass

for i in range(6):
    if i == 3:
        pass
    else:
        print(i)
