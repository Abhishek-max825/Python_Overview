'''
<-- lambda functions -->

- > lambda is predefined function name its just like function inside another function
- > x , y are the values that his been taken just like parameters 
- > x + y are the calculation that should be done and return something

'''    

square = lambda x : x * x
# This is a tiny function that takes one number (x) and multiplies it by itself
# It's like writing: x × x or x²
# The lambda keyword is just Python's way of saying "here's a quick little function"
print(square(3))
# 9

sum = lambda x, y : x + y
'''
As good as writing 
  def sum(x,y):
     return  x + y

'''
print(sum(6,4))
# 10

