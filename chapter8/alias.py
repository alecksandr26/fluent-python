

carl = {"age" : 20, "name" : "carl"}


lewis = carl

# With this we print the memory direction
print(id(carl))
print(id(lewis))


lewis['name'] = 'lewis'


print(carl)


# To do a copy instead of use a
james = lewis.copy()
james['name'] = 'james'


print(james)
print(id(james))
print(carl)

print(carl is james)    # False
print(carl is lewis)    # True



