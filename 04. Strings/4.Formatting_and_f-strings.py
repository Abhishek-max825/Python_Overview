#string formatting

template = "dear {}, you are awesome.Take this {}$ bag"
a = "jhon"
a1 = 10000
b = "jack"
b1 = 1000
c = "marry"
c1 = 300

s1 = template.format(a,a1)
print(s1)
# dear jhon, you are awesome.Take this 10000$ bag

#f-strings -->created after 3.6 version

print(f"{b} you are awesome and take this {b1}$ bag")
# jack you are awesome and take this 1000$ bag