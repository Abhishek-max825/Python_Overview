import string as s

sentence = "  i love python programming  "
print(sentence)
print(sentence.strip())

print(sentence.title())

count = 0
for i in sentence:
    if i.lower() == "o":
        count+=1
print("count of o is :",count)        

value = "123abc"
print(value.isalnum())

sent = "My name is {name} and I am {age} years old."
print(sent.format(name="John",age="30"))

name  = "Alice" 
age = 25

print(f"My name is {name} and I am {age} years old.")

name = "nayan"

if name == name[::-1]:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")    
