

"""
Manipulate the arguments 
"""
def decorator_args(func):
    # We can manipulate the args like this
    def wraper(*args, **kargs):
        print("args: ", args)
        print("args[0]: ", args[0])
        print("args[1]: ", args[1])
        
        print("kargs: ", kargs)
        return func(*args, **kargs)
    return wraper



@decorator_args
def target(n, n2):
    return n + n2


"""
Making sure that we just have even numbers
"""
def decorator_even(func):
    def is_even(*args):
        for n in args:
            # Finish the runtime of the function never executing the function
            if not n % 2 == 0:
                return 0
                
        return func(*args)

    return is_even



@decorator_even
def sum_even(*args) -> int:
    return sum(list(args))




"""
Also we can get arguments through the decorators
"""


def func_upper_decorator(active = False):
    def decorator(func):
        def func_to_run(*args, **kargs):
            if active:
                for n in args:
                    if not n % 2 == 0:
                        return 0
                    
            return func(*args)
        return func_to_run
    return decorator
    


@func_upper_decorator(False)
def mul(a, b):
    return a * b

"""
this is something similar
mul = (func_upper_decorator())(mul)
"""

def main():
    print(target(1, 2))
    print("\n")
    print(sum_even(2, 2))
    print(mul(1, 2))

    
if __name__ == "__main__":
    main()



