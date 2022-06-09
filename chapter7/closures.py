

"""
This is the correct way to do it
"""

class Average:
    def __init__(self):
        self.nums = []

    # __call__: After executing the object we can call it again and this function will execute
    def __call__(self, new_value):
        self.nums.append(new_value)
        s = sum(self.nums)
        return s / len(self.nums)


"""
Another way to do it
"""

def make_averager():
    nums = []
    
    def avg(value):
        nums.append(value)
        s = sum(nums)
        return s / len(nums)
    
    return avg



"""
Another version with functions
"""
def make_averager2():
    cout = 0
    total = 0

    def avg(var):
        nonlocal cout, total
        cout += 1
        total += var
        return total / cout
    
    return avg


# To use closures first create the object
#avg = Average()
#avg = make_averager()
avg = make_averager2()


# Now we can execute
print(avg(5))
print(avg(4))
print(avg(3))
print(avg(2))
print(avg(1))
