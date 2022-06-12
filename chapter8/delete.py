# Now there is no way to have a garbage collector in python
# For that reason there is a library that we should use when we are delaing with objects

# With this module we can create deconstructors 
import weakref


s1 = {1, 2, 3}
s2 = s1

def deconstructor():
    print("Good bye my friend")

# We pass the deconstructor function 
ender = weakref.finalize(s1, deconstructor)
    
# Delete the object
del s1

# but acutally s1 continues alive
print(s2)

# We can know that printing this variable
print(ender.alive)


# To actually delete that space of memory needs to happen two things
# That the program finishes or we overwrite that space of memory

# See what happens when I overwrite
print("Overwritting")
s2 = "Hello"
print("OverWrited")
print(ender.alive)


