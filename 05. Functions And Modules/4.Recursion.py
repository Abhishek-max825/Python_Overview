# fibonacci series
# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7....
# fib(0) = 0
# fib(1) = 1
# fib(2) = fib(1) + fib(0)
# fib(3) = fib(2) + fib(1)
# fib(4) = fib(3) + fib(2)
# fib(5) = fib(4) + fib(3)
# fib(6) = fib(5) + fib(4)
# fib(n) = fib(n-2) + fib(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    else :
        return fib(n-2) + fib(n-1)
    

result = fib(5)    
print(result)


# working steps
'''
fromula : 
         fab(n-2) + fab(n-1)     

Step 1: fib(6)
Step 2: fib(4) + fib(5)     
Step 3: fib(2) + fib(3) + fib(5)
Step 4: fib(0) + fib(1) + fib(1) + fib(2) + fib(5)
Step 5: 0 + 1 + 1 + fib(0) + fib(1) + fib(3) + fib(4)
Step 6: 0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(2) + fib(3)
Step 7: 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(0) + fib(1) + fib(1) + fib(2)
Step 8: 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0)+ fib(1)
Step 9: 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8

'''
