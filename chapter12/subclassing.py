

# Here We inherited all the methods from the dict class but we replace the __setitem__ method
# For this new one 
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict(one = 1)
print(dd)

dd['two'] = 2

print(dd)

dd.update(three = 3)

print(dd)

"""
As you can see we are overwriting an a very important method which is __setitem__ but we can overwrite
any type of method in python, thats something that I don't like because its broken, as you can see the
__setitem__ its not completly replace it
"""







