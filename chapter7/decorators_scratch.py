"""

Decorate a function si the same thing if we encapsulate a function inside a nother function
"""


"""
This is the first way
"""
# This is the decorator, just return another function where we execute the target
def decorator(target_func):
    def func_to_execute():
        print('Before executing target function')
        target_func()
        print("After executing target function")
    
    return func_to_execute



"""
The second way
"""

wrapped_func = None

def func_to_execute2():
    global wrapped_func
    print("Decorator2")
    print("Before executing target")
    wrapped_func()
    print("After executing target")


def decorator2(target_func):
    global wrapped_func
    wrapped_func = target_func
    return func_to_execute2


"""
The function to wrapp
"""
    
# The function to decorate
def target():
    print('running target ')


# Here I encapsulate the function and rewrited as new function
target = decorator2(target)


# And execute the new function 
target()





