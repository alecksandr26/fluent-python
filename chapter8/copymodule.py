# We can run the module 'copy' to do a very deep copies of our objects
import copy


class Buss:
    def __init__(self, passagers = None):
        if passagers == None:
            self.passagers = []
        else:
            # With this we can do a simple copy of the object list 
            self.passagers = copy.copy(passagers)
        

    def pick(self, name):
        self.passagers.append(name)

    def drop(self, name):
        self.passagers.remove(name)


# Now for example

bus1 = Buss()

bus1.pick('rama')
bus1.pick('pedro')
bus1.pick('lupe')


# To do a very deep copy we can run
bus2 = copy.deepcopy(bus1)

print(id(bus2))
print(id(bus1))


# We need to take care about alias and reference things
# Take a look this class and how we get a variable from reference
class HauntedBus:
    # It suppous that this shit is better
    def __init__(self, passagers = []):
        self.passagers = passagers




