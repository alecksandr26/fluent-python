"""
This is an exmaple of an pythonic object, I create a simple object
Basically its a good idea to create pythonic object
"""

from array import array
import math


class Vector2d:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Permits to iterate a list of 'Vector2d'
    def __iter__(self):
        return (i for i in (self.x, self.y))

    # Return something when you try to print Vector2d
    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r},{!r})".format(class_name, *self)

    # Convert the object to a string variable
    def __str__(self):
        return str(tuple(self))

    # Return the bytes fromt he object 
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    # Is the operator overloading to compare two variables
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    # When you run the function abs to the object it calculates the magnitud
    def __abs__(self):
        return math.hypot(self.x, self.y)

    # So basically the bool object function return true if the vector has magnitud 
    def __bool__(self):
        return bool(abs(self))
    









